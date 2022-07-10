# MySQL日志系统：binlog、redo log和undo log
日志是 MySQL 数据库的重要组成部分，比如数据持久化、主从复制、数据回滚等操作都依赖日志系统来实现。本文将介绍MySQL的三种日志：归档日志binlog、重做日志redo log 和回滚日志undo log。

<!--more-->

## binlog 归档日志

### 什么是binlog

二进制日志(binary log)描述了数据库更改的“事件”，比如建表、更改表数据等操作，它属于逻辑日志，由 `Server ` 层记录，记录了数据库所有的逻辑操作。还包含了关于每条语句更新数据的时间信息，不记录查询语句的日志，比如SELECT语句，如果要查看所有语句的日志，可以使用通用查询日志（general query log）。

binlog主要有两个用途:

- 主从复制。将源服务器（Master 端）上binlog发送到Slave 端，Slave 端根据binlog重放事务，实现主从数据保持一致。
- 数据恢复。binlog是通过增量的形式进行写入的，可使用binlog恢复某一时刻的数据。

下面来看看MySQL中如何使用binlog。

### 开启binlog

查看binlog是否开启：`show variables like '%log_bin%';`

```sql
mysql> show variables like '%log_bin%';
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    15
Current database: mysql

+---------------------------------+------------------------------------------------+
| Variable_name                   | Value                                          |
+---------------------------------+------------------------------------------------+
| log_bin                         | ON                                             |
| log_bin_basename                | D:\tools\mysql-8.0.16-winx64\data\binlog       |
| log_bin_index                   | D:\tools\mysql-8.0.16-winx64\data\binlog.index |
| log_bin_trust_function_creators | OFF                                            |
| log_bin_use_v1_row_events       | OFF                                            |
| sql_log_bin                     | ON                                             |
+---------------------------------+------------------------------------------------+
6 rows in set, 1 warning (0.81 sec)
```

如果没有开启，需修改配置文件，新增：

```ini
[mysqld]
log-bin=mysql-bin 
```

然后重启MySQL。

MySQL 5.7.7 之后的版本中，binlog日志格式默认采用`ROW`，Row 格式不记录 SQL 语句上下文相关信息，仅记录每一行的数据修改。

```sql
mysql> show variables like 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+
1 row in set, 1 warning (0.00 sec)
```

binlog日志通常在事务提交时才记录，mysql 通过 `sync_binlog` 参数来控制 biglog 刷入磁盘的时机，其取值范围是 `0-N`：

- 0：由系统自行判断何时写入磁盘；
- 1：每次提交时写入磁盘
- N：每N个事务写入磁盘

MySQL 5.7.7 之后的版本默认为 `1`。


```sql
mysql> show variables like 'sync_binlog';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| sync_binlog   | 1     |
+---------------+-------+
1 row in set, 1 warning (0.00 sec)
```



### 查看binlog

刷新日志：`Flush logs;` , 会产生一个新编号的binlog文件。

查看所有binlog文件：

```sql
mysql> show binary logs;
+---------------+-----------+-----------+
| Log_name      | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000742 |       178 | No        |
| binlog.000743 |      1571 | No        |
| binlog.000744 |       415 | No        |
| binlog.000745 |       155 | No        |
+---------------+-----------+-----------+
4 rows in set (0.00 sec)
```

查看当前写入的binlog文件:

```sql
mysql> show master status;
+---------------+----------+--------------+------------------+-------------------+
| File          | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+---------------+----------+--------------+------------------+-------------------+
| binlog.000745 |      155 |              |                  |                   |
+---------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)
```

接下来创建一个数据表，并插入数据库，SQL语句如下：

```sql
create table department(
    id int,
    name varchar(255) not null
);

ALTER TABLE department CHANGE COLUMN name dept varchar(255);

insert into department (id, dept) values (1,'开发');
insert into department (id, dept) values (2,'测试');
update department set dept=产品 where id=2;
```

查看数据：

```sql
mysql> select * from department;
+------+------+
| id   | dept |
+------+------+
|    1 | 开发 |
|    2 | 测试 |
+------+------+
2 rows in set (0.00 sec)
```

然后使用 `show binlog events;` 命令查看binlog内容:

```sql
mysql> show binlog events in 'binlog.000745';
+---------------+------+----------------+-----------+-------------+---------------------------------------------------------------------------------------------------+
| Log_name      | Pos  | Event_type     | Server_id | End_log_pos | Info                                                                                              |
+---------------+------+----------------+-----------+-------------+---------------------------------------------------------------------------------------------------+
| binlog.000745 |    4 | Format_desc    |         1 |         124 | Server ver: 8.0.16, Binlog ver: 4                                                                 |
| binlog.000745 |  124 | Previous_gtids |         1 |         155 |                                                                                                   |
| binlog.000745 |  155 | Anonymous_Gtid |         1 |         232 | SET @@SESSION.GTID_NEXT= 'ANONYMOUS'                                                              |
| binlog.000745 |  232 | Query          |         1 |         393 | use `testdb`; create table department(
    id int,
    name varchar(255) not null
) /* xid=191 */ |
| binlog.000745 |  393 | Anonymous_Gtid |         1 |         470 | SET @@SESSION.GTID_NEXT= 'ANONYMOUS'                                                              |
| binlog.000745 |  470 | Query          |         1 |         621 | use `testdb`; ALTER TABLE department CHANGE COLUMN name dept varchar(255) /* xid=192 */           |
| binlog.000745 |  621 | Anonymous_Gtid |         1 |         700 | SET @@SESSION.GTID_NEXT= 'ANONYMOUS'                                                              |
| binlog.000745 |  700 | Query          |         1 |         777 | BEGIN                                                                                             |
| binlog.000745 |  777 | Table_map      |         1 |         843 | table_id: 100 (testdb.department)                                                                 |
| binlog.000745 |  843 | Write_rows     |         1 |         891 | table_id: 100 flags: STMT_END_F                                                                   |
| binlog.000745 |  891 | Xid            |         1 |         922 | COMMIT /* xid=193 */                                                                              |
| binlog.000745 |  922 | Anonymous_Gtid |         1 |        1001 | SET @@SESSION.GTID_NEXT= 'ANONYMOUS'                                                              |
| binlog.000745 | 1001 | Query          |         1 |        1078 | BEGIN                                                                                             |
| binlog.000745 | 1078 | Table_map      |         1 |        1144 | table_id: 100 (testdb.department)                                                                 |
| binlog.000745 | 1144 | Write_rows     |         1 |        1192 | table_id: 100 flags: STMT_END_F                                                                   |
| binlog.000745 | 1192 | Xid            |         1 |        1223 | COMMIT /* xid=194 */                                                                              |
+---------------+------+----------------+-----------+-------------+---------------------------------------------------------------------------------------------------+
16 rows in set (0.00 sec)
```

可以看到binlog记录了执行过程。



### 使用binlog恢复数据

先删除数据表：

```sql
mysql> drop table department;
Query OK, 0 rows affected (0.28 sec)

mysql> select * from department;
ERROR 1146 (42S02): Table 'testdb.department' doesn't exist
```

windows中可以使用 mysqlbinlog.exe 来使用binlog恢复数据到某个位置，我的存放地址为 `D:\tools\mysql-8.0.16-winx64\bin` 。

使用mysqlbinlog命令恢复：

```bash
$ mysqlbinlog --no-defaults "D:\tools\mysql-8.0.16-winx64\data\binlog.000745" --start-position=124 --stop-position=1223 > d:\\test.sql
```

登录mysql服务器，执行：`source d:\\test.sql`

查询数据：

```sql
mysql> select * from department;
+------+------+
| id   | dept |
+------+------+
|    1 | 开发 |
|    2 | 测试 |
+------+------+
2 rows in set (0.00 sec)
```

数据成功恢复了。

## redo log 重做日志

前面介绍了binlog日志是在事务提交时才记录的，如果MySQL在事务执行过程中突然奔溃，使用binlog日志无法保证事务完整性，没有 crash-safe 的能力，这也是MySQL 引擎 MyISAM的一个缺点。crash-safe指MySQL服务器奔溃重启后，能够保证：

- 所有已经提交的事务的数据仍然存在。
- 所有没有提交的事务的数据可以自动回滚。

InnoDB 引擎通过redo log(重做日志)和undo log(回滚日志)这两个日志保证了MySQL的crash-safe 能力，他们都是InnoDB 引擎引入的日志，属于引擎层的日志。前面说了binlog是server层记录的日志，所以使用各种引擎的MySQL服务器都可以使用它。

### WAL技术

redo log属于物理日志，记录的是事务对某个数据页做了哪些修改，只记录修改相比存储整个数据页的性能更优。redo log的记录采用了WAL(Write-Ahead Logging) 技术，也就是先写日志，再写磁盘，这样进一步提升了性能。

当执行一条DML语句的时候，InnoDB 引擎会先把记录写到内存(redo log buffer)中，然后在系统在适当的时候将这个操作记录更新到磁盘(redo log file)。这个写入磁盘的时机可以通过 `innodb_flush_log_at_trx_commit` 参数来配置：

- 0：每秒刷新写入磁盘，当系统崩溃，可能会丢失1秒钟的数据。
- 1：实时写，实时刷。事务每次提交都会写入磁盘，Innodb 默认设置的就是1。
- 2：实时写，延迟刷。每次提交仅写入到内存，然后每秒将内存中的日志写入到磁盘中。

```sql
mysql> show variables like 'innodb_flush_log_at_trx_commit';
+--------------------------------+-------+
| Variable_name                  | Value |
+--------------------------------+-------+
| innodb_flush_log_at_trx_commit | 1     |
+--------------------------------+-------+
1 row in set, 1 warning (0.00 sec)
```

redo log大小固定，通过循环写入的方式,

```sql
mysql> show variables like '%innodb_log%';
+------------------------------------+----------+
| Variable_name                      | Value    |
+------------------------------------+----------+
| innodb_log_buffer_size             | 16777216 |
| innodb_log_checksums               | ON       |
| innodb_log_compressed_pages        | ON       |
| innodb_log_file_size               | 50331648 |
| innodb_log_files_in_group          | 2        |
| innodb_log_group_home_dir          | .\       |
| innodb_log_spin_cpu_abs_lwm        | 80       |
| innodb_log_spin_cpu_pct_hwm        | 50       |
| innodb_log_wait_for_flush_spin_hwm | 400      |
| innodb_log_write_ahead_size        | 8192     |
+------------------------------------+----------+
10 rows in set, 1 warning (0.01 sec)
```



### 两阶段提交

redo log 的写入包括了两个步骤：prepare 和 commit，也就是"两阶段提交"。目的是为了使 redo log 和 binlog 保持一致，步骤如下：

1. InnoDB 写redo log，标记为prepare状态；
2. 执行器写binlog；
3. InnoDB 写redo log，标记为commit状态。

使用两阶段提交可以保证主从数据一致。

## undo log 回滚日志

redo log保证数据持久性，而undo log用于保证事务操作的原子性。undo log属于逻辑日志，记录了数据的反向操作语句，保证进行事务回滚时，可以将数据还原。主要有两个功能：

- 事务回滚：保证原子性
- 多版本并发控制(MVCC)：隔离性

```sql
mysql> show variables like '%undo%';
+--------------------------+------------+
| Variable_name            | Value      |
+--------------------------+------------+
| innodb_max_undo_log_size | 1073741824 |
| innodb_undo_directory    | .\         |
| innodb_undo_log_encrypt  | OFF        |
| innodb_undo_log_truncate | ON         |
| innodb_undo_tablespaces  | 2          |
+--------------------------+------------+
5 rows in set, 1 warning (0.01 sec)
```

- `innodb_max_undo_log_size`：日志文件大小
- `innodb_undo_directory` ：存放目录
- `innodb_undo_tablespaces`：创建undo文件个数，会在mysql的data目录下创建命名为undo_001~undo_002的undo tablespace文件。

undo log默认存放在 `data/ibdata1` 中，如果开启了 `innodb_file_per_table` 则会保存到每个表的.ibd文件中。

```sql
mysql> show variables like 'innodb_file_per_table';
+-----------------------+-------+
| Variable_name         | Value |
+-----------------------+-------+
| innodb_file_per_table | ON    |
+-----------------------+-------+
1 row in set, 1 warning (0.01 sec)
```



## update语句执行流程

简单介绍了这3种日志之后，来看一下一条更新语句执行过程中这些日志是如何记录的。

```sql
update department set dept='产品' where id=2;
```

主要流程如下：

1. 分析器对SQL 语句进行解析，通过词法和语法解析知道这条语句要做什么。
2. 执行器通过InnoDB引擎提供的接口读取id=2这一行数据，如果数据在内存中就直接返回行数据，如果不在就从磁盘中读取。
3. 执行器将这行数据的`dept`设置为 `产品 `。
4. InnoDB将旧行数据写入undo log中。
5. InnoDB将新行更新到内存。
6. InnoDB写redo log并标记为prepare状态。
7. 执行器写binlog，并把 binlog 写入磁盘。
8. 执行器调用InnoDB的提交事务接口，InnoDB写redo log并标记为commit状态，更新完成。。

本文介绍了MySQL的三种重要日志：物理日志 redo log和undo log 和逻辑日志 binlog，它还有其它日志，比如Error log、General query log、Relay log、Slow query log、DDL log等，他们都是MySQL数据库的重要组成部分，日志记录在一定程度上影响MySQL服务的性能，但他们是必不可少的，备份的频率需要根据具体业务来进行配置。





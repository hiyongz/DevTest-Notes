# Python日期时间获取与转换
python 日期时间获取与转换
<!--more-->

## 世界时、原子时和世界协调时
### 世界时
世界时（Universal Time, UT）是根据地球自转周期确定的时间，1s为全年内每日平均长度的1/86400，由于地球绕太阳公转的轨道不是圆的，地球与太阳之间的距离不是固定的，导致太阳相对绕地球的周期不等于地球自转周期，通过对产生的时差进行修正，称为“平均太阳时”。根据国际协定，将英国格林威治所在子午圈（又称本初子午线）的平太阳时，定义为零类世界时（UT0）。由于地球的旋转轴会有微小移动（每年有几厘米的移动），对极移效应进行修正后的时间称为为一类世界时UT1。一类世界时UT1也有原因不明的季节性周期变化，对此进行修正，便得到更加均匀的二类世界时UT2。

### 原子时
原子时钟是利用铯原子振荡周期极为规律的特性研制而出，原子时(international atomic time,TAI)的秒长定义为铯 \-133 原子能级跃迁辐射9192631770周所持续的时间。原子钟的精度可以达到每100万年误差才1秒。在要求更高时间精度的天文、航海、航天等领域发挥了巨大的作用。

### 世界协调时
世界协调时(Coordinatde Universal Time, UTC)基于国际原子时，以原子时秒长为基础，在时刻上尽量接近于格林威治标准时间(GMT)，通过不规则的加入闰秒来抵消地球自转变慢的影响，保证UTC与世界时（UT1）相差不超过0.9秒。

## epoch time
Unix epoch (Unix time, POSIX time, Unix timestamp)，是一种时间表示方式，定义为从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数。Unix时间戳不仅被使用在Unix 系统、类Unix系统中，也在许多其他操作系统中被广泛采用。

### 2038问题
32位操作系统将epoch日期存储为有符号的32位整数，此类系统的Unix时间戳最多可以使用到格林威治时间2038年01月19日03时14分07秒（二进制：01111111 11111111 11111111 11111111）。其后一秒，二进制数字会变为10000000 00000000 00000000 00000000，发生溢出错误，造成系统将时间误解为1901年12月13日20时45分52秒。这很可能会引起软件故障，甚至是系统瘫痪(称为2038年问题或者Y2038)。

使用64位二进制数字表示时间的系统（最多可以使用到格林威治时间292,277,026,596年12月04日15时30分08秒）则基本不会遇到这类溢出问题。

## python time
时间格式在线转换：[https://www.epochconverter.com/](https://www.epochconverter.com/)
时区转换
* [国际时区转换在线计算器](http://www.99cankao.com/date/timezone.php)
* [世界时区划分时差查询](http://www.beijing-time.org/shiqu/)

Python time文档：[https://docs.python.org/zh-cn/3/library/time.html](https://docs.python.org/zh-cn/3/library/time.html)
### python获取当前时间
* time.time()：获取当前的epoch时间（时间戳）
* time.localtime()：获取本地时间
* time.gmtime()：获取GMT时间
```python
>> import time; 
>> time.time()
1612661504.1785676
>> time.localtime()
time.struct_time(tm_year=2021, tm_mon=2, tm_mday=7, tm_hour=11, tm_min=23, tm_sec=20, tm_wday=6, tm_yday=38, tm_isdst=0)
```
### 标准时间转换为epoch时间
本文将标准时间定义为ISO 8601格式时间：YYYY-MM-DD hh:mm:ss.mil

两种方法转换为 Unix timestamp：
* calendar.timegm：转换的时间格式为格林威治标准时间
* time.mktime：转换的时间为本地时间（考虑了时区）

```python
>> import calendar, time
>> date_time = time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S')
>> calendar.timegm(date_time)
946730040
>> time.mktime(date_time)
946701240.0
```

### epoch时间转换为标准时间
* time.localtime(epoch_time)：转换为本地时间，或者获取本地时间
* time.gmtime(epoch_time)：转换为GMT时间，或者获取GMT时间
* datetime.datetime.utcfromtimestamp(epoch_time)：UTC时间
* datetime.datetime.fromtimestamp(epoch_time)：本地时间

```python
>> import time
>> epoch_time = 946730040
>> time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch_time)) 
'Sat, 01 Jan 2000 20:34:00'
>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch_time)) 
'2000-01-01 20:34:00'
>> time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch_time)) 
'2000-01-01 12:34:00'
>> import datetime
>>> datetime.datetime.fromtimestamp(epoch_time)
datetime.datetime(2000, 1, 1, 20, 34)
>>> datetime.datetime.utcfromtimestamp(epoch_time)
datetime.datetime(2000, 1, 1, 12, 34)
```


## python datetime

### 获取当前时间（本地时间）

```python
import datetime
now_time = datetime.datetime.now()
print(now_time.strftime("%Y-%m-%d %H:%M:%S"))
print(now_time.strftime("%A")）
print(now_time.strftime("%w")）
```
out：
```
2020-09-28 14:15:24
Monday
1
```
### 时间格式化
```python
import datetime
timestr = "2020-10-01 18:30:00"
print(datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S"))
```
out：
```
2020-10-01 18:30:00
```

### timedelta
timedelta表示一个时间段，可用于时间计算。
语法：
```
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

```python
import datetime
now_time = datetime.datetime.now()
# 当前时间加一天
now_time + datetime.timedelta(days=1)
# 当前时间减一周
now_time + datetime.timedelta(weeks=-1)
```




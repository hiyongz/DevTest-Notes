# 禅道二次开发技巧

本文记录一些进行禅道二次开发的技巧。



## 代码调试

### 方法1：error_log方法

将php.ini文件中的log_errors设置成on

```bash
$ vi /opt/zbox/etc/php/php.ini
```

其中日志路径为 `/opt/zbox/logs/php_error_log`

然后在代码中使用error_log方法来保存日志：

```php
// 打印字符串
error_log("". $this->app->tab ."\r\n", 3,"/opt/zbox/logs/php_error_log");

// 打印数组
error_log("". var_export($cases,true) ."\r\n", 3,"/opt/zbox/logs/php_error_log");
```

清空日志：

```bash
$ > /opt/zbox/logs/php_error_log
```

### 方法2：file_put_contents方法

```php
// 字符串
file_put_contents("/opt/zbox/logs/php_error_log","HELLO\r\n",FILE_APPEND);
file_put_contents("/opt/zbox/logs/php_error_log","". $cases ."\r\n",FILE_APPEND);

// 数组
file_put_contents("/opt/zbox/logs/php_error_log",var_export($cases,true),FILE_APPEND);
```

### 方法3：a($var)方法

a($var)方法是禅道框架的工具类 `helper.class.php`（app\zentao\framework\base\helper.class.php）提供的一个方法，可用来打印变量信息，可在module、control和view方法中使用，调用后会直接显示在前端web页面上。

```php
function a($var)
{
    echo "<xmp class='a-left'>";
    print_r($var);
    echo "</xmp>";
}
```

也可以使用PHP的内置函数die(status)来打印，用来退出当前的php脚本，status不可以是数组、对象类型。

## 禅道扩展技巧

这里记录禅道二次开发的一些技巧。

### 1、读取当前用户

```php    
$this->app->user->account //当前用户
$this->loadModel("user")->getPairs() // 读取用户
```

### 2、读取当前模块方法名

```php
$this->app->getModuleName() // 获取当前模块名
$this->app->getMethodName() // 获取当前方法名
$this->app->getParams() // 获取当前方法参数变量
$this->app->getURI(true) // 获取当前URL
$this->app->tab // 获取左侧菜单名
```

### 3、加载模块、语言

```php
$this->app->loadModel('testtask'); // 加载模块
$this->app->loadLang('testtask'); // 加载语言
```

### 4、重定向到父页面

```php
// control:
return $this->send(array('result' => 'success', 'message' => $this->lang->saveSuccess, 'locate' => 'parent'));

die(js::reload('parent'));

return print(js::reload('parent'));

die(js::reload('parent.parent'));

die(js::closeModal('parent.parent', '', "function(){parent.parent.$('a.refresh').click()}")); // 关闭窗口并点击刷新

die(js::closeModal('parent.parent', 'this'))

// js:
parent.location.href = createLink('execution', 'importPlanStories', 'executionID=' + executionID + '&planID=' + planID);
parent.$.closeModal();
$.zui.closeModal();

```

### 5、统计代码执行耗时

```php
$time_start = microtime(true);
$time_end = microtime(true);
a($time_end - $time_start);
```

### 6、获取禅道数据库操作的SQL语句

输出sql语句

```php
$case = $this->dao->select('id, title')->from(TABLE_CASE)->where('id')->eq('1')->fetch();
$sql = $this->dao->printSQL();
// 或者
$sql = $this->dao->select('id, title')->from(TABLE_CASE)->where('id')->eq('1')->query();
```



### 7、直接执行SQL语句

对于复杂的SQL语句，可以写好SQL语句后直接执行。
```php
$sql =  "SELECT id, title FROM zt_case where id='1'";
$case = $this->dao->query($sql)->fetch();
// 等价于
$case = $this->dao->select('id, title')->from(TABLE_CASE)->where('id')->eq('1')->fetch();

```


### 8、fetch方法

view方法中调用其它模块，获取这个方法的输出内容：

```php
<?php include '../../common/view/header.html.php';?>
<?php echo $this->fetch('block', 'dashboard', 'module=my');?>
<?php include '../../common/view/footer.html.php';?>
```

control方法中调用其它模块的control方法

```php
echo $this->fetch('personnel', 'unbindWhitelist', "id=$id&confirm=$confirm");
die($this->fetch('file', 'buildExportTPL', "module=$module&templateID=$templateID"));
```

### 9、禅道session设置

```php
$this->session->set('test', "666"); // 设置session
a($this->session->testtesttesttesttest); // 读取session
```

### 10、PHP empty方法

```php
empty("")       : true
empty(null)     : true
empty(undefined): true
empty(array())  : true
empty([])       : true
empty(false)    : true
empty(0)        : true
empty("0")      : true
empty(true)     : false
empty(1)        : false
empty(-1)       : false
empty("1")      : false
empty("php")    : false
```

php判断是否为空排除0

https://stackoverflow.com/questions/732979/php-whats-an-alternative-to-empty-where-string-0-is-not-treated-as-empty

```php
if($cellValue === '0' || !empty($cellValue))
```
### 11、PHP格式化字符串

```php
$lang->report->gerrit->urlerror    = '无法访问Gerrit服务器：<a href="%s" target="_blank"><strong>%s</strong></a>，请检查网络环境。';

$gerritTips = sprintf($this->lang->report->gerrit->urlerror,  $gerritURL,$gerritURL);
```

### 12、post表单提交问题

前端控件禁用时（`calss=disabled`），表单提交时不会提交到后台，可使用hidden属性隐藏input：

```php
<td class="w-300px"><?php echo $fileName . html::hidden('fileName', $fileName);?></td>
```



## 文件下载

### zip文件下载

压缩文件方法：

```php
public function zipfile($filearray, $filename)
{
    $zip = new ZipArchive();
    if($zip->open($filename, ZIPARCHIVE::OVERWRITE | ZIPARCHIVE::CREATE)===TRUE)
    {
        for ($i = 0; $i < count($filearray); $i++){
            $attachfile= $filearray[$i];
            $zip->addfile($attachfile, basename($attachfile));
        }
        $zip->close();
        foreach($filearray as $file) unlink($file); // 删除文件
    }
}
```

删除目录方法：

```php
public function deldir($path) {
    if(is_dir($path)){
        //扫描一个文件夹内的所有文件夹和文件并返回数组
        $p = scandir($path);
        //如果 $p 中有两个以上的元素则说明当前 $path 不为空
        if (count($p)>2) {
            foreach($p as $val){
                //排除目录中的.和..
                if($val !="." && $val !=".."){
                    if (is_dir($path.$val)) {
                        $this->deldir($path.$val.'/'); //递归子目录删除
                    } else {
                        unlink($path.$val); //删除文件
                    }
                }
            }
        }
    }
    return rmdir($path);
}
```

生成zip压缩文件并下载：

```php
/* 压缩文件 */
$zipFileName  = 'test.zip';
$zipFilePath  = $caseSavePath . $zipFileName; // $caseSavePath为待压缩文件以及压缩文件保存路径
$this->zipfile($fileList, $zipFilePath); // 压缩文件，$fileList为文件列表

/* 下载文件 */
header("Content-type: application/zip"); 
header("Content-Disposition: attachment; filename=$zipFileName");
header("Content-length: " . filesize($zipFilePath));
header("Pragma: no-cache"); 
header("Expires: 0"); 
readfile("$zipFilePath");
```



### Excel 文件下载

下载xlsx格式文件：

```php
$xlsxFileName = basename($FilePath);

header("Content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"); 
header("Content-Disposition: attachment; filename=$xlsxFileName");
header("Content-length: " . filesize($xlsxFilePath));
header("Pragma: no-cache"); 
header("Expires: 0"); 
readfile("$xlsxFilePath");
```
下载xls格式文件：

```php
$xlsxFileName = basename($FilePath);

header('Content-Type: application/vnd.ms-excel');
header("Content-Disposition: attachment; filename=$xlsxFileName");
header("Content-length: " . filesize($xlsxFilePath));
header("Pragma: no-cache"); 
header("Expires: 0"); 
readfile("$xlsxFilePath");
```

其它文档类型的Content-type：

```php
application/vnd.ms-powerpoint  // *.ppt
application/vnd.openxmlformats-officedocument.presentationml.presentation // *.pptx
application/vnd.openxmlformats-officedocument.wordprocessingml.document // *.docx
```

### 参考文档

1. [https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#redirect-output-to-a-clients-web-browser](https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#redirect-output-to-a-clients-web-browser)
2. [ms office - PHP xls, xlsx, ppt, pptx headers - Stack Overflow](https://stackoverflow.com/questions/3318288/php-xls-xlsx-ppt-pptx-headers)
3. [php - Create a zip file and download it - Stack Overflow](https://stackoverflow.com/questions/12225964/create-a-zip-file-and-download-it)


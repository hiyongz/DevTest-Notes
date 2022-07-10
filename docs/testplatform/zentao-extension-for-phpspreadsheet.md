# 禅道二次开发（四）：集成

PhpSpreadsheet是一个PHP表格文件处理库，可用来读写excel文件，本文介绍如何在禅道中引入PhpSpreadsheet库，可以使用它来解析Excel文件，比如上传excel格式的测试用例、导出测试用例为excel格式等。



## 安装PhpSpreadsheet

PhpSpreadsheet要求PHP 7.3及以上版本，如果禅道使用的PHP版本低于7.3请不要使用它来处理excel格式文件。

由于禅道安装在centos7中，这里介绍如何在centos7中安装PhpSpreadsheet，另外顺便也记录一下在windows系统中安装phpspreadsheet的步骤。

### linux安装

这里介绍centos7中如何安装PhpSpreadsheet到禅道目录下。

#### 1. 安装composer

需要使用composer进行安装PhpSpreadsheet，先安装一下composer工具。

安装：

```bash
# 下载composer
$ curl -sS https://getcomposer.org/installer | php
All settings correct for using Composer
Downloading...

Composer (version 2.2.7) successfully installed to: /root/composer.phar
Use it: php composer.phar

# 将composer.phar文件移动到bin目录以便全局使用composer命令
$ mv composer.phar /usr/local/bin/composer

# 切换国内源
$ composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

```

#### 2. 卸载低版本PHP

卸载原来的低版本PHP：

```bash
$ rpm -qa|grep php
php-cli-5.4.16-48.el7.x86_64
php-common-5.4.16-48.el7.x86_64
php-5.4.16-48.el7.x86_64
$ rpm -e php-cli-5.4.16-48.el7.x86_64
错误：依赖检测失败：
        php-cli(x86-64) = 5.4.16-48.el7 被 (已安裝) php-5.4.16-48.el7.x86_64 需要
$ rpm -e php-5.4.16-48.el7.x86_64
警告：/etc/httpd/conf.d/php.conf 已另存为 /etc/httpd/conf.d/php.conf.rpmsave
$ rpm -e php-cli-5.4.16-48.el7.x86_64
$ rpm -e php-common-5.4.16-48.el7.x86_64

```

将禅道的PHP 加入环境变量：

```bash
vi /etc/profile

export PATH="$PATH:/opt/zbox/bin/"

source /etc/profile

```

#### 3. 安装phpspreadsheet

进入禅道目录安装phpspreadsheet：

```bash
$ cd /opt/zbox/app/zentao/lib
$ mkdir excel
$ cd excel
$ composer require phpoffice/phpspreadsheet
```

会自动安装到vendor目录下：

```bash
$ pwd
/opt/zbox/app/zentao/lib/excel/vendor
$ ls
autoload.php  composer  ezyang  maennchen  markbaker  myclabs  phpoffice  psr  symfony

```

### windows安装

我使用的是XAMPP软件包配置的PHP环境，和linux中一样，先安装PHP依赖管理工具composer。

#### 1. 安装composer

下载phar文件 `composer.phar`：[https://getcomposer.org/download/](https://getcomposer.org/download/)，复制到`D:\tools\xampp\php\pear` 目录下，创建 `composer.bat` 文件，编写代码：

```bash
@php %~dp0composer.phar %*
```

然后将 `D:\tools\xampp\php\pear`  目录添加到环境变量。

打开cmd窗口，执行 `composer -V` 查看是否安装成功：

```bash
$ composer -V
Composer version 2.3.3 2022-04-01 22:15:35
```

也可以下载 [Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe) 文件进行安装。

#### 2. 安装phpspreadsheet

进入  `D:\tools\xampp\php\pear`  目录下，执行：

```bash
composer require phpoffice/phpspreadsheet
```

如果报如下错误：

```php
Installation failed, deleting ./composer.json.

In RequireCommand.php line 210:

  No composer.json present in the current directory (./composer.json), this may be the cause of the following excepti
  on.


In PackageDiscoveryTrait.php line 308:

  Package phpoffice/phpspreadsheet has requirements incompatible with your PHP version, PHP extensions and Composer v
  ersion:
    - phpoffice/phpspreadsheet 1.22.0 requires ext-gd * but it is not present.
```

修改 `D:\tools\xampp\php\php.ini` 文件，取消 `extension=gd` 和 `extension=fileinfo` 的注释。

安装完成后执行 `composer info` 可看到安装的 `phpoffice/phpspreadsheet` 包。



## 禅道集成PhpSpreadsheet

PhpSpreadsheet安装到禅道目录后就可以使用它来处理excel文件了，先在module目录下创建模块excel，然后在`/module/excel` 创建文件model.php，编写读取Excel文件方法：

```php
<?php
require '/opt/zbox/app/zentao/lib/excel/vendor/autoload.php';
use PhpOffice\PhpSpreadsheet\IOFactory;
use PhpOffice\PhpSpreadsheet\Reader\Xlsx;
use PhpOffice\PhpSpreadsheet\Reader\Xls;
use PhpOffice\PhpSpreadsheet\Cell\Coordinate;

class excelModel extends model
{
    /**
     * Parse Excel.
     *
     * @param  string    $fileName
     * @access public
     * @return void
     */
    public function readexcel($fileName)    { 
        
        // $reader = new Xlsx();
        // $spreadsheet = $reader->load($fileName);
        $reader = IOFactory::createReader('Xlsx');
        $spreadsheet = $reader->load($fileName);
        
        // $datas = $spreadsheet->getActiveSheet()->toArray();
        $worksheet = $spreadsheet->getActiveSheet();
        $worksheetArray = $worksheet->toArray();
        
        }
}
```

PhpSpreadsheet的更多使用方法可参考官方文档：[https://phpspreadsheet.readthedocs.io/en/latest/](https://phpspreadsheet.readthedocs.io/en/latest/) 。

## 安装PHPExcel

简单介绍一下PHPExcel库的安装方法，和PhpSpreadsheet安装类似。

composer安装

```bash
composer require phpoffice/phpexcel
```

禅道引用：

```php
<?php
require "/opt/zbox/app/zentao/lib/phpexcel/vendor/phpoffice/phpexcel/Classes/PHPExcel.php";

$reader= PHPExcel_IOFactory::createReaderForFile($fileName);
$spreadsheet = $reader->load($fileName);
$worksheet  = $spreadsheet->getSheetByName(工作表名称);
$data = $worksheet->toArray();
```


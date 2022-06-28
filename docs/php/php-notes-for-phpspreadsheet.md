# PhpSpreadsheet读写Excel文件

本文介绍PhpSpreadsheet读写excel文件的一些使用方法。



## 简介
PhpSpreadsheet要求PHP 7.3及以上版本，是PHPExcel库的扩展版本，可用来读写xls、xlsx、CSV、HTML等格式文件。

| Format                                                       | Reading | Writing |
| ------------------------------------------------------------ | ------- | ------- |
| Open Document Format/OASIS (.ods)                            | ✓       | ✓       |
| Office Open XML (.xlsx) Excel 2007 and above                 | ✓       | ✓       |
| BIFF 8 (.xls) Excel 97 and above                             | ✓       | ✓       |
| BIFF 5 (.xls) Excel 95                                       | ✓       |         |
| SpreadsheetML (.xml) Excel 2003                              | ✓       |         |
| Gnumeric                                                     | ✓       |         |
| HTML                                                         | ✓       | ✓       |
| SYLK                                                         | ✓       |         |
| CSV                                                          | ✓       | ✓       |
| PDF (using either the TCPDF, Dompdf or mPDF libraries, which need to be installed separately) |         | ✓       |

PhpSpreadsheet安装方法可参考[禅道二次开发（四）：集成PhpSpreadsheet解析Excel文件]()

下面来介绍PhpSpreadsheet读写excel格式文件方法。

## 写入excel文件

以写入Xlsx格式文件为例，

```php
<?php

require 'vendor/autoload.php';
 
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

/* 写入excel */
$fileName = './test.xlsx';
$spreadsheet = new Spreadsheet();
$sheet = $spreadsheet->getActiveSheet();
$sheet->setCellValue('A1', 'Hello World !');
$sheet->setCellValue('C3', '你好 !');
 
$writer = new Xlsx($spreadsheet);
$writer->save($fileName);
?>
```

### 工作表默认样式

可以设置工作表默认样式，比如：

```php
$spreadsheet->getDefaultStyle()->getFont()->setName('宋体'); // 字体
$spreadsheet->getDefaultStyle()->getFont()->setSize(8); // 字体大小
$spreadsheet->getDefaultStyle()->getAlignment()->setWrapText(true); // 自动换行
$spreadsheet->getDefaultStyle()->getAlignment()->setVertical(Alignment::VERTICAL_CENTER); //垂直居中
```

### 单元格样式

```php
use PhpOffice\PhpSpreadsheet\Style\Alignment;

$spreadsheet->getActiveSheet()->getStyle('A1:D4')->getAlignment()->setWrapText(true); // 自动换行
$caseSpreadsheet->getActiveSheet()->getStyle('A1:D4')->getAlignment()->setVertical(Alignment::VERTICAL_CENTER); //垂直居中
```
单元格对齐方式包括水平对齐和垂直对齐：

```php
// 水平对齐样式
HORIZONTAL_GENERA
HORIZONTAL_LEFT
HORIZONTAL_RIGHT
HORIZONTAL_CENTER
HORIZONTAL_CENTER_CONTINUOUS
HORIZONTAL_JUSTIFY 
HORIZONTAL_FILL
HORIZONTAL_DISTRIBUTED // Excel2007 only

// 垂直对齐样式
VERTICAL_BOTTOM
VERTICAL_TOP
VERTICAL_CENTER
VERTICAL_JUSTIFY
VERTICAL_DISTRIBUTED  // Excel2007 only
```


除了设置单元格的字体，还可以设置边框，填充颜色等样式信息。

比如设置单元格背景颜色：

```php
$spreadsheet->getActiveSheet()->getStyle('E2')->getFill()
    ->setFillType(\PhpOffice\PhpSpreadsheet\Style\Fill::FILL_SOLID)
    ->getStartColor()->setARGB('FFFF0000');

// 多个单元格，如果设置多个单元格推荐此方法，性能更优。
$spreadsheet->getActiveSheet()->getStyle('B3:B7')->getFill()
    ->setFillType(\PhpOffice\PhpSpreadsheet\Style\Fill::FILL_SOLID)
    ->getStartColor()->setARGB('FFFF0000');
```

注意：颜色代码为ARGB，带了Alpha通道。

设置单元格高度，某一行高度：

```php
$spreadsheet->getActiveSheet()->getRowDimension('10')->setRowHeight(100);
$spreadsheet->getActiveSheet()->getDefaultRowDimension()->setRowHeight(15); // 默认行高
```

设置某列：

```php
// 设置列宽
$spreadsheet->getActiveSheet()
            ->getColumnDimension('A') 
            ->setWidth(30);
            
// 自动列宽
$spreadsheet->getActiveSheet()
            ->getColumnDimension('A')
            ->setAutoSize(true);

// 默认列宽
$spreadsheet->getActiveSheet()
            ->getDefaultColumnDimension() 
            ->setWidth(12); 
```



### 单元格数据类型

```php
use PhpOffice\PhpSpreadsheet\Cell\DataType;
$spreadsheet->getActiveSheet()->setCellValueExplicit("A1", "123", DataType::TYPE_STRING);

/*
TYPE_STRING2
TYPE_STRING
TYPE_FORMULA
TYPE_NUMERIC
TYPE_BOO
TYPE_NULL
TYPE_INLINE
TYPE_ERROR
*/
```

数字添加引号前缀：

```php
$spreadsheet->getActiveSheet()->setCellValueExplicit("A1", "123", DataType::TYPE_STRING);
$spreadsheet->getActiveSheet()->getStyle("A1")->setQuotePrefix(true);
// $spreadsheet->getActiveSheet()->getStyle("A1")->getNumberFormat()->setFormatCode(NumberFormat::FORMAT_TEXT);
```

设置数据有效性：

```php
use PhpOffice\PhpSpreadsheet\Cell\DataValidation;

$objValidation = $spreadsheet->getActiveSheet()->getCell('C1')->getDataValidation(); // 设置数据有效性的单元格
$objValidation -> setType(DataValidation::TYPE_LIST)
    -> setErrorStyle(DataValidation::STYLE_INFORMATION)
    -> setAllowBlank(false)
    -> setShowInputMessage(true)
    -> setShowErrorMessage(true)
    -> setShowDropDown(true)
    -> setErrorTitle('错误提示')
    -> setError('您输入的值有误')
    -> setPromptTitle('结果')
    -> setFormula1('"成功,失败"');
```

### 冻结单元格

```php
$sheet = $spreadsheet->getActiveSheet();
$sheet->freezePane('A2'); // 冻结第一行
$sheet->freezePane('B1'); // 冻结第一列
$sheet->freezePane('B3'); // 冻结B3单元格
```

### 单元格条件格式

可以设置单元格的条件格式，可以对满足某个条件的单元格设置样式，比如设置大于80的单元格：

```php
$conditional = new \PhpOffice\PhpSpreadsheet\Style\Conditional();
$conditional->setConditionType(\PhpOffice\PhpSpreadsheet\Style\Conditional::CONDITION_CELLIS);
$conditional->setOperatorType(\PhpOffice\PhpSpreadsheet\Style\Conditional::OPERATOR_GREATERTHAN);
$conditional->addCondition(80);
$conditional->getStyle()->getFont()->getColor()->setARGB(\PhpOffice\PhpSpreadsheet\Style\Color::COLOR_DARKGREEN);
$conditional->getStyle()->getFill()->setFillType(\PhpOffice\PhpSpreadsheet\Style\Fill::FILL_SOLID);
$conditional->getStyle()->getFill()->getStartColor()->setARGB(\PhpOffice\PhpSpreadsheet\Style\Color::COLOR_GREEN);

$conditionalStyles = $spreadsheet->getActiveSheet()->getStyle('A1:A10')->getConditionalStyles();
$conditionalStyles[] = $conditional;

$spreadsheet->getActiveSheet()->getStyle('A1:A10')->setConditionalStyles($conditionalStyles);
```

可以使用的条件及操作符：

```php
// Condition types
CONDITION_NONE
CONDITION_CELLIS
CONDITION_CONTAINSTEXT
CONDITION_EXPRESSION
CONDITION_CONTAINSBLANKS
CONDITION_NOTCONTAINSBLANKS
CONDITION_DATABAR
CONDITION_NOTCONTAINSTEXT

// Operator types
OPERATOR_NONE
OPERATOR_BEGINSWITH
OPERATOR_ENDSWITH
OPERATOR_EQUA
OPERATOR_GREATERTHAN
OPERATOR_GREATERTHANOREQUAL
OPERATOR_LESSTHAN
OPERATOR_LESSTHANOREQUAL
OPERATOR_NOTEQUAL
OPERATOR_CONTAINSTEXT
OPERATOR_NOTCONTAINS
OPERATOR_BETWEEN
OPERATOR_NOTBETWEEN
```

### 写入图片

将图片写入某个单元格中：

```php
$drawing = new \PhpOffice\PhpSpreadsheet\Worksheet\Drawing();
$drawing->setName('Logo');
$drawing->setDescription('Logo');
$drawing->setPath($diagramPath);
$drawing->setHeight(120);
$drawing->setCoordinates("D2");

$drawing->setOffsetX(0);
$drawing->setRotation(0);
$drawing->getShadow()->setVisible(true);
$drawing->getShadow()->setDirection(0);
$drawing->setWorksheet($spreadsheet->getActiveSheet());
```

### 设置超链接

给单元格设置超链接：

```php
$spreadsheet->getActiveSheet()->getCell('B2')->getHyperlink()->setUrl("sheet://'Sheetname'!A1"); // 当前文档位置
$spreadsheet->getActiveSheet()->getCell('B2')->getHyperlink()->setUrl("https://www.baidu.com/"); // 外链地址
```



## 读取excel文件

下面介绍读取excel文件方法。

### 读取文本数据

```php
<?php

require 'vendor/autoload.php';
 
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

/* 读取excel */
// $reader = new Xlsx();
// $spreadsheet = $reader->load($fileName);
$reader = IOFactory::createReader('Xlsx');
$spreadsheet = $reader->load($fileName);
// $reader->setReadDataOnly(true); // 设置后无法获取excel中的图片

$worksheet = $spreadsheet->getActiveSheet();
// $worksheet   = $spreadsheet->getSheetByName('testcase');
// $rawCasedata = $worksheet->toArray();
$highestRow  = $worksheet->getHighestRow(); // 取得总行数
$highestColumn = $worksheet->getHighestColumn(); // 取得总列数
$highestColumnIndex = Coordinate::columnIndexFromString($highestColumn); // 取得总列数

$excelData = [];
for ($row = 1; $row <= $highestRow; $row++) {
    for ($col = 1; $col <= $highestColumnIndex; $col++) {
        $excelData[$row][] = (string)$worksheet->getCellByColumnAndRow($col, $row)->getValue();
    }
}

echo "<pre>";
print_r($excelData);
echo "</pre>";

?>
```

结果：

```php
Array
(
    [1] => Array
        (
            [0] => Hello World !
            [1] => 
            [2] => 
        )

    [2] => Array
        (
            [0] => 
            [1] => 
            [2] => 
        )

    [3] => Array
        (
            [0] => 
            [1] => 
            [2] => 你好 !
        )

)
```

### 读取图片

读取Excel文件中的图片，支持png、gif和jpg格式图片：

```php
<?php

require 'vendor/autoload.php';
 
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\IOFactory;
use PhpOffice\PhpSpreadsheet\Cell\Coordinate;

$fileName = './test.xlsx';
$reader = IOFactory::createReader('Xlsx');
$spreadsheet = $reader->load($fileName);
$worksheet = $spreadsheet->getActiveSheet();

/* 读取excel中的图片 */
$imgpath = './';
$imgArray = array();
foreach ($worksheet->getDrawingCollection() as $drawing) {
    list($startColumn, $startRow) = Coordinate::coordinateFromString($drawing->getCoordinates());
    print_r($startColumn);
    print_r($startRow);
    switch ($drawing->getExtension()) {
    case 'jpeg':
        $source = imagecreatefromjpeg($drawing->getPath());
        $imgname = $imgpath . $drawing->getCoordinates() . '.jpg';
        imagejpeg($source, $imgname);
        break;
    case 'png':
        $source = imagecreatefrompng($drawing->getPath());
        $imgname = $imgpath . $drawing->getCoordinates() . '.png';
        imagepng($source, $imgname);
        break;
    default:  
        echo "Unsupported file type: " . $drawing->getExtension() . "\n";;              
    }
}
```

### 读取超链接

读取超链接：

```php
$spreadsheet = $reader->load($fileName);
$worksheet = $spreadsheet->getActiveSheet();
$spreadsheet->getActiveSheet()->getCell('A1')->hasHyperlink();  // 判断是否有超链接
$url = $spreadsheet->getActiveSheet()->getCell('A1')->getHyperlink()->getUrl(); // 读取超链接

```







## 下载文件

在服务器上创建了excel文件后，可以将它下载到客户端。

```php
// redirect output to client browser
header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
header("Content-Disposition: attachment;filename=$downloadFileName");
header('Cache-Control: max-age=0');
$writer    = new PhpOffice\PhpSpreadsheet\Writer\Xlsx($spreadsheet);
$writer->save('php://output');
```

当然也可以下载已经生成的xlsx格式文件：

```php
$FileName = basename($FilePath);
header("Content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"); 
header("Content-Disposition: attachment; filename=$FileName");
header("Content-length: " . filesize($FilePath));
header("Pragma: no-cache"); 
header("Expires: 0"); 
readfile("$FilePath");
```

xls格式文件类型为：`application/vnd.ms-excel` 。

这里就介绍这么多了，PhpSpreadsheet的更多使用方法可参考官方文档：[https://phpspreadsheet.readthedocs.io/en/latest/](https://phpspreadsheet.readthedocs.io/en/latest/)。



## 参考资料

1. github地址：[https://github.com/PHPOffice/PhpSpreadsheet](https://github.com/PHPOffice/PhpSpreadsheet)
2. PhpSpreadsheet文档地址：[https://phpspreadsheet.readthedocs.io/en/latest/](https://phpspreadsheet.readthedocs.io/en/latest/)
3. 设置自动换行：https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#alignment-and-wrap-text
4. https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#formatting-cells
5. 某一行高度：https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#setting-a-rows-height
6. 默认高度：https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#setting-the-default-row-height
7. 写入图片：https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#add-a-drawing-to-a-worksheet
8. https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#conditional-formatting-a-cell
9. https://phpspreadsheet.readthedocs.io/en/latest/topics/conditional-formatting/
10. 下载excel文件：https://phpspreadsheet.readthedocs.io/en/latest/topics/recipes/#redirect-output-to-a-clients-web-browser

<center><b>--THE END--<b></center>

> 说人坏话只能说明自己也同样抱有小气的本性。——太宰治《人间失格》
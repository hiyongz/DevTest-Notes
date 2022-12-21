# PHP笔记（三）：数组相关操作方法


本文记录一些PHP数组处理的方法。



## 1. 检查数组中是否存在某个值

[in_array](https://www.php.net/manual/zh/function.in-array.php)(mixed `$needle`, array `$haystack`, bool `$strict` = **`false`**): bool

- 检查数组中是否存在某个值
- 如果 `strict` 的值为 **`true`** ，还会检查 `needle` 的[类型](https://www.php.net/manual/zh/language.types.php)是否和 `haystack` 中的相同。

举例：

```php
<?php
    
/* in_array */
$array1 = ['one', 'two', 'three', 'four', 'five'];
if (in_array("one", $array1)) {
    echo "Got one";
}
?>
```

结果：

```php
Got one
```

## 2. 检查数组或者变量方法

变量检查：

- [isset()](https://www.php.net/manual/zh/function.isset.php) - 检测变量是否已声明并且其值不为 null，释放变量使用 [unset()](https://www.php.net/manual/zh/function.unset.php) 方法。
- [defined()](https://www.php.net/manual/zh/function.defined.php) - 检查某个名称的常量是否存在
- [empty()](https://www.php.net/manual/zh/function.empty.php) - 检查一个变量是否为空，PHP中的“空”元素包括：空字符串`""`、数字`0` 、浮点数`0.0` 、字符串`"0"` 、**`null`**、**`false`**、空数组`array()` 、声明了但没有值的变量`$var`。
- [is_null()](https://www.php.net/manual/zh/function.is-null.php) - 检测变量是否为 null。
- [property_exists()](https://www.php.net/manual/zh/function.property-exists.php) - 检查对象或类是否具有该属性。
- [method_exists()](https://www.php.net/manual/zh/function.method-exists.php) - 检查类的方法是否存在。

数组检查：

- [array_keys](https://www.php.net/manual/zh/function.array-keys.php)(`$array`) - 返回数组中所有键名。
- [array_keys](https://www.php.net/manual/zh/function.array-keys.php)(`$array`, `$search_value`):  返回`search_value` 值的键名。
- [array_key_exists](https://www.php.net/manual/zh/function.array-key-exists.php)( `$key`,  `$array`) - 检查数组里是否有指定的键名或索引。
- [array_search](https://www.php.net/manual/zh/function.array-search.php)(`$needle`,  `$haystack`) - 在数组 `$haystack` 中搜索给定的值`$needle`，返回相应的键名。



## 3. 过滤数组元素

[array_filter](https://www.php.net/manual/zh/function.array-filter.php)(array `$array`, ?[callable](https://www.php.net/manual/zh/language.types.callable.php) `$callback` = **`null`**, int `$mode` = 0): array

-  `array` 数组中的每个值会传递给 `callback` 回调函数，如果 `callback` 回调函数返回 **`true`**，则将 `array` 数组中的当前值返回到结果 array 数组中。
- 如果不设置 `callback` 回调函数，会删除数组 `array` 中的所有“空”元素。
- 过滤后的array 数组键名不会重新索引，可以使用 [array_values()](https://www.php.net/manual/zh/function.array-values.php) 函数对数组进行重新索引。
- `$mode = 0` - 默认值，接受值作为唯一参数
- `$mode = ARRAY_FILTER_USE_KEY` - 接受键名作为唯一参数
- `$mode = ARRAY_FILTER_USE_BOTH` - 同时接受键名和键值

举例：

```php
<?php

/* array_filter */
$array1 = [0 => '', 1 => 'one', 2 => 'two', 3 => 'three', 4 => 'four', 5 => 'five'];
$array1 = array_filter($array1);
echo "<pre>";
print_r($array1);
echo "</pre>";

/* array_values */
$array1 = array_values($array1);  // 重新索引
echo "<pre>";
print_r($array1);
echo "</pre>";


function odd($var)
{
    return $var & 1;
}
function even($var)
{
    return !($var & 1);
}

$array1 = ['one' => 1, 'two' => 2, 'three' => 3, 'four' => 4, 'five' => 5];
$array_even = array_filter($array1, "even");
$array_odd = array_filter($array1, "odd");
echo "<pre>";
print_r($array_even);
echo "</pre>";
echo "<pre>";
print_r($array_odd);
echo "</pre>";


$array2 = [1 => 'one', 2 => 'two', 3 => 'three', 4 => 'four', 5 => 'five'];
$array_even = array_filter($array2,function($var){ return(!($var & 1));},ARRAY_FILTER_USE_KEY);
$array_odd = array_filter($array2,function($var){ return($var & 1);},ARRAY_FILTER_USE_KEY);
echo "<pre>";
print_r($array_even);
echo "</pre>";
echo "<pre>";
print_r($array_odd);
echo "</pre>";
?>

```

结果：

```php
Array
(
    [1] => one
    [2] => two
    [3] => three
    [4] => four
    [5] => five
)
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
    [4] => five
)
Array
(
    [two] => 2
    [four] => 4
)
Array
(
    [one] => 1
    [three] => 3
    [five] => 5
)
Array
(
    [2] => two
    [4] => four
)
Array
(
    [1] => one
    [3] => three
    [5] => five
)
```

## 4. 删除数组元素

① [array_pop](https://www.php.net/manual/zh/function.array-pop.php)(array `&$array`) - 删除数组最后一个元素

举例：

```php
<?php
    
/* array_pop */
$array1 = ['one', 'two', 'three', 'four', 'five'];
$last = array_pop($array1);
echo "<pre>";
print_r($array1);
echo "</pre>";

?>
```
结果：

```php
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
)
```

② [array_shift](https://www.php.net/manual/zh/function.array-shift.php)(array `&$array`) - 将数组开头的单元移出数组并作为结果返回

举例：

```php
<?php
    
/* array_shift */
$array1 = ['one', 'two', 'three', 'four', 'five'];
$first = array_shift($array1);
echo "<pre>";
print_r($array1);
echo "</pre>";

?>
```
结果：

```php
Array
(
    [0] => two
    [1] => three
    [2] => four
    [3] => five
)
```

## 5. 插入数组元素

① [array_unshift](https://www.php.net/manual/zh/function.array-unshift.php)(`&$array`, `...$values`) - 在数组开头插入一个或多个元素

举例：

```php
<?php    
/* array_unshift */
$array1 = ['one', 'two', 'three', 'four', 'five'];
array_unshift($array1, '0', 'zero');
echo "<pre>";
print_r($array1);
echo "</pre>";

?>
```
结果：

```php
Array
(
    [0] => 0
    [1] => zero
    [2] => one
    [3] => two
    [4] => three
    [5] => four
    [6] => five
)
```

② [array_push](https://www.php.net/manual/zh/function.array-push.php)(`&$array`, `...$values`) - 将一个或多个单元压入数组的末尾（入栈）

建议直接使用 `$array[] = `追加元素。

举例：

```php
<?php    
/* array_push */
$array1 = ['one', 'two', 'three', 'four', 'five'];
array_push($array1, 'six', 'seven');
$array1[] = 'eight';
echo "<pre>";
print_r($array1);
echo "</pre>";

?>
```
结果：

```php
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
    [4] => five
    [5] => six
    [6] => seven
    [7] => eight
)
```

③ [array_merge](https://www.php.net/manual/zh/function.array-merge.php)(`...$arrays`) — 合并一个或多个数组

举例：

```php
<?php    
/* array_merge */
$array1 = ['one', 'two', 'three'];
$array2 = ['four', 'five'];
$array3 = array_merge($array1, $array2);
$array1[] = 'eight';
echo "<pre>";
print_r($array3);
echo "</pre>";

?>
```
结果：

```php
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
    [4] => five
)
```

## 6. 返回数组最后一个元素

[end](https://www.php.net/manual/zh/function.end.php)(`&$array`) - 将 `array` 的内部指针移动到最后一个单元并返回其值。

[array_key_last](https://www.php.net/manual/zh/function.array-key-last.php)(`$array`) - 获取一个数组的最后一个键值

举例：

```php
<?php
/* end */
$array1 = ['one', 'two', 'three'];
$last = end($array1);
echo "<pre>";
print_r($last);
echo "</pre>";

echo current($array1) . "<br />\n"; // 返回数组中的当前值
reset($array1); // 将数组的内部指针指向第一个单元
echo current($array1) . "<br />\n";
next($array1); // 将数组的内部指针向后移动一位
echo current($array1) . "<br />\n";
prev($array1); // 将数组的内部指针向前移动一位
echo current($array1) . "<br />\n";

/* array_key_last */
$array1 = ['one', 'two', 'three'];
$last = array_key_last($array1);
echo "<pre>";
print_r($last);
echo "</pre>";
    
?>
```

结果：

```php
three
three
one
two
one
2
```



## 7. 数组切片

[array_slice](https://www.php.net/manual/zh/function.array-slice.php)( `$array`,   `$offset`,  `$length` = **`null`**,  `$preserve_keys` = **`false`**
) - 返回根据 `offset` 和 `length` 参数所指定的 `array` 数组中的一段序列。

举例：

```php
<?php
/* array_slice */
$array1 = ['one', 'two', 'three', 'four', 'five'];
$output = array_slice($array1, 2);  
print_r($output) ;
echo "<br />\n";

$output = array_slice($array1, -3, 2);  // 返回 "d"
print_r($output) ;
echo "<br />\n";

$output = array_slice($array1, 0, 3); 
print_r($output) ;
echo "<br />\n";

$output = array_slice($array1, 1, -3); 
print_r($output) ;
echo "<br />\n";

$output = array_slice($array1, 1, 3); 
print_r($output) ;
echo "<br />\n";

$output = array_slice($array1, 1, 3, true); 
print_r($output) ;
echo "<br />\n";
?>
```

结果：

```php
Array ( [0] => three [1] => four [2] => five )
Array ( [0] => three [1] => four )
Array ( [0] => one [1] => two [2] => three )
Array ( [0] => two )
Array ( [0] => two [1] => three [2] => four )
Array ( [1] => two [2] => three [3] => four )
```

## 8. 判断两个数组是否相等

[array_diff](https://www.php.net/manual/zh/function.array-diff.php)( `$array`,  `...$arrays`) - 返回在 `array` 中但是不在其他 array 里的值。可用于判断两个数组是否相等。

[array_diff_key](https://www.php.net/manual/zh/function.array-diff-key.php)( `$array`,  `...$arrays`) - 返回在 `array` 中但是未出现在任何其它数组中的键名的值。

举例：

```php
<?php
/* array_diff */
$array1 = ['one', 'two', 'three'];
$array2 = ['one', 'two', 'three', 'four', 'five'];
$output1 = array_diff($array1, $array2);
$output2 = array_diff($array2, $array1);
if (empty($output1) and empty($output2)) {
    echo "The arrays are equal";
} else {
    echo "The arrays are not equal";
}

?>
```

结果：

```php
The arrays are not equal
```

## 9. 替换数组元素

[array_replace](https://www.php.net/manual/zh/function.array-replace.php)( `$array`, `...$replacements`) - 使用传递的数组替换第一个数组的元素

举例：

```php
<?php
/* array_replace */
$array1 = ['one', 'two', 'three'];
$array2 = ['four', 'five', 'six'];
$output = array_replace($array1, $array2);
echo "<pre>";
print_r($output);
echo "</pre>";

$array1 = ['one', 'two', 'three', '', '', ''];
$array2 = ['', '', '', 'four', 'five', 'six'];
$output = array_replace($array1,array_slice($array2,3,null,$preserve_keys = true));
echo "<pre>";
print_r($output);
echo "</pre>";

?>
```

结果：

```php
Array
(
    [0] => four
    [1] => five
    [2] => six
)
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
    [4] => five
    [5] => six
)
```



## 10. 移除数组重复元素

[array_unique](https://www.php.net/manual/zh/function.array-unique.php) - 移除数组中重复的值

举例：

```php
<?php
/* array_unique */
$array1 = ['one', 'two', 'three', 'four', 'five', 'five'];
$output = array_unique($array1);
echo "<pre>";
print_r($output);
echo "</pre>";

?>
```

结果：

```php
Array
(
    [0] => one
    [1] => two
    [2] => three
    [3] => four
    [4] => five
)
```

## 11. 数组排序

常用排序函数如下表：

| 函数名称                                                     | 排序依据 | 数组索引键保持                    | 排序的顺序               |
| :----------------------------------------------------------- | :------- | :-------------------------------- | :----------------------- |
| [array_multisort()](https://www.php.net/manual/zh/function.array-multisort.php) | 值       | string 键保持不变，int 键重新索引 | 第一个数组或者由选项指定 |
| [asort()](https://www.php.net/manual/zh/function.asort.php)  | 值       | 是                                | 升序：根据键值升序排序   |
| [arsort()](https://www.php.net/manual/zh/function.arsort.php) | 值       | 是                                | 降序                     |
| [krsort()](https://www.php.net/manual/zh/function.krsort.php) | 键       | 是                                | 降序                     |
| [ksort()](https://www.php.net/manual/zh/function.ksort.php)  | 键       | 是                                | 升序：根据键名升序排序   |
| [natcasesort()](https://www.php.net/manual/zh/function.natcasesort.php) | 值       | 是                                | 自然排序，大小写不敏感   |
| [natsort()](https://www.php.net/manual/zh/function.natsort.php) | 值       | 是                                | 自然排序                 |
| [rsort()](https://www.php.net/manual/zh/function.rsort.php)  | 值       | 否                                | 降序                     |
| [shuffle()](https://www.php.net/manual/zh/function.shuffle.php) | 值       | 否                                | 随机                     |
| [sort()](https://www.php.net/manual/zh/function.sort.php)    | 值       | 否                                | 升序                     |
| [uasort()](https://www.php.net/manual/zh/function.uasort.php) | 值       | 是                                | 由用户定义               |
| [uksort()](https://www.php.net/manual/zh/function.uksort.php) | 键       | 是                                | 由用户定义               |
| [usort()](https://www.php.net/manual/zh/function.usort.php)  | 值       | 否                                | 由用户定义               |

例1：asort

```php
<?php
/* asort */
$array1 = ['two' => 2, 'one' => 1, 'four' => 4, 'three' => 3, 'five' => 5];
asort($array1);
echo "<pre>";
print_r($array1);
echo "</pre>";
?>
```

结果：

```php
Array
(
    [one] => 1
    [two] => 2
    [three] => 3
    [four] => 4
    [five] => 5
)
```

例2：ksort

```php
/* ksort */
$array1 = [1 => 'one', 3 => 'three', 2 => 'two', 5 => 'five', 4 => 'four'];
ksort($array1);
echo "<pre>";
print_r($array1);
echo "</pre>";
?>
```

结果：

```php
Array
(
    [1] => one
    [2] => two
    [3] => three
    [4] => four
    [5] => five
)
```

例3：array_multisort()多维数组排序

```php
$records = array(
    array(
        'id' => 2,
        'name' => 'zhangsan',
    ),
    array(
        'id' => 1,
        'name' => 'lishi',
    ),
    array(
        'id' => 3,
        'name' => 'wanger',
    )
);

$ids = array_column($records, 'id');
array_multisort($ids, SORT_DESC, $records); // 根据id进行降序排序
// array_multisort($ids, SORT_DESC, SORT_NUMERIC, $records); // 按照数字大小比较 SORT_STRING - 按照字符串比较

echo "<xmp class='a-left'>";
print_r($records);
echo "</xmp>";
```

结果：

```php
Array
(
    [0] => Array
        (
            [id] => 3
            [name] => wanger
        )

    [1] => Array
        (
            [id] => 2
            [name] => zhangsan
        )

    [2] => Array
        (
            [id] => 1
            [name] => lishi
        )

)
```



## 12.读取多维数组某一列的值

[array_column](https://www.php.net/manual/zh/function.array-column)方法可用来读取多维数组或对象数组某一列的值。

```php
$records = array(
    array(
        'id' => 1,
        'name' => 'zhangsan',
    ),
    array(
        'id' => 2,
        'name' => 'lishi',
    ),
    array(
        'id' => 3,
        'name' => 'wanger',
    )
);

echo "<xmp class='a-left'>";
print_r($records);
echo "</xmp>";

$names = array_column($records, 'name', 'id');
echo "<xmp class='a-left'>";
print_r($names);
echo "</xmp>";
```

结果：

```php
Array
(
    [0] => Array
        (
            [id] => 1
            [name] => zhangsan
        )

    [1] => Array
        (
            [id] => 2
            [name] => lishi
        )

    [2] => Array
        (
            [id] => 3
            [name] => wanger
        )

)
Array
(
    [1] => zhangsan
    [2] => lishi
    [3] => wanger
)
```

参考资料：

1. 数组排序：[https://www.php.net/manual/zh/array.sorting.php](https://www.php.net/manual/zh/array.sorting.php)
2. [https://www.php.net/manual/zh/book.array.php](https://www.php.net/manual/zh/book.array.php)





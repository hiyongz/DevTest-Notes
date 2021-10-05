# Linux Bash编程：将整数分解为n个随机数
本文介绍使用shell实现将一个整数m随机分解为n个数。

<!--more-->

要求：
1. 将一个整数m分解为n个随机数，n个随机数之和要等于m
2. 指定随机数的最小值

分析：

这与leetcode上的两道题类似：

1. [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)

2. [剑指 Offer 14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)

下面来介绍一种思路：

1. 随机抽取 `n-1` 个区间为`(0,  m)`的数，得到数组`a`
2. 将`0`和`m`加入数组`a`中
3. 对数组`a`进行升序排序
4. 按顺序计算数组`a`中相邻元素的差值：后一个元素减去前一个元素。差值组成的数组就是我们要的结果。


shell脚本SplitInteger.sh：
```bash
#!/bin/bash

SplitInteger()
{    
    let SIZE_BYTES=$SIZE_BYTES-$NUMBER*$minNum
    declare -a num_list
    num_list[0]=0
    num_list[1]=$SIZE_BYTES
    let num=$NUMBER
    for i in $(seq 2 $num); do
        random_rate=`echo "scale=4 ; ${RANDOM}/32767" | bc -l` # 生成0-1的随机数 
        # let random_bytes=$(( SIZE_BYTES*random_rate ))
        random_bytes=`echo "$SIZE_BYTES*$random_rate" | bc` # 字符类型转换为数字类型进行运算
        # echo "$random_bytes"
        num_list[$i]=`echo $random_bytes | xargs printf "%.*f\n" 0` # 对结果进行四舍五入计算
    done

    # echo "Array in unsorted order :"
    # echo ${num_list[*]}

    num_length=${#num_list[*]}
    BubbleSort   # 排序

    # 计算差值

    let rand_len=$num_length-2
    for i in $(seq 0 $rand_len); do
        new_list[$i]=`echo "${num_list[$(( i+1 ))]}-${num_list[$i]}+$minNum" | bc`
    done

    # echo "Diff Array:"
    echo "${new_list[*]}"

    sum=0
    for (( i=0;i<${#new_list[*]};i++ ))
    do
        let sum=sum+${new_list[$i]}
    done

    echo $sum

}

let SIZE_BYTES=100
let NUMBER=10
let minNum=5
SplitInteger
exit 0
```
执行：
```bash
$ sh SplitInteger.sh 
8 12 6 16 9 12 11 9 5 12
100
```

`BubbleSort`为冒泡排序方法，具体实现参考[Linux Bash编程：字符串处理](https://blog.csdn.net/u010698107/article/details/119855830)。






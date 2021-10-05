# Linux Bash编程：Fisher–Yates shuffle 洗牌算法
本文介绍使用shell语法来实现Fisher–Yates shuffle 洗牌算法。

<!--more-->

## Fisher-Yates shuffle 算法简介

Fisher–Yates shuffle 洗牌算法可以用于对数组进行随机排列，它的时间复杂度为O(n)，伪代码如下：

```bash
To shuffle an array a of n elements (indices 0..n-1):
for i from n - 1 downto 1 do
	j = random integer with 0 <= j <= i
	exchange a[j] and a[i]
```


假定有一个数组a=[1, 2, 3, 4, 5, 6, 7, 8, 9]，数组长度为n，打乱a中元素的具体迭代步骤如下：
1. 生成一个[0, n-1]区间的随机数k；
2. 将第k个元素和第n-1个元素进行交换；
3. 进行下一轮迭代，生成一个[0, n-2]区间的随机数k，将第k个元素和第n-2个元素进行交换， 迭代次数为n-1次：从n-1取到1；
4. 最终得到一个打乱的数组。

下表是一个数组的具体打乱过程，打乱后的数组是(9 4 8 1 2 3 5 6 7)

| 随机数 | 原数组                  | 新数组                               |
| ------ | ----------------------- | ------------------------------------ |
| 0-8：6 | a = (1 2 3 4 5 6 7 8 9) | 交换a[8]和a[6] ：(1 2 3 4 5 6 9 8 7) |
| 0-7：5 | a = (1 2 3 4 5 6 9 8 7) | 交换a[7]和a[5] ：(1 2 3 4 5 8 9 6 7) |
| 0-6：4 | a = (1 2 3 4 5 8 9 6 7) | 交换a[6]和a[4] ：(1 2 3 4 9 8 5 6 7) |
| 0-5：2 | a = (1 2 3 4 9 8 5 6 7) | 交换a[5]和a[2] ：(1 2 8 4 9 3 5 6 7) |
| 0-4：1 | a = (1 2 8 4 9 3 5 6 7) | 交换a[4]和a[1] ：(1 9 8 4 2 3 5 6 7) |
| 0-3：0 | a = (1 9 8 4 2 3 5 6 7) | 交换a[3]和a[0] ：(4 9 8 1 2 3 5 6 7) |
| 0-2：2 | a = (4 9 8 1 2 3 5 6 7) | 交换a[2]和a[2] ：(4 9 8 1 2 3 5 6 7) |
| 0-1：0 | a = (4 9 8 1 2 3 5 6 7) | 交换a[1]和a[0] ：(9 4 8 1 2 3 5 6 7) |

## shell实现

shuffle.sh : 

```bash
#!/bin/bash

shuffle() {
   local i tmp size max rand
   # 打乱顺序
   # Knuth-Fisher-Yates shuffle algorithm
   size=${#my_array[*]}
   max=$(( 32767 / size * size ))
   # echo "max: $max"
   for ((i=size-1; i>0; i--)); do
      while (( (rand=$RANDOM) >= max )); do :; done
      rand=$(( rand % (i+1) ))    
      # 交换
      tmp=${my_array[i]} 
      my_array[i]=${my_array[rand]} 
      my_array[rand]=$tmp
      echo ${my_array[*]}
   done
}

my_array=(1 2 3 4 5 6 7 8 9)
shuffle
echo ${my_array[*]}
```

执行效果：

```bash
$ sh shuffle.sh 
1 2 3 4 9 6 7 8 5
1 8 3 4 9 6 7 2 5
7 8 3 4 9 6 1 2 5
7 8 6 4 9 3 1 2 5
7 8 6 9 4 3 1 2 5
7 9 6 8 4 3 1 2 5
7 6 9 8 4 3 1 2 5
7 6 9 8 4 3 1 2 5
```



参考：

1. https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
2. https://gaohaoyang.github.io/2016/10/16/shuffle-algorithm/#top
3. https://stackoverflow.com/questions/5533569/simple-method-to-shuffle-the-elements-of-an-array-in-bash-shell






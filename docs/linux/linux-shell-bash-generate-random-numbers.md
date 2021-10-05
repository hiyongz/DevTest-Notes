# 随机数生成、对浮点数进行四舍五入运算
本文介绍使用shell实现随机数生成以及对浮点数进行四舍五入运算

<!--more-->



## 随机数生成
### 生成0-1之间的随机数

生成0-1的随机数：
```bash
#!/bin/bash
random_number=`echo "scale=4 ; ${RANDOM}/32767" | bc -l` # 生成0-1的随机数
# random_number=`bc -l <<< "scale=4 ; ${RANDOM}/32767"`
echo $random_number

exit 0
```
执行：
```bash
$ sh random.sh 
.8696
$ sh random.sh 
.4517
$ sh random.sh 
.5126
```

- `${RANDOM}`函数产生0 - 32767之间的伪随机整数。其中32767（2^15 - 1）是有符号16位整数的上限。
- `scale=4`：保留4位小数

### 生成0-n之间的随机数
生成0-10之间的随机数：
```bash
#!/bin/bash
size=10
max=$(( 32767 / size * size ))
while (( (rand=$RANDOM) >= max )); do :; done
rand=$(( rand % (size+1) )) 
echo $rand
```
生成1-10之间的随机数：
```bash
#!/bin/bash
size=10
max=$(( 32767 / size * size ))
while (( (rand=$RANDOM) >= max )); do :; done
rand=$(( rand % (size) + 1 )) 
echo $rand
```

`max=$(( 32767 / size * size ))`语句比较关键，这么处理的原因是${RANDOM}产生的最大数是32767，如果生成1-10之间的随机数，需要去掉32761-32767之间的数，否则会导致出现9和10的概率和其它数不一样。

## 对浮点数进行四舍五入运算

可以使用 `printf "%.*f\n" [精度] [浮点数]` 命令对浮点数进行四舍五入运算。

```bash
$ printf "%.*f\n" 0 6.666
7
$ printf "%.*f\n" 1 6.666
6.7
$ printf "%.*f\n" 2 6.666
6.67
```

bash脚本示例：

```bash
#!/bin/bash

random_number=`echo "scale=4 ; ${RANDOM}/32767" | bc -l` # 生成0-1的随机数
number=`echo "$random_number*100" | bc`
echo $number
number_round1=`echo $number | xargs printf "%.*f\n" 0`
echo $number_round1

number_round2=`echo $number | xargs printf "%.*f\n" 1`
echo $number_round2

exit 0
```

执行结果如下：

```bash
97.8900
98
97.9
```



**参考：**

1. https://unix.stackexchange.com/questions/167058/how-to-round-floating-point-numbers-in-shell












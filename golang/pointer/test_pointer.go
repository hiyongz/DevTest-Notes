package main

import "fmt"

func main() {	
	var num *int // 定义指针
	num = new(int)
	*num = 20
	fmt.Println("pointer num: ", num) 
	fmt.Println("value of num: ", *num) 

	str1 := "Hello world !" // 初始化
	p := &str1   // 对变量str1取地址，并把地址赋给p，p就是一个指针，指向str1的值
	fmt.Println("pointer p: ", p) 
	fmt.Println("value of p: ", *p)  // 对指针取值，得到p指向的值

	*p = "test"        // 通过指针赋值，Golang的指针不能参与算术运算
	fmt.Println("pointer p: ", p) 
	fmt.Println("value of p: ", *p) 
}
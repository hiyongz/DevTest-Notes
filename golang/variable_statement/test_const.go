package main

import (
	"fmt"
)

func main() {
	const name string = "zhangsan"
	fmt.Println(name)

	const course1, course2 = "math", "english"
	fmt.Println(course1, course2)

	const age = 20
	age = age + 1 // 不能改变age
	fmt.Println(age)
}
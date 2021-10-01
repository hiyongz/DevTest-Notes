package main

import (
	"fmt"
)

func main() {
	var name string = "zhangsan"
	fmt.Println(name)

	var hight float32
	fmt.Println(hight)

	var course1, course2 = "math", "english"
	fmt.Println(course1, course2)

	age := 20
	age = age + 1
	fmt.Println(age)

	var (
		name1 string = "zhangsan"
		name2 string = "lishi"
	)
	fmt.Println(name1, name2)
}
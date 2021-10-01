package main

import (
	"fmt"
)


func test_if() {
	var grade = 70
	if grade >= 90 {
		fmt.Println("A" )
	} else if grade < 90 && grade >= 80 {
		fmt.Println("B" )
	} else if grade < 80 && grade > 60 {
		fmt.Println("C" )
	} else {
		fmt.Println("D" )
	}
}

func test_switch() {

	var grade = "B"

	switch grade {
	case "A":
		fmt.Println("优秀")
	case "B":
		fmt.Println("良好")
		fallthrough
	case "C":
		fmt.Println("中等")
	default:
		fmt.Println("不及格")
	}
}

func main() {	
	test_if()
	test_switch()
}
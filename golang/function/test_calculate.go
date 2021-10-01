package main

import (
	"errors"
	"fmt"
)

type operate func(x, y int) int

func calculate(x int, y int, op operate) (int, error) {
	if op == nil {
		return 0, errors.New("invalid operation")
	}
	return op(x, y), nil
}

func add(x, y int) int {
	return x + y
}

func sub(x, y int) int {
	return x - y
}

func multiply(x, y int) int {
	return x * y	
}

func divide(x, y int) int {
	return x / y	
}

func main() {
	x, y := 36, 6
	// op := func(x, y int) int {
	// 	return x + y
	// }
	result, _ := calculate(x, y, add)
	fmt.Println("The result: ",result)

	result, _ = calculate(x, y, sub)
	fmt.Println("The result: ",result)

	result, _ = calculate(x, y, multiply)
	fmt.Println("The result: ",result)

	result, _ = calculate(x, y, divide)
	fmt.Println("The result: ",result)
	
	result, _ = calculate(x, y, nil)
	fmt.Println("The result: ",result)	
}

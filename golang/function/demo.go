package main

import (
	"fmt"
	"errors"
)

type calculate func(x int, y int) (float64, error)

func add(x int, y int) (float64, error) {	
	if y == 0 {
		return 0, errors.New("can't divide by zero!!")
	}
	res := float64(x) / float64(y)	
	return res, nil
}

func main() {
	value1 := 3
	value2 := 2
    value3 := 0
	res, err := add(value1, value2)
	fmt.Printf("%d / %d = %f (error: %v)\n", value1, value2, res, err)
	res, err = add(value1, value3)
	fmt.Printf("%d / %d = %f (error: %v)\n", value1, value3, res, err)

	var cal calculate
	cal = add
	res, err = cal(3,2)
	fmt.Printf("The result: %f (error: %v)\n", res, err)
}

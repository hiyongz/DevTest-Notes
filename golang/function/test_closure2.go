package main

import (
	"fmt"
)

type exponent func(uint64) uint64

func nth_power(exp uint64) exponent {
	return func(base uint64) uint64 {
		result := uint64(1)
		for i := exp ; i > 0; i >>= 1 {
			if i&1 != 0 {
				result *= base
			}
			base *= base
		}
		return result
	}
}

func main() {
	square := nth_power(2) // 平方
	cube := nth_power(3) // 立方	
	fmt.Println(square(5))
	fmt.Println(cube(5))
}

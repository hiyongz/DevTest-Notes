package main

import "fmt"

var block = "package"

func modify_global() {
	block = "new"
}

func main() {
	// block := "function"
	{
		block := "inner"
		fmt.Printf("The block is %s.\n", block)
	}
	fmt.Printf("The block is %s.\n", block)
	modify_global()
	fmt.Printf("The block is %s.\n", block)
}

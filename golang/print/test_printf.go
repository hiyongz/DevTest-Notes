package main

import (
	"fmt"
)

func main() {
	var age = 22
	fmt.Printf("I'm %d years old\n", age)

	str1 := "Hello world !"
	fmt.Printf("%s\n", str1)
	fmt.Printf(str1)
	fmt.Print("\n")
	str_hex := fmt.Sprintf("% 02x", str1)
	fmt.Printf("type of str_hex: %T\n", str_hex)
	fmt.Println(str_hex)
}

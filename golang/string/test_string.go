package main

import (
	"fmt"
)

func main() {
	str := "你好world"
	fmt.Printf("The string: %q\n", str)
	fmt.Printf("runes(char): %q\n", []rune(str))
	fmt.Printf("runes(hex): %x\n", []rune(str))
	fmt.Printf("bytes(hex): [% x]\n", []byte(str))

	for i, c := range str {
		fmt.Printf("%d: %q [% x]\n", i, c, []byte(string(c)))
	}
}


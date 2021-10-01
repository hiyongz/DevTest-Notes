package main

import (
	"bytes"
	"fmt"
	"strings"
)

func DemoBytes() {
	var buffer bytes.Buffer
	buffer.WriteString("hello ")
	buffer.WriteString("world !")
	fmt.Printf("length: %d\n", buffer.Len())
	fmt.Printf("capacity: %d\n", buffer.Cap())
	fmt.Println(buffer.String())
	fmt.Println()

	p1 := make([]byte, 5)
	// p1 := []byte{1,2,3,4,5}
	n, _ := buffer.Read(p1)
	fmt.Println(string(p1))
	fmt.Println(buffer.String())
	fmt.Printf("%d bytes were read. (call Read)\n", n)
	fmt.Printf("The length of buffer: %d\n", buffer.Len())
	fmt.Printf("The capacity of buffer: %d\n", buffer.Cap())

}

func main() {
	DemoBytes()
	// DemoStrings()
}

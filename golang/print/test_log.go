package main

import (
	"log"
)

func main() {
	var age = 22
	log.Printf("I'm %d years old", age)

	str1 := `Hello world !`
	log.Println(str1)
	log.Print(str1)
	log.Printf("%s", str1)
}

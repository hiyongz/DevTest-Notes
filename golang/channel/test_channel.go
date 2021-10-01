package main

import "fmt"

func main() {

	str1 := []string{"hello","world", "!"}
	ch1 := make(chan string, len(str1))

	for _, str := range str1 {
		ch1 <- str
	}

	ch1 <- "123"

	for i := 0; i < len(str1); i++ {
		elem := <- ch1
		fmt.Println(elem)
	}

	ch1 <- "123"



}

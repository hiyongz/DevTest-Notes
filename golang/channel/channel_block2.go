package main

import (
    "fmt"
)

func main() {
    str1 := []string{"hello","world", "!"}
	ch1 := make(chan string, 0)

    go func() {
        for _, str := range str1 {
            ch1 <- str
        }
        close(ch1)
    }()

	for i := 0; i < len(str1); i++ {
		elem := <- ch1
		fmt.Println(elem)
	}

}
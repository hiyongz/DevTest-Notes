package main

import (
	"fmt"
)

func main() {
	// 示例1。
	// 只能发不能收的通道。
	// var WriteChan = make(chan<- int, 1)
	var WriteChan = make(chan<- interface{}, 1)
	// 只能收不能发的通道。
	// var ReadChan = make(<-chan int, 1)
	var ReadChan = make(<-chan interface{}, 1)
	// 这里打印的是可以分别代表两个通道的指针的16进制表示。
	fmt.Printf("The useless channels: %v, %v\n", WriteChan, ReadChan)

	fmt.Println(WriteChan)
	fmt.Println(ReadChan)

	Chan1 := OnlyReadChan(6)
	num := <- Chan1
	fmt.Println(num)
}



func OnlyReadChan(num int) <-chan int {
	ch := make(chan int, 1)
	ch <- num
	close(ch)
	return ch
}


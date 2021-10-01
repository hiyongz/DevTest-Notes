package main

import (
	"fmt"
	"time"
)

var count1 = make([]int, 100)

func testdemo(i int, n int) {
	// 对变量count执行10次加1
	count1[i] = i
	fmt.Println(count1)
}


func main() {
	// var count = 0
	// 使用WaitGroup等待10个goroutine完成

	for i := 0; i < 100; i++ {
		go testdemo(i, count1[i])
	}
	// 等待10个goroutine完成
	fmt.Println(count1)
	for {
		time.Sleep(1 * time.Second)
	}
}

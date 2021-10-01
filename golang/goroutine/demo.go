package main

import (
	"fmt"
	"sync"
)

func main() {
	// var count = 0
	// 使用WaitGroup等待10个goroutine完成
	var wg sync.WaitGroup
	
	wg.Add(100)
	for i := 0; i < 100; i++ {
		go func() {
			var count = 0
			defer wg.Done()
			// 对变量count执行10次加1
			for j := 0; j < 100000; j++ {
				count++
			}
			fmt.Println(count)
		}()
	}
	// 等待10个goroutine完成
	wg.Wait()
	// fmt.Println(count)
}

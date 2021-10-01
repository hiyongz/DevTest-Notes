package main

import (
	"fmt"
	"sync/atomic"
	"time"
	"sync"

)

var (
    balance int32
	wg sync.WaitGroup
)

// 存钱
func deposit(value int32) {
	for {		
		fmt.Printf("余额: %d\n", balance)
		atomic.AddInt32(&balance, value)
		fmt.Printf("存 %d 后的余额: %d\n", value, balance)
		fmt.Println()
		if balance == 10000 {
			break
		}
		time.Sleep(time.Millisecond * 500)
	}
    wg.Done()
}

// 取钱
func withdrawAll(value int32) {
    defer wg.Done()
	
	for {
		if atomic.CompareAndSwapInt32(&balance, value, 0) {
			break
		}
		time.Sleep(time.Millisecond * 500)
	}
	fmt.Printf("余额: %d\n", value)
    fmt.Printf("取 %d 后的余额: %d\n", value, balance)
    fmt.Println()    
}

func main() {
	wg.Add(2)	
	go deposit(1000)  // 每次存1000
	go withdrawAll(10000)
    wg.Wait()

    fmt.Printf("当前余额: %d\n", balance)
}

func init() {
    balance = 1000 // 初始账户余额为1000    
}



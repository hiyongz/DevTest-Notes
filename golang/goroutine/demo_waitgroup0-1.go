package main

import (
	"flag"
	"fmt"
	// "math/rand"
	"sync"
	"time"
)

var (
    mutex   sync.Mutex
    balance int
    protecting uint  // 是否加锁
    sign = make(chan struct{}, 10) //通道，用于等待所有goroutine
)

var wg sync.WaitGroup

// 存钱
func deposit(value int) {
    if protecting == 1 {
        mutex.Lock()
        defer mutex.Unlock()
    }

    fmt.Printf("余额: %d\n", balance)
    balance += value
    fmt.Printf("存 %d 后的余额: %d\n", value, balance)
    fmt.Println()

    wg.Done()
}

// 取钱
func withdraw(value int) {
    defer wg.Done()
    if protecting == 1 {
        mutex.Lock()
        defer mutex.Unlock()
    }

    fmt.Printf("余额: %d\n", balance)
    balance -= value
    fmt.Printf("取 %d 后的余额: %d\n", value, balance)
    fmt.Println()    
}

func main() {
	// var wg sync.WaitGroup
	wg.Add(5)
    for i:=0; i < 5; i++ {
        go deposit(500)  // 存500
    }
    wg.Wait()

    time.Sleep(time.Duration(3) * time.Second)
    
    wg.Add(5)
    for i:=0; i < 5; i++ {
        go withdraw(500) // 取500
    }
    wg.Wait()

    fmt.Printf("当前余额: %d\n", balance)
}

func init() {
    balance = 1000 // 初始账户余额为1000
    flag.UintVar(&protecting, "protecting", 1, "是否加锁，0表示不加锁，1表示加锁")
}



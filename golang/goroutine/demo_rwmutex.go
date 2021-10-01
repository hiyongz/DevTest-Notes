package main

import (
	"fmt"
	"sync"
)

// account 代表计数器。
type account struct {
	num uint         // 操作次数
	balance int		 // 余额
	rwMu  *sync.RWMutex // 读写锁
}

var sign = make(chan struct{}, 15) //通道，用于等待所有goroutine

// 查看余额：使用读锁
func (c *account) check() {
	defer func() {
        sign <- struct{}{}
    }()
	c.rwMu.RLock()
	defer c.rwMu.RUnlock()
	fmt.Printf("%d 次操作后的余额: %d\n", c.num, c.balance)
}

// 存钱：写锁
func (c *account) deposit(value int) {
	defer func() {
        sign <- struct{}{}
    }()
    c.rwMu.Lock()
	defer c.rwMu.Unlock()	

	fmt.Printf("余额: %d\n", c.balance)   
	c.num += 1
    c.balance += value
    fmt.Printf("存 %d 后的余额: %d\n", value, c.balance)
    fmt.Println() 
}

// 取钱：写锁
func (c *account) withdraw(value int) {
    defer func() {
        sign <- struct{}{}
    }()
	c.rwMu.Lock()
	defer c.rwMu.Unlock()	  
	fmt.Printf("余额: %d\n", c.balance)     
	c.num += 1
    c.balance -= value
	fmt.Printf("取 %d 后的余额: %d\n", value, c.balance)
    fmt.Println() 	
}


func main() {
	c := account{0, 1000, new(sync.RWMutex)}
	// count(&c)

	for i:=0; i < 5; i++ {
        go c.withdraw(500) // 取500
        go c.deposit(500)  // 存500
		go c.check()
    }

    // wg.Wait()
    for i := 0; i < 15; i++ {
		<-sign
	}
	fmt.Printf("%d 次操作后的余额: %d\n", c.num, c.balance)


	redundantUnlock()
}

func count(c *account) {

    for i:=0; i < 5; i++ {
        go c.withdraw(500) // 取500
        go c.deposit(500)  // 存500
		go c.check()
    }

    // wg.Wait()
    for i := 0; i < 15; i++ {
		<-sign
	}
	fmt.Printf("%d 次操作后的余额: %d\n", c.num, c.balance)
}

func redundantUnlock() {
	var rwMu sync.RWMutex

	// 示例1。
	// rwMu.Unlock() // 这里会引发panic。

	// 示例2。
	// rwMu.RUnlock() // 这里会引发panic。

	// 示例3。
	rwMu.RLock()
	// rwMu.Unlock() // 这里会引发panic。
	rwMu.RUnlock()

	// 示例4。
	rwMu.Lock()
	//rwMu.RUnlock() // 这里会引发panic。
	rwMu.Unlock()
}

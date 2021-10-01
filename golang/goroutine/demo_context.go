package main

import (
	"context"
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

var (
	balance int32
)

// 存钱
func deposit(value int32, id int, deferFunc func()) {
	defer func() {
		deferFunc()
	}()

	for {
		currBalance := atomic.LoadInt32(&balance)
		newBalance := currBalance + value
		time.Sleep(time.Millisecond * 500)

		if atomic.CompareAndSwapInt32(&balance, currBalance, newBalance) {
			fmt.Printf("ID: %d, 存 %d 后的余额: %d\n", id, value, balance)
			break
		} else {
			// fmt.Printf("操作失败\n")
		}
	}
}

// 取钱
func withdraw(value int32) {	
	for {
		currBalance := atomic.LoadInt32(&balance)
		newBalance := currBalance - value
		if atomic.CompareAndSwapInt32(&balance, currBalance, newBalance) {
			fmt.Printf("取 %d 后的余额: %d\n", value, balance)
			break
		}
	}
}

func WithCancelDemo() {
	total := 10000
	cxt, cancelFunc := context.WithCancel(context.Background())
	for i := 1; i <= 100; i++ {
		num := rand.Intn(2000) // 随机数
		go deposit(int32(num), i, func() {
			if atomic.LoadInt32(&balance) >= int32(total) {
				cancelFunc()
			}
		})
	}
	<-cxt.Done()
	withdraw(10000)
	fmt.Println("退出")

}

func DeadlineDemo() {
	total := 10000
	deadline := time.Now().Add(2 * time.Second)
	ctx, cancelFunc := context.WithDeadline(context.Background(), deadline)
	for i := 1; i <= 100; i++ {
		num := rand.Intn(2000) // 随机数
		go deposit(int32(num), i, func() {
			if atomic.LoadInt32(&balance) >= int32(total) {
				cancelFunc()
			}
		})
	}
	select {
	case <-ctx.Done():
	    fmt.Println(ctx.Err())
	}
	fmt.Println("超时退出")	
}

func WithTimeoutDemo() {
	total := 10000
	ctx, _ := context.WithTimeout(context.Background(), 2*time.Second)
	for i := 1; i <= 100; i++ {
		num := rand.Intn(2000) // 随机数
		go deposit(int32(num), i, func() {
			if atomic.LoadInt32(&balance) >= int32(total) {
				// cancelFunc()
			}
		})
	}
	select {
	case <-ctx.Done():
	    fmt.Println(ctx.Err())
	}
	fmt.Println("超时退出")	
}

func WithValueDemo() {

	rootNode := context.Background()
	ctx1, cancelFunc := context.WithCancel(rootNode)
	defer cancelFunc()

	ctx2 := context.WithValue(ctx1, "key2", "value2")
	ctx3 := context.WithValue(ctx2, "key3", "value3")
	fmt.Printf("ctx3: key2 %v\n", ctx3.Value("key2"))
	fmt.Printf("ctx3: key3 %v\n", ctx3.Value("key3"))

	fmt.Println()

	ctx4, _ := context.WithTimeout(ctx3, time.Hour)
	fmt.Printf("ctx4: key2 %v\n", ctx4.Value("key2"))
	fmt.Printf("ctx4: key3 %v\n", ctx4.Value("key3"))

	
}

func main() {
	
	// WithCancelDemo()
	// DeadlineDemo()
	// WithTimeoutDemo()
	WithValueDemo()
}

func init() {
	balance = 1000 // 初始账户余额为1000
}

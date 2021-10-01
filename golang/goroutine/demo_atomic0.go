package main

import (
	"fmt"
	"sync/atomic"
)

func demo1() {
	num := int32(20)
	atomic.AddInt32(&num, 3)
	fmt.Printf("The number: %d\n", num)

	atomic.AddInt32(&num, -3)
	fmt.Printf("The number: %d\n", num)
}

func demo2() {
	num := int32(20)	
	fmt.Println(atomic.LoadInt32(&num))

	atomic.StoreInt32(&num, 30)
	fmt.Println(num)

	old := atomic.SwapInt32(&num, 60)
	fmt.Println(num)
	fmt.Println(old)
}

func addDemo() {
    // 减法操作
	num := uint32(18)
	delta := int32(-3)
	atomic.AddUint32(&num, uint32(delta))
	fmt.Printf("The number: %d\n", num)
	atomic.AddUint32(&num, ^uint32(-(-3)-1))
	fmt.Printf("The number: %d\n", num)

	fmt.Printf("The two's complement of %d: %b\n",
		delta, uint32(delta)) // -3的补码。
	fmt.Printf("The equivalent: %b\n", ^uint32(-(-3)-1)) // 与-3的补码相同。
	fmt.Println()
}

func CompareAndSwap() {
	num:= int32(18)
	atomic.CompareAndSwapInt32(&num, 20, 0)
	fmt.Printf("The number: %d\n", num)
	atomic.CompareAndSwapInt32(&num, 18, 0)
	fmt.Printf("The number: %d\n", num)
}

// 自旋锁
func TryLock() {

}



func main() {

	// demo1()
	demo2()
	// addDemo()
	// CompareAndSwap()

}
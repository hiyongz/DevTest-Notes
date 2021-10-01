package main

import (
	// "errors"
	"fmt"
	"sync"
	// "sync/atomic"
	// "time"
)


func demo1() {
	var num = 6
	var once sync.Once

	add_one := func() {
		num = num + 1
	}

	minus_one := func() {
		num = num - 1
	}	

	once.Do(add_one)
	fmt.Printf("The num: %d\n", num)
	once.Do(minus_one)
	fmt.Printf("The num: %d\n", num)
}

func demo2() {
	var num = 6
	var once1 sync.Once
	var once2 sync.Once

	add_one := func() {
		num = num + 1
	}

	minus_one := func() {
		num = num - 1
	}	

	once1.Do(add_one)
	fmt.Printf("The num: %d\n", num)
	once2.Do(minus_one)
	fmt.Printf("The num: %d\n", num)

}


func main() {
	demo1()
	demo2()
}
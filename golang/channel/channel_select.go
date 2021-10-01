package main

import (
	"fmt"
	"math/rand"
	"time"
)

var channels = [3]chan int{
	nil,
	make(chan int),
	nil,
}

var numbers = []int{1, 2, 3}

func main() {
	// Testselect1()
	// Testselect1_2()
	// Testselect1_3()
	TestForSelect()
	TestForSelect2()
}

func Testselect1() {
	// 准备好几个通道。
	intChannels := [3]chan int{
		make(chan int, 1),
		make(chan int, 1),
		make(chan int, 1),
	}
	// 随机选择一个通道，并向它发送元素值。
	index := rand.Intn(3)
	fmt.Printf("The index: %d\n", index)
	intChannels[index] <- index
	// 哪一个通道中有可取的元素值，哪个对应的分支就会被执行。
	select {
	case <-intChannels[0]:
		fmt.Println("The first candidate case is selected.")
	case <-intChannels[1]:
		fmt.Println("The second candidate case is selected.")
	case elem := <-intChannels[2]:
		fmt.Printf("The third candidate case is selected, the element is %d.\n", elem)
	default:
		fmt.Println("No candidate case is selected!")
	}
}


func Testselect1_2() {
	ch1 := make(chan int, 2)
	num := 2
	
	select {
		case data := <-ch1:
			fmt.Println("Read data: ", data)
		case ch1 <- num:
			fmt.Println("Write data: ", num)	
		default:
			fmt.Println("No candidate case is selected!")
	}
}

// 示例2。
func Testselect1_3() {
	intChan := make(chan int, 1)
	// 一秒后关闭通道。
	time.AfterFunc(time.Second, func() {
		close(intChan)
	})
	select {
	case _, ok := <-intChan:
		if !ok {
			fmt.Println("The candidate case is closed.")
			break
		}
		fmt.Println("The candidate case is selected.")
	}
}


func getNumber(i int) int {
	fmt.Printf("numbers[%d]\n", i)
	return numbers[i]
}

func getChan(i int) chan int {
	fmt.Printf("channels[%d]\n", i)
	return channels[i]
}

func Testselect2() {
	select {
	case getChan(0) <- getNumber(0):
		fmt.Println("The first candidate case is selected.")
	case getChan(1) <- getNumber(1):
		fmt.Println("The second candidate case is selected.")
	case getChan(2) <- getNumber(2):
		fmt.Println("The third candidate case is selected")
	default:
		fmt.Println("No candidate case is selected!")
	}
}


func TestForSelect() {
	ch1 := make(chan int, 1)
	num := 6
	loop:
	for {
		select {
		case ch1 <- num:
			fmt.Println("Write data: ", num)
		case data := <-ch1:
			fmt.Println("Read data: ", data)
			break loop
		}
	}
	fmt.Println(ch1)
}

func TestForSelect2() {
	ch1 := make(chan int, 1)
	num := 6
	for {
		select {
		case ch1 <- num:
			fmt.Println("Write data: ", num)
		case data := <-ch1:
			fmt.Println("Read data: ", data)
			goto loop

		}
	}	
	loop:
	fmt.Println(ch1)
}
package main

import "fmt"


func modifyArray(a [3]int) [3]int {
	a[1] = 0
	return a
}

func modifySlice(a []int) []int {
	a[1] = 0
	return a
}

func main() {
	l1 := [3]int{1, 2, 3}
	fmt.Println("value of l1:  ",l1)
	fmt.Printf("address of l1: %p\n",&l1)

	l2 := modifyArray(l1)
	fmt.Printf("address of l2: %p\n",&l2)
	fmt.Println("value of l1:  ",l1)
	fmt.Println("value of l2:  ",l2)

	slice1 := []int{1, 2, 3}
	fmt.Println("value of slice1:  ",slice1)
	fmt.Printf("address of slice1: %p\n",&slice1)

	slice2 := modifySlice(slice1)
	fmt.Printf("address of slice2: %p\n",&slice2)
	fmt.Println("value of slice1:  ",slice1)
	fmt.Println("value of slice2:  ",slice2)

	slice2[2] = 6
	fmt.Println("value of slice1:  ",slice1)
	fmt.Println("value of slice2:  ",slice2)

	slice1 = []int{1, 2, 3}
	slice3 := make([]int, len(slice1))
	copy(slice3, slice1)
	slice3[1] = 6
	fmt.Printf("address of slice1: %p\n",&slice1)
	fmt.Printf("address of slice3: %p\n",&slice3)
	fmt.Println("value of slice1:  ",slice1)
	fmt.Println("value of slice3:  ",slice3)



}


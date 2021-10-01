package main

// import "fmt"

func main() {
	ch1 := make(chan int, 1)
	ch1 <- 1
	close(ch1)
	// ele := <-ch1
	// fmt.Println(ele)

	// ele1, statu1 := <-ch1
	// fmt.Println(ele1, statu1)
	// ele2, statu2 := <-ch1
	// fmt.Println(ele2, statu2)

	// ch1 <- 2
	close(ch1)

}
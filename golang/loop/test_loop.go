package main

import "fmt"

func TestForLoop() {
	sum := 0
	for i := 1; i < 5; i++ {
		sum += i
	}
	fmt.Println(sum) // 10 (1+2+3+4)
}

func TestWhile() {
	sum := 0
	n := 0
	for n < 5 {
		sum += n
		n += 1
	}
	fmt.Println(sum) // 10 (1+2+3+4)
}

func TestInfiniteloop() {
	sum := 0
	for {
		sum++	
		if sum == 100 {
			break
		}	
	}
	fmt.Println(sum)
}

func TestRangeloop() {	
	strings := []string{"hello", "world"}
	for index, str := range strings {
		fmt.Println(index, str)
	}
}

func TestExitloop() {
	sum := 0
	for {
		sum++		
		if sum%2 != 0 {
			fmt.Println(sum)
			continue
		}
		if sum >= 10 {
			break
		}
	}
	fmt.Println(sum)
}

func TestGotoloop1() {
	sum := 0
	sum2 := 0
	n := 0
	LOOP: for n <= 10 {
		if n%2 == 0 {
			sum += n
			n++
			goto LOOP
		}
		sum2 += n
		n++
	}
	fmt.Println(sum) // 30 (0+2+4+6+8+10)
	fmt.Println(sum2) // 25 (1+3+5+7+9)
}

func TestGotoloop2() {
	sum := 0
	n := 0
	LOOP: for n <= 10 {
		if n == 8 {
			break LOOP
		}
		sum += n
		n++
	}
	fmt.Println(sum) // 28 (0+1+2+3+4+5+6+7)
}

func gotoTag() {
    for m := 1; m < 10; m++ {
    n := 1
    LOOP: if n <= m {
        fmt.Printf("%dx%d=%d ",n,m,m*n)
        n++
        goto LOOP
    } else {
        fmt.Println("")
    }
    n++
    }
}


func main() {
	// TestForLoop()
	// TestWhile()
	// TestInfiniteloop()
	// TestRangeloop()
	TestExitloop()
	// TestGotoloop2()
	// gotoTag()
}
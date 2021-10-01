package main

import "fmt"

func main() {
	m := make(map[string]int)

    // 使用经典的"name[key]=value"来为键设置值
    m["k1"] = 7
    m["k2"] = 13
    m["k3"] = 16
	fmt.Println(len(m))

	for index, str := range m {
		fmt.Println(index, str)
	}
}
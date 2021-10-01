package main

import (
	"fmt"
	"net"
	"time"
)

// 客户端
// https://studygolang.com/articles/9240
// https://blog.csdn.net/benben_2015/article/details/79304608
func main() {
	conn, err := net.DialTimeout("tcp", "www.baidu.com:80", 2*time.Second)
	if err != nil {
		fmt.Println("err :", err)
		return
	} else {
		fmt.Println("connect successful")
	}
	defer conn.Close() // 关闭连接

}

package main

import (
	"fmt"
	mylog "log"
	"os"
	"time"
)

var log *mylog.Logger
var logFile *os.File

func logger() {
	timestamp := time.Now().Unix()
	timeNow := time.Unix(timestamp, 0)
	timeString := timeNow.Format("2006-01-02-15-04-05")
	fmt.Println(timeString)
	filenames := timeString + ".log"
	fmt.Println(filenames)
	logFile, err := os.Create(filenames)
	// defer logFile.Close()
	if err != nil {
		log.Fatalln("open file error !")
	}
	log = mylog.New(logFile, "[Debug]", mylog.LstdFlags)
	log.Println("********************************************")
	log.Println("开始 反复随机修改AX1806信道，U18自动连接测试")
}

func test() {
	log.Println("结束 反复随机修改AX1806信道，U18自动连接测试")
}

func main() {
	logger()
	test()
	defer logFile.Close()
}

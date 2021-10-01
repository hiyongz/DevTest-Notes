package main

import (
	"flag"
	"fmt"
	"os"
)

var name string

// 方式3。
var cmdLine = flag.NewFlagSet("question", flag.ExitOnError)

func init() {

	// 方式3。
	cmdLine.StringVar(&name, "name", "everyone", "The greeting object.")
	// flag.StringVar(&name, "name", "everyone", "The greeting object.")
}

func main() {

	// 方式3。
	cmdLine.Parse(os.Args[1:])
	flag.Parse()
	fmt.Printf("Hello, %s!\n", name)
}
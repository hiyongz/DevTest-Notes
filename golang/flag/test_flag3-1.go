package main

import (
	"flag"
	"fmt"
	"os"
)

var name string

// 方式3。
//var cmdLine = flag.NewFlagSet("question", flag.ExitOnError)

func init() {

	flag.StringVar(&name, "name", "everyone", "The greeting object.")
}

func main() {
	// 方式1。
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", "question")
		flag.PrintDefaults()
	}
	
	flag.Parse()
	fmt.Printf("Hello, %s!\n", name)
}
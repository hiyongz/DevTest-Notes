
package main



import (
  "flag"
  "testGo/test_lib2/lib"
)

var name string

func init() {
  flag.StringVar(&name, "name", "everyone", "The greeting object.")
}

func main() {
  flag.Parse()
  lib.hello(name)
}
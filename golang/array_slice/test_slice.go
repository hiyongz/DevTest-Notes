
package main

import "fmt"

func main() {
  // 示例1。
  s1 := make([]int, 5)
  fmt.Printf("The length of s1: %d\n", len(s1))
  fmt.Printf("The capacity of s1: %d\n", cap(s1))
  fmt.Printf("The value of s1: %d\n", s1)
  s2 := make([]int, 5, 8)
  fmt.Printf("The length of s2: %d\n", len(s2))
  fmt.Printf("The capacity of s2: %d\n", cap(s2))
  fmt.Printf("The value of s2: %d\n", s2)
}
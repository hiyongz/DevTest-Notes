package main

import (
	"fmt"
	"strings"
)

func DemoBytesBuffer(n int) {
	var buffer bytes.Buffer

	for i := 0; i < n; i++ {
		buffer.WriteString("hello ")
		buffer.WriteString("world !")
	}
}

func DemoWriteString(n int) {
	var builder1 strings.Builder
	for i := 0; i < n; i++ {
		builder1.WriteString("hello ")
		builder1.WriteString("world !")
	}
}

func DemoStringsJoin(n int) {
	str1 := "hello "
	str2 := "world !"
	str3 := ""
	for i := 0; i < n; i++ {
		str3 = strings.Join([]string{str3, str1}, "")
		str3 = strings.Join([]string{str3, str2}, "")
	}

}

func DemoPlus(n int) {

	str1 := "hello "
	str2 := "world !"
	str3 := ""
	for i := 0; i < n; i++ {
		str3 += str1
		str3 += str2
	}
}

func DemoAppend(n int) {

	str1 := "hello "
	str2 := "world !"
	var str3 []byte
	for i := 0; i < n; i++ {
		str3 = append(str3, []byte(str1)...)
		str3 = append(str3, []byte(str2)...)
	}
}

func DemoSprintf(n int) {
	str1 := "hello "
	str2 := "world !"
	str3 := ""
	for i := 0; i < n; i++ {
		str3 = fmt.Sprintf("%s%s", str3, str1)
		str3 = fmt.Sprintf("%s%s", str3, str2)
	}
}
func main() {
	DemoAppend(1)
	DemoSprintf(2)
	DemoStringsJoin(3)
}

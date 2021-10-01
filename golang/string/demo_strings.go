package main

import (
	"fmt"
	"io"
	"strings"
)

func DemoStrings() {
	var builder1 strings.Builder
	builder1.WriteString("hello")
	// fmt.Printf("The length 0f builder1: %d\n", builder1.Len())
	builder1.WriteByte(' ')
	builder1.WriteString("world")
	builder1.Write([]byte{' ', '!'})
	fmt.Println(builder1.String())

	f1 := func(b strings.Builder) {
		// b.WriteString("world !")  //会报错
	}
	f1(builder1)

	builder1.Reset()
	fmt.Printf("The length of builder1: %d\n", builder1.Len())

	reader1 := strings.NewReader("hello world!")
	buf1 := make([]byte, 6)
	fmt.Printf("reading index: %d\n", reader1.Size()-int64(reader1.Len()))

	reader1.Read(buf1)
	fmt.Println(string(buf1))

	fmt.Printf("reading index: %d\n", reader1.Size()-int64(reader1.Len()))

	reader1.Read(buf1)
	// n, _ = reader1.Read(buf1)
	fmt.Println(string(buf1))
	fmt.Printf("reading index: %d\n", reader1.Size()-int64(reader1.Len()))
	fmt.Println()

	// ReadAt方法
	buf2 := make([]byte, 6)
	offset1 := int64(6)
	n, _ := reader1.ReadAt(buf2, offset1)
	fmt.Printf("%d bytes were read. (call ReadAt, offset: %d)\n", n, offset1)
	fmt.Printf("The reading index in reader: %d\n",
		reader1.Size()-int64(reader1.Len()))
	fmt.Println(string(buf2))
	fmt.Println()

	// Seek方法
	reader2 := strings.NewReader("hello world!")
	offset2 := int64(6)
	readingIndex, _ := reader2.Seek(offset2, io.SeekCurrent)
	fmt.Printf("reading index: %d\n", readingIndex)

	reader2.Read(buf2)
	fmt.Printf("reading index: %d\n", reader2.Size()-int64(reader2.Len()))
	fmt.Println(string(buf2))
}

func main() {
	DemoBytes()
	// DemoStrings()
}

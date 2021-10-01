package main

import (
	"encoding/hex"
	"fmt"
	"log"
	"strconv"
)

// 加法运算
func add(x, y int) int {
	return x + y
}

func init() {
	fmt.Println("main  init....")
}

func tlv_length(data_len int64) (data1 byte, data2 byte){
	var s1 string
	var s2 string
	s := strconv.FormatInt(data_len, 16)
	if len(s) == 3 {
		s1 = "0" + string(s[0])
		s2 = s[len(s)-2:]
	} else if len(s) == 4 {
		s1 = s[0:2]
		s2 = s[2:4]
	} else if len(s) == 2 {
		s1 = "00"
		s2 = s[0:2]
	} else if len(s) == 1 {
		s1 = "00"
		s2 = s
	} else {
		log.Fatalf("data eror")
	}

	d1, _ := hex.DecodeString(s1)
	d2, _ := hex.DecodeString(s2)
	return d1[0],d2[0]

}

func main() {
	var value1 int = 2
	var value2 = 3
	sum := add(value1, value2)
	fmt.Printf("%d + %d = %d\n", value1, value2, sum)

	// a := `"dev_info"`
	// b := []byte(`"dev_info"`)
	// fmt.Printf("%s", a)
	// fmt.Printf("%s\n", b[0])

	// fmt.Printf("%0.2x\n", num)
	// num_hex := fmt.Sprintf("%02x", num)
	data1, data2 := tlv_length(566)
	fmt.Println(data1)
	fmt.Println(data2)
}

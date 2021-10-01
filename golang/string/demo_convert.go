package main

import (
	"encoding/hex"
	"fmt"
)

func main() {
    strData := "36"
    
    // 将HEX编码的字符串转换为HEX数据
	data1, _ := hex.DecodeString(strData)
	fmt.Println(data1[0])
	fmt.Printf("%#x\n",data1[0])
	for n,v:=range data1{
		fmt.Printf("strData[%d]值十进制为：%v , 16进制为：%#x \n",n,v,v)
	}

	// 将HEX数据转换为HEX编码的字符串
	fmt.Printf("strsdata = %v  \n",hex.EncodeToString(data1))

}

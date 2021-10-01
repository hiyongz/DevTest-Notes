package main

import (
	"bytes"
	"fmt"
	"log"
	"os/exec"
)

func exec_c() {
	randstr1 := "6033ff352c5a8395f75cba2162be574f0f712da5f4e4595cf50281ce567416c1"
	log.Printf("type of randstr %T", randstr1)
	// randstr := "123"
	log.Println(fmt.Sprintf("randstr : %s", randstr1))
	// randstr := fmt.Sprintf("%x", randstr1)
	mac2 := "d8380ddbce90"

	cmd := exec.Command("./test_openssl", mac2, randstr1)
	// cmd.Stdout = os.Stdout
	// cmd.Stderr = os.Stderr

	// err := cmd.Run()
	// if err != nil {
	// 	log.Fatalf("failed to call cmd.Run(): %v", err)
	// }

	data, err := cmd.Output()
	if err != nil {
		log.Fatalf("failed to call Output(): %v", err)
	}
	log.Printf("666666666666666\n")
	log.Printf("output: %s", data)
	log.Printf("output: %T", data)
	log.Printf("output: %x", data)
	log.Printf("666666666666666\n")

}

func exec_shell() {
	mac := "char devmac[] = {\"D8380DDBCE90\"};"
	randstr := [5]byte{'a', 'b', 'c', 'd', 'e'}

	var buffer bytes.Buffer
	for index := range randstr {
		hex_data := fmt.Sprintf("%02x", randstr[index])
		if index == 0 {
			buffer.WriteString("char buff[] = {")
		}
		buffer.WriteString("0x")
		buffer.WriteString(hex_data)

		if index != len(randstr)-1 {
			buffer.WriteString(",")
		} else {
			buffer.WriteString("};")
		}

	}
	randstrs := buffer.String()
	log.Printf("randstrs: %s", randstrs)

	mac_sed := fmt.Sprintf("s/char\\ devmac\\[\\].*$/%s/", mac)
	cmd_sed_mac := fmt.Sprintf("sed -i '%s' test_devencrypt.c", mac_sed)
	log.Printf("cmd_sed: %s", cmd_sed_mac)
	cmd := exec.Command("bash", "-c", cmd_sed_mac)
	_, err := cmd.Output()
	if err != nil {
		log.Fatalf("failed to update mac address: %v", err)
	}

	randstr_sed := fmt.Sprintf("s/char\\ buff\\[\\].*$/%s/", randstrs)
	cmd_sed_randstr := fmt.Sprintf("sed -i '%s' test_devencrypt.c", randstr_sed)
	log.Printf("cmd_sed: %s", cmd_sed_randstr)
	_, err = exec.Command("bash", "-c", cmd_sed_randstr).Output()
	if err != nil {
		log.Fatalf("failed to update randstr: %v", err)
	}
}

func main() {

	header2 := make([]byte, 45)
	header2[0] = 0x0
	log.Printf("header2: %s", header2)
	log.Printf("header11: %d", len(string(header2)))
	log.Println("header2:", header2[0])
	log.Printf("header2: %d", len(header2))

	if header2[0] == 0 {
		log.Printf("header2: %x", header2)
	}
	exec_shell()

}

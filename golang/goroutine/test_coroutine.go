package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
	// "time"
)

var apNum *int
var netInterface *string
var macAddrs [256]string

//var ipArray []string
type ApDevData struct {
	Index         int
	Ip            string
	Mac           string
	InterfaceName string
	Manager       string
	Key           string
	//body []byte
	Conn *net.TCPConn
}

type ScanStr struct {
	Cmd     int `json:"cmd"`
	Src     int `json:"src"`
	UdpPort int `json:"udp_port"`
}

type BindOrReConnStr struct {
	Cmd    int    `json:"cmd"`
	Access string `json:"access"`
	Ip     string `json:"ip"`
	Port   int    `json:"port"`
	Mac    string `json:"mac"`
	AcSn   string `json:"ac_sn"`
}

var devArray map[int]*ApDevData

// d8:38:0d:db:ce:90
var macAddrPre = [8]string{"d8:38:0d:01:00:", "d8:38:0d:02:00:", "d8:38:0d:03:00:", "d8:38:0d:04:00:", "d8:38:0d:05:00:", "d8:38:0d:06:00:", "d8:38:0d:07:00:", "d8:38:0d:08:00:"}
var macAddrLetter = [16]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
var ipAddrPre = [8]string{"172.16.10.", "172.16.11.", "172.16.12.", "172.16.13.", "172.16.14.", "172.16.15.", "172.16.16.", "172.16.17."}

func LetterAlignment(letter [16]string) [256]string {
	// 0-f 字母组合
	var letters [256]string
	var k = 0
	for _, v1 := range letter {
		for _, v2 := range letter {
			letters[k] = v1 + v2
			k += 1
		}
	}
	return letters
}

func exeSysCommand(cmdStr string) string {
	cmd := exec.Command("sh", "-c", cmdStr)
	opBytes, err := cmd.Output()
	if err != nil {
		fmt.Println(err)
		return ""
	}
	return string(opBytes)
}

func AddVirtualNetworkCard(apNum int) {
	ids := apNum / 200
	remain := apNum % 200
	mac_i := 1
	for i := 0; i <= ids; i++ {
		var times int
		if i != ids {
			times = 201
		} else {
			times = remain
			if remain == 0 {
				return
			}
		}

		for j := 2; j <= times+1; j++ {
			tempMac := macAddrPre[i] + macAddrs[mac_i] // Mac地址
			mac_i += 1
			tempmac1 := strings.Replace(tempMac, ":", "", -1)
			tempmac2 := strings.ToUpper(tempmac1)
			log.Println(tempmac1)
			log.Println(tempmac2)
			tempIp := ipAddrPre[i] + strconv.Itoa(j) // Ip地址
			interfaceName := fmt.Sprintf("%s:%d", *netInterface, i*200+j-1)
			log.Println(interfaceName)

			msg := fmt.Sprintf("ifconfig %s %s netmask 255.255.0.0 up", interfaceName, tempIp)
			log.Println(msg)
			// exeSysCommand(msg)
			ap := &ApDevData{
				Ip:            tempIp,
				Mac:           tempMac,
				InterfaceName: interfaceName,
				Index:         i*200 + j - 1,
				Manager:       "",
				Key:           "",
				//body: []byte(""),
			}
			devArray[i*200+j-1] = ap
		}
	}
}

func DumpNetInterfaces() {
	lists, err := net.Interfaces()
	if err != nil {
		log.Println(err)
		os.Exit(1)
	}
	for _, address := range lists {
		log.Println(address.Name)
		// 检查ip地址判断是否回环地址
	}
}

func main() {

	// netInterface = flag.String("i", "etn0", "net interface name")
	// apNum = flag.Int("n", 1000, "ap numbers")
	// flag.Parse()

	netInterface = new(string)
	*netInterface = "eth1"

	apNum = new(int)
	*apNum = 3

	AddVirtualNetworkCard(*apNum)
	// InitWebListen()
	DumpNetInterfaces()
	// go StartUdpProcess()
	// //Traverse(*apNum)
	// for {
	// 	time.Sleep(1 * time.Second)
	// }
}

func init() {
	log.SetFlags(log.Lmicroseconds | log.Lshortfile)
	devArray = make(map[int]*ApDevData, 0)
	macAddrs = LetterAlignment(macAddrLetter)
	// log.Println(mac2)
}

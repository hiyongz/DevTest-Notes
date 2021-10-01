func cmd_dev_allocate_sn_a(conn *net.TCPConn) (allocate_sn_data []byte) {
	// 读取的数据第一个字节表示数据长度的情况
	allocate_sn_data = make([]byte, 1024)
	c := bufio.NewReader(conn)
	for {
		n, err := c.ReadByte() // n表示数据长度
		if err != nil {
			log.Println("recv failed. ", err)
		}
		_, err = io.ReadFull(c, allocate_sn_data[:int(n)])

		// log.Println(fmt.Sprintf("recv SN : %x", allocate_sn_data))
		fmt.Printf("recv SN : %d", n)
		log.Println(fmt.Sprintf("recv SN : %x", allocate_sn_data[:n]))
		log.Println(fmt.Sprintf("recv SN : %s", allocate_sn_data[:n]))

	}
	return allocate_sn_data
}

func Read(conn *net.TCPConn, info string) {
	log.Println("reading.....")
	reader := bufio.NewReader(conn)
	var buffer bytes.Buffer
	for {
		ba, isPrefix, err := reader.ReadLine()
		if err != nil {
			if err == io.EOF {
				break
			}
			// return "", err
			log.Println("err: ", err,info)
		}
		buffer.Write(ba)
		if !isPrefix {
			break
		}

	}
	log.Println("data: ", buffer.String(),info)
	// return buffer.String(), nil
}
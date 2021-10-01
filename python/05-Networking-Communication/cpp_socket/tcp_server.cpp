#include <stdio.h>  
#include <winsock2.h>  //初始化网络编程函数

#pragma comment(lib,"ws2_32.lib")  

int main(int argc, char* argv[])
{
	//初始化WSA  
	WORD sockVersion = MAKEWORD(2, 2);
	WSADATA wsaData;//WSADATA，一种数据结构。这个结构被用来存储被WSAStartup函数调用后返回的Windows Sockets数据。它包含Winsock.dll执行的数据。
	
    //加载winsock库，初始化系统环境，以便以后关于网络的函数调用
	if (WSAStartup(sockVersion, &wsaData) != 0)
	{
		return 0;
	}

	//创建套接字(监听的端口)
	SOCKET slisten = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (slisten == INVALID_SOCKET)
	{
		printf("socket error !");
		return 0;
	}

	//绑定IP和端口,在sockaddr_in结构中装入地址信息  
	sockaddr_in sin;
	sin.sin_family = AF_INET;
	sin.sin_port = htons(8887); //htons:将主机无符号短整型数转换成网络字节顺序
	sin.sin_addr.S_un.S_addr = INADDR_ANY;//指定地址为0.0.0.0的地址
	//套接字和本地地址绑定
	if (bind(slisten, (LPSOCKADDR)&sin, sizeof(sin)) == SOCKET_ERROR)
	{
		printf("bind error !");
	}

	//开始监听  
	if (listen(slisten, 5) == SOCKET_ERROR) //sockfd：用于标识一个已捆绑未连接套接口的描述字。
											//backlog：等待连接队列的最大长度。
	{
		printf("listen error !");
		return 0;
	}

	//循环接收数据  
	SOCKET sClient;
	sockaddr_in remoteAddr;
	int nAddrlen = sizeof(remoteAddr);
	char revData[255];
	while (true)
	{
		//printf("等待连接...\n");
		sClient = accept(slisten, (SOCKADDR *)&remoteAddr, &nAddrlen);
		if (sClient == INVALID_SOCKET)
		{
			printf("accept error !");
			continue;
		}
		//printf("接受到一个连接：%s \r\n", inet_ntoa(remoteAddr.sin_addr));//打印出连接者的ip

		//接收数据  
		int ret = recv(sClient, revData, 255, 0);
		if (ret > 0)
		{
			// 为防止打印出错,把字符串结尾设为0x00
			revData[ret] = 0x00;
			//printf(revData);
		}
		int nums = atoi(revData);
		//printf("%d\n", nums);

		if (nums == 6)
		{
			printf(revData);
		}
		else
		{
			printf("%d", 1);
		}
		//发送数据  
		//const char * sendData = "你好，TCP客户端！\n";
		const char * sendData = "1\n";
		send(sClient, sendData, strlen(sendData), 0);
		closesocket(sClient);
	}

	closesocket(slisten);
	WSACleanup();
	return 0;
}

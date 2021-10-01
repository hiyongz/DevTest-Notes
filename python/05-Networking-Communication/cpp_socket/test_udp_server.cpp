#include "Winsock2.h"
#include "stdio.h"
#pragma comment(lib,"ws2_32.lib")  
int main()
{

	////////////////////////////////////////加载套接字////////////////////////////////////////////////////
	WORD wVersionRequested;//套接字库版本号
	WSADATA wsaData;
	int err;

	wVersionRequested = MAKEWORD(2, 2);//定义套接字的版本号

	err = WSAStartup(wVersionRequested, &wsaData);//创建套接字
	if (err != 0) {
		return 0;
	}
	///创建套接字失败处理
	if (LOBYTE(wsaData.wVersion) != 2 ||
		HIBYTE(wsaData.wVersion) != 2)
	{
		WSACleanup();
		return 0;
	}

	SOCKET SrvSock = socket(AF_INET, SOCK_DGRAM, 0);//创建套接字
	SOCKADDR_IN SrvAddr;
	SrvAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//绑定服务端IP地址
	SrvAddr.sin_family = AF_INET;//服务端地址族
	SrvAddr.sin_port = htons(6001);//绑定服务端端口号

	bind(SrvSock, (SOCKADDR*)&SrvAddr, sizeof(SOCKADDR));

	int len = sizeof(SOCKADDR);
	char buff[100];
	SOCKADDR ClistAddr;

	
	int ret = recvfrom(SrvSock, buff, 100, 0, (SOCKADDR*)&ClistAddr, &len);//等待接收客户端的请求到来
	if (ret > 0)
	{
		buff[ret] = 0x00;
		//printf(revData);
	}
	printf("%s\n", buff);//把客户端发送来的buff信息打印出来

	closesocket(SrvSock);//关闭套接字
	WSACleanup();


	system("pause");
	return 0;
}
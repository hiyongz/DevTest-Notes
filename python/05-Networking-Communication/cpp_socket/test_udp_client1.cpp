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

	SOCKET ClistSock = socket(AF_INET, SOCK_DGRAM, 0);//创建套接字类型

	SOCKADDR_IN SrvAddr;
	SrvAddr.sin_family = AF_INET;//选择地址族
	SrvAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//服务端的IP地址
	SrvAddr.sin_port = htons(6001);//服务端的端口号

	sendto(ClistSock, "hello", strlen("hello") + 1, 0, (SOCKADDR*)&SrvAddr, sizeof(SOCKADDR));//往服务端发送"hello"消息
	closesocket(ClistSock);//关闭套接字
	WSACleanup();//

	return 0;
}
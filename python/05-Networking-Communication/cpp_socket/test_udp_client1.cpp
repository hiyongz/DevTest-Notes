#include "Winsock2.h"
#include "stdio.h"
#pragma comment(lib,"ws2_32.lib")  
int main()
{

	////////////////////////////////////////�����׽���////////////////////////////////////////////////////
	WORD wVersionRequested;//�׽��ֿ�汾��
	WSADATA wsaData;
	int err;

	wVersionRequested = MAKEWORD(2, 2);//�����׽��ֵİ汾��

	err = WSAStartup(wVersionRequested, &wsaData);//�����׽���
	if (err != 0) {
		return 0;
	}
	///�����׽���ʧ�ܴ���
	if (LOBYTE(wsaData.wVersion) != 2 ||
		HIBYTE(wsaData.wVersion) != 2)
	{
		WSACleanup();
		return 0;
	}

	SOCKET ClistSock = socket(AF_INET, SOCK_DGRAM, 0);//�����׽�������

	SOCKADDR_IN SrvAddr;
	SrvAddr.sin_family = AF_INET;//ѡ���ַ��
	SrvAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//����˵�IP��ַ
	SrvAddr.sin_port = htons(6001);//����˵Ķ˿ں�

	sendto(ClistSock, "hello", strlen("hello") + 1, 0, (SOCKADDR*)&SrvAddr, sizeof(SOCKADDR));//������˷���"hello"��Ϣ
	closesocket(ClistSock);//�ر��׽���
	WSACleanup();//

	return 0;
}
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

	SOCKET SrvSock = socket(AF_INET, SOCK_DGRAM, 0);//�����׽���
	SOCKADDR_IN SrvAddr;
	SrvAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//�󶨷����IP��ַ
	SrvAddr.sin_family = AF_INET;//����˵�ַ��
	SrvAddr.sin_port = htons(6001);//�󶨷���˶˿ں�

	bind(SrvSock, (SOCKADDR*)&SrvAddr, sizeof(SOCKADDR));

	int len = sizeof(SOCKADDR);
	char buff[100];
	SOCKADDR ClistAddr;

	
	int ret = recvfrom(SrvSock, buff, 100, 0, (SOCKADDR*)&ClistAddr, &len);//�ȴ����տͻ��˵�������
	if (ret > 0)
	{
		buff[ret] = 0x00;
		//printf(revData);
	}
	printf("%s\n", buff);//�ѿͻ��˷�������buff��Ϣ��ӡ����

	closesocket(SrvSock);//�ر��׽���
	WSACleanup();


	system("pause");
	return 0;
}
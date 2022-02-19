@echo off

REM 指定FTP用户名
set ftpUser=pingtai
REM 指定FTP密码
set ftpPass=pingtai
REM 指定FTP服务器地址
set ftpIp=172.16.30.75
REM 指定FTP服务器软件发布路径
REM set ftpFolder=/release/ugw6.0/ugw6.0_dailybuild/dev_ugw6.0_main/latest_version/RX27pro/
set ftpFolder=%1
REM 指定软件本地存放路径
REM set LocalFolder=D:/jenkins/workspace/FTP_release_download/RX27pro
set LocalFolder=%2

echo open %ftpIp% > download.ftp
echo user %ftpUser% %ftpPass% >> download.ftp
echo cd %ftpFolder% >> download.ftp
REM 更改本地目录
echo lcd %LocalFolder% >> download.ftp
echo prompt off >> download.ftp
REM 使用二进制文件传输方式
echo bin >> download.ftp
REM 下载文件
REM echo get US_RX27ProV1.0_V13.6.11.3__multi_BCM6756.bin >> download.ftp
echo mget *.bin >> download.ftp
echo bye >> download.ftp
ftp -n -s:download.ftp

if exist %LocalFolder%/*.bin (
	REM download successful
	echo soft_path=RX27pro > rf_include.ini
) else (
    REM download fail
	cd.>rf_include.ini
    exit 1
)


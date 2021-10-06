# charles SSL证书安装
charles抓取https协议报文需要配置SSL通用证书，否则会导致乱码，本文介绍Charles 的 CA 证书安装方法。

<!--more-->

## 1. 电脑安装SSL证书
选择 “Help” -> “SSL Proxying” -> “Install Charles Root Certificate”
![](api-test-charles-ca-certificate-install/charles_ca_certificate.png)
![](api-test-charles-ca-certificate-install/charles_ca_certificate2.png)
## 2. 浏览器安装SwitchyOmega插件
插件下载地址：https://github.com/FelisCatus/SwitchyOmega/releases

设置代理：
charles默认代理端口为8888
![](api-test-charles-ca-certificate-install/charles_switchomega.png)
设置完成后，浏览器开启charles代理。

## 3. 配置SSL的抓取域名
选择 “Proxy” -> “SSL Proxying Settings” 
![](api-test-charles-ca-certificate-install/charles_ssl_setting.png)

启用SSL代理，配置location
![](api-test-charles-ca-certificate-install/charles_ssl_setting2.png)
## 4. 浏览器安装SSL证书
选择 “Help” -> “SSL Proxying” -> “Install Charles Root Certificate on a Mobile Device or Remote Browser”
![](api-test-charles-ca-certificate-install/charles_ca_certificate3.png)

弹出如下提示框
![](api-test-charles-ca-certificate-install/charles_ca_certificate4.png)

浏览器地址栏输入“chls.pro/ssl” 下载证书
![](api-test-charles-ca-certificate-install/charles_shls_ssl.png)

chrome浏览器安装：
![](api-test-charles-ca-certificate-install/charles_chrome_ssl_setting.png)

## 5. 手机安装SSL证书
设置手机代理
![](api-test-charles-ca-certificate-install/android-proxy.png)

手机浏览器输入“chls.pro/ssl” 下载证书
![](api-test-charles-ca-certificate-install/android-chls.png)

点击下载的证书文件进行安装
![](api-test-charles-ca-certificate-install/android-chls-install.png)
![](api-test-charles-ca-certificate-install/android-chls-install2.png)

设置PIN码后安装成功

手机浏览器访问baidu，charles查看https报文：
![](api-test-charles-ca-certificate-install/android-proxy-baidu.png)证书安装成功






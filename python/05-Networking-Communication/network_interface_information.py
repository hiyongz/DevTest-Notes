#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/8 16:33
# @Author:  haiyong
# @File:    network_interface_information.py

# 读取网络接口信息

from netifaces import ifaddresses, AF_INET, AF_INET6, AF_LINK
from netifaces import interfaces, gateways
import winreg as wr
import platform


class NicInformation():
    """
    类说明：获取网卡信息
    """

    def __init__(self):
        """初始化数据

        """
        # 网卡接口设备名
        self.ifname = None

    def __get_key(self, ifname):
        """获取网卡键值

        :param ifname: 网卡接口设备名

        :return: 成功返回网卡键值;否则返回错误信息。
        """
        self.ifname = ifname
        # 获取所有网络接口卡的键值
        id = interfaces()
        # 存放网卡键值与键值名称的字典pip
        key_name = {}
        try:
            # 建立链接注册表，"HKEY_LOCAL_MACHINE"，None表示本地计算机
            reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
            reg_key = wr.OpenKey(reg,
                                 r'SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}')
        except WindowsError:
            raise WindowsError("找不到子键路径 %s" % self.ifname)

        for i in id:
            try:
                # 尝试读取每一个网卡键值下对应的Name
                reg_subkey = wr.OpenKey(reg_key, i + r'\Connection')
                # 如果存在Name，写入key_name字典
                key_name[wr.QueryValueEx(reg_subkey, 'Name')[0]] = i
            except Exception:
                pass
        return key_name[self.ifname]

    def get_nic_ip_address(self, ifname,type="ipv4"):
        """功能描述：获取网卡ipv4地址
        :param ifname：网卡接口设备名
        :return: 成功返回网卡IPv4地址；否则，返回错误信息。
        """

        if type == "ipv4":
            af_inet = AF_INET
        elif type == "ipv6":
            af_inet = AF_INET6
        # 判断系统是否为Linux
        if platform.system() == "Linux":
            try:
                # 返回ip地址信息
                return ifaddresses(self.ifname)[af_inet][0]['addr']
            except ValueError:
                raise ValueError("获取不到Linux环境网卡设备名 %s IPv4地址" % (self.ifname))

        # 判断是否为Windows系统
        elif platform.system() == "Windows":
            # 调用函数get_key，获取到了网卡的键值
            key = self.__get_key(ifname)
            if not key:
                key = "无法获取到Windows环境网卡设备名%s IPv4键值" % (self.ifname)
                raise RuntimeError(key)
            else:
                # 返回ip地址信息
                ips = ifaddresses(key)[af_inet]
                ip_list = []
                for ip_i in ips:
                    if not ip_i['addr'].startswith("fe80::"):
                        ip_list.append(ip_i['addr'])
                return ','.join(ip_list)
        else:
            print('您的系统本程序暂时不支持，目前只支持Linux、Windows')

    def get_nic_ipv6_gateway(self, ifname):
        """功能描述：获取网卡IPv6网关地址
        :param ifname：网卡接口设备名
        :return: 成功返回网卡IPv6网关地址；否则，返回错误信息。
        """
        # 判断是否为Windows系统
        if platform.system() == "Windows":
            # 调用函数get_key，获取到了网卡的键值
            key = self.__get_key(ifname)
            if not key:
                key = "无法获取到Windows环境网卡设备名%s IPv4键值" % (self.ifname)
                raise RuntimeError(key)
            else:
                # 返回网卡IPv6网关地址信息
                gateway = gateways()[AF_INET6]
                gate_list = []
                for gate_i in gateway:
                    if key in gate_i and not gate_i[0].startswith("fe80::1"):
                        gate_list.append(gate_i[0])
                return ','.join(gate_list)
        else:
            print('本程序暂时只支持Windows')
    def get_nic_mac_address(self, ifname):
        """功能描述：获取网卡mac地址
        :param ifname：网卡接口设备名
        :return: 成功返回网卡MAC地址，否则，返回错误信息
        """
        key = self.__get_key(ifname)
        if not key:
            key = "无法获取到Windows环境网卡设备名%s 键值" % (self.ifname)
            raise RuntimeError(key)
        else:
            return ifaddresses(key)[AF_LINK][0]['addr']

if __name__ == '__main__':
    nic = NicInformation()
    ip2 = nic.get_nic_ip_address("WLAN",type="ipv6")
    print(ip2)
    ip = nic.get_nic_ipv6_gateway("WLAN")
    print(ip)
    mac = nic.get_nic_mac_address("WLAN")
    print(mac)

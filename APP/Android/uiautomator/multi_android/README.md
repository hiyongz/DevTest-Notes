# Android手机挂机脚本说明

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)

## 背景

多台安卓手机自动化执行切换并刷新指定的应用；

## 安装
本脚本可在Windows系统上执行。

1、脚本使用Python语言开发，要求安装Python3.7及以上版本。

2、由于需要使用 `adb` 工具读取手机序列号，需要安装Android SDK 平台工具中提供的Android SDK Platform-Tools。将tools工具中的 `platform-tools.zip` 解压后添加到环境变量中即可。

3、命令行执行 `pip install - r requirements.txt` 安装脚本所需第三方Python库。

## 使用说明

1、将手机序列号填到 `config.ini`配置文件中

手机通过USB连接PC，手机开启调试模式，取消锁屏密码，然后命令窗口执行 `adb devices` 获取手机的序列号。将序列号填入配置文件：

```ini
[phone_serial]
phone1=TEV0218201001493
phone2=CUYDU19626004019
```

2、在脚本所在目录打开cmd窗口，执行如下命令启动挂机脚本：

```sh
$ python dpi_android.py
```

3、日志保存

执行过程中，命令行窗口会实时打印日志，日志会自动保存到 `log` 目录下，日志默认以脚本启动时间命名。

4、停止

脚本采用了死循环，如果要停止脚本执行，关掉命令窗口或者 `Ctrl + C`停止执行。
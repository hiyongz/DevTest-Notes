@echo off

echo tidevice -u %1 wdaproxy -B %2 --port %3

tidevice -u %1 wdaproxy -B %2 --port %3

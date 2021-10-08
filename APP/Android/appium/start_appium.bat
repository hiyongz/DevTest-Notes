@echo off REM 回显到控制台上

start cmd /k """taskkill /f /im adb.exe&adb start-server&node "C:\Program Files\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js" --address 127.0.0.1 --port 4723 --session-override --log-level debug --log d:/appium-server.log"""
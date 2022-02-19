@echo off
call D:\\attrobot3\\Scripts\\activate.bat
python D:\\jenkins_workspace\\svn_check.py

:svn_check
:: 读取配置
for /f "tokens=1,2 delims==" %%a in (D:\\jenkins_workspace\\rf_include.ini) do (
	if %%a==tag set tag=%%b
	if %%a==user set user=%%b
	if %%a==time set time=%%b
) 
echo %tag%
echo %user%
echo %time%
echo %cd%

:: 没有指定标签退出
IF NOT DEFINED tag EXIT 1

robot -d D:\\jenkins_workspace\\rf_results --include=%tag% D:\Rebot_F_script\MX\MX6
*** Settings ***
Resource          ../02_流程层/登录流程.txt

*** Test Cases ***
case_1.1_正确用户名密码登录成功
    [Setup]    进入用户登录页面
    用户登录    ${username}    ${password}
    [Teardown]    退出登录

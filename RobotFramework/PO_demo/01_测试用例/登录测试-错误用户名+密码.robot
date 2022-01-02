*** Settings ***
Default Tags      login
Library           DateTime

*** Test Cases ***
case_1.1_错误用户名+密码
    log    错误用户名+密码

case_1.2_错误用户名+正确密码
    log    错误用户名+正确密码

case_1.3_正确用户名+错误密码
    log    正确用户名+错误密码

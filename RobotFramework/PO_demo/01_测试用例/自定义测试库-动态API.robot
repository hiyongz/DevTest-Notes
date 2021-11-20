*** Settings ***
Library           MyDynamicLibrary

*** Test Cases ***
case_001
    ${res}    Test Add    2    3    5
    Should Be True    ${res}

case_002
    ${res}    Test Sub    6    1    results=5
    Should Be True    ${res}

case_003
    example test2

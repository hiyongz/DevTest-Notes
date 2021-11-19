*** Settings ***
Library           MyDynamicLibrary

*** Test Cases ***
case_001
    ${sum}    Test Add    2    3    5
    Should Be True    ${sum}

case_002
    ${sum}    Test Sub    6    1    results=5
    Should Be True    ${sum}

*** Settings ***
Library           MyHybridLibrary

*** Test Cases ***
case_001
    ${sum}    Test Add    2    3    5
    Should Be True    ${sum}

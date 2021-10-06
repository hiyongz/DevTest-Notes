# 键盘输入keycode
列出UI自动化测试中用到的keycode

<!--more-->

## Android keycode
appium模拟键盘事件表，参考：[https://developer.android.com/reference/android/view/KeyEvent.html](https://developer.android.com/reference/android/view/KeyEvent.html)

```python
driver.keyevent()
driver.press_keycode()
```


```text
****************电话键****************
KEYCODE_CALL 拨号键 5
KEYCODE_ENDCALL 挂机键 6
KEYCODE_HOME 按键Home 3
KEYCODE_MENU 菜单键 82
KEYCODE_BACK 返回键 4
KEYCODE_SEARCH 搜索键 84
KEYCODE_CAMERA 拍照键 27
KEYCODE_FOCUS 拍照对焦键 80
KEYCODE_POWER 电源键 26
KEYCODE_NOTIFICATION 通知键 83
KEYCODE_MUTE 话筒静音键 91
KEYCODE_VOLUME_MUTE 扬声器静音键 164
KEYCODE_VOLUME_UP 音量增加键 24
KEYCODE_VOLUME_DOWN 音量减小键 25
 
****************控制键****************
KEYCODE_ENTER 回车键 66
KEYCODE_ESCAPE ESC键 111
KEYCODE_DPAD_CENTER 导航键 确定键 23
KEYCODE_DPAD_UP 导航键 向上 19
KEYCODE_DPAD_DOWN 导航键 向下 20
KEYCODE_DPAD_LEFT 导航键 向左 21
KEYCODE_DPAD_RIGHT 导航键 向右 22
KEYCODE_MOVE_HOME 光标移动到开始键 122
KEYCODE_MOVE_END 光标移动到末尾键 123
KEYCODE_PAGE_UP 向上翻页键 92
KEYCODE_PAGE_DOWN 向下翻页键 93
KEYCODE_DEL 退格键 67
KEYCODE_FORWARD_DEL 删除键 112
KEYCODE_INSERT 插入键 124
KEYCODE_TAB Tab键 61
KEYCODE_NUM_LOCK 小键盘锁 143
KEYCODE_CAPS_LOCK 大写锁定键 115
KEYCODE_BREAK Break/Pause键 121
KEYCODE_SCROLL_LOCK 滚动锁定键 116
KEYCODE_ZOOM_IN 放大键 168
KEYCODE_ZOOM_OUT 缩小键 169
 
****************组合键****************
KEYCODE_ALT_LEFT Alt+Left
KEYCODE_ALT_RIGHT Alt+Right
KEYCODE_CTRL_LEFT Control+Left
KEYCODE_CTRL_RIGHT Control+Right
KEYCODE_SHIFT_LEFT Shift+Left
KEYCODE_SHIFT_RIGHT Shift+Right
 
****************基本****************
KEYCODE_0 按键'0' 7
KEYCODE_1 按键'1' 8
KEYCODE_2 按键'2' 9
KEYCODE_3 按键'3' 10
KEYCODE_4 按键'4' 11
KEYCODE_5 按键'5' 12
KEYCODE_6 按键'6' 13
KEYCODE_7 按键'7' 14
KEYCODE_8 按键'8' 15
KEYCODE_9 按键'9' 16
KEYCODE_A 按键'A' 29
KEYCODE_B 按键'B' 30
KEYCODE_C 按键'C' 31
KEYCODE_D 按键'D' 32
KEYCODE_E 按键'E' 33
KEYCODE_F 按键'F' 34
KEYCODE_G 按键'G' 35
KEYCODE_H 按键'H' 36
KEYCODE_I 按键'I' 37
KEYCODE_J 按键'J' 38
KEYCODE_K 按键'K' 39
KEYCODE_L 按键'L' 40
KEYCODE_M 按键'M' 41
KEYCODE_N 按键'N' 42
KEYCODE_O 按键'O' 43
KEYCODE_P 按键'P' 44
KEYCODE_Q 按键'Q' 45
KEYCODE_R 按键'R' 46
KEYCODE_S 按键'S' 47
KEYCODE_T 按键'T' 48
KEYCODE_U 按键'U' 49
KEYCODE_V 按键'V' 50
KEYCODE_W 按键'W' 51
KEYCODE_X 按键'X' 52
KEYCODE_Y 按键'Y' 53
KEYCODE_Z 按键'Z' 54

```
## 键盘 keycode
Web自动化测试模拟键盘输入
```python
from selenium.webdriver.common.keys import Keys

input_element=driver.find_element_by_id("id_name")
input_element.send_keys(Keys.NUMPAD3)
input_element.send_keys(Keys.CONTROL, "a")
```

selenium按键
```python
NULL = '\ue000'
CANCEL = '\ue001'  # ^break
HELP = '\ue002'
BACKSPACE = '\ue003'
BACK_SPACE = BACKSPACE
TAB = '\ue004'
CLEAR = '\ue005'
RETURN = '\ue006'
ENTER = '\ue007'
SHIFT = '\ue008'
LEFT_SHIFT = SHIFT
CONTROL = '\ue009'
LEFT_CONTROL = CONTROL
ALT = '\ue00a'
LEFT_ALT = ALT
PAUSE = '\ue00b'
ESCAPE = '\ue00c'
SPACE = '\ue00d'
PAGE_UP = '\ue00e'
PAGE_DOWN = '\ue00f'
END = '\ue010'
HOME = '\ue011'
LEFT = '\ue012'
ARROW_LEFT = LEFT
UP = '\ue013'
ARROW_UP = UP
RIGHT = '\ue014'
ARROW_RIGHT = RIGHT
DOWN = '\ue015'
ARROW_DOWN = DOWN
INSERT = '\ue016'
DELETE = '\ue017'
SEMICOLON = '\ue018'
EQUALS = '\ue019'

NUMPAD0 = '\ue01a'  # number pad keys
NUMPAD1 = '\ue01b'
NUMPAD2 = '\ue01c'
NUMPAD3 = '\ue01d'
NUMPAD4 = '\ue01e'
NUMPAD5 = '\ue01f'
NUMPAD6 = '\ue020'
NUMPAD7 = '\ue021'
NUMPAD8 = '\ue022'
NUMPAD9 = '\ue023'
MULTIPLY = '\ue024'
ADD = '\ue025'
SEPARATOR = '\ue026'
SUBTRACT = '\ue027'
DECIMAL = '\ue028'
DIVIDE = '\ue029'

F1 = '\ue031'  # function  keys
F2 = '\ue032'
F3 = '\ue033'
F4 = '\ue034'
F5 = '\ue035'
F6 = '\ue036'
F7 = '\ue037'
F8 = '\ue038'
F9 = '\ue039'
F10 = '\ue03a'
F11 = '\ue03b'
F12 = '\ue03c'

META = '\ue03d'
COMMAND = '\ue03d'
```



```text
vbKeyLButton 1 鼠标左键 
vbKeyRButton 2 鼠标右键 
vbKeyCancel 3 CANCEL 键 
vbKeyMButton 4 鼠标中键 
vbKeyBack 8 BACKSPACE 键 
vbKeyTab 9 TAB 键 
vbKeyClear 12 CLEAR 键 
vbKeyReturn 13 ENTER 键 
vbKeyShift 16 SHIFT 键 
vbKeyControl 17 CTRL 键 
vbKeyMenu 18 菜单键 
vbKeyPause 19 PAUSE 键 
vbKeyCapital 20 CAPS LOCK 键 
vbKeyEscape 27 ESC 键 
vbKeySpace 32 SPACEBAR 键 
vbKeyPageUp 33 PAGEUP 键 
vbKeyPageDown 34 PAGEDOWN 键 
vbKeyEnd 35 END 键 
vbKeyHome 36 HOME 键 
vbKeyLeft 37 LEFT ARROW 键 
vbKeyUp 38 UP ARROW 键 
vbKeyRight 39 RIGHT ARROW 键 
vbKeyDown 40 DOWN ARROW 键 
vbKeySelect 41 SELECT 键 
vbKeyPrint 42 PRINT SCREEN 键 
vbKeyExecute 43 EXECUTE 键 
vbKeySnapshot 44 SNAP SHOT 键 
vbKeyInser 45 INS 键 
vbKeyDelete 46 DEL 键 
vbKeyHelp 47 HELP 键 
vbKeyNumlock 144 NUM LOCK 键 


A 键到 Z 键与其 ASCII 码的相应值'A' 到 'Z' 是一致的
常数 值 描述 
vbKeyA 65 A 键 
vbKeyB 66 B 键 
vbKeyC 67 C 键 
vbKeyD 68 D 键 
vbKeyE 69 E 键 
vbKeyF 70 F 键 
vbKeyG 71 G 键 
vbKeyH 72 H 键 
vbKeyI 73 I 键 
vbKeyJ 74 J 键 
vbKeyK 75 K 键 
vbKeyL 76 L 键 
vbKeyM 77 M 键 
vbKeyN 78 N 键 
vbKeyO 79 O 键 
vbKeyP 80 P 键 
vbKeyQ 81 Q 键 
vbKeyR 82 R 键 
vbKeyS 83 S 键 
vbKeyT 84 T 键 
vbKeyU 85 U 键 
vbKeyV 86 V 键 
vbKeyW 87 W 键 
vbKeyX 88 X 键 
vbKeyY 89 Y 键 
vbKeyZ 90 Z 键 


0 键到 9 键与其 ASCII 码的相应值 '0' 到 '9' 是一致的
常数 值 描述 
vbKey0 48 0 键 
vbKey1 49 1 键 
vbKey2 50 2 键 
vbKey3 51 3 键 
vbKey4 52 4 键 
vbKey5 53 5 键 
vbKey6 54 6 键 
vbKey7 55 7 键 
vbKey8 56 8 键 
vbKey9 57 9 键 


数字小键盘上的键
常数 值 描述 
vbKeyNumpad0 96 0 键 
vbKeyNumpad1 97 1 键 
vbKeyNumpad2 98 2 键 
vbKeyNumpad3 99 3 键 
vbKeyNumpad4 100 4 键 
vbKeyNumpad5 101 5 键 
vbKeyNumpad6 102 6 键 
vbKeyNumpad7 103 7 键 
vbKeyNumpad8 104 8 键 
vbKeyNumpad9 105 9 键 
vbKeyMultiply 106 乘号 (*) 键 
vbKeyAdd 107 加号 (+) 键 
vbKeySeparator 108 ENTER 键（在数字小键盘上） 
vbKeySubtract 109 减号 (-) 键 
vbKeyDecimal 110 小数点 (.) 键 
vbKeyDivide 111 除号 (/) 键 


功能键
常数 值 描述 
vbKeyF1 112 F1 键 
vbKeyF2 113 F2 键 
vbKeyF3 114 F3 键 
vbKeyF4 115 F4 键 
vbKeyF5 116 F5 键 
vbKeyF6 117 F6 键 
vbKeyF7 118 F7 键 
vbKeyF8 119 F8 键 
vbKeyF9 120 F9 键 
vbKeyF10 121 F10 键 
vbKeyF11 122 F11 键 
vbKeyF12 123 F12 键 
vbKeyF13 124 F13 键 
vbKeyF14 125 F14 键 
vbKeyF15 126 F15 键 
vbKeyF16 127 F16 键 
```




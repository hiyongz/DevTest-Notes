# iOS APP�Զ�����class chain��λ����

��[iOS APP�Զ�����predicate��λ](https://blog.csdn.net/u010698107/article/details/120318075)�н�����iOS APP��predicate��λ���������Ľ�����XPath�﷨�Ƚ����Ƶ�class chain��λ������


## class chain ��λ
class chain ��λ������**[mykola-mokhnach](https://github.com/mykola-mokhnach)**��������XPath�Ƚ����ƣ�����ʵ�ֲַ��ѯ�������Ĳ�ѯ���ܸ��ߣ�ͨ����class chain��ѯӳ�䵽һϵ�е�XCUITest�����У��������ӽڵ㣬����XPath�����ݹ�ز�ѯ����UI����

class chain ֧��Predicate�ַ���ƥ�䣬�������class chain ��λ������

### ���ӽڵ�����

ѡ�����Ԫ�أ�������XPath�﷨�еķ�б��`/`��

```bash
XCUIElementTypeWindow[`label BEGINSWITH "text"`][-1] # ѡ��label��foo��ͷ�����һ��
XCUIElementTypeWindow/XCUIElementTypeButton[3] # ѡ��window�Ķ���Ԫ��XCUIElementTypeButton�ĵ�3����������1��ʼ��
XCUIElementTypeWindow/*[3]  # ѡ��window�ĵ�3������Ԫ��
XCUIElementTypeWindow # ѡ�������Ӵ���
XCUIElementTypeWindow[2] # ѡ��ڶ�������
XCUIElementTypeWindow[2]/XCUIElementTypeAny # ѡ��ڶ����Ӵ��ڵ�������Ԫ��
```



### ����ڵ�����

������XPath�﷨�е�˫��б��`//`

```bash
**/XCUIElementTypeCell[`name BEGINSWITH "A"`][-1]/XCUIElementTypeButton[10] # ѡ��name��A��ͷ�����һ��CellԪ�صĵ�10����Ԫ��
**/XCUIElementTypeCell[`name BEGINSWITH "B"`] # ѡ��name��B��ͷ������CellԪ��
**/XCUIElementTypeCell[`name BEGINSWITH "C"`]/XCUIElementTypeButton[10] # ѡ��name��C��ͷ�ĵ�һ��CellԪ�صĵ�10����Ԫ��
**/XCUIElementTypeCell[`name BEGINSWITH "D"`]/**/XCUIElementTypeButton # ѡ��name��D��ͷ�ĵ�һ��CellԪ�������к��Button
```

ʹ��class chain��λ����Ҫע�����¼��㣺
- Predicate�ַ���Ҫд���������У�����ʹ�÷����Ű�����
- Predicate���ʽӦ��д������ǰ��

## class chain��λʾ��
ʹ��[facebook-wda](https://github.com/openatx/facebook-wda)����Ԫ�ص��������

```python
s = c.session('com.apple.Preferences') # ������

s(classChain='XCUIElementTypeWindow/**/XCUIElementTypeCell[`label BEGINSWITH "��Ļ"`]').click() # �������Ļʹ��ʱ�䡿
s(classChain='**/XCUIElementTypeCell[`label BEGINSWITH "��Ļ"`]').click()
s(classChain='**/XCUIElementTypeTable/*[`name == "֪ͨ"`]').click() # �����֪ͨ��
s(classChain='**/XCUIElementTypeCell[7]').click() # �����֪ͨ��
```

����Ķ�λ���Ҳ����ʹ��XPath�﷨����Ӧ���£�
```python
s(xpath='//XCUIElementTypeWindow//XCUIElementTypeCell[starts-with(@label,"��Ļ")]').click()
s(xpath='//XCUIElementTypeCell[starts-with(@label,"��Ļ")]').click()
s(xpath='//XCUIElementTypeTable/*[@name="֪ͨ"]').click()
s(xpath='//XCUIElementTypeCell[7]').click()
```

XPath��λЧ�ʱ�class chain�ͣ�����ʹ��class chain�����ж�λ��

**�ο��ĵ���**

1. [https://github.com/facebookarchive/WebDriverAgent/wiki/Class-Chain-Queries-Construction-Rules](https://github.com/facebookarchive/WebDriverAgent/wiki/Class-Chain-Queries-Construction-Rules)

2. [https://github.com/appium/appium-xcuitest-driver/pull/391](https://github.com/appium/appium-xcuitest-driver/pull/391)


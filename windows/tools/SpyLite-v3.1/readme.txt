Spy++ Lite 3.1.0.1   2018-11-28

    Spy++ Lite是一款功能丰富的编程辅助工具，适用于获取窗口句柄并分析窗体结构。可以探测32位和64位应用程序。可以以十六进制和十进制显示窗口句柄、窗口样式和类样式等数值。可以获取父窗口和兄弟窗口、子窗口结构并形成句柄树，还可以调节窗口的状态和行为，获取程序路径、给窗口截图等。软件还支持获取列表控件数据，如任务管理器、股票行情数据等，还支持获取树视图、下拉框、列表框和菜单数据和字体信息等。

    下面举几个例子来小试牛刀：
    1、激活灰色按钮：
    打开任一文件的属性窗口，它的右下角处“应用”按钮都是不可用的（灰色的）。拖动本软件的探测器指针选中该按钮。切换至“消息”标签页，勾选“窗口可用”。看到了吧？“应用”按钮被我们激活了。

    2、监视IE上网记录：
    用本软件的探测器指针选中IE的地址栏。看到它的窗口类名为Edit；切换至“窗口”标签页，点击“父窗口”标签，使父窗口成为当前窗口；切换到“类”标签页，看到其类名为ComboBox；再依照上步点击，将得到父窗口类名依次是ComboBoxEx32、ReBarWindow32、WorkerW，直到最外层的IEFrame。此时再点击“子窗口列表”按钮，依次双击子窗口，看看能否找到地址栏Edit。窗体结构清楚了，我们就不难用FindWindowEx、SendMessage、GetClassName、GetWindowText等几个API函数来监视上网记录了。
    3、无论是32位还是64位应用程序，用Spy++ Lite选中后，都可以获取其所在位置并打开。

    4、可以获取类名为ListCtrl、ListView、TreeCtrl、TreeView、ComboBox、ListBox的窗口数据内容和菜单文本。

升级日志：
2.4-3.1
    增加功能：
    1、支持探测64位应用程序；
    2、探测兄弟窗口和子窗口并形成句柄树；
    3、支持获取类名为ListCtrl、ListView、TreeCtrl、TreeView、ComboBox、ListBox的窗口数据内容和菜单文本。
2.2-2.4
    增加功能:
    1、更换内部控件，引用主题风格；
    2、修正细节问题；
    3、提供不同编程语言的开源版本。
2.1-2.2
    增加功能:
    1、去除对对话框控件的依赖；
    2、修正进程ID的显示BUG。
2.0-2.1
    增加功能：
    1、可以直接选中不可用的窗口；
    2、子窗口列表；
    3、进入多级子窗口并可导出。
1.1-2.0
    增加功能：
    1、显示窗口ID、进程ID、程序文件路径；
    2、窗口样式、扩展样式、类样式并列表给出；
    3、消息功能，改变窗口的最大化、最小化、是否可见、是否可用等状态；
    4、窗口截图。

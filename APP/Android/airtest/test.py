
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# poco(text='行情').click()
# poco(textMatches='^行.*$', enable=True).click()
# poco("android:id/tabs").child("android.widget.RelativeLayout")[1].offspring(text="行情").click()

# poco("android.widget.RelativeLayout").sibling(text="行情").click()

ele = poco(text='行情')
print(ele.attr('type'))  # 属性
print(ele.attr('text')) # text属性
print(ele.get_bounds())  # 边界框
print(ele.get_position()) # 像素坐标
print(ele.get_size()) # UI 元素大小
print(ele.get_name())  # 元素名称
print(ele.get_text())  # 元素文本值，和ele.attr('text')一样
print(ele.exists())  # 元素是否存在





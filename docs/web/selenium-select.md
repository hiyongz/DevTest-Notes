# Select下拉框
在web自动化测试中，经常会遇到下拉框，对列出的选项进行选择，或者判断选择的选项，本文将介绍如何使用Selenium去操作下拉框，实现自动化测试。

<!--more-->

## 测试页面

URL http://sahitest.com/demo/selectTest.htm

![](selenium-select/1.png)
## Select方法

使用WebElement类的send_keys(value)方法也可以选择下拉框（select标签）的值，但它只能使用选项的value值来定位：

```python
self.driver.get("http://sahitest.com/demo/selectTest.htm")
ele = self.driver.find_element_by_id('s3Id')
print(ele.text) # 打印select所有选项值
ele.send_keys("o2val") # 选择value=o2val 的选项
print(ele.get_attribute("value")) # 打印所选择的value值
```

结果：

```python
o1
o2
o3
    With spaces
    With nbsp
o2val
```



select类所有方法：

1. **select_by_index**(*index*)：通过选项index选择
2. **select_by_value**(*value*)：通过选项value值选择
3. **select_by_visible_text**(*text*)：过显示的文本选择
4. **deselect_by_index**(*index*)：取消选择，用于多选
5. **deselect_by_value**(*value*)：取消选择，用于多选
6. **deselect_by_visible_text**(*text*)：取消选择，用于多选
7. **deselect_all**()：全部取消，用于多选
8. options：所有选项
9. first_selected_option：第一个选择的选项（多选情况下）或者当前选择的选项（单选）
10. all_selected_options：所有已经选择的选项

## 选择

**select_by_index、select_by_value、select_by_visible_text三种方法选择**

first_selected_option.text返回当前所选择的选项值

```python
self.driver.get("http://sahitest.com/demo/selectTest.htm")
ele = self.driver.find_element_by_id('s3Id')
selected_element = Select(ele)  # 实例化Select
selected_element.select_by_index(1)
# for select in selected_element.all_selected_options:
#     print(select.text)
print(selected_element.first_selected_option.text) # 打印当前选择的选项值
sleep(1)
selected_element.select_by_value("o2val")
print(selected_element.first_selected_option.text)
sleep(1)
selected_element.select_by_visible_text("o3")
print(selected_element.first_selected_option.text)
sleep(1)
```



结果：

```python
o1 
o2 
o3
```



## 取消选择

取消选择**deselect不能用于下拉框选择，只能用于多选，即属性**multiple="multiple"的select标签。

取消选择有**deselect_by_index**、**deselect_by_value**、**deselect_by_visible_text**、**deselect_all四种方法**

all_selected_options返回所有已选择的选项

```python
self.driver.get("http://sahitest.com/demo/selectTest.htm")
## 多选
ele2 = self.driver.find_element_by_id('s4Id')
selected_element2 = Select(ele2)  # 实例化Select
selected_element2.select_by_index(1)
selected_element2.select_by_index(2)
selected_element2.select_by_index(3)
print("######")
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_index(1)
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_value("o2val")
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_visible_text("o3")
for select in selected_element2.all_selected_options:
    print(select.text)
```



结果：

```python
######
o1
o2
o3
######
o2
o3
######
o3
######
```


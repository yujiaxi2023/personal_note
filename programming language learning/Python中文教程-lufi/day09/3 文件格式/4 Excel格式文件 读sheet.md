python内部并未提供处理excel文件的功能，想在python中操作excel需要安装模块openpyxl
```python
pip install openpyxl
```
模块继承了python中操作excel的相关功能

**1. 读excel**
- 读sheet
```python
from openpyxl import load_workbook  
  
wb = load_workbook("file/Book1.xlsx")  
  
# sheet 相关操作  
  
# 1. 获取excel文件中所有sheet名称  
print(wb.sheetnames) # ['数据导出', '用户列表‘, 'sheet1', 'shhet2']  
  
# 2. 选择sheet 基于sheet名称  
sheet = wb['数据导出']  
  
cell = sheet.cell(1,2)  
print(cell.value) # 选择单元格  
  
  
# 3. 选择sheet 基于索引位置  
sheet0 = wb.worksheets[0]  
cell = sheet.cell(1,2)  
print(cell.value)  
  
# 4. 循环所有的sheet  
for name in wb.sheetnames:  
    sheet = wb[name]  
    cell = sheet.cell(1,1)  # 读取第一行第一列，循环所有的sheet
    print(cell.value)  
      
for sheet in wb.worksheets:  
    cell = sheet.cell(1, 1)  # 直接可以取每一个sheet
    print(cell.value)  
      
for sheet in wb:  
    cell = sheet.cell(1, 1)  # 跟worksheet是类似的
    print(cell.value)
```

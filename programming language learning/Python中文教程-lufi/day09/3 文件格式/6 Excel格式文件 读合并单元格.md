```python
from  openpyxl import  load_workbook  
  
wb = load_workbook('file/Book1.xlsx')  
sheet = wb.worksheets[1]  
  
# 获取第n行第n列的数据（从1开始）  
c1 = sheet.cell(1,1)  
print(c1)  
print(c1.value)  
  
c2 = sheet.cell(1,2)  
print(c2) #  
print(c2.value)  
  
c3 = sheet.cell(10,2)  
print(c3) #  
print(c3.value)  
  
c4 = sheet.cell(11,2)  
print(c4) #  
print(c4.value)  
  
"""  
<Cell 'Sheet2'.A1>  
距离2024年元旦还有  
<MergedCell 'Sheet2'.B1>  
None  
  
列也是只有第一列包含信息，如果是行列结合就是第一行第一列有信息  
<Cell 'Sheet2'.B10>  
思维  
<MergedCell 'Sheet2'.B11>  
None  
"""  
  
# 循环获取每一行每一列数据  
for row in sheet.rows:  
    print(row)
```
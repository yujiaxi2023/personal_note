打开excel文件时一样的操作
```python
from openpyxl import load_workbook  
  
wb = load_workbook('file/Book1.xlsx')  
sheet = wb.worksheets[0]  
  
# 1. 获取第n行第n列单元格  
cell = sheet.cell(1, 1)  
# 获取单元格的时候是从1开始不是从0开始，这跟python不一样  
print(cell.value) # 获得单元格的文本信息  
print(cell.style) # 样式  
print(cell.font) # 字体  
print(cell.alignment) # 排列情况 水平居中等等  
"""  
距离2024年元旦还有  
Normal  
<openpyxl.styles.fonts.Font object>  
Parameters: （一个特殊的对象，包含有很多信息内容）  
name='Calibri', charset=None, family=None, b=True, i=False, strike=None, outline=None, shadow=None, condense=None, color=<openpyxl.styles.colors.Color object>  
Parameters:  
rgb=None, indexed=None, auto=None, theme=1, tint=0.0, type='theme', extend=None, sz=14.0, u=None, vertAlign=None, scheme='minor'  
<openpyxl.styles.alignment.Alignment object>  
Parameters:  
horizontal='center', vertical='center', textRotation=0, wrapText=None, shrinkToFit=None, indent=0.0, relativeIndent=0.0, justifyLastLine=None, readingOrder=0.0  
"""  
  
# 2. 获取某个单元格  
c1 = sheet["A2"] # 通过excel中的单元格位置信息直接获得单元格信息  
print(c1.value)  
  
c2 = sheet["D6"]  
print(c2.value)  
"""  
这是今年第几周  
无事可忙情况下 8个小时 晚上23前  
"""  
  
# 3. 获取第n行所有的单元格  
print(sheet[1]) # 获取第一行所有单元格 元组  
# (<Cell 'Sheet1'.A1>, <MergedCell 'Sheet1'.B1>, <MergedCell 'Sheet1'.C1>, <Cell 'Sheet1'.D1>, <Cell 'Sheet1'.E1>, <MergedCell 'Sheet1'.F1>, <MergedCell 'Sheet1'.G1>, <MergedCell 'Sheet1'.H1>, <MergedCell 'Sheet1'.I1>, <MergedCell 'Sheet1'.J1>, <MergedCell 'Sheet1'.K1>, <MergedCell 'Sheet1'.L1>, <MergedCell 'Sheet1'.M1>, <MergedCell 'Sheet1'.N1>, <MergedCell 'Sheet1'.O1>, <MergedCell 'Sheet1'.P1>, <MergedCell 'Sheet1'.Q1>, <MergedCell 'Sheet1'.R1>, <MergedCell 'Sheet1'.S1>, <MergedCell 'Sheet1'.T1>, <MergedCell 'Sheet1'.U1>, <MergedCell 'Sheet1'.V1>, <MergedCell 'Sheet1'.W1>, <MergedCell 'Sheet1'.X1>, <MergedCell 'Sheet1'.Y1>, <MergedCell 'Sheet1'.Z1>, <MergedCell 'Sheet1'.AA1>, <MergedCell 'Sheet1'.AB1>, <MergedCell 'Sheet1'.AC1>, <MergedCell 'Sheet1'.AD1>, <MergedCell 'Sheet1'.AE1>, <MergedCell 'Sheet1'.AF1>, <MergedCell 'Sheet1'.AG1>, <MergedCell 'Sheet1'.AH1>, <MergedCell 'Sheet1'.AI1>, <MergedCell 'Sheet1'.AJ1>, <MergedCell 'Sheet1'.AK1>)  
  
for cell in sheet[5]:  
    print(cell.value)  
  
  
# 4. 获取所有行的数据  
for row in sheet.rows:  
    print(row[0].value) # 获取到每一行的第0列，这里是0是因为从元组中获得数据，所以是从0开始  
  
# 5. 获取所有列的数据  
for col in sheet.columns:  
    print(col[0].value) # 获取每一列的第0行
```
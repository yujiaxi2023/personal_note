Excel中想要写文件，大致要分为在：
- 原Excel文件基础上写入内容
```python
from  openpyxl import load_workbook  
  
wb = load_workbook('file/Book1.xlsx')  
sheet = wb.worksheets[0]  
  
# 找到单元格，修改其中的内容  
cell = sheet.cell(1,1)  
cell.value = "new start"  
  
# 将excel文件保存到一个新的xlsx文件中  
wb.save('file/p2.xlsx')
```

- 新建excel文件写内容
```python
from openpyxl import  workbook  
  
# 创建excel且会默认创建一个sheet（名称为sheet）  
wb = workbook.Workbook()  
  
# sheet = wb.worksheets[0]  
sheet = wb['Sheet']  
  
# 找到单元格，修改其中内容  
cell = sheet.cell(1,1)  
cell.value = "newstarts"  
  
# 将excel文件保存到p2.xlsx文件中  
wb.save('file/p3.xlsx')
```


了解了读取excel和创建excel之后，后续对于excel中的sheet和cell操作基本上都相同

修改sheet的操作
```python
from openpyxl import workbook  
wb = workbook.Workbook()  
  
# 1. 修改sheet 名称  
sheet = wb.worksheets[0]  
sheet.title = "dataset"  
wb.save("p1.xlsx")  
  
# 2. 创建sheet并设置sheet颜色  
sheet = wb.create_sheet("workplan", 0)  
sheet.sheet_properties.tabColor = "1072BA"  
# 往上搜索RGB的对照表  
wb.save("p1.xlsx")  
  
# 3. 默认打开的sheet  
wb.active = 0  
wb.save("p1.xlsx")  
  
# 4. 拷贝sheet  
sheet = wb.create_sheet("workplan1", 0)  
sheet.sheet_properties.tabColor = "1072BA"  
# 可以先创建一个sheet  
# 也可以直接用一个sheet  
# sheet = wb['dataset']  
  
new_sheet = wb.copy_worksheet(wb["Sheet"])  
new_sheet.title = "newnewplan"  
wb.save("p1.xlsx")  
  
# 5. 删除sheet  
del wb['newnewplan']  
wb.save('p1.xlsx')
```

修改单元格操作
```python
from openpyxl import load_workbook  
from openpyxl.styles import *  
  
wb = load_workbook('file/p1.xlsx')  
  
sheet = wb.worksheets[0]  
  
# 1. 获取某个单元格，修改值  
cell = sheet.cell(1,1)  
cell.value = "start"  
wb.save('p4.xlsx')  
  
# 2. 获取某个单元格，修改值  
sheet['B2'] = "alex"  
wb.save('p4.xlsx')  
  
# 3. 获取某些单元格 修改值  
cell_list = sheet["B3":"C3"]  
"""  
获得一个元组  
(  
    (cell, cell),    (cell, cell),)  
进行循环的单元格的修改  
"""  
for row in cell_list:  
    for cell in row:  
        cell.value = "new value"  
wb.save("p4.xlsx")  
  
  
# 4. 对齐方式  
cell = sheet.cell(1,1)  
  
# horizontal,水平方向对齐方式：”general“， ”left“， ”center“，“right”，“fill”，“justify”，“centerContinuous”，”distributed“  
# vertical，垂直方向对齐方式："top","center","bottom", "justify","distributed"  
# text_rotation,旋转角度  
# wrap_text,是否自动换行  
cell.alignment = Alignment(horizontal="center",vertical='distributed',text_rotation=45,wrap_text = True)  
wb.save('p4.xlsx')  
  
# 5. 设置单元格边框  
# side的style有如下："dashDot", "dashDotDot","dashed","dotted","double","hair","medium","mediumDashDot",  
# "mediumDashDotDot", "mediumDashed", "slantDashDot","thick", "thin"  
  
cell = sheet.cell(9,2)  
cell.border = Border(  
    top=Side(style='thin', color='FFB6C1'),  
    bottom=Side(style='dashed',color='9932CC'),  
    left=Side(style='dashed',color='9932CC'),  
    right=Side(style='dashed',color='9932CC'),  
    diagonal=Side(style="thin",color="483D8B"), # 对角线  
    diagonalUp=True, # 左下-右上  
    # diagonalDown=True # 左上-右下  
)  
wb.save('p4.xlsx')  
# 注意，执行的时候需要关闭excel文件，否则会拒绝访问  
# 需要引入Alignment Border Side 模块，全部在openpyxl.styles中
```
![[Pasted image 20230805163505.png]]
styles中常见的的各种功能 如上图所示
```python
# 6. 字体  
cell = sheet.cell(5,1)  
cell.font = Font(name="Segoe UI", size=45, color="ff0000", underline='single')  
wb.save('p4.xlsx')  
  
# 7. 背景色  
cell = sheet.cell(5,3)  
cell.fill = PatternFill('solid', fgColor='99ccff')  
wb.save('p4.xlsx')  
  
# 8. 渐变背景色  
cell = sheet.cell(5,5)  
cell.fill = GradientFill('linear', stop=("FFFFFF", '99ccff', '000000')) # 指定左中右三种颜色，还可以添加  
wb.save('p4.xlsx')  
  
# 9. 宽高（从索引1开始）  
sheet.row_dimensions[1].height = 50  
sheet.column_dimensions['E'].width = 100  
  
# 10. 合并单元格  
sheet.merge_cells("B2:D8")  
sheet.merge_cells(start_row=15, start_column=3, end_column=8, end_row=18)  
wb.save('p2.xlsx')  
  
sheet.unmerge_cells('B2:D8')  
wb.save('p4.xlsx')  
  
# 11. 写入公式  
sheet = wb.worksheet[0]  
sheet['D1']="summary"  
sheet['D2']='=B2*C2'  
wb.save('p2.xlsx')  
  
sheet = wb.worksheet[0]  
sheet["D3"] = '=SUM(B3,C3)'  
wb.save("p2.xlsx")  
  
# 12. 删除  
# idx 要删除的索引位置  
# amount，从索引位置开始要删除的个数（默认为1）  
sheet.delete_rows(idx=1, amount=2)  
sheet.delete_cols(idx=1, amount=3)  
wb.save("p2.xlsx")  
  
# 13. 插入  
sheet.insert_rows(idx=5, amount=10)  
sheet.insert_cols(idx=3, amount=2)  
wb.save('p2.xlsx')  
  
# 14. 循环写内容  
sheet = wb["Sheet"]  
cell_range = sheet["A1:C2"] # 选中一块区域写入值  
for row in cell_range:  
    for cell in row:  
        cell.value="xx"  
  
for row in sheet.iter_rows(min_row=5, min_col=1, max_row=10, max_col=7): # 从几行几列开始到几行几列结束，这块区域进行写值  
    for cell in row:  
        cell.value = "oo"  
wb.save("p4.xlsx")  
  
  
# 15. 移动  
# 将H2：J10 范围的数据，向右移动15个位置，向上移动1个位置  
sheet.move_range("H2:J10", rows=-1, cols=15) # 负数向上，正数向下对于row 负数向左，正数向右，对于col  
wb.save('p2.xlsx')  
  
# 让公式进行移动，并且要进行变化或者保留两种  
sheet = wb.worksheet['0']  
sheet['D1'] = "summary"  
sheet['D2'] = "=B2*C2"  
sheet['D3'] = "=SUM(B3,C3)"  
sheet.move_range("B1:D3", cols=10, translate=True) # True 是会自动变更公式，False就是不动  
wb.save('p2.xlsx')  
  
# 16. 打印区域  
sheet.print_area = "A1:D200"  
wb.save("p2.xlsx")  
  
# 17. 打印，每个页面固定表头  
sheet.print_title_cols = "A:D"  
sheet.print_title_rows = "1:3"  
wb.save("p2.xlsx")  
# 如果打印的太长了，想保留每个页面都有一个表头，就可以这样设置
```


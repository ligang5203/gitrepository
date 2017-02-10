# coding: UTF-8
import xlrd
import xdrlib, sys

data = xlrd.open_workbook('D:\\test.xlsx')  # 打开excel表格
table = data.sheet_by_index(0)              # 通过索引获取第一张工作表
# table = data.sheet_by_name('Sheet1')      # 通过表单名称获取第一张工作表
nrows = table.nrows                         # 获取行数
# ncols = table.ncols                       # 获取列数

for i in range(nrows):                      # 循环输出每行数据
    print table.row_values(i)

cell_C4 = table.cell(3, 2).value            # 获取单元格C4（第4行第3列）的值
# cell_c4 = table.row(3)[2].value           # 使用行列索引获取单元格的值
print cell_C4

# excel写入数据
row = 3                                     # 行数
col = 2                                     # 列数
ctype = 1                                   # 单元格值的类型：0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
value = 'new test'                          # 单元格的具体值
xf = 0                                      # 扩展的格式化
table.put_cell(row, col, ctype, value, xf)  # 写入到excel C4格

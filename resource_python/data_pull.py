import glob

import sys

import os

import datetime

import re

import win32api

import win32con
import xlrd
import xlwt

export_list_title = ['姓名', '工号', '公司名称', '部门', '组别', '性别', '级别', '入职日期', '离职日期',
                     '虚拟入职日期', '转正日期', '毕业院校', '学历', '专业', '毕业时间', '岗位', '出生年月',
                     '身份证号', '联系方式', '月份', '入职时长', '员工状态', ]
sheet_name_include = ['在职', '休假', '离职']

def read_excel_files(filename_list):
    for file in filename_list:
        print(file)
        workbook = xlrd.open_workbook(filename=file)
        for sheet_index, sheet_name in enumerate(workbook.sheet_names()):
            for one in sheet_name_include:
                if one in sheet_name:
                    print(sheet_index, sheet_name)
                    global company, emp_status
                    company = os.path.basename(file)[0:4]
                    emp_status = one
                    read_excel_sheet(workbook.sheet_by_name(sheet_name))
    pass

def read_excel_sheet(sheet_name):
    #  判断每个 sheet 标题栏的行号 title_base
    #  依据要生成的 标题 栏的名称， 获取 索引 index 的位置，不存在则为空
    #  按照索引，写入新的excel中
    export_dict_title_index = {}
    title_row_index = None
    # 确定 title_row_index
    for row_index in range(sheet_name.nrows):
        for col_index in range(sheet_name.ncols):
            if sheet_name.cell_value(row_index, col_index) == export_list_title[0]:
                # print(sheet_name.cell_value(row_index, col_index), row_index, col_index)
                title_row_index = row_index
                break
    # 确定索引位置
    for col_index in range(sheet_name.ncols):
        if sheet_name.cell_value(title_row_index, col_index) in export_list_title:
            export_dict_title_index[sheet_name.cell_value(title_row_index, col_index)] = col_index
    # print(export_dict_title_index)
    # 输入数据
    for row_index in range(title_row_index + 1, sheet_name.nrows):
        data_list = []
        for one in export_list_title:
            if sheet_name.cell_value(row_index, export_dict_title_index['姓名']) == '':
                continue
            if export_dict_title_index.get(one):
                data_list.append(sheet_name.cell_value(row_index, export_dict_title_index[one]))
            elif one == '公司名称':
                data_list.append(company)
            elif one == '员工状态':
                data_list.append(emp_status)
            elif one == '月份':
                try:
                    datetime.datetime.strptime(sheet_name.cell_value(row_index, export_dict_title_index['出生年月']),
                        '%Y-%m-%d')
                except:
                    data_list.append('')
                else:
                    data_list.append(str(
                        datetime.datetime.strptime(
                        sheet_name.cell_value(row_index, export_dict_title_index['出生年月']),'%Y-%m-%d').month))
                pass
            else:
                data_list.append('')
        # print(data_list)
        sheet_write.send(data_list)
    pass


def write_sheet_generator():
    workbook_name = xlwt.Workbook()
    sheet_name = workbook_name.add_sheet('人员名单')
    row_index = 0
    while True:
        data_list = yield
        if data_list is False:
            break
        # print(data_list)
        for col_index, one in enumerate(data_list):
            # sheet_name.write(row_index, col_index, one)
            # 写入公式。 但是在职与离职的入职时长，公式不一致
            # sheet_name.write(row_index, col_index, xlwt.Formula(one))
            sheet_name.write(row_index, col_index, one)
        if len(data_list) != 0:
            row_index += 1
    workbook_name.save('报表数据_{date}.xls')
    pass


if __name__ == '__main__':
    win32api.MessageBox(0, '请将所有花名册放到当前文件夹', "报表数据源文件生成", win32con.MB_OK)
    # 防止因为打包为 exe 文件，路径定位错误
    path = sys.path[0]
    if os.path.isfile(sys.path[0]):
        path = os.path.dirname(sys.path[0])
    files = glob.glob(path + os.sep + '*.xlsx')
    if len(files) == 0:
        win32api.MessageBox(0, '当前文件夹无任何花名册,正在退出', "报表数据源文件生成", win32con.MB_OK)
        exit(0)
    print(files)
    sheet_write = write_sheet_generator()
    next(sheet_write)
    sheet_write.send(export_list_title)
    read_excel_files(files)
    sheet_write.send(False)

    # 关闭生成器，并保存
    # next(write_sheet_generator(flag=False))
    # sheet.save('报表数据_{date}.xls'.format(date=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
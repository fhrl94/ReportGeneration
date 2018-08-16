import glob

import sys

import os

import datetime

import win32api
from collections import Counter

import win32con
import xlrd
import xlwt


class ExcelColumnStructure:
    # sex_choices = ('男', '女')
    # company_name_choices = ('信息科技', '百捷集团', '盛世百捷', '百度推广')

    col_type_list = ['str', 'int', 'date', 'str_choice']

    def __init__(self, builder):
        self.index = builder.index
        self.name = builder.name
        self.db_name = builder.db_name
        self.col_type = builder.col_type
        self.tuple_choice = builder.tuple_choice
        self.is_null = builder.is_null
        self.length = builder.length
        self.repeat = builder.repeat
        pass

    def check_regulation(self, value):
        """

        :param value:
        :return: 日期型数据返回日期，其余返回 str
        """
        # 空类型 不检查
        if value is None or value == "":
            if self.is_null is None:
                raise UserWarning("数据列 {name} 不能为空".format(name=self.name))
            return None
        else:
            # 检查 长度
            if not (self.length is None) and len(str(value)) != self.length:
                raise UserWarning("数据列 {name} 长度不为 {length}，当前值为 {value},请检查 excel 数据列格式或数值".format(name=self.name,
                                                                                                    length=self.length,
                                                                                                    value=value))
            # 检查选项
            if not (self.tuple_choice is None):
                if not (value in self.tuple_choice):
                    raise UserWarning("数据列 {name} 必须在 {tuple_choice}，请检查数据列，或联系管理员".format(name=self.name,
                                                                                           tuple_choice='、'.join(
                                                                                               self.tuple_choice)))
            if self.col_type == 'str':
                if not isinstance(value, str):
                    raise UserWarning("数据列 {name} 不为文本，当前值为{value},请检查数据列".format(name=self.name, value=value))
            if self.col_type == 'int':
                try:
                    int(value)
                except ValueError:
                    raise UserWarning(
                        "数据列 {name} 不是数值，当前值为 {value},请检查 excel 数据列格式或数值".format(name=self.name, value=value))
            # 日期检查
            if self.col_type == 'date':
                try:
                    return datetime.datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    raise UserWarning(
                        "数据列 {name} 不是日期，当前值为 {value},请检查 excel 数据列格式或数值".format(name=self.name, value=value))
                except TypeError:
                    raise UserWarning(
                        "数据列 {name} 不是日期，当前值为 {value},请检查 excel 数据列格式或数值".format(name=self.name, value=value))
        return value

    class ExcelColumnStructureBuild:

        def __init__(self):
            self.index = None
            self.name = None
            self.col_type = None
            self.tuple_choice = None
            self.is_null = False
            self.length = None
            self.repeat = False

        def set_index(self, index):
            assert isinstance(index, int), "必须为 int 类型"
            self.index = index
            return self

        def set_name(self, name):
            self.name = name
            return self

        def set_db_name(self, db_name):
            self.db_name = db_name
            return self

        def set_col_type(self, col_type):
            assert col_type in ExcelColumnStructure.col_type_list, "只能在下列类型中选择:{data}".format(
                data="、".join(ExcelColumnStructure.col_type_list))
            self.col_type = col_type
            return self

        def set_is_null(self, is_null):
            assert isinstance(is_null, bool), "必须为 bool 类型"
            self.is_null = is_null
            return self

        def set_tuple_choice(self, tuple_choice):
            assert isinstance(tuple_choice, tuple), "必须为 tuple 类型"
            self.tuple_choice = tuple_choice
            return self

        def set_length(self, length):
            assert isinstance(length, int), "必须为 int 类型"
            self.length = length
            return self

        def set_repeat(self, repeat):
            assert isinstance(repeat, bool), "必须为 bool 类型"
            self.repeat = repeat
            return self

        def built(self):
            self._check()
            return ExcelColumnStructure(self)

        def _check(self):
            # 检查 索引、名称、类型不为 None
            if self.index is None:
                raise UserWarning("没有设置 index")
            if self.name is None:
                raise UserWarning("没有设置 name")
            if self.db_name is None:
                raise UserWarning("没有设置 db_name")
            if self.col_type is None:
                raise UserWarning("没有设置 col_type")
            #
            if self.col_type == 'str_choice' and self.tuple_choice is None:
                raise UserWarning("没有设置 tuple_choice")
                pass


# export_list_title = ['姓名', '工号', '公司名称', '部门', '组别', '性别', '级别', '入职日期', '离职日期',
#                      '虚拟入职日期', '转正日期', '毕业院校', '学历', '专业', '毕业时间', '岗位', '出生年月',
#                      '身份证号', '联系方式', '月份', '入职时长', '员工状态', ]
# sheet_name_include = ('在职', '休假', '离职')

export_list_column = [{'name': '姓名', 'db_name': 'name', 'col_type': 'str', },
                      {'name': '工号', 'db_name': 'code', 'col_type': 'int', 'length': 10, 'repeat': True, },
                      {'name': '公司名称', 'db_name': 'company', 'col_type': 'str_choice',
                       'tuple_choice': ('信息科技', '百捷集团', '盛世百捷', '百度推广'), },
                      {'name': '部门', 'db_name': 'department', 'col_type': 'str', },
                      {'name': '组别', 'db_name': 'group', 'col_type': 'str', },
                      {'name': '性别', 'db_name': 'gender', 'col_type': 'str_choice', 'tuple_choice': ('男', '女'), },
                      {'name': '级别', 'db_name': 'level', 'col_type': 'str', },
                      {'name': '入职日期', 'db_name': 'entry_date', 'col_type': 'date', },
                      {'name': '离职日期', 'db_name': 'dimission_date', 'col_type': 'date', 'is_null': True, },
                      {'name': '虚拟入职日期', 'db_name': 'division_date', 'col_type': 'date', },
                      {'name': '转正日期', 'db_name': 'emp_positive_date', 'col_type': 'date', 'is_null': True, },
                      {'name': '毕业院校', 'db_name': 'graduate_institutions', 'col_type': 'str', 'is_null': True, },
                      {'name': '学历', 'db_name': 'education_background', 'col_type': 'str', 'is_null': True, },
                      {'name': '专业', 'db_name': 'emp_profession', 'col_type': 'str', 'is_null': True, },
                      {'name': '毕业时间', 'db_name': 'graduate_date', 'col_type': 'str', 'is_null': True, },
                      {'name': '岗位', 'db_name': 'emp_position', 'col_type': 'str', },
                      {'name': '出生年月', 'db_name': 'birth_date', 'col_type': 'date', },
                      {'name': '身份证号', 'db_name': 'id_card_num', 'col_type': 'str', 'length': 18, },
                      {'name': '联系方式', 'db_name': 'emp_tel', 'col_type': 'int', 'length': 11, },
                      {'name': '月份', 'db_name': 'mouth_mun', 'col_type': 'int', },
                      {'name': '入职时长', 'db_name': 'time_of_entry', 'col_type': 'str', },
                      {'name': '员工状态', 'db_name': 'emp_status', 'col_type': 'str_choice',
                       'tuple_choice': ('在职', '休假', '离职'), }, ]
export_list_title = [one['name'] for one in export_list_column]
for key_name, count in Counter(export_list_title).items():
    if count > 1:
        raise UserWarning("export_list_column 初始化错误，请联系管理员，存在重复的 name {name}".format(name=key_name))
company_list = [list(one['tuple_choice']) for one in export_list_column if one['name'] == '公司名称'][0]
sheet_name_include = [one['tuple_choice'] for one in export_list_column if one['name'] == '员工状态'][0]
reg_type_dict = {'name': 'set_name', 'db_name': 'set_db_name', 'col_type': 'set_col_type', 'is_null': 'set_is_null',
                 'tuple_choice': 'set_tuple_choice', 'length': 'set_length', 'repeat': 'set_repeat'}
export_list_column_regulation = []
for count, column in enumerate(export_list_column):
    reg = ExcelColumnStructure.ExcelColumnStructureBuild().set_index(count)
    for key, val in column.items():
        if key in reg_type_dict.keys():
            getattr(reg, reg_type_dict[key])(val)
        else:
            raise UserWarning("初始化错误")
    export_list_column_regulation.append(reg.built())
excel_name = '报表数据_{date}.xls'.format(date=datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))


def read_excel_files(filename_list):
    for file in filename_list:
        print(file)
        workbook = xlrd.open_workbook(filename=file)
        if not len(workbook.sheet_names()):
            win32api.MessageBox(0, "花名册【{file}】没有sheet，请查看".format(file=file), "报表数据源文件生成", win32con.MB_OK)
            quit(0)
        for sheet_index, sheet_name in enumerate(workbook.sheet_names()):
            for one in sheet_name_include:
                if one in sheet_name:
                    print(sheet_index, sheet_name)
                    global company, emp_status
                    company = os.path.basename(file)[0:4]
                    if not (company in company_list):
                        win32api.MessageBox(0, "花名册名称前缀必须包含【{company}】其中一个".format(company="、".join(company_list)),
                                            "报表数据源文件生成", win32con.MB_OK)
                        quit(0)
                    emp_status = one
                    try:
                        read_excel_sheet(workbook.sheet_by_name(sheet_name))
                    except UserWarning:
                        win32api.MessageBox(0,
                                            '花名册【{file}】中\n{sheet} 的数据数据错误\n{text}'.format(file=os.path.basename(file),
                                                                                           sheet=sheet_name,
                                                                                           text=sys.exc_info()[1]),
                                            "报表数据源文件生成", win32con.MB_OK)
                        quit(0)
                    break
            else:
                if not ("司龄补回表" in sheet_name):
                    win32api.MessageBox(0, "花名册【{file}】中\nsheet【{sheet_name}】的名称必须包含【{emp_status}】其中之一".format(
                        file=os.path.basename(file), sheet_name=sheet_name,
                        emp_status='、'.join(list(sheet_name_include) + ['司龄补回表'])), "报表数据源文件生成", win32con.MB_OK)
                    quit(0)
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
        # 数据验证
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
                        datetime.datetime.strptime(sheet_name.cell_value(row_index, export_dict_title_index['出生年月']),
                                                   '%Y-%m-%d').month))
                pass
            else:
                data_list.append('')
        # print(data_list)
        sheet_write.send(data_list)
    pass


# 数据验证
def data_validation(data_list):
    """

    :param data_list:
    :return: 日期型数据返回日期，其余返回 str
    """
    assert len(export_list_column_regulation) == len(data_list), "数据长度与标题不一致"
    result_list = []
    for counts, one in enumerate(export_list_column_regulation):
        result_list.append(one.check_regulation(data_list[counts]))
    return result_list
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
        # 数据验证
        if len(data_list) and row_index != 0:
            data_validation(data_list)
        for col_index, one in enumerate(data_list):
            # sheet_name.write(row_index, col_index, one)
            # 写入公式。 但是在职与离职的入职时长，公式不一致
            # sheet_name.write(row_index, col_index, xlwt.Formula(one))
            sheet_name.write(row_index, col_index, one)
        if len(data_list) != 0:
            row_index += 1
    workbook_name.save(excel_name)
    pass


def repetition_check():
    workbook = xlrd.open_workbook(filename=excel_name)
    sheet_ins = workbook.sheet_by_index(0)
    repeat_index_list = {}
    for times, one in enumerate(export_list_column):
        if one.get('repeat'):
            repeat_index_list[times] = []
    for row in range(1, sheet_ins.nrows - 1):
        for times, value_list in repeat_index_list.items():
            value_list.append(sheet_ins.cell_value(row, times))
    repeat_dict_error = {}
    for times, value_list in repeat_index_list.items():
        repeat_list = []
        for key, count in Counter(value_list).items():
            if count > 1:
                repeat_list.append({key: count})
        repeat_dict_error[export_list_title[int(times)]] = repeat_list
    error_text = []
    for repeat_error_name, value_error in repeat_dict_error.items():
        for one in value_error:
            error_text.append(
                "{name} 存在重复项，是 {error_data}".format(name=repeat_error_name, error_data='、'.join(one.keys())))
    if len(error_text):
        win32api.MessageBox(0, "\n".join(error_text), "报表数据源文件生成", win32con.MB_OK)


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
    try:
        sheet_write.send(False)
    except StopIteration:
        pass
    repetition_check()

    # 关闭生成器，并保存  # next(write_sheet_generator(flag=False))  # sheet.save('报表数据_{date}.xls'.format(date=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))

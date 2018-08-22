import copy
import os
import sys
import time

import xlrd
import xlwt
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy

from report_generation.models import EmployeesInfo
from resource_python.data_pull import export_list_title, data_validation, export_list_column


class SheetOptions():
    export_dict_title = {'姓名': 'name', '工号': 'code', '公司名称': 'company', '部门': 'department', '组别': 'group',
                         '性别': 'gender', '级别': 'level', '入职日期': 'entry_date', '离职日期': 'dimission_date',
                         '虚拟入职日期': 'division_date', '转正日期': 'emp_positive_date', '毕业院校': 'graduate_institutions',
                         '学历': 'education_background', '专业': 'emp_profession', '毕业时间': 'graduate_date',
                         '岗位': 'emp_position', '出生年月': 'birth_date', '身份证号': 'id_card_num', '联系方式': 'emp_tel',
                         '员工状态': 'emp_status', '月份': 'mouth_mun', '入职时长': 'time_of_entry', }

    def __init__(self, sheet_title_name, sheet_filter_relation):
        assert isinstance(sheet_filter_relation, dict), "必须使用字典类型"
        for one in sheet_title_name:
            if one not in self.export_dict_title.keys():
                raise UserWarning(
                    "不存在表头 {one}，请在 {list} 中选择".format(one=one, list='、'.join(self.export_dict_title.keys())))
        for row_name, row_name_value in sheet_filter_relation.items():
            if row_name not in self.export_dict_title.keys():
                raise UserWarning(
                    "不存在过滤列 {one}，请在 {list} 中选择".format(one=row_name, list='、'.join(self.export_dict_title.keys())))
            # if isinstance(row_name_value[0], FilterRelation) is False:
            #     # TODO 遍历类属性
            #     print(123)
            #     print(row_name_value[0])
            #     raise UserWarning("不存在过滤关系 {one}，请在 {list} 中选择".format(one=row_name_value[0],
            #         list='、'.join(dir(FilterRelation))))
            assert isinstance(row_name_value, dict), "条件必须为数组"
            assert len(row_name_value) >= 1, "至少有一个条件"
            # 列表
            self.sheet_title_name = sheet_title_name
            # 过滤条件关系为 字典 {row_name: (options, (result...))}
            self.sheet_filter_relation = sheet_filter_relation

    #  筛选数据
    def date_filter(self):

        filter_list = Q()
        for row_name, relation_values in self.sheet_filter_relation.items():
            for relation, condition in relation_values.items():
                parameter = self.export_dict_title[row_name] + relation[0]
                filter_list_tmp = Q()
                if relation[1] == 'include':
                    for one in condition:
                        filter_list_tmp = filter_list_tmp | Q(**{parameter: one})
                elif relation[1] == 'exclude':
                    for one in condition:
                        filter_list_tmp = filter_list_tmp & ~Q(**{parameter: one})
                else:
                    raise UserWarning('FilterRelation 类格式错误')
                filter_list = filter_list & filter_list_tmp
        sheet_title_name_list = []
        for one in self.sheet_title_name:
            sheet_title_name_list.append(self.export_dict_title[one])
        # print(sheet_title_name_list)
        # print(EmployeesInfo.objects.filter(filter_list).values_list(*sheet_title_name_list))
        # sheet_data_list = [self.sheet_title_name, ]
        # for one in EmployeesInfo.objects.filter(filter_list).values(*sheet_title_name_list):
        #     sheet_data_list.append(one)
        # TODO 数据测试
        return EmployeesInfo.objects.filter(filter_list).values_list(*sheet_title_name_list)
        pass

    pass

    #


class WorkSheetWrite:
    # 居中
    general_style = xlwt.XFStyle()
    # 对齐方式
    general_style_alignment = xlwt.Formatting.Alignment()
    general_style_alignment.horz = xlwt.Formatting.Alignment.HORZ_CENTER
    general_style_alignment.vert = xlwt.Formatting.Alignment.VERT_CENTER
    general_style.alignment = general_style_alignment
    # 边框
    general_style_borders = xlwt.Formatting.Borders()
    general_style_borders.bottom = xlwt.Formatting.Borders.THIN
    general_style_borders.top = xlwt.Formatting.Borders.THIN
    general_style_borders.left = xlwt.Formatting.Borders.THIN
    general_style_borders.right = xlwt.Formatting.Borders.THIN
    general_style.borders = general_style_borders

    # 居中 日期格式
    date_style = copy.deepcopy(general_style)
    date_style.num_format_str = "YYY-MM-DD"
    # 左对齐
    left_horz_style = copy.deepcopy(general_style)
    left_horz_style_alignment = xlwt.Formatting.Alignment()
    left_horz_style_alignment.horz = xlwt.Formatting.Alignment.HORZ_LEFT
    left_horz_style_alignment.vert = xlwt.Formatting.Alignment.VERT_CENTER
    left_horz_style.alignment = left_horz_style_alignment
    export_dict_title_type = {'姓名': left_horz_style, '工号': general_style, '公司名称': general_style, '部门': left_horz_style,
                              '组别': left_horz_style, '性别': general_style, '级别': left_horz_style, '入职日期': date_style,
                              '离职日期': date_style, '虚拟入职日期': date_style, '转正日期': date_style, '毕业院校': left_horz_style,
                              '学历': left_horz_style, '专业': left_horz_style, '毕业时间': general_style,
                              '岗位': left_horz_style, '出生年月': date_style, '身份证号': general_style, '联系方式': general_style,
                              '员工状态': general_style, '月份': general_style, '入职时长': left_horz_style, }

    # self.sheet_ins 有多个，
    def __init__(self, workbook_name):
        self._workbook_name = workbook_name
        self._create_worksheet()
        self.workbook_sheet_style_dict = {}
        pass

    def _create_worksheet(self):
        self.workbook_ins = xlwt.Workbook()
        pass

    # def add_sheet_name(self, sheet_name):
    #     self.workbook_ins.add_sheet(sheet_name)
    #     pass

    def title_name_write(self, sheet_name, title_name_list):
        try:
            sheet_ins = self.workbook_ins.add_sheet(sheet_name)
        except Exception:
            sheet_ins = self.workbook_ins.add_sheet(sheet_name)
        # try:
        #     sheet_ins = self.workbook_ins.get_sheet(sheet_name)
        # except Exception:
        #     sheet_ins = self.workbook_ins.add_sheet(sheet_name)
        sheet_name_col_style = []
        for col_index, title_name in enumerate(title_name_list):
            # TODO 可能存在序号
            sheet_ins.write(0, col_index, title_name, self.general_style)
            sheet_ins.col(col_index).width = 3500
            if self.export_dict_title_type.get(title_name):
                sheet_name_col_style.append(self.export_dict_title_type[title_name])
            else:
                raise UserWarning("不存在{title_name}此列的格式".format(title_name=title_name))
        self.workbook_sheet_style_dict[sheet_name] = sheet_name_col_style
        pass

    def title_data_write(self, sheet_name, date_list):
        sheet_ins = self.workbook_ins.get_sheet(sheet_name)
        sheet_name_col_style_list = self.workbook_sheet_style_dict[sheet_name]
        for row_index, row_data in enumerate(date_list):
            # TODO 可能存在序号
            assert len(row_data) == len(sheet_name_col_style_list), "数据与标题的长度不一致"
            for col_index, col_data in enumerate(row_data):
                sheet_ins.write(row_index + 1, col_index, col_data, sheet_name_col_style_list[col_index])

    def save(self):
        print(os.path.basename(self._workbook_name))
        file_path = sys.path[0] + os.path.sep + 'report_generation/tmp'
        if os.path.exists(file_path) is False:
            os.mkdir(file_path)
        self.workbook_ins.save(file_path + os.path.sep + os.path.basename(self._workbook_name) + '.xls')
        pass


def set_selected(workbook_conf_ins):
    def set_reload(modeladmin, request, queryset):
        clear_temp()
        work_sheet_write_ins = WorkSheetWrite(workbook_conf_ins['workbook_name'])
        for one_sheet in workbook_conf_ins['sheet_list']:
            work_sheet_write_ins.title_name_write(one_sheet['sheet_name'], one_sheet['title_name_list'])
            work_sheet_write_ins.title_data_write(one_sheet['sheet_name'], SheetOptions(one_sheet['title_name_list'],
                                                                                        one_sheet[
                                                                                            'col_filter']).date_filter())
            work_sheet_write_ins.save()
        return download_file(sys.path[0] + '/report_generation/tmp/' + workbook_conf_ins['workbook_name'] + '.xls',
                             workbook_conf_ins['workbook_name'], 'xls')

    set_reload.short_description = ugettext_lazy(u"{name}表下载".format(name=workbook_conf_ins['workbook_name']))
    set_reload.__name__ = u"{name}表下载".format(name=workbook_conf_ins['workbook_name'])
    return set_reload


def xadmin_set_selected(workbook_conf_ins):
    # 对应 do_action 函数
    def set_reload(self, queryset):
        clear_temp()
        work_sheet_write_ins = WorkSheetWrite(workbook_conf_ins['workbook_name'])
        for one_sheet in workbook_conf_ins['sheet_list']:
            work_sheet_write_ins.title_name_write(one_sheet['sheet_name'], one_sheet['title_name_list'])
            work_sheet_write_ins.title_data_write(one_sheet['sheet_name'], SheetOptions(one_sheet['title_name_list'],
                                                                                        one_sheet[
                                                                                            'col_filter']).date_filter())
            work_sheet_write_ins.save()
        return download_file(sys.path[0] + '/report_generation/tmp/' + workbook_conf_ins['workbook_name'] + '.xls',
                             workbook_conf_ins['workbook_name'], 'xls')

    set_reload.short_description = ugettext_lazy(u"{name}表下载".format(name=workbook_conf_ins['workbook_name']))
    set_reload.__name__ = u"{name}表下载".format(name=workbook_conf_ins['workbook_name'])
    return set_reload


def clear_temp():
    """
    清除上次生产的文件
    :return:
    """
    temp_dir_list = ['/report_generation/tmp/', ]
    for one in temp_dir_list:
        if not os.path.exists(sys.path[0] + one):
            os.mkdir(sys.path[0] + one)
        for del_file in os.listdir(sys.path[0] + one):
            os.remove(sys.path[0] + one + del_file)
    pass


def file_iterator(file_name, chunk_size=512):
    """
    文件下载【迭代器】 ，节省下载的内存
    :param file_name: 文件名称
    :param chunk_size:
    :return:
    """
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def download_file(file_path_name, download_file_name, category):
    """
    减少下载时，大文件的内存使用
    :param file_path_name: 文件绝对路径
    :param download_file_name: 下载的文件名称
    :param category: 下载的类型
    :return:
    """
    # response = StreamingHttpResponse(file_iterator(file_path_name))
    # xadmin 不支持 StreamingHttpResponse
    response = HttpResponse(file_iterator(file_path_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{name}{now}.{category}"'.format(
        name=urlquote(download_file_name), now=(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))),
        category=category)
    return response


def load_data(path_name):
    # export_list_title
    sheet_name = xlrd.open_workbook(filename=path_name).sheet_by_name('人员名单')
    EmployeesInfo.objects.all().delete()
    EmployeesInfo.objects.bulk_create(read_excel_sheet(sheet_name))
    pass


def read_excel_sheet(sheet_name):
    """

    :param sheet_name:
    :return: 花名册中的每一列生成为 EmployeesInfo 对象的列表
    """
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
    print(export_dict_title_index)
    # 输入数据
    data_ins_list = []
    for row_index in range(title_row_index + 1, sheet_name.nrows):
        data_list = []
        # 数据验证
        for one in export_list_title:
            if sheet_name.cell_value(row_index, export_dict_title_index['姓名']) == '':
                continue
            if not (export_dict_title_index.get(one, None) is None):
                data_list.append(sheet_name.cell_value(row_index, export_dict_title_index[one]))
            else:
                raise UserWarning("列标题{name}必须包含{column}".format(name=one, column="、".join(export_list_title)))
        # 数据验证
        data_ins_list.append(create_employees_info_ins(data_validation(data_list)))
    return data_ins_list
    pass


def create_employees_info_ins(data_list):
    emp_ins = EmployeesInfo()
    for index, column in enumerate(data_list):
        setattr(emp_ins, export_list_column[index]['db_name'], column)
    return emp_ins

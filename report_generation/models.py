import datetime
import sys

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class EmployeesInfo(models.Model):

    name = models.CharField(verbose_name='姓名', max_length=5)
    code = models.CharField(verbose_name='工号', max_length=10, validators=[RegexValidator(r'^[\d]{10}$')], unique=True)
    company = models.CharField(verbose_name='公司名称', max_length=20)
    department = models.CharField(verbose_name='部门', max_length=20)
    group = models.CharField(verbose_name='组别', max_length=5, null=True)
    gender = models.CharField(verbose_name='性别', max_length=5)
    level = models.CharField(verbose_name='级别', max_length=10)
    entry_date = models.DateField(verbose_name='入职日期')
    dimission_date = models.DateField(verbose_name='离职日期', null=True)
    division_date = models.DateField(verbose_name='虚拟入职日期')
    emp_positive_date = models.DateField(verbose_name='转正日期', null=True)
    graduate_institutions = models.CharField(verbose_name='毕业院校', max_length=30, null=True)
    education_background = models.CharField(verbose_name='学历', max_length=10, null=True)
    emp_profession = models.CharField(verbose_name='专业', max_length=10, null=True)
    # 数据源无法控制
    graduate_date = models.CharField(verbose_name='毕业时间', max_length=12, null=True)
    emp_position = models.CharField(verbose_name='岗位', max_length=20, null=True)
    birth_date = models.DateField(verbose_name='出生年月')
    id_card_num = models.CharField(verbose_name='身份证号', max_length=10, validators=[RegexValidator(r'^[\d]{17}[\dxX]$')],
                                   )
    emp_tel = models.CharField(verbose_name='联系方式', max_length=5, validators=[RegexValidator(r'^[\d]{11}$')])
    mouth_mun = models.PositiveIntegerField(verbose_name='月份')
    time_of_entry = models.CharField(verbose_name='入职时长', max_length=50)
    # TODO 状态为 在职、离职、休假
    emp_status = models.CharField('员工状态', max_length=4)

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name
        pass

    def __str__(self):
        return self.name
    pass

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{upload_to}/{filename}_{time}'.format(upload_to=sys.path[0] + '/upload/', filename=filename,
                                                  time=datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S'))

class UploadHistory(models.Model):
    # 表的结构:
    # path_name = models.FileField('文件名称', upload_to=sys.path[0] + '/upload/%Y_%m_%d/%H', )
    path_name = models.FileField('文件名称', upload_to=user_directory_path, )
    upload_time = models.DateTimeField('上传时间', auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '报表自动生成文件上传'
        verbose_name_plural = verbose_name


class WorkbookInfo(models.Model):

    workbook_name = models.CharField(verbose_name="报表名称", max_length=50)
    # TODO 需要标记收件人备注信息
    receiver = models.CharField(verbose_name="收件人", max_length=255)
    cc = models.CharField(verbose_name="抄送人", max_length=255)
    send_time = models.DateField("发送时间")
    # TODO 发送频次

    def __str__(self):
        return str(self.workbook_name)

    class Meta:
        verbose_name = '报表展示'
        verbose_name_plural = verbose_name

class SheetInfo(models.Model):
    sheet_name = models.CharField(verbose_name="sheet 名称", max_length=50)
    column_name_list = models.CharField(verbose_name="列名称", max_length=300)
    workbook_ins = models.ForeignKey(WorkbookInfo, on_delete=models.CASCADE, verbose_name='报表名称')

    def __str__(self):
        return str(self.sheet_name)

    class Meta:
        verbose_name = 'Sheet 展示'
        verbose_name_plural = verbose_name


class FilterColInfo(models.Model):

    filter_col = models.CharField(verbose_name="列名称", max_length=30)
    #   数据校验 或 使用 choices
    filter_relation = models.CharField(verbose_name="过滤关系", max_length=30)
    condition_list = models.CharField(verbose_name="条件列表", max_length=255)
    sheet_ins = models.ForeignKey(SheetInfo, on_delete=models.CASCADE, verbose_name='报表名称')

    def __str__(self):
        return str(self.filter_col)

    class Meta:
        verbose_name = '筛选条件 展示'
        verbose_name_plural = verbose_name
    pass

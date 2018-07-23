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
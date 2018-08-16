from collections import OrderedDict

from django.contrib import admin

# Register your models here.
from report_generation.models import EmployeesInfo, UploadHistory
from report_generation.views import set_selected, load_data
from resource_python.constants import actions_config


@admin.register(EmployeesInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    # import_export_args = {'import_resource_class': EmployeesInfoResource, }
    list_display = ('name', 'code', 'company', 'department', 'group', 'gender', 'level', 'entry_date', 'dimission_date',
                    'division_date', 'emp_positive_date', 'graduate_institutions', 'education_background',
                    'emp_profession', 'graduate_date', 'emp_position', 'birth_date', 'id_card_num', 'emp_tel',
                    'emp_status',)
    list_filter = ('company', 'department', 'emp_status', 'dimission_date', 'entry_date', 'birth_date')
    search_fields = ('name', 'code',)
    ordering = ('code',)

    def get_actions(self, request):
        fns = [set_selected(one) for one in actions_config]
        actions = [self.get_action(fn) for fn in fns]
        actions = OrderedDict((name, (func, name, desc)) for func, name, desc in actions)
        return actions
        pass


@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'path_name', 'upload_time',)
    exclude = []
    actions = ['admin_loading_init', ]

    def admin_loading_init(self, request, queryset):
        # 数据初始化
        assert len(queryset) == 1, "只允许选择一个"
        load_data(str(queryset[0].path_name))
        pass

    pass

    admin_loading_init.short_description = '读取数据'

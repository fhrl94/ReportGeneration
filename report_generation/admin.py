from collections import OrderedDict

from django.contrib import admin

# Register your models here.
from report_generation.models import EmployeesInfo
from report_generation.views import set_selected
from resource_python.constants import actions_config


@admin.register(EmployeesInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    # import_export_args = {'import_resource_class': EmployeesInfoResource, }
    list_display = ('name', 'code', 'company', 'department', 'group', 'gender', 'level', 'entry_date',
                    'dimission_date', 'division_date', 'emp_positive_date', 'graduate_institutions',
                    'education_background', 'emp_profession', 'graduate_date', 'emp_position', 'birth_date',
                    'id_card_num', 'emp_tel', 'emp_status',)
    list_filter = ('company', 'department', 'emp_status', 'dimission_date', 'entry_date', 'birth_date')
    search_fields = ('name', 'code',)
    ordering = ('code',)
    # actions = get_actions()


    def get_actions(self, request):
        fns = [set_selected(one) for one in actions_config]
        actions = [self.get_action(fn) for fn in fns]
        actions = OrderedDict((name, (func, name, desc)) for func, name, desc in actions)
        return actions
        pass
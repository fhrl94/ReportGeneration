import sys

import xadmin
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from xadmin.plugins.actions import BaseActionView
from xadmin.plugins.utils import get_context_dict
from xadmin.views import CommAdminView, BaseAdminPlugin, filter_hook

# 继承BaseAdminPlugin类
from report_generation.models import EmployeesInfo, UploadHistory
from report_generation.resources import EmployeesInfoResource
from report_generation.views import xadmin_set_selected, download_file, load_data
from resource_python.constants import actions_config


class ImportMenuPlugin(BaseAdminPlugin):
    # 使用插件时需要在ModelAdmin类中设置import_export_args属性，插件初始化时使用ModelAdmin的import_export_args进行赋值
    import_export_args = {}

    # 返回True则加载插件，在list列表中显示导入按钮
    def init_request(self, *args, **kwargs):
        return bool(self.import_export_args.get('import_resource_class'))

    def block_top_toolbar(self, context, nodes):
        has_change_perm = self.has_model_perm(self.model, 'change')
        has_add_perm = self.has_model_perm(self.model, 'add')
        if has_change_perm and has_add_perm:
            model_info = (self.opts.app_label, self.opts.model_name)
            import_url = reverse('xadmin:%s_%s_import' % model_info, current_app=self.admin_site.name)
            context = get_context_dict(context or {})  # no error!
            context.update({'import_url': import_url, })
            nodes.append(loader.render_to_string('xadmin/blocks/model_list.top_toolbar.importexport.import.html',
                                                 context=context))


def get_actions():
    actions = []
    for workbook_conf_ins in actions_config:
        action_class = xadmin_set_selected(workbook_conf_ins)
        action = type(action_class.__name__, (BaseActionView,),
                      {'action_name': action_class.__name__, 'description': action_class.short_description,
                       'do_action': action_class})
        actions.append(action)
    return actions


@xadmin.sites.register(EmployeesInfo)
class EmployeeInfoAdmin(object):
    import_export_args = {'import_resource_class': EmployeesInfoResource, }
    list_display = ('name', 'code', 'company', 'department', 'group', 'gender', 'level', 'entry_date', 'dimission_date',
                    'division_date', 'emp_positive_date', 'graduate_institutions', 'education_background',
                    'emp_profession', 'graduate_date', 'emp_position', 'birth_date', 'id_card_num', 'emp_tel',
                    'emp_status',)
    list_filter = ('company', 'department', 'emp_status', 'dimission_date', 'entry_date', 'birth_date')
    search_fields = ('name', 'code',)
    ordering = ('code',)
    actions = get_actions()  # actions = [avs,]


@xadmin.sites.register(UploadHistory)
class UploadHistoryAdmin(object):
    list_display = ('id', 'path_name', 'upload_time',)
    exclude = []
    actions = ['admin_loading_init', ]

    def admin_loading_init(self, request, queryset):
        # 数据初始化
        assert len(queryset) == 1, "只允许选择一个"
        load_data(str(queryset[0].path_name))
        pass

    admin_loading_init.short_description = '读取数据'
    pass


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '报表生成'
    # 设置base_site.html的Footer
    site_footer = '报表生成处理平台'


xadmin.site.register(CommAdminView, GlobalSetting)

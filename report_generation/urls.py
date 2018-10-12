"""ReportGeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView

from report_generation.views import WorkbookInfoView, workbook_info_view_list, SheetInfoView, sheet_info_view_list, \
    get_column_title_list, get_column_condition_list, filter_col_info_view_list, FilterColInfoView, download_custom, \
    index_custom

urlpatterns = [
    # excel 表连接
    url(r'^workbook_info_(?:id=(?P<id>\d+))$', WorkbookInfoView.as_view(), name='WorkbookViewInfo'),
    url(r'^workbook_list_info_(?:page=(?P<page_index>\d+))$', workbook_info_view_list, name='WorkbookViewListInfo'),
    # sheet 链接
    url(r'^sheet_info_(?:id=(?P<id>\d+))$', SheetInfoView.as_view(), name='SheetViewInfo'),
    url(r'^sheet_list_info_(?:id=(?P<id>\d+))&(?:page=(?P<page_index>\d+))$',
        sheet_info_view_list, name='SheetViewListInfo'),
    url(r'^get_column_title_list$', get_column_title_list, name='GetColumnTitleList'),
    # 条件链接
    url(r'^filter_col_info_(?:id=(?P<id>\d+))$', FilterColInfoView.as_view(), name='FilterColInfoView'),
    url(r'^filter_col_list_info_(?:id=(?P<id>\d+))&(?:page=(?P<page_index>\d+))$', filter_col_info_view_list,
        name='FilterColViewListInfo'),
    url(r'^get_column_condition_list_(?:key=(?P<key>\w+))', get_column_condition_list, name='GetColumnConditionList'),
    #
    url(r'^download_custom_(?:id=(?P<id>\d+))$', download_custom, name='DownloadCustom'),
    url(r'^index$', index_custom, name='CustomHtml'),    # 这里将url的根路径指向vue中的index页面
]

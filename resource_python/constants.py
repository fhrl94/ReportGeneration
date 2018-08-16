import datetime


class FilterRelation:
    greater_than = ('__gt', 'include')
    greater_than_or_equal = ('__gte', 'include')
    less_than = ('__lt', 'include')
    less_than_or_equal = ('__lte', 'include')
    equal_to = ('', 'include')
    like = ('__icontains', 'include')
    is_null = ('__isnull', 'include')
    not_in_like = ('__icontains', 'exclude')

actions_config = [
    # ————————————————————————————
    # 1、【推广】客户发展部员工名册
    {'workbook_name': '【推广】客户发展部员工名册',
     'sheet_list': [
         {'sheet_name': '在职',
          'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', ],
          'col_filter':
              {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
               '部门': {FilterRelation().equal_to: ('客户发展部',)},
               '员工状态': {FilterRelation().equal_to: ('在职',)},
                            }
          },
         {'sheet_name': '休假',
          'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', ],
          'col_filter':
              {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
               '部门': {FilterRelation().equal_to: ('客户发展部',)},
               '员工状态': {FilterRelation().equal_to: ('休假',)},
          }
          },
         {'sheet_name': '离职',
          'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '离职日期', ],
          'col_filter':
              {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
               '部门': {FilterRelation().equal_to: ('客户发展部',)},
               '员工状态': {FilterRelation().equal_to: ('离职',)},
               '离职日期': {
                       FilterRelation.greater_than_or_equal: (
                       (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=-1)).replace(day=1), ),
                        }
          }
          },
     ]},
    # ————————————————————————————————————
    # 2、【推广】百度本地广告事业部台账 - 数据
    {'workbook_name': '【推广】百度本地广告事业部台账 - 数据',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '休假',
              'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', '离职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 3、【推广】百度本地广告事业部台账 - 支持
    {'workbook_name': '【推广】百度本地广告事业部台账 - 支持',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', '转正日期'],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 4、【推广】运营增值部人员名单
    {'workbook_name': '【推广】运营增值部人员名单',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '毕业院校', '学历',
                                  '专业', '毕业时间', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('运营增值部',)},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '毕业院校',
                                  '学历', '专业', '毕业时间', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('运营增值部',)},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '离职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('运营增值部',)},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 5、【推广】客户发展部、大客户部人员名单
    {'workbook_name': '【推广】客户发展部、大客户部人员名单',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('客户发展部', '大客户部', )},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('客户发展部', '大客户部', )},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('客户发展部', '大客户部', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 6、【推广】每月离职人员名单
    {'workbook_name': '【推广】每月离职人员名单',
         'sheet_list': [
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '离职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
                   '离职日期': {
                       FilterRelation.greater_than_or_equal: (
                       (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=-1)).replace(day=1), ),
                       FilterRelation.less_than: (datetime.datetime.now().replace(day=1), ),
                        }
                   }
              },
         ]},
    # ——————————————————————————————————
    # 7、【集团各公司】上月入职人员信息
    {'workbook_name': '【集团各公司】上月入职人员信息',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '入职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
                   '入职日期': {
                       FilterRelation.greater_than_or_equal: (
                       (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=-1)).replace(day=1), ),
                       FilterRelation.less_than: (datetime.datetime.now().replace(day=1), ),
                        }
              }
              },
             {'sheet_name': '休假',
              'title_name_list': ['姓名', '部门', '组别', '入职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
                   '入职日期': {
                       FilterRelation.greater_than_or_equal: (
                       (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=-1)).replace(day=1), ),
                       FilterRelation.less_than: (datetime.datetime.now().replace(day=1), ),
                        }
              }
              },
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '入职日期', '离职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
                   '离职日期': {
                       FilterRelation.greater_than_or_equal: (
                      (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=-1)).replace(day=1),),
                      FilterRelation.less_than: (datetime.datetime.now().replace(day=1),),
                   }
              }
              },
         ]},
    # ——————————————————————————————————
    # 8、【推广】百推人员名单
    {'workbook_name': '【推广】百推人员名单',
         'sheet_list': [
             {'sheet_name': '在职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '毕业院校', '学历', '专业', '毕业时间', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '部门': {FilterRelation().equal_to: ('运营增值部', '百度本地广告事业部', '地市拓展部', '业务运营部',
                                                      '运营支持中心', )},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '毕业院校', '学历', '专业', '毕业时间', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                   '部门': {FilterRelation().equal_to: ('运营增值部', '百度本地广告事业部', '地市拓展部', '业务运营部',
                                                      '运营支持中心', )},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '离职日期', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                   '部门': {FilterRelation().equal_to: ('运营增值部', '百度本地广告事业部', '地市拓展部', '业务运营部',
                                                      '运营支持中心', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 9、【集团各公司】人员信息表
    {'workbook_name': '【集团各公司】人员信息表',
         'sheet_list': [
             {'sheet_name': '推广（含远郊）在职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '推广（含远郊）休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '推广（含远郊）离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', '离职日期'],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
             {'sheet_name': '人资中心在职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', )},
                   '部门': {FilterRelation().equal_to: ('人力资源中心', )},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '人资中心休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', )},
                   '部门': {FilterRelation().equal_to: ('人力资源中心', )},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '人资中心离职',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '虚拟入职日期', '入职时长', '出生年月', '离职日期'],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', )},
                   '部门': {FilterRelation().equal_to: ('人力资源中心', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 10、【推广】百度推广最新人员名册
    {'workbook_name': '【推广】百度推广最新人员名册',
         'sheet_list': [
             {'sheet_name': '推广（含远郊）在职',
              'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '身份证号', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('在职',)},
              }
              },
             {'sheet_name': '推广（含远郊）休假',
              'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '身份证号', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                   '员工状态': {FilterRelation().equal_to: ('休假',)},
              }
              },
             {'sheet_name': '推广（含远郊）离职',
              'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '离职日期', '身份证号', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('离职',)},
              }
              },
         ]},
    # ——————————————————————————————————
    # 11、【集团各公司】2018年Qx季度生日名单
    {'workbook_name': '【集团各公司】{year}年Q{num}季度生日名单'.format(year=datetime.datetime.now().year,
                                                          num=int(datetime.datetime.now().month/3) + 1),
         'sheet_list': [
             {'sheet_name': '推广（含远郊）在职、休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '出生年月', '联系方式', '月份', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '月份': {
                       FilterRelation.greater_than_or_equal: (datetime.datetime.now().month,),
                      # 因为是 季度初，不存在跨年的问题
                      FilterRelation.less_than: (datetime.datetime.now().month + 3,),
                   }
              }
              },
             {'sheet_name': '集团在职、休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '出生年月', '联系方式', '月份', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '月份': {
                       FilterRelation.greater_than_or_equal: (datetime.datetime.now().month,),
                      # 因为是 季度初，不存在跨年的问题
                      FilterRelation.less_than: (datetime.datetime.now().month + 3,),
                   }
              }
              },
             {'sheet_name': '信息科技在职、休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '出生年月', '联系方式', '月份', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('信息科技', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '月份': {
                       FilterRelation.greater_than_or_equal: (datetime.datetime.now().month,),
                      # 因为是 季度初，不存在跨年的问题
                      FilterRelation.less_than: (datetime.datetime.now().month + 3,),
                   }
              }
              },
             {'sheet_name': '盛世百捷在职、休假',
              'title_name_list': ['姓名', '部门', '组别', '性别', '级别', '岗位', '出生年月', '联系方式', '月份', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('盛世百捷', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '月份': {
                       FilterRelation.greater_than_or_equal: (datetime.datetime.now().month,),
                      # 因为是 季度初，不存在跨年的问题
                      FilterRelation.less_than: (datetime.datetime.now().month + 3,),
                   }
              }
              },
         ]},
    # ——————————————————————————————————
    # 12、【集团各公司】未转正人员名单
    {'workbook_name': '【集团各公司】未转正人员名单',
         'sheet_list': [
             {'sheet_name': '推广（含远郊）在职且未转正',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百度推广', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '转正日期': {FilterRelation().is_null: (True,)
                   }
              }
              },
             {'sheet_name': '推广（含远郊）离职', 'title_name_list': ['姓名', '身份证号', '联系方式', ],
                  'col_filter': {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                                 '员工状态': {FilterRelation().equal_to: ('离职',)},
                                 }},
             {'sheet_name': '集团在职且未转正',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('百捷集团', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '转正日期': {FilterRelation().is_null: (True,)
                   }
              }
              },
             {'sheet_name': '集团离职',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                             '员工状态': {FilterRelation().equal_to: ('离职',)},
                                 }},
             {'sheet_name': '信息科技在职且未转正',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('信息科技', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '转正日期': {FilterRelation().is_null: (True,)
                   }
              }
              },
             {'sheet_name': '信息科技离职',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                             '员工状态': {FilterRelation().equal_to: ('离职',)},
                                 }},
             {'sheet_name': '盛世百捷在职且未转正',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter':
                  {'公司名称': {FilterRelation().equal_to: ('盛世百捷', )},
                   '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                   '转正日期': {FilterRelation().is_null: (True,)
                   }
              }
              },
             {'sheet_name': '盛世百捷离职',
              'title_name_list': ['姓名', '身份证号', '联系方式', ],
              'col_filter': {'公司名称': {FilterRelation().equal_to: ('盛世百捷',)},
                             '员工状态': {FilterRelation().equal_to: ('离职',)},
                                 }},
         ]},
    # ——————————————————————————————————
    # 13、【信息科技】信息科技员工花名册
    {'workbook_name': '【信息科技】信息科技员工花名册', 'sheet_list': [
        {'sheet_name': '在职',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期',
                             '身份证号', '联系方式', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', )},
                        }},
        {'sheet_name': '休假',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期',
                             '身份证号', '联系方式', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('休假',)}, }},
        {'sheet_name': '离职',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '岗位', '入职日期', '转正日期',
                             '离职日期', '身份证号', '联系方式', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('离职', )},
                        }},
            ]},
    # ——————————————————————————————————
    # 14、【集团】集团花名册+身份证号
    {'workbook_name': '【集团】集团花名册+身份证号', 'sheet_list': [
        {'sheet_name': '在职',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '身份证号', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', )},
                        }},
        {'sheet_name': '休假',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '身份证号', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                        '员工状态': {FilterRelation().equal_to: ('休假',)}, }},
        {'sheet_name': '离职',
         'title_name_list': ['工号', '姓名', '部门', '组别', '性别', '级别', '入职日期', '转正日期', '离职日期', '身份证号', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                        '员工状态': {FilterRelation().equal_to: ('离职', )},
                        }},
            ]},
    # ——————————————————————————————————
    # 15、【信息科技】信息科技每月在职、离职人员名单
    {'workbook_name': r'【信息科技】信息科技每月在职、离职人员名单', 'sheet_list': [
        {'sheet_name': '在职',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', )},
                        }},
        {'sheet_name': '休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('休假',)}, }},
        {'sheet_name': '离职',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', '离职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('离职', )},
                        }},
            ]},
    # ——————————————————————————————————
    # 16、【集团各公司】各公司名单人数汇总表
    {'workbook_name': '【集团各公司】各公司名单人数汇总表', 'sheet_list': [
        {'sheet_name': '总监级以上（四个公司的总监级以上）',
         'title_name_list': ['公司名称', '姓名', '部门', '组别', '性别', '级别', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团', '百度推广', '信息科技', '盛世百捷')},
                        '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                        '级别': {FilterRelation().like: ('总监', '总经理', '总裁', '董事')},
                        }},
        {'sheet_name': '集团在职、休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百捷集团',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                        '级别': {FilterRelation().not_in_like: ('总监', '总经理', '总裁', '董事')},
                        }},
        {'sheet_name': '推广在职、休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                        '级别': {FilterRelation().not_in_like: ('总监', '总经理', '总裁', '董事')},
                        }},
        {'sheet_name': '信息科技在职、休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('信息科技',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                        '级别': {FilterRelation().not_in_like: ('总监', '总经理', '总裁', '董事')},
                        }},
        {'sheet_name': '盛世百捷在职、休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('盛世百捷',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', '休假')},
                        '级别': {FilterRelation().not_in_like: ('总监', '总经理', '总裁', '董事')},
                        }},
    ]},
    # ——————————————————————————————————
    # 17、【推广】百度本地广告事业部极捷号大区人员名单
    {'workbook_name': '【推广】百度本地广告事业部极捷号大区人员名单', 'sheet_list': [
        {'sheet_name': '在职',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                        '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                        '组别': {FilterRelation().like: ('极捷号',)},
                        '员工状态': {FilterRelation().equal_to: ('在职', )},
                        }},
        {'sheet_name': '休假',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                        '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                        '组别': {FilterRelation().like: ('极捷号',)},
                        '员工状态': {FilterRelation().equal_to: ('休假',)}, }},
        {'sheet_name': '离职',
         'title_name_list': ['姓名', '部门', '组别', '级别', '入职日期', '离职日期', ],
         'col_filter': {'公司名称': {FilterRelation().equal_to: ('百度推广',)},
                        '部门': {FilterRelation().equal_to: ('百度本地广告事业部',)},
                        '组别': {FilterRelation().like: ('极捷号',)},
                        '员工状态': {FilterRelation().equal_to: ('离职', )},
                        }},
            ]},

]

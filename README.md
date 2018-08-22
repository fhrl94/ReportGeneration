# 报表自动生成

## 功能

整合多个 excel 表中的数据，将不同的 column 数据存储到 sqlite3 数据库, 通过设置特定的模板刷选出对应的数据填充到 sheet 中,
 将所有 sheet 组合为 excel 报表.主要完成了以下几个功能

1. excel 数据读取 `使用 xlrd 第三方库`

2. 校验 excel 格式校验类 `ExcelColumnStructure `, 生成一个字段检测对象,此对象主要检查 date, int, str_choice ;
以及检查当前数据是否可以为空; 最终结果有哪些是不能重复的. 需要
[初始配置](https://github.com/fhrl94/ReportGeneration/blob/4a88cfd9dbf3a4ba11c7943c1d2aec318cbc7afe/resource_python/data_pull.py#L153).

   | 列名称   | 数据库名称     | 类型       | 选项                     | 是否为空 | 长度   | 重复项检查 |
   | -------- | -------------- | ---------- | ------------------------ | -------- | ------ | ---------- |
   | name     | db_name        | col_type   | tuple_choice             | is_null  | length | repeat     |
   | 姓名     | name           | str        |                          |          |        |            |
   | 工号     | code           | int        |                          |          | 10     | TRUE       |
   | 离职日期 | dimission_date | date       |                          | TRUE     |        |            |
   | 员工状态 | emp_status     | str_choice | ('在职', '休假', '离职') |          |        |            |

3. 通过 格式校验后, 将生成的 excel 表上传, 解析后可获得所有数据.

4. 通过[编写模板](https://github.com/fhrl94/ReportGeneration/blob/4a88cfd9dbf3a4ba11c7943c1d2aec318cbc7afe/resource_python/constants.py#L14), 将在管理站点上生成对应的 `action` , 选择人员后可以按照规则下载 excel 表

##  配置

`report_generation/models.py`  主要配置需要存储的数据列

`resource_python/data_pull.py`  主要配置为 `export_list_column ` , 即导出 excel 表的表头 + 表头对应的格式类型

`resource_python/constants.py`  主要配置 `actions_config ` , 即要下载 excel 的模板
webpackJsonp([1],{NHnr:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=i("7+uW"),n=i("mvHQ"),s=i.n(n),a=i("mtWM"),l=i.n(a),_=i("mw3O"),r=i.n(_),c={name:"Modal",props:{show:Boolean},data:function(){return{}},methods:{close:function(){this.show=!this.show,this.$emit("close")}}},d={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("transition",{staticClass:"modal fade",attrs:{name:"modal-fade"}},[i("div",{directives:[{name:"show",rawName:"v-show",value:t.show,expression:"show"}],staticClass:"modal-backdrop",on:{click:t.close}},[i("div",{staticClass:"modal-dialog modal-content",staticStyle:{width:"61.8%"},attrs:{role:"dialog","aria-labelledby":"modalTile","arial-describedby":"modalDescription"},on:{click:function(t){t.stopPropagation()}}},[i("div",{staticClass:"modal-header",attrs:{id:"modalTitle"}},[i("button",{staticClass:"close",attrs:{type:"button","aria-label":"Close modal"},on:{click:t.close}},[t._v("×")]),t._v(" "),t._t("header",[i("h4",[t._v("这是Modal弹框的标题")])])],2),t._v(" "),i("div",{staticClass:"modal-body",attrs:{id:"modalDescription"}},[t._t("body",[t._v("\n                    这是Modal弹框的主体\n                ")])],2),t._v(" "),i("div",{staticClass:"modal-footer"},[t._t("footer_ok"),t._v(" "),t._t("footer",[i("button",{staticClass:"btn btn-default",attrs:{type:"button","aria-label":"Close modal"},on:{click:t.close}},[t._v("关闭")])])],2)])])])},staticRenderFns:[]};var u=i("VU/8")(c,d,!1,function(t){i("qTUC")},"data-v-22301896",null).exports,v={name:"SheetNameDetail",components:{Modal:u},props:["SheetIns"],data:function(){return{filter_col_info_list:[],page_index:1,page_count_max:10,page_max:10,filter_col_ins:"",isModalVisibleDetail:!1,isModalVisibleAdd:!1,filter_col_info_list_ins:{},filter_column_info:{},filter_column_info_list:[],filter_column_info_str:"",condition_list:[],get_column_condition_list:[],input_type_status:"",get_column_title_list:[]}},methods:{PageClick:function(t){this.page_index=t,this.GetFilterColList()},GetFilterColList:function(){var t=this;l.a.get("/report_generation/filter_col_list_info_id="+this.SheetIns.id+"&page="+this.page_index).then(function(e){t.page_max=e.data.page_max,t.page_count_max=e.data.page_count_max,t.filter_col_info_list=[],e.data.page_info.forEach(function(e){t.filter_col_info_list.push(e)})})},filter_col_add_ok:function(t){0!==this.condition_list.length&&(t.condition_list=this.condition_list,this.condition_list=[]),void 0!==t.filter_col?void 0!==t.filter_relation?void 0!==t.condition_list?(this.filter_column_info_list.push(t),this.filter_column_info={},console.log(this.filter_column_info_list),t.sheet_ins_id=this.SheetIns.id,t.condition_list=s()(t.condition_list),l.a.post("/report_generation/filter_col_info_id=0",r.a.stringify({FilterInfoIns:t})),this.GetFilterColList(),this.closeModal(),this.filter_col_info_list_ins={}):alert("必须选择 条件"):alert("必须选择 关系"):alert("必须选择 列")},filter_col_add:function(){this.condition_list=[],this.showModalAdd()},filter_col_edit:function(t){this.filter_col_info_list_ins=JSON.parse(s()(t)),this.condition_list=JSON.parse(this.filter_col_info_list_ins.condition_list),this.showModalAdd()},filter_col_del:function(t){var e=this;l.a.delete("/report_generation/filter_col_info_id="+t.id).then(function(){e.GetFilterColList()}),this.GetFilterColList()},GetColumnTitleList:function(){var t=this;l.a.get("/report_generation/get_column_title_list").then(function(e){t.get_column_title_list=e.data})},GetColumnConditionList:function(){var t=this;l.a.get("/report_generation/get_column_condition_list_key="+this.filter_col_info_list_ins.filter_col).then(function(e){"fail"!==e.data?t.get_column_condition_list=e.data:t.get_column_condition_list=[]})},showModalDetail:function(){this.isModalVisibleDetail=!0},showModalAdd:function(){this.isModalVisibleAdd=!0,this.GetColumnTitleList()},closeModal:function(){this.isModalVisibleAdd=!1,this.isModalVisibleDetail=!1,this.filter_col_info_list_ins={},this.GetFilterColList()}},watch:{SheetIns:function(){this.GetFilterColList()},filter_col_info_list_ins:{handler:function(){this.GetColumnConditionList()},deep:!0}}},h={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("table",{staticClass:"table table-bordered table-hover table-responsive table-striped"},[i("col",{attrs:{width:"200",span:"4"}}),t._v(" "),i("tbody",[t._m(0),t._v(" "),t._l(t.filter_col_info_list,function(e){return i("tr",{key:e},[i("td",{staticClass:"text-center",staticStyle:{"text-align":"center"}},[t._v(t._s(e.filter_col))]),t._v(" "),i("td",{staticClass:"text-center"},[t._v(t._s(e.filter_relation))]),t._v(" "),i("td",{staticClass:"text-center"},[t._v(t._s(e.condition_list))]),t._v(" "),i("td",{staticClass:"text-center"},[i("button",{staticClass:"btn btn-warning btn-xs el-icon-edit",on:{click:function(i){t.filter_col_edit(e)}}},[t._v("修改")]),t._v(" "),i("button",{staticClass:"btn btn-danger btn-xs el-icon-remove-outline",on:{click:function(i){t.filter_col_del(e)}}},[t._v("删除")])])])}),t._v(" "),i("tr",[i("td",{staticClass:"text-center",attrs:{colspan:"4"}},[i("button",{staticClass:"btn btn-primary",on:{click:function(e){t.filter_col_add()}}},[t._v("新增")])])])],2)]),t._v(" "),i("div",{staticClass:"text-center"},[i("ul",{staticClass:"pagination"},[i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index>1,expression:"page_index >1"}],on:{click:function(e){t.PageClick(t.page_index-1)}}},[i("a",[t._v("上一页")])]),t._v(" "),t._l(t.page_max,function(e){return i("li",{key:e,class:{active:t.page_index===e},on:{click:function(i){t.PageClick(e)}}},[i("a",{attrs:{href:"#"}},[t._v(t._s(e))])])}),t._v(" "),i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index<t.page_max,expression:"page_index<page_max"}],on:{click:function(e){t.PageClick(t.page_index+1)}}},[i("a",[t._v("下一页")])]),t._v(" "),i("li",[i("a",[t._v("共 "+t._s(t.page_max)+" 页, 当前第 "+t._s(t.page_index)+" 页")])])],2)]),t._v(" "),i("Modal",{attrs:{show:t.isModalVisibleAdd},on:{close:t.closeModal}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("h4",[t._v("请填写报表数据")])]),t._v(" "),i("div",{staticClass:"content",staticStyle:{height:"600px","overflow-y":"scroll","overflow-x":"hidden"},attrs:{slot:"body"},slot:"body"},[i("form",{attrs:{action:"#",method:"post"},on:{submit:function(e){e.preventDefault(),t.filter_col_add_ok(t.filter_col_info_list_ins)}}},[i("div",{staticClass:"form-group"},[i("label",{attrs:{for:"filter_col"}},[t._v("列名称")]),t._v(" "),i("el-select",{attrs:{id:"filter_col",required:""},model:{value:t.filter_col_info_list_ins.filter_col,callback:function(e){t.$set(t.filter_col_info_list_ins,"filter_col",e)},expression:"filter_col_info_list_ins['filter_col']"}},t._l(t.get_column_title_list,function(e){return i("el-option",{key:e,attrs:{for:e,value:e},domProps:{textContent:t._s(e)}})})),t._v(" "),i("label",{attrs:{for:"filter_relation"}},[t._v("过滤关系")]),t._v(" "),i("el-select",{attrs:{id:"filter_relation",required:""},model:{value:t.filter_col_info_list_ins.filter_relation,callback:function(e){t.$set(t.filter_col_info_list_ins,"filter_relation",e)},expression:"filter_col_info_list_ins['filter_relation']"}},[i("el-option",{attrs:{value:">="}},[t._v("大于等于")]),t._v(" "),i("el-option",{attrs:{value:">"}},[t._v("大 于")]),t._v(" "),i("el-option",{attrs:{value:"<="}},[t._v("小于等于 ")]),t._v(" "),i("el-option",{attrs:{value:"<"}},[t._v("小 于")]),t._v(" "),i("el-option",{attrs:{value:"is Null"}},[t._v("值是否为空")]),t._v(" "),i("el-option",{attrs:{value:"="}},[t._v("等 于")]),t._v(" "),i("el-option",{attrs:{value:"like"}},[t._v("包 含")]),t._v(" "),i("el-option",{attrs:{value:"not like"}},[t._v("不 包 含")])],1),t._v(" "),[">=",">","<","<="].indexOf(t.filter_col_info_list_ins.filter_relation)>=0?i("label",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.condition_list,expression:"condition_list"}],attrs:{type:"date"},domProps:{value:t.condition_list},on:{input:function(e){e.target.composing||(t.condition_list=e.target.value)}}})]):t._e(),t._v(" "),["is Null"].indexOf(t.filter_col_info_list_ins.filter_relation)>=0?i("el-radio-group",{model:{value:t.condition_list,callback:function(e){t.condition_list=e},expression:"condition_list"}},[i("el-radio",{attrs:{type:"radio",label:"True"}},[t._v("是")]),t._v(" "),i("el-radio",{attrs:{type:"radio",label:"False"}},[t._v("否")])],1):t._e(),t._v(" "),["like","not like"].indexOf(t.filter_col_info_list_ins.filter_relation)>=0?i("el-select",{attrs:{multiple:"",placeholder:"请选择",filterable:"","allow-create":""},model:{value:t.condition_list,callback:function(e){t.condition_list=e},expression:"condition_list"}},t._l(t.get_column_condition_list,function(t){return i("el-option",{key:t,attrs:{label:t,value:t}})})):t._e(),t._v(" "),["="].indexOf(t.filter_col_info_list_ins.filter_relation)>=0?i("el-select",{attrs:{multiple:"",placeholder:"请选择",filterable:""},model:{value:t.condition_list,callback:function(e){t.condition_list=e},expression:"condition_list"}},t._l(t.get_column_condition_list,function(t){return i("el-option",{key:t,attrs:{label:t,value:t}})})):t._e()],1),t._v(" "),i("div",{staticClass:"text-center justify-content-center"},[i("button",{staticClass:"btn btn-primary",attrs:{type:"submit","aria-label":"Close modal"}},[t._v("确认")])])])])])],1)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("tr",[e("th",{staticClass:"text-center"},[this._v("列名称")]),this._v(" "),e("th",{staticClass:"text-center"},[this._v("过滤关系")]),this._v(" "),e("th",{staticClass:"text-center"},[this._v("条件列表")]),this._v(" "),e("th",{staticClass:"text-center"},[this._v("\n                状态\n            ")])])}]};var f={name:"sheets-name",components:{Modal:u,SheetNameDetail:i("VU/8")(v,h,!1,function(t){i("r9pn")},"data-v-6ed52b5c",null).exports},props:["WorkbookIns"],data:function(){return{page_index:1,page_count_max:10,page_max:10,sheet_list_ins:{},isModalVisibleDetail:!1,isModalVisibleAdd:!1,sheet_list:[],get_column_title_list:[],column_title_list:[],filter_column_info:[],sheet_ins:""}},methods:{PageClick:function(t){this.page_index=t,this.GetSheetList()},GetSheetList:function(){var t=this;l.a.get("/report_generation/sheet_list_info_id="+this.WorkbookIns.id+"&page="+this.page_index).then(function(e){t.page_max=e.data.page_max,t.page_count_max=e.data.page_count_max,t.sheet_list=[],e.data.page_info.forEach(function(e){t.sheet_list.push(e)})})},GetColumnTitleList:function(){var t=this;l.a.get("/report_generation/get_column_title_list").then(function(e){t.get_column_title_list=e.data})},sheet_add:function(){this.column_title_list=[],this.showModalAdd()},sheet_edit:function(t){this.sheet_list_ins=JSON.parse(s()(t)),this.column_title_list=this.sheet_list_ins.column_name_list.split(","),this.showModalAdd()},sheet_add_ok:function(t){t.workbook_ins_id=this.WorkbookIns.id,0!==t.column_name_list.length?(t.column_name_list=t.column_name_list.join(","),l.a.post("/report_generation/sheet_info_id=0",r.a.stringify({SheetIns:t})),this.GetSheetList(),this.closeModal()):alert("列名称 必须选中一个及以上")},sheet_detail:function(t){this.sheet_ins=t,this.showModalDetail()},sheet_del:function(t){var e=this;l.a.delete("/report_generation/sheet_info_id="+t.id).then(function(){e.GetSheetList()}),this.GetSheetList()},showModalDetail:function(){this.isModalVisibleDetail=!0},showModalAdd:function(){this.isModalVisibleAdd=!0,this.GetColumnTitleList()},closeModal:function(){this.isModalVisibleAdd=!1,this.isModalVisibleDetail=!1,this.sheet_list_ins={},this.GetSheetList()}},watch:{WorkbookIns:function(){this.GetSheetList()},column_title_list:function(){this.sheet_list_ins.column_name_list=this.column_title_list}}},p={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("table",{staticClass:"table table-bordered table-hover table-responsive table-striped"},[i("col",{attrs:{width:"200",span:"3"}}),t._v(" "),i("tbody",[t._m(0),t._v(" "),t._l(t.sheet_list,function(e){return i("tr",{key:e},[i("td",{staticClass:"text-center",staticStyle:{"text-align":"center"}},[t._v(t._s(e.sheet_name))]),t._v(" "),i("td",{staticClass:"text-center"},[t._v(t._s(e.column_name_list))]),t._v(" "),i("td",{staticClass:"text-center"},[i("button",{staticClass:"btn btn-warning el-icon-edit btn-xs",on:{click:function(i){t.sheet_edit(e)}}},[t._v("修改")]),t._v(" "),i("button",{staticClass:"btn btn-danger el-icon-remove-outline btn-xs",on:{click:function(i){t.sheet_del(e)}}},[t._v("删除")]),t._v(" "),i("button",{staticClass:"btn btn-primary el-icon-zoom-in btn-xs",on:{click:function(i){t.sheet_detail(e)}}},[t._v("筛选条件查看")])])])}),t._v(" "),i("tr",[i("td",{staticClass:"text-center",attrs:{colspan:"4"}},[i("button",{staticClass:"btn btn-primary el-icon-circle-plus-outline",on:{click:function(e){t.sheet_add()}}},[t._v("新增")])])])],2)]),t._v(" "),i("div",{staticClass:"text-center"},[i("ul",{staticClass:"pagination"},[i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index>1,expression:"page_index >1"}],on:{click:function(e){t.PageClick(t.page_index-1)}}},[i("a",[t._v("上一页")])]),t._v(" "),t._l(t.page_max,function(e){return i("li",{key:e,class:{active:t.page_index===e},on:{click:function(i){t.PageClick(e)}}},[i("a",{attrs:{href:"#"}},[t._v(t._s(e))])])}),t._v(" "),i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index<t.page_max,expression:"page_index<page_max"}],on:{click:function(e){t.PageClick(t.page_index+1)}}},[i("a",[t._v("下一页")])]),t._v(" "),i("li",[i("a",[t._v("共 "+t._s(t.page_max)+" 页, 当前第 "+t._s(t.page_index)+" 页")])])],2)]),t._v(" "),i("Modal",{attrs:{show:t.isModalVisibleDetail},on:{close:t.closeModal}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("h4",[t._v(t._s(t.sheet_ins.sheet_name))])]),t._v(" "),i("div",{staticClass:"content",attrs:{slot:"body"},slot:"body"},[i("sheet-name-detail",{attrs:{SheetIns:t.sheet_ins}})],1)]),t._v(" "),i("Modal",{attrs:{show:t.isModalVisibleAdd},on:{close:t.closeModal}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("h4",[t._v("请填写报表数据")])]),t._v(" "),i("div",{staticClass:"content",attrs:{slot:"body"},slot:"body"},[i("form",{attrs:{action:"#",method:"post"},on:{submit:function(e){e.preventDefault(),t.sheet_add_ok(t.sheet_list_ins)}}},[i("div",{staticClass:"form-group"},[i("label",{attrs:{for:"sheet_name"}},[t._v("sheet名称")]),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.sheet_list_ins.sheet_name,expression:"sheet_list_ins['sheet_name']"}],staticClass:"form-control",attrs:{id:"sheet_name",type:"text",placeholder:"请输入",required:""},domProps:{value:t.sheet_list_ins.sheet_name},on:{input:function(e){e.target.composing||t.$set(t.sheet_list_ins,"sheet_name",e.target.value)}}}),t._v(" "),i("label",{attrs:{for:"column_name_list"}},[t._v("列名称")]),t._v(" "),i("div",[i("textarea",{directives:[{name:"model",rawName:"v-model",value:t.sheet_list_ins.column_name_list,expression:"sheet_list_ins['column_name_list']"}],staticClass:"form-control",attrs:{id:"column_name_list",type:"text",placeholder:"请在下面的选择项进行勾选",disabled:"",rows:"3"},domProps:{value:t.sheet_list_ins.column_name_list},on:{input:function(e){e.target.composing||t.$set(t.sheet_list_ins,"column_name_list",e.target.value)}}}),t._v(" "),t._l(t.get_column_title_list,function(e){return i("label",{key:e,staticClass:"checkbox-inline",attrs:{for:e}},[i("input",{directives:[{name:"model",rawName:"v-model",value:t.column_title_list,expression:"column_title_list"}],staticClass:"checkbox-inline",attrs:{type:"checkbox",id:e},domProps:{value:e,checked:Array.isArray(t.column_title_list)?t._i(t.column_title_list,e)>-1:t.column_title_list},on:{change:function(i){var o=t.column_title_list,n=i.target,s=!!n.checked;if(Array.isArray(o)){var a=e,l=t._i(o,a);n.checked?l<0&&(t.column_title_list=o.concat([a])):l>-1&&(t.column_title_list=o.slice(0,l).concat(o.slice(l+1)))}else t.column_title_list=s}}}),t._v("\n                            "+t._s(e)+"\n                        ")])})],2),t._v(" "),i("div",{staticClass:"text-center justify-content-center"},[i("button",{staticClass:"btn btn-primary",attrs:{type:"submit","aria-label":"Close modal"}},[t._v("确认")])])])])])])],1)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("tr",[e("th",{staticClass:"text-center"},[this._v("sheet名称")]),this._v(" "),e("th",{staticClass:"text-center"},[this._v("列名称")]),this._v(" "),e("th",{staticClass:"text-center"},[this._v("\n                状态\n            ")])])}]};var m={name:"work-book",components:{Modal:u,SheetsName:i("VU/8")(f,p,!1,function(t){i("NpcT")},"data-v-5694b4f4",null).exports},data:function(){return{page_index:1,page_count_max:10,page_max:10,isModalVisibleDetail:!1,isModalVisibleAdd:!1,modal_workbook_ins:"",report_generation:{},report_generation_list:[],DjangoCookie:""}},methods:{PageClick:function(t){this.page_index=t,this.GetWorkbookList()},report_generation_add:function(){this.showModalAdd()},report_generation_edit:function(t){this.report_generation=JSON.parse(s()(t)),this.showModalAdd()},report_generation_add_ok:function(t){l.a.post("/report_generation/workbook_info_id=0",r.a.stringify({ReportGenerationIns:t})),this.GetWorkbookList(),this.closeModal()},workbook_detail:function(t){this.modal_workbook_ins=t,this.showModalDetail()},report_generation_del:function(t){var e=this;l.a.delete("/report_generation/workbook_info_id="+t.id,{headers:{"X-CSRFToken":this.DjangoCookie}}).then(function(t){e.GetWorkbookList()}),this.GetWorkbookList()},download_custom:function(t){window.open("/report_generation/download_custom_id="+t.id)},showModalDetail:function(){this.isModalVisibleDetail=!0},showModalAdd:function(){this.isModalVisibleAdd=!0},closeModal:function(){this.isModalVisibleDetail=!1,this.isModalVisibleAdd=!1,this.report_generation={},this.GetWorkbookList()},GetWorkbookList:function(){var t=this;l.a.get("/report_generation/workbook_list_info_page="+this.page_index).then(function(e){t.page_max=e.data.page_max,t.page_count_max=e.data.page_count_max,t.report_generation_list=[],e.data.page_info.forEach(function(e){t.report_generation_list.push(e)})})}},created:function(){this.GetWorkbookList()}},b={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("table",{staticClass:"table table-bordered table-hover table-responsive table-striped"},[t._m(0),t._v(" "),i("tbody",[t._m(1),t._v(" "),t._l(t.report_generation_list,function(e){return i("tr",{key:e},[i("td",[t._v(t._s(e.workbook_name))]),t._v(" "),i("td",[t._v(t._s(e.receiver))]),t._v(" "),i("td",[t._v(t._s(e.cc))]),t._v(" "),i("td",[t._v(t._s(e.send_time))]),t._v(" "),i("td",[i("button",{staticClass:"btn btn-warning el-icon-edit btn-xs",on:{click:function(i){t.report_generation_edit(e)}}},[t._v("修改")]),t._v(" "),i("button",{staticClass:"btn btn-danger el-icon-remove-outline btn-xs",on:{click:function(i){t.report_generation_del(e)}}},[t._v("删除")]),t._v(" "),i("button",{staticClass:"btn btn-primary el-icon-zoom-in btn-xs",on:{click:function(i){t.workbook_detail(e)}}},[t._v("详细")]),t._v(" "),i("button",{staticClass:"btn btn-success el-icon-download btn-xs",on:{click:function(i){t.download_custom(e)}}},[t._v("预览")])])])}),t._v(" "),i("tr",[i("td",{staticClass:"text-center",attrs:{colspan:"6"}},[i("button",{staticClass:"btn btn-primary el-icon-circle-plus-outline",on:{click:function(e){t.report_generation_add()}}},[t._v("新增")]),t._v(" "),i("a",{staticClass:"btn btn-success el-icon-back",attrs:{href:"/xadmin/"}},[t._v("管理网站")])])])],2)]),t._v(" "),i("div",{staticClass:"text-center"},[i("ul",{staticClass:"pagination"},[i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index>1,expression:"page_index >1"}],on:{click:function(e){t.PageClick(t.page_index-1)}}},[i("a",[t._v("上一页")])]),t._v(" "),t._l(t.page_max,function(e){return i("li",{key:e,class:{active:t.page_index===e},on:{click:function(i){t.PageClick(e)}}},[i("a",{attrs:{href:"#"}},[t._v(t._s(e))])])}),t._v(" "),i("li",{directives:[{name:"show",rawName:"v-show",value:t.page_index<t.page_max,expression:"page_index<page_max"}],on:{click:function(e){t.PageClick(t.page_index+1)}}},[i("a",[t._v("下一页")])]),t._v(" "),i("li",[i("a",[t._v("共 "+t._s(t.page_max)+" 页, 当前第 "+t._s(t.page_index)+" 页")])])],2)]),t._v(" "),i("Modal",{attrs:{show:t.isModalVisibleDetail},on:{close:t.closeModal}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("h4",[t._v(t._s(t.modal_workbook_ins.workbook_name))])]),t._v(" "),i("div",{staticClass:"content",attrs:{slot:"body"},slot:"body"},[i("sheets-name",{attrs:{WorkbookIns:t.modal_workbook_ins}})],1)]),t._v(" "),i("Modal",{attrs:{show:t.isModalVisibleAdd},on:{close:t.closeModal}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("h4",[t._v("请填写报表数据")])]),t._v(" "),i("div",{staticClass:"content",attrs:{slot:"body"},slot:"body"},[i("form",{attrs:{action:"#",method:"post"},on:{submit:function(e){e.preventDefault(),t.report_generation_add_ok(t.report_generation)}}},[i("div",{staticClass:"form-group"},[i("label",{attrs:{for:"workbook_name"}},[t._v("自动生成表单名称")]),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.report_generation.workbook_name,expression:"report_generation['workbook_name']"}],staticClass:"form-control",attrs:{id:"workbook_name",type:"text",placeholder:"请输入",required:""},domProps:{value:t.report_generation.workbook_name},on:{input:function(e){e.target.composing||t.$set(t.report_generation,"workbook_name",e.target.value)}}}),t._v(" "),i("label",{attrs:{for:"receiver"}},[t._v("收件人")]),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.report_generation.receiver,expression:"report_generation['receiver']"}],staticClass:"form-control",attrs:{id:"receiver",type:"email",placeholder:"请输入",required:""},domProps:{value:t.report_generation.receiver},on:{input:function(e){e.target.composing||t.$set(t.report_generation,"receiver",e.target.value)}}}),t._v(" "),i("label",{attrs:{for:"cc"}},[t._v("抄送人")]),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.report_generation.cc,expression:"report_generation['cc']"}],staticClass:"form-control",attrs:{id:"cc",type:"text",placeholder:"请输入",required:""},domProps:{value:t.report_generation.cc},on:{input:function(e){e.target.composing||t.$set(t.report_generation,"cc",e.target.value)}}}),t._v(" "),i("label",{attrs:{for:"send_time"}},[t._v("发送时间")]),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.report_generation.send_time,expression:"report_generation['send_time']"}],staticClass:"form-control",attrs:{id:"send_time",type:"date",placeholder:"请输入",required:""},domProps:{value:t.report_generation.send_time},on:{input:function(e){e.target.composing||t.$set(t.report_generation,"send_time",e.target.value)}}}),t._v(" "),i("div",{staticClass:"text-center justify-content-center"},[i("button",{staticClass:"btn btn-primary el-icon-success",attrs:{type:"submit","aria-label":"Close modal"}},[t._v("确认")])])])])])])],1)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("caption",{staticClass:"text-center"},[e("h2",[this._v("报表展示")])])},function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("tr",[i("th",[t._v("自动生成表单名称")]),t._v(" "),i("th",[t._v("收件人")]),t._v(" "),i("th",[t._v("抄送人")]),t._v(" "),i("th",[t._v("发送时间")]),t._v(" "),i("th",[t._v("\n                  状态\n                ")])])}]};var g={name:"App",components:{WorkBook:i("VU/8")(m,b,!1,function(t){i("XwEA")},"data-v-f855ecc2",null).exports}},k={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("work-book")],1)},staticRenderFns:[]};var x=i("VU/8")(g,k,!1,function(t){i("nOG/")},null,null).exports,C=i("/ocq");o.default.use(C.a);var w=new C.a({routes:[{path:"/"}]}),y=i("H93t"),M=i.n(y);i("TsY+");o.default.use(M.a),o.default.config.productionTip=!1,new o.default({el:"#app",router:w,components:{App:x},template:"<App/>",render:function(t){return t(x)}})},NpcT:function(t,e){},"TsY+":function(t,e){},XwEA:function(t,e){},"nOG/":function(t,e){},qTUC:function(t,e){},r9pn:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.3c17d147b5c87bb059ff.js.map
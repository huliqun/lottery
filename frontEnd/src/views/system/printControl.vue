<template>
  <section class="content-header">
    <h1>
      打印
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 基本管理</a></li>
      <li class="active">打印</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-8">
      <div class="box box-info">
        <div class="box-header with-border ui-sortable-handle">
          <!-- tools box -->
          <div class="pull-right box-tools">
            <button type="button" class="btn btn-box-tool" data-widget="collapse" data-toggle="tooltip" title="Collapse" style="margin-right: 5px;">
              <i class="fa fa-minus"></i>
            </button>
          </div>
          <!-- /. tools -->
          <i class="fa fa-bar-chart-o"></i>
          <h3 class="box-title">
            查询
          </h3>
        </div>
        <div class="box-body">
          <table id="table" data-show-export="true">
        </table>
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="box box-success">
      <div class="box-header with-border ui-sortable-handle">
        <!-- tools box -->
        <div class="pull-right box-tools">
          <button type="button" class="btn btn-box-tool" data-widget="collapse" data-toggle="tooltip" title="Collapse" style="margin-right: 5px;">
            <i class="fa fa-minus"></i>
          </button>
        </div>
        <!-- /. tools -->
        <i class="fa fa-desktop"></i>
        <h3 class="box-title">
          工作台
        </h3>
      </div>
      <div class="box-body">
        <div id="scroll-desk">
          <div id="deskForm">
            <div class="hidden">{{ userID }}</div>
            <div class="form-group">
              <label>代码</label>
              <input class="form-control" v-model="code" name="code">
            </div>
            <div class="form-group">
              <label>简称</label>
              <input class="form-control" v-model="name" name="name">
            </div>
            <div class="form-group">
              <label>全称</label>
              <input class="form-control" v-model="fullName" name="fullName">
            </div>
            <div class="form-group">
              <label>联系电话</label>
              <input class="form-control" v-model="telePhone" name="telePhone">
            </div>
            <div class="form-group">
              <label>用户名</label>
              <input class="form-control" v-model="userName" name="userName">
            </div>
          </div>
        </div>
      </div>
      <div class="box-footer no-border">
        <button type="button" class="btn btn-primary" v-on:click="printPreview"><i class="fa fa-fw fa-plus"></i>打印预览</button>
        <button type="button" class="btn btn-info" v-on:click="print"><i class="fa fa-fw fa-edit"></i>打印</button>
        <button type="button" class="btn btn-warning" v-on:click="printDesign"><i class="fa fa-fw fa-remove"></i>打印设计</button>
      </div>
    </div>
  </div>
  </section>
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
var common = require('commonFunc')
var lodopPrint = require('lodopPrintFunc')
var billPrint = require('billPrintFunc')
var LODOP
let currentRow
let currentRowIndex

function desk2Json (obj) {
  return {
    'userID': obj.userID,
    'code': obj.code,
    'name': obj.name,
    'fullName': obj.fullName,
    'telePhone': obj.telePhone,
    'userName': obj.userName,
    'modifyTime': obj.modifyTime
  }
}
function deskClean (obj) {
  $('#deskForm').bootstrapValidator('resetForm', true)
  obj.userID = ''
  obj.code = ''
  obj.name = ''
  obj.fullName = ''
  obj.telePhone = ''
  obj.userName = ''
  obj.modifyTime = ''
}
export default {
  data: function () {
    return {
      pagePara: '',
      userID: '',
      code: '',
      name: '',
      fullName: '',
      telePhone: '',
      userName: '',
      modifyTime: ''
    }
  },
  name: 'carrierControl',
  store: vuexStore,
  vuex: {
    actions: {
      setError: setError
    }
  },
  route: {
    canReuse: false
  },
  created: function () {
    var _self = this
    function initPage () {
      _self.$http.post('/api/basic/carriercontrol?method=init', {}).then((response) => {
        _self.pagePara = response.json()['data']
        // _self.gender = undefined
        // _self.IDType = undefined
        console.log('init success')
      }, (response) => {
        console.log('init error')
        common.dealErrorCommon(_self, response)
      })
    }
    initPage()
  },
  ready: function () {
    var _self = this
    function formatdesk (row) {
      _self.userID = row['userID']
      _self.code = row['code']
      _self.name = row['name']
      _self.fullName = row['fullName']
      _self.telePhone = row['telePhone']
      _self.userName = row['userName']
      _self.modifyTime = row['modifyTime']
    }
    function getData () {
      _self.$http.post('/api/basic/carriercontrol?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $('#table').bootstrapTable('load', {
          data: retdata
        })
        return retdata
      }, (response) => {
        // error callback
        console.log('get data error')
        console.log(response.status)
        console.log(response.data)
      })
    }
    function initTable () {
      $('#table').bootstrapTable({
        height: common.getTableHeight(),
        columns: [{
          field: 'userID',
          align: 'center',
          visible: false
        }, {
          field: 'code',
          align: 'center',
          title: '代码',
          sortable: true
        }, {
          field: 'name',
          align: 'center',
          title: '简称'
        }, {
          field: 'fullName',
          align: 'center',
          title: '全称'
        }, {
          field: 'telePhone',
          align: 'center',
          title: '联系电话'
        }, {
          field: 'userName',
          align: 'center',
          title: '用户名'
        }, {
          field: 'modifyTime',
          align: 'center',
          visible: false
        }],
        idField: 'userID',
        search: true,
        showRefresh: true,
        showToggle: true,
        showColumns: true,
        showPaginationSwitch: true,
        pagination: true,
        striped: true,
        showFooter: false,
        pageList: [10, 25, 50, 100, 'ALL'],
        locale: 'zh-CN',
        onClickRow: function (row, $element) {
          $('#deskForm').data('bootstrapValidator').updateStatus('userName', 'NOT_VALIDATED')
          $('#deskForm').data('bootstrapValidator').updateStatus('code', 'NOT_VALIDATED')
          currentRow = row
          currentRowIndex = $element[0].rowIndex - 1
          formatdesk(row)
        },
        onRefresh: function () {
          getData()
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)
    }
    function initValidators () {
      $('#deskForm').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
          valid: 'glyphicon glyphicon-ok',
          invalid: 'glyphicon glyphicon-remove',
          validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
          code: {
            validators: {
              notEmpty: {
                message: '代码不能为空'
              }
            }
          },
          userName: {
            validators: {
              notEmpty: {
                message: '用户名不能为空'
              }
            }
          }
        }
      })
    }

    $(function () {
      common.initControlSize()
      initTable()
      getData()
      initValidators()
    })
  },
  methods: {
    printPreview: function (event) {
      LODOP = lodopPrint.getLodop()
      for (var i = 0; i < 10; i++) {
        billPrint.containerPrint(LODOP, i)
        LODOP.NewPage()
      }
      LODOP.PREVIEW()
      console.log('打印预览')
    },
    print: function (event) {
      console.log('打印')
    },
    printDesign: function (event) {
      console.log('打印设计')
    }
  }
}
</script>
<style>
</style>

<template>
  <section class="content-header">
    <h1>
      承运人参数维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 系统管理</a></li>
      <li class="active">承运人参数维护</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar" class="pull-right">
            <div class="form-inline" role="form">
              <div class="form-group">
                <div class="form-group">
                  <button id="modifyM" class="btn btn-primary" v-on:click="modifyM" disabled>
                    <i class="glyphicon glyphicon-pencil"></i> 修改
                  </button>
                </div>
              </div>
            </div>
          </div>
          <table id="table"></table>
        </div>
      </div>
    </div>
  </section>
  <div class="modal fade" id="modifyModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
      <div class="modal-dialog" role="document" style="width: 500px;">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>船代参数维护</h4>
          </div>
          <div class="modal-body" id="formM">
            <div class="form-group">
              <label>承运人</label>
              <input class="form-control" v-model="currentRow.caName" disabled>
            </div>
            <div class="form-group">
              <label>操作员</label>
              <select class="form-contro select2" multiple style="width:100%" name="operatorID" id="operatorID">
              </select>
            </div>
            <div class="form-group">
              <label>放箱员</label>
              <select class="form-contro select2" multiple style="width:100%" name="putterID" id="putterID">
              </select>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" v-on:click="modify"><i class="fa fa-fw fa-plus"></i>修改</button>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
var common = require('commonFunc')
function desk2Json (obj) {
  return {
    'uid': obj.currentRow.uid,
    'carrierID': obj.currentRow.carrierID,
    'operatorID': $('#operatorID').val()[0],
    'putterID': $('#putterID').val()[0]
  }
}
function deskClean (obj) {
  $('#deskForm').bootstrapValidator('resetForm', true)
  obj.carrierName = ''
  $('#operatorID').val(null).trigger('change')
  $('#putterID').val(null).trigger('change')
  var columns = ['operatorID', 'putterID']
  common.changeValidatorStatus($('#deskForm'), columns, 'NOT_VALIDATED')
}
export default {
  data: function () {
    return {
      pagePara: '',
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'carrierParaControl',
  mixins: [common.baseMixin],
  store: vuexStore,
  vuex: {
    actions: {
      setError: setError
    }
  },
  route: {
    canReuse: false
  },
  ready: function () {
    var _self = this
    var $table = $('#table')
    function formatdesk (row) {
      _self.carrierName = row.carrierInfo.name
      if (row.operatorID) {
        $('#operatorID').val([row.operatorID]).trigger('change')
      }
      if (row.putterID) {
        $('#putterID').val([row.putterID]).trigger('change')
      }
      var columns = ['operatorID', 'putterID']
      common.changeValidatorStatus($('#deskForm'), columns, 'NOT_VALIDATED')
    }
    function getData () {
      _self.$http.post('/api/putbox/carrierParaControl?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $table.bootstrapTable('load', {
          data: retdata
        })
      }, (response) => {
        // error callback
        console.log('get data error')
        common.dealErrorCommon(_self, response)
      })
    }
    function operatorIDFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['operatorInfo'].length; i++) {
        if (_self.pagePara['operatorInfo'][i].id === value) {
          return _self.pagePara['operatorInfo'][i].text
        }
      }
      return ''
    }
    function putterIDFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['putterInfo'].length; i++) {
        if (_self.pagePara['putterInfo'][i].id === value) {
          return _self.pagePara['putterInfo'][i].text
        }
      }
      return ''
    }
    function initTable () {
      $table.bootstrapTable({
        height: common.getTableHeight(),
        columns: [
          {
            field: 'uid',
            visible: false
          },
          {
            align: 'center',
            valign: 'middle',
            field: 'state',
            radio: true
          },
          common.BTRowFormat('caName', '船代名'),
          common.BTRowFormatWithFormatter('operatorID', '操作员', operatorIDFormatter),
          common.BTRowFormatWithFormatter('putterID', '放箱员', putterIDFormatter)
        ],
        idField: 'uid',
        uniqueId: 'uid',
        toolbar: '#toolbar',
        clickToSelect: true,
        striped: true,
        search: true,
        showRefresh: true,
        locale: 'zh-CN',
        onCheck: function (row) {
          $('#modifyM').prop('disabled', false)
          _self.currentRow = $.extend(true, {}, row)
          _self.oldRow = $.extend(true, {}, row)
          $('#operatorID').val([row.operatorID]).trigger('change')
          $('#putterID').val([row.putterID]).trigger('change')
        },
        onRefresh: function () {
          getData()
        }
      })
      setTimeout(function () {
        $table.bootstrapTable('resetView')
      }, 200)
      common.changeTableClass($table)
    }
    function initValidators () {
      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          operatorID: common.BVNotEmput('操作员不能为空'),
          putterID: common.BVNotEmput('放箱员不能为空')
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/carrierParaControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2($('#operatorID'), retData['operatorInfo'])
        common.initSelect2($('#putterID'), retData['putterInfo'])
        console.log('init success')
      }, (response) => {
        console.log('init error')
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      initPage()
      common.initControlSize()
      initTable()
      getData()
      initValidators()
    })
  },
  methods: {
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#operatorID').val(this.oldRow.operatorID).trigger('change')
      $('#putterID').val(this.oldRow.putterID).trigger('change')
      $('#modifyModal').modal('show')
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult($('#formM'))) {
        _self.currentRow.operatorID = $('#operatorID').val()[0]
        _self.currentRow.putterID = $('#putterID').val()[0]
        console.log(_self.currentRow)
        _self.$http.post('/api/putbox/carrierParaControl?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('updateByUniqueId', { id: retData.uid, row: retData })
          console.log('modify success')
          common.dealSuccessCommon('修改成功')
          $('#modifyModal').modal('hide')
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(this, response)
        })
      }
    }
  }
}
</script>
<style>
</style>

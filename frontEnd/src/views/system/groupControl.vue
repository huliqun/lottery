<template>
  <section class="content-header">
    <h1>
      用户组维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 系统管理</a></li>
      <li class="active">用户组维护</li>
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
                  <button id="addM" class="btn btn-info" v-on:click="addM">
                    <i class="glyphicon glyphicon-plus"></i> 增加
                  </button>
                </div>
              </div>
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
  <div class="modal fade" id="AddModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document" style="width: 300px;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>增加操作员</h4>
        </div>
        <div class="modal-body"  id="formA">
          <div class="form-group" id="userGroupName">
            <label>用户组名称</label>
            <input class="form-control" v-model="userGroupNameA" name="userGroupNameA">
          </div>
          <div class="form-group">
            <label>用户组状态</label>
            <select class="form-contro select2" multiple style="width:100%" id='userGroupStatusA'>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" v-on:click="add"><i class="fa fa-fw fa-plus"></i>增加</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="modifyModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
      <div class="modal-dialog" role="document" style="width: 300px;">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>修改操作员</h4>
          </div>
          <div class="modal-body" id="formM">
            <div class="form-group">
              <label>用户组名称</label>
              <input class="form-control" v-model="currentRow.userGroupName" name="userGroupNameM">
            </div>
            <div class="form-group">
              <label>用户组状态</label>
              <select class="form-contro select2" multiple style="width:100%" id='userGroupStatusM'>
              </select>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-info" v-on:click="modify"><i class="fa fa-fw fa-edit"></i>修改</button>
            <button type="button" class="btn btn-warning" v-on:click="delete"><i class="fa fa-fw fa-remove"></i>删除</button>
          </div>
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

export default {
  data: function () {
    return {
      pagePara: '',
      userGroupNameA: '',
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'groupControl',
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
      _self.userGroupID = row['userGroupID']
      _self.userGroupName = row['userGroupName']
      $('#userGroupStatus').val([row['userGroupStatus']]).trigger('change')
    }
    function getData () {
      _self.$http.post('/api/system/groupcontrol?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $table.bootstrapTable('load', {
          data: retdata
        })
      }, (response) => {
        // error callback
        common.dealErrorCommon(this, response)
      })
    }
    function userGroupStatusFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['statusInfo'].length; i++) {
        if (_self.pagePara['statusInfo'][i].id === value) {
          return _self.pagePara['statusInfo'][i].text
        }
      }
      return ''
    }
    function initTable () {
      $table.bootstrapTable({
        height: common.getTableHeight(),
        columns: [
          {
            field: 'userGroupID',
            visible: false
          },
          {
            align: 'center',
            valign: 'middle',
            field: 'state',
            radio: true
          },
          common.BTRowFormat('userGroupName', '用户组名称'),
          common.BTRowFormatWithFormatter('userGroupStatus', '用户组状态', userGroupStatusFormatter)
        ],
        idField: 'userGroupID',
        uniqueId: 'userGroupID',
        toolbar: '#toolbar',
        clickToSelect: true,
        locale: 'zh-CN',
        onCheck: function (row) {
          $('#modifyM').prop('disabled', false)
          _self.currentRow = $.extend(true, {}, row)
          _self.oldRow = $.extend(true, {}, row)
          $('#userGroupStatusM').val(row.userGroupStatus).trigger('change')
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
      $('#formA').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userGroupNameA: common.BVNotEmput('用户组名称不能为空'),
          userGroupStatusA: common.BVNotEmput('用户组状态不能为空')
        }
      })

      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userGroupNameM: common.BVNotEmput('用户组名称不能为空'),
          userGroupStatusM: common.BVNotEmput('用户组状态不能为空')
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/system/groupcontrol?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2($('#userGroupStatusA'), retData['statusInfo'])
        common.initSelect2($('#userGroupStatusM'), retData['statusInfo'])
        console.log('init success')
      }, (response) => {
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      initPage()
      initValidators()
      common.initControlSize()
      initTable()
      getData()
    })
  },
  methods: {
    addM: function (event) {
      this.userGroupNameA = ''
      $('#userGroupStatusA').val(null).trigger('change')
      $('#AddModal').modal('show')
    },
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#userGroupStatusA').val([this.oldRow.userGroupStatus]).trigger('change')
      $('#modifyModal').modal('show')
    },
    add: function (event) {
      var _self = this
      if (common.getValidateResult($('#formA'))) {
        var workRow = {
          'userGroupID': '',
          'userGroupName': _self.userGroupNameA,
          'userGroupStatus': $('#userGroupStatusA').val()[0]
        }
        _self.$http.post('/api/system/groupcontrol?method=add', workRow).then((response) => {
          console.log('add success')
          workRow['userGroupId'] = response.json()['data']['userGroupId']
          $('#table').bootstrapTable('insertRow', { index: 0, row: workRow })
          _self.userGroupNameA = ''
          $('#userGroupStatusA').val(null).trigger('change')
          $('#formA').data('bootstrapValidator').resetForm()
          common.dealSuccessCommon('增加成功')
          console.log('add success')
        }, (response) => {
          common.dealErrorCommon(_self, response)
        })
      }
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult($('#formM'))) {
        _self.currentRow.userGroupStatus = $('#userGroupStatusM').val()[0]
        _self.$http.post('/api/system/groupcontrol?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          $('#table').bootstrapTable('updateByUniqueId', { id: _self.currentRow.userGroupID, row: _self.currentRow })
          common.dealSuccessCommon('修改成功')
          $('#modifyModal').modal('hide')
        }, (response) => {
          common.dealErrorCommon(_self, response)
        })
      }
    },
    delete: function (event) {
      var _self = this
      common.dealConfrimCommon('用户删除', function () {
        _self.$http.post('/api/system/groupcontrol?method=delete', _self.currentRow).then((response) => {
          $('#table').bootstrapTable('remove', { field: 'userGroupID', values: [_self.currentRow.userGroupID] })
          common.dealSuccessCommon('删除成功')
          $('#modifyModal').modal('hide')
          console.log('delete success')
        }, (response) => {
          common.dealErrorCommon(_self, response)
        })
      })
    }
  }
}
</script>
<style>
</style>

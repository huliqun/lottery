<template>
  <section class="content-header">
    <h1>
      操作员维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 系统管理</a></li>
      <li class="active">操作员维护</li>
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
          <div class="form-group">
            <label>用户名</label>
            <input class="form-control" v-model="userNameA" name="userNameA">
          </div>
          <div class="form-group">
            <label>姓名</label>
            <input class="form-control" v-model="nameA" name="nameA" v-on:change="makeHelpMarkA">
          </div>
          <div class="form-group">
            <label>客户代码</label>
            <input class="form-control" v-model="helpMarkA" name="helpMarkA">
          </div>
          <div class="form-group">
            <label>手机</label>
            <input type="tel" class="form-control" v-model="mobileA" name="mobileA">
          </div>
          <div class="form-group">
            <label>邮箱</label>
            <input type="text" class="form-control" v-model="emailA" name="emailA">
          </div>
          <div class="form-group">
            <label>用户组</label>
            <select class="form-contro select2" multiple style="width:100%" name="userGroupA" id="userGroupA">
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
              <label>用户名</label>
              <input class="form-control" v-model="currentRow.userName" name="userNameM" disabled>
            </div>
            <div class="form-group">
              <label>姓名</label>
              <input class="form-control" v-model="currentRow.name" name="nameA" v-on:change="makeHelpMarkM">
            </div>
            <div class="form-group">
              <label>客户代码</label>
              <input class="form-control" v-model="currentRow.helpMark" name="helpMarkM">
            </div>
            <div class="form-group">
              <label>手机</label>
              <input type="tel" class="form-control" v-model="currentRow.mobile" name="mobileM">
            </div>
            <div class="form-group">
              <label>邮箱</label>
              <input type="text" class="form-control" v-model="currentRow.email" name="emailM">
            </div>
            <div class="form-group">
              <label>用户组</label>
              <select class="form-contro select2" multiple style="width:100%" name="userGroupM" id="userGroupM">
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
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
var common = require('commonFunc')
var pinyin = require('pinyin')
export default {
  data: function () {
    return {
      pagePara: '',
      userNameA: '',
      nameA: '',
      helpMarkA: '',
      mobileA: '',
      emailA: '',
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'operatorControl',
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
    function getData () {
      _self.$http.post('/api/system/operatorcontrol?method=search', {}).then((response) => {
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
    function userGroupFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['groupInfo'].length; i++) {
        if (_self.pagePara['groupInfo'][i].id === parseInt(value)) {
          return _self.pagePara['groupInfo'][i].text
        }
      }
      return ''
    }
    function initTable () {
      $table.bootstrapTable({
        height: common.getTableHeight(),
        columns: [
          {
            field: 'userID',
            visible: false
          },
          {
            align: 'center',
            valign: 'middle',
            field: 'state',
            radio: true
          },
          common.BTRowFormat('userName', '用户名'),
          common.BTRowFormat('name', '姓名'),
          common.BTRowFormat('helpMark', '客户代码'),
          common.BTRowFormat('mobile', '电话'),
          common.BTRowFormat('email', '邮箱'),
          common.BTRowFormat('userName', '用户名'),
          common.BTRowFormatWithFormatter('userGroupID', '用户组', userGroupFormatter)
        ],
        idField: 'userID',
        uniqueId: 'userID',
        toolbar: '#toolbar',
        striped: true,
        clickToSelect: true,
        search: true,
        showRefresh: true,
        locale: 'zh-CN',
        onCheck: function (row) {
          $('#modifyM').prop('disabled', false)
          _self.currentRow = $.extend(true, {}, row)
          _self.oldRow = $.extend(true, {}, row)
          $('#userGroupM').val([row.userGroupID]).trigger('change')
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
          userNameA: common.BVUsername,
          nameA: common.BVNotEmput('姓名不能为空'),
          helpMarkA: common.BVNotEmput('客户代码'),
          userGroupA: common.BVNotEmput('用户操作组不能为空'),
          emailA: common.BVEmail,
          mobileA: common.BVMobile
        }
      })

      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userNameM: common.BVUsername,
          nameM: common.BVNotEmput('姓名不能为空'),
          helpMarkM: common.BVNotEmput('客户代码'),
          userGroupM: common.BVNotEmput('用户操作组不能为空'),
          emailM: common.BVEmail,
          mobileM: common.BVMobile
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/system/operatorcontrol?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2($('#userGroupA'), retData['groupInfo'])
        common.initSelect2($('#userGroupM'), retData['groupInfo'])
        console.log('init success')
      }, (response) => {
        console.log('init error')
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
      this.userNameA = ''
      this.nameA = ''
      this.helpMarkA = ''
      this.emailA = ''
      this.mobileA = ''
      $('#userGroupA').val(null).trigger('change')
      $('#AddModal').modal('show')
    },
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#userGroupM').val(this.oldRow.userGroupID).trigger('change')
      $('#modifyModal').modal('show')
    },
    add: function (event) {
      var _self = this
      if (common.getValidateResult($('#formA'))) {
        var workRow = {
          'userID': '',
          'userName': _self.userNameA,
          'name': _self.nameA,
          'helpMark': _self.helpMarkA,
          'email': _self.emailA,
          'mobile': _self.mobileA,
          'userGroupID': $('#userGroupA').val()[0]
        }
        _self.$http.post('/api/system/operatorcontrol?method=add', workRow).then((response) => {
          workRow.userID = response.json()['data']['userID']
          $('#table').bootstrapTable('insertRow', { index: 0, row: workRow })
          this.userNameA = ''
          this.nameA = ''
          this.helpMarkA = ''
          this.emailA = ''
          this.mobileA = ''
          $('#userGroupA').val(null).trigger('change')
          $('#formA').data('bootstrapValidator').resetForm()
          common.dealSuccessCommon('增加成功')
        }, (response) => {
          console.log('add error')
          common.dealErrorCommon(_self, response)
        })
      }
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult($('#formM'))) {
        _self.currentRow.userGroupID = $('#userGroupM').val()[0]
        _self.$http.post('/api/system/operatorcontrol?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          $('#table').bootstrapTable('updateByUniqueId', { id: _self.currentRow.userID, row: _self.currentRow })
          common.dealSuccessCommon('修改成功')
          $('#modifyModal').modal('hide')
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(_self, response)
        })
      }
    },
    delete: function (event) {
      var _self = this
      common.dealConfrimCommon('用户删除', function () {
        _self.$http.post('/api/system/operatorcontrol?method=delete', _self.currentRow).then((response) => {
          $('#table').bootstrapTable('remove', { field: 'userID', values: [_self.currentRow.userID] })
          console.log('delete success')
          common.dealSuccessCommon('删除成功')
          $('#modifyModal').modal('hide')
        }, (response) => {
          console.log('delete error')
          common.dealErrorCommon(_self, response)
        })
      })
    },
    makeHelpMarkA: function (event) {
      var py = pinyin(this.nameA, {
        style: pinyin.STYLE_FIRST_LETTER, // 设置拼音风格
        heteronym: true
      })
      this.helpMarkA = py.join('').toUpperCase()
    },
    makeHelpMarkM: function (event) {
      var py = pinyin(this.currentRow.name, {
        style: pinyin.STYLE_FIRST_LETTER, // 设置拼音风格
        heteronym: true
      })
      this.currentRow.helpMark = py.join('').toUpperCase()
    }
  }
}
</script>
<style>
</style>

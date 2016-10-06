<template>
  <section class="content-header">
    <h1>
      放箱员维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">放箱员维护</li>
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
    <div class="modal-dialog" role="document" style="width: 500px;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>增加放箱员</h4>
        </div>
        <div class="modal-body" id="formA">
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>用户名</label>
                <input class="form-control" v-model="userNameA" name="userNameA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>姓名</label>
                <input class="form-control" v-model="nameA" name="nameA" v-on:change="makeHelpMarkA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>手机</label>
                <input type="tel" class="form-control" v-model="mobileA" name="mobileA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>客户代码</label>
                <input class="form-control" v-model="helpMarkA" name="helpMarkA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>性别</label>
                <select class="form-contro select2" multiple style="width:100%" name="genderA" id="genderA">
                </select>
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>出生日期</label>
                <input class="form-control" v-model="birthdayA" name="birthdayA" id="birthdayA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>证件类型</label>
                <select class="form-contro select2" multiple style="width:100%" name="IDTypeA" id="IDTypeA">
                </select>
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>证件号码</label>
                <input class="form-control" v-model="IDNoA" name="IDNoA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>邮箱</label>
                <input type="text" class="form-control" v-model="emailA" name="emailA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-12">
              <div class="form-group">
                <label>相关图像</label>
                <div>
                  <putter-img-upload v-bind:urls.sync='urlsA'></putter-img-upload>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" v-on:click="add"><i class="fa fa-fw fa-plus"></i>增加</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="modifyModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
      <div class="modal-dialog" role="document" style="width: 500px;">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>修改放箱员</h4>
          </div>
          <div class="modal-body" id="formM">
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>用户名</label>
                  <input class="form-control" v-model="currentRow.userName" name="userNameM" disabled>
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>姓名</label>
                  <input class="form-control" v-model="currentRow.name" name="nameM" v-on:change="makeHelpMarkM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>手机</label>
                  <input type="tel" class="form-control" v-model="currentRow.mobile" name="mobileM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>客户代码</label>
                  <input class="form-control" v-model="currentRow.helpMark" name="helpMarkM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>性别</label>
                  <select class="form-contro select2" multiple style="width:100%" name="genderM" id="genderM">
                  </select>
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>出生日期</label>
                  <input class="form-control" v-model="currentRow.birthday" name="birthdayM" id="birthdayM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>证件类型</label>
                  <select class="form-contro select2" multiple style="width:100%" name="IDTypeM" id="IDTypeM">
                  </select>
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>证件号码</label>
                  <input class="form-control" v-model="currentRow.IDNo" name="IDNoM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>邮箱</label>
                  <input type="text" class="form-control" v-model="currentRow.email" name="emailM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-12">
                <div class="form-group">
                  <label>相关图像</label>
                  <div>
                    <putter-img-upload v-bind:urls.sync='urlsM'></putter-img-upload>
                  </div>
                </div>
              </div>
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
import putterImgUpload from '../../components/putBox/putterImgUpload'
var common = require('commonFunc')
var pinyin = require('pinyin')
export default {
  data: function () {
    return {
      pagePara: '',
      userNameA: '',
      nameA: '',
      helpMarkA: '',
      IDNoA: '',
      birthdayA: '',
      mobileA: '',
      emailA: '',
      urlsA: [],
      urlsM: [],
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'putterControl',
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
  components: {
    putterImgUpload
  },
  ready: function () {
    var _self = this
    var $table = $('#table')
    function getData () {
      _self.$http.post('/api/putbox/puttercontrol?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $table.bootstrapTable('load', {
          data: retdata
        })
        $('.tuto-thumbox-detail').each(function () {
          $(this).thumbox({ thumbs: 3, openImageEffect: 'easeOutBack', closeImageEffect: 'easeInBack', scrollDockEffect: 'easeInOutBack' })
        })
      }, (response) => {
        // error callback
        common.dealErrorCommon(_self, response)
      })
    }
    function IDTypeFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['IDTypeInfo'].length; i++) {
        if (_self.pagePara['IDTypeInfo'][i].id === value) {
          return _self.pagePara['IDTypeInfo'][i].text
        }
      }
      return ''
    }
    function genderTypeFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['genderInfo'].length; i++) {
        if (_self.pagePara['genderInfo'][i].id === value) {
          return _self.pagePara['genderInfo'][i].text
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
            align: 'center',
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
          common.BTRowFormat('helpMark', '用户代码'),
          common.BTRowFormatWithFormatter('gender', '性别', genderTypeFormatter),
          common.BTRowFormatWithFormatter('IDType', '证件类型', IDTypeFormatter),
          common.BTRowFormat('IDNo', '证件号码'),
          common.BTRowFormat('birthday', '出生日期'),
          common.BTRowFormat('mobile', '电话'),
          common.BTRowFormat('email', '邮箱'),
          common.BTRowFormatWithPhotoFormatter('images', '图片', common.imagesFormatter)
        ],
        idField: 'userID',
        uniqueId: 'userID',
        toolbar: '#toolbar',
        search: true,
        showRefresh: true,
        striped: true,
        clickToSelect: true,
        locale: 'zh-CN',
        onCheck: function (row) {
          $('#modifyM').prop('disabled', false)
          _self.currentRow = $.extend(true, {}, row)
          _self.oldRow = $.extend(true, {}, row)
          $('#genderM').val([row.gender]).trigger('change')
          $('#IDTypeM').val([row.IDType]).trigger('change')
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
          helpMarkA: common.BVNotEmput('客户代码不能为空'),
          emailA: common.BVEmail,
          mobileA: common.BVMobile,
          genderA: common.BVNotEmput('性别不能为空'),
          birthdayA: common.BVDate,
          IDTypeA: common.BVNotEmput('证件类型不能为空'),
          IDNoA: common.BVNotEmput('证件号码不能为空')
        }
      })
      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userNameM: common.BVUsername,
          nameM: common.BVNotEmput('姓名不能为空'),
          helpMarkM: common.BVNotEmput('客户代码不能为空'),
          emailM: common.BVEmail,
          mobileM: common.BVMobile,
          genderM: common.BVNotEmput('性别不能为空'),
          birthdayM: common.BVDate,
          IDTypeM: common.BVNotEmput('证件类型不能为空'),
          IDNoM: common.BVNotEmput('证件号码不能为空')
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/puttercontrol?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2($('#genderA'), retData['genderInfo'])
        common.initSelect2($('#IDTypeA'), retData['IDTypeInfo'])
        common.initSelect2($('#genderM'), retData['genderInfo'])
        common.initSelect2($('#IDTypeM'), retData['IDTypeInfo'])
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
      common.initDatepicker($('#birthdayA'))
      common.initDatepicker($('#birthdayM'))
    })
  },
  methods: {
    addM: function (event) {
      this.userNameA = ''
      this.nameA = ''
      this.helpMarkA = ''
      this.IDNoA = ''
      this.birthdayA = ''
      this.helpMarkA = ''
      this.mobileA = ''
      this.$broadcast('fileUploadClear')
      $('#genderA').val(null).trigger('change')
      $('#IDTypeA').val(null).trigger('change')
      $('#formA').data('bootstrapValidator').resetForm()
      $('#AddModal').modal('show')
    },
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#genderM').val(this.oldRow.gender).trigger('change')
      $('#IDTypeM').val(this.oldRow.IDType).trigger('change')
      $('#formM').data('bootstrapValidator').resetForm()
      $('#modifyModal').modal('show')
    },
    add: function (event) {
      var _self = this
      if (common.getValidateResult($('#formA'))) {
        var workRow = {
          'userName': _self.userNameA,
          'name': _self.nameA,
          'helpMark': _self.helpMarkA,
          'gender': $('#genderA').val()[0],
          'IDType': $('#IDTypeA').val()[0],
          'IDNo': _self.IDNoA,
          'birthday': _self.birthdayA,
          'mobile': _self.mobileA,
          'email': _self.emailA,
          'images': _self.urlsA
        }
        _self.$http.post('/api/putbox/puttercontrol?method=add', workRow).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('insertRow', { index: 0, row: retData })
          _self.userNameA = ''
          _self.nameA = ''
          _self.helpMarkA = ''
          $('#genderA').val(null).trigger('change')
          $('#IDTypeA').val(null).trigger('change')
          _self.IDNoA = ''
          _self.birthdayA = ''
          _self.mobileA = ''
          _self.emailA = ''
          _self.$broadcast('fileUploadClear')
          $('#formA').data('bootstrapValidator').resetForm()
          common.dealSuccessCommon('增加成功')
          console.log('add success')
        }, (response) => {
          console.log('add error')
          common.dealErrorCommon(_self, response)
        })
      }
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult($('#formM'))) {
        _self.currentRow.gender = $('#genderM').val()[0]
        _self.currentRow.IDType = $('#IDTypeM').val()[0]
        _self.currentRow.images = $.extend(true, [], _self.urlsM)
        _self.$http.post('/api/putbox/puttercontrol?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('updateByUniqueId', { id: _self.currentRow.userID, row: retData })
          common.dealSuccessCommon('修改成功')
          $('#modifyModal').modal('hide')
          console.log('modify success')
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(_self, response)
        })
      }
    },
    delete: function (event) {
      var _self = this
      common.dealConfrimCommon('用户删除', function () {
        _self.$http.post('/api/putbox/puttercontrol?method=delete', _self.currentRow).then((response) => {
          $('#table').bootstrapTable('remove', { field: 'userID', values: [_self.currentRow.userID] })
          common.dealSuccessCommon('删除成功')
          $('#modifyModal').modal('hide')
          console.log('delete success')
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

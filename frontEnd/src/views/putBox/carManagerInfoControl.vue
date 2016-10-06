<template>
  <section class="content-header">
    <h1>
      用箱人信息管理
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">用箱人信息管理</li>
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
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>增加用箱人</h4>
        </div>
        <div class="modal-body" id="formA">
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>客户账号</label>
                <input class="form-control" v-model="userNameA" name="userNameA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>客户全称</label>
                <input class="form-control" v-model="fullNameA" name="fullNameA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>客户名称</label>
                <input type="tel" class="form-control" v-model="nameA" name="nameA" v-on:change="makeHelpMarkA">
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
                <label>手机</label>
                <input class="form-control" v-model="mobileA" name="mobileA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>邮箱</label>
                <input class="form-control" v-model="emailA" name="emailA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>联系方式</label>
                <input type="text" class="form-control" v-model="contactA" name="contactA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>地址</label>
                <input class="form-control" v-model="addressA" name="addressA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>邮编</label>
                <input type="text" class="form-control" v-model="zipCodeA" name="zipCodeA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>电话</label>
                <input class="form-control" v-model="telephoneA" name="telephoneA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>传真</label>
                <input type="text" class="form-control" v-model="faxA" name="faxA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-12">
              <div class="form-group">
                <label>相关图像</label>
                <div>
                  <car-manager-img-upload v-bind:urls.sync='urlsA'></car-manager-img-upload>
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
                  <label>客户账号</label>
                  <input class="form-control" v-model="currentRow.userName" name="userNameM" disabled>
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>客户全称</label>
                  <input class="form-control" v-model="currentRow.fullName" name="fullNameM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>客户名称</label>
                  <input type="tel" class="form-control" v-model="currentRow.name" name="nameM" v-on:change="makeHelpMarkA">
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
                  <label>手机</label>
                  <input class="form-control" v-model="currentRow.mobile" name="mobileM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>邮箱</label>
                  <input class="form-control" v-model="currentRow.email" name="emailM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>联系方式</label>
                  <input type="text" class="form-control" v-model="currentRow.contact" name="contactM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>地址</label>
                  <input class="form-control" v-model="currentRow.address" name="addressM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>邮编</label>
                  <input type="text" class="form-control" v-model="currentRow.zipCode" name="zipCodeM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>电话</label>
                  <input class="form-control" v-model="currentRow.telephone" name="telephoneM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>传真</label>
                  <input type="text" class="form-control" v-model="currentRow.fax" name="faxM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-12">
                <div class="form-group">
                  <label>相关图像</label>
                  <div>
                    <car-manager-img-upload v-bind:urls.sync='urlsM'></car-manager-img-upload>
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
import carManagerImgUpload from '../../components/putBox/carManagerImgUpload'
var common = require('commonFunc')
var pinyin = require('pinyin')
export default {
  data: function () {
    return {
      pagePara: '',
      userNameA: '',
      fullNameA: '',
      nameA: '',
      helpMarkA: '',
      mobileA: '',
      emailA: '',
      contactA: '',
      addressA: '',
      zipCodeA: '',
      telephoneA: '',
      faxA: '',
      urlsA: [],
      urlsM: [],
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'carManagerInfoControl',
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
    carManagerImgUpload
  },
  ready: function () {
    var _self = this
    function getData () {
      _self.$http.post('/api/putbox/carManagerInfoControl?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $('#table').bootstrapTable('load', {
          data: retdata
        })
      }, (response) => {
        // error callback
        common.dealErrorCommon(_self, response)
      })
    }
    function initTable () {
      console.log(common.getTableHeight())
      $('#table').bootstrapTable({
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
          common.BTRowFormat('fullName', '全称'),
          common.BTRowFormat('helpMark', '用户代码'),
          common.BTRowFormat('mobile', '电话'),
          common.BTRowFormat('email', '邮箱'),
          common.BTRowFormat('contact', '联系方式'),
          common.BTRowFormat('address', '地址'),
          common.BTRowFormat('zipCode', '邮编'),
          common.BTRowFormat('telephone', '电话'),
          common.BTRowFormat('fax', '传真'),
          common.BTRowFormatWithPhotoFormatter('images', '图片', common.imagesFormatter)
        ],
        idField: 'userID',
        uniqueId: 'userID',
        toolbar: '#toolbar',
        clickToSelect: true,
        search: true,
        showRefresh: true,
        striped: true,
        locale: 'zh-CN',
        onCheck: function (row) {
          $('#modifyM').prop('disabled', false)
          _self.currentRow = $.extend(true, {}, row)
          _self.oldRow = $.extend(true, {}, row)
        },
        onRefresh: function () {
          getData()
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)
      common.changeTableClass($('#table'))
    }
    function initValidators () {
      $('#formA').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userNameA: common.BVUsername,
          nameA: common.BVNotEmput('姓名不能为空'),
          helpMarkA: common.BVNotEmput('客户代码不能为空')
        }
      })
      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userNameM: common.BVUsername,
          nameM: common.BVNotEmput('姓名不能为空'),
          helpMarkM: common.BVNotEmput('客户代码不能为空')
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/carManagerInfoControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
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
    addM: function (event) {
      var _self = this
      _self.userNameA = ''
      _self.fullNameA = ''
      _self.nameA = ''
      _self.helpMarkA = ''
      _self.mobileA = ''
      _self.emailA = ''
      _self.contactA = ''
      _self.addressA = ''
      _self.zipCodeA = ''
      _self.telephoneA = ''
      _self.faxA = ''
      this.$broadcast('fileUploadDestroy')
      $('#formA').data('bootstrapValidator').resetForm()
      $('#AddModal').modal('show')
    },
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#genderM').val(this.oldRow.gender).trigger('change')
      $('#IDTypeM').val(this.oldRow.IDType).trigger('change')
      $('#modifyModal').modal('show')
    },
    add: function (event) {
      var _self = this
      if (common.getValidateResult($('#formA'))) {
        var workRow = {
          'userName': _self.userNameA,
          'fullName': _self.fullNameA,
          'name': _self.nameA,
          'helpMark': _self.helpMarkA,
          'mobile': _self.mobileA,
          'email': _self.emailA,
          'contact': _self.contactA,
          'address': _self.addressA,
          'zipCode': _self.zipCodeA,
          'telephone': _self.telephoneA,
          'fax': _self.faxA,
          'images': _self.urlsA
        }
        this.$http.post('/api/putbox/carManagerInfoControl?method=add', workRow).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('insertRow', { index: 0, row: retData })
          _self.userNameA = ''
          _self.fullNameA = ''
          _self.nameA = ''
          _self.helpMarkA = ''
          _self.mobileA = ''
          _self.emailA = ''
          _self.contactA = ''
          _self.addressA = ''
          _self.zipCodeA = ''
          _self.telephoneA = ''
          _self.faxA = ''
          this.$broadcast('fileUploadDestroy')
          $('#formA').data('bootstrapValidator').resetForm()
          common.dealSuccessCommon('增加成功')
          console.log('add success')
        }, (response) => {
          console.log('add error')
          common.dealErrorCommon(this, response)
        })
      }
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult($('#formM'))) {
        _self.currentRow.images = $.extend(true, [], _self.urlsM)
        this.$http.post('/api/putbox/carManagerInfoControl?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('updateByUniqueId', { id: retData.userID, row: retData })
          common.dealSuccessCommon('修改成功')
          $('#modifyModal').modal('hide')
          console.log('modify success')
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(this, response)
        })
      }
    },
    delete: function (event) {
      var _self = this
      common.dealConfrimCommon('用户删除', function () {
        _self.$http.post('/api/putbox/carManagerInfoControl?method=delete', _self.currentRow).then((response) => {
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

<template>
  <section class="content-header">
    <h1>
      堆场维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 基本管理</a></li>
      <li class="active">堆场维护</li>
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
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>增加堆场</h4>
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
                <label>名称</label>
                <input class="form-control" v-model="nameA" name="nameA"  v-on:change="makeHelpMarkA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>全称</label>
                <input class="form-control" v-model="fullNameA" name="fullNameA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>简称</label>
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
            <div class="col-xs-4">
              <div class="form-group">
                <label>省</label>
                <input class="form-control" v-model="provinceA" name="provinceA">
              </div>
            </div>
            <div class="col-xs-4">
              <div class="form-group">
                <label>市</label>
                <input class="form-control" v-model="cityA" name="cityA">
              </div>
            </div>
            <div class="col-xs-4">
              <div class="form-group">
                <label>区</label>
                <input class="form-control" v-model="regionA" name="regionA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-12">
              <div class="form-group">
                <label>详细地址</label>
                <input class="form-control" v-model="addressA" name="addressA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>联系人</label>
                <input class="form-control" v-model="contactNameA" name="contactNameA">
              </div>
            </div>

            <div class="col-xs-6">
              <div class="form-group">
                <label>联系方式</label>
                <input class="form-control" v-model="contactA" name="contactA">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-6">
              <div class="form-group">
                <label>网址</label>
                <input class="form-control" v-model="webSiteA" name="webSiteA">
              </div>
            </div>
            <div class="col-xs-6">
              <div class="form-group">
                <label>GPS</label>
                <input class="form-control" v-model="GPSA" name="GPSA">
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
            <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>维护堆场</h4>
          </div>
          <div class="modal-body" id="formM">
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>用户名</label>
                  <input class="form-control" v-model="currentRow.userName" name="userNameM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>名称</label>
                  <input class="form-control" v-model="currentRow.name" name="nameM"  v-on:change="makeHelpMarkM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>简称</label>
                  <input class="form-control" v-model="currentRow.helpMark" name="helpMarkM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>全称</label>
                  <input class="form-control" v-model="currentRow.fullName" name="fullNameM">
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
              <div class="col-xs-4">
                <div class="form-group">
                  <label>省</label>
                  <input class="form-control" v-model="currentRow.province" name="provinceM">
                </div>
              </div>
              <div class="col-xs-4">
                <div class="form-group">
                  <label>市</label>
                  <input class="form-control" v-model="currentRow.city" name="cityM">
                </div>
              </div>
              <div class="col-xs-4">
                <div class="form-group">
                  <label>区</label>
                  <input class="form-control" v-model="currentRow.region" name="regionM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-12">
                <div class="form-group">
                  <label>详细地址</label>
                  <input class="form-control" v-model="currentRow.address" name="addressM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>联系人</label>
                  <input class="form-control" v-model="currentRow.contactName" name="contactNameM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>联系方式</label>
                  <input class="form-control" v-model="currentRow.contact" name="contactM">
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xs-6">
                <div class="form-group">
                  <label>网址</label>
                  <input class="form-control" v-model="currentRow.webSite" name="webSiteM">
                </div>
              </div>
              <div class="col-xs-6">
                <div class="form-group">
                  <label>GPS</label>
                  <input class="form-control" v-model="currentRow.GPS" name="GPSM">
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
var common = require('commonFunc')
var pinyin = require('pinyin')
export default {
  data: function () {
    return {
      pagePara: '',
      userNameA: '',
      nameA: '',
      mobileA: '',
      emailA: '',
      helpMarkA: '',
      fullNameA: '',
      provinceA: '',
      cityA: '',
      regionA: '',
      addressA: '',
      contactNameA: '',
      contactA: '',
      webSiteA: '',
      GPSA: '',
      currentRow: '',
      oldRow: ''
    }
  },
  name: 'containerYardControl',
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
    function getData () {
      _self.$http.post('/api/basic/containerYardControl?method=search', {}).then((response) => {
        var retdata = response.json()['data']
        $('#table').bootstrapTable('load', {
          data: retdata
        })
      }, (response) => {
        // error callback
        console.log('get data error')
        common.dealErrorCommon(_self, response)
      })
    }

    function webSiteFormatter (value, row) {
      return '<a href="' + value + '" target="blank">' + value + '</a>'
    }

    function initTable () {
      $('#table').bootstrapTable({
        height: common.getTableHeight(),
        columns: [{
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
        common.BTRowFormat('name', '名称'),
        common.BTRowFormat('mobile', '手机'),
        common.BTRowFormat('email', '邮箱'),
        common.BTRowFormat('helpMark', '简称'),
        common.BTRowFormatWithFormatter('fullName', '全称', common.remarkFormatter),
        common.BTRowFormat('province', '省'),
        common.BTRowFormat('city', '市'),
        common.BTRowFormat('region', '区'),
        common.BTRowFormatWithFormatter('address', '详细地址', common.remarkFormatter),
        common.BTRowFormat('contactName', '联系人'),
        common.BTRowFormat('contact', '联系方式'),
        common.BTRowFormatWithFormatter('webSite', '网址', webSiteFormatter),
        {
          field: 'GPS',
          title: 'GPS信息',
          align: 'center',
          valign: 'middle',
          visible: false
        }],
        idField: 'userID',
        uniqueId: 'userID',
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
        },
        onAll: function (name, args) {
          $('[data-toggle="popover"]').each(function () {
            $(this).popover()
          })
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
          nameA: common.BVNotEmput('名称不能为空'),
          helpMarkA: common.BVNotEmput('简称不能为空')
        }
      })
      $('#formM').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
          userNameM: common.BVUsername,
          nameM: common.BVNotEmput('名称不能为空'),
          helpMarkM: common.BVNotEmput('简称不能为空')
        }
      })
    }

    $(function () {
      initTable()
      common.initControlSize()
      getData()
      initValidators()
    })
  },
  methods: {
    addM: function (event) {
      this.userNameA = ''
      this.nameA = ''
      this.mobileA = ''
      this.emailA = ''
      this.helpMarkA = ''
      this.fullNameA = ''
      this.provinceA = ''
      this.cityA = ''
      this.regionA = ''
      this.addressA = ''
      this.contactNameA = ''
      this.contactA = ''
      this.webSiteA = ''
      this.GPSA = ''
      $('#formA').data('bootstrapValidator').resetForm()
      $('#AddModal').modal('show')
    },
    modifyM: function (event) {
      this.currentRow = $.extend(true, {}, this.oldRow)
      $('#formM').data('bootstrapValidator').resetForm()
      $('#modifyModal').modal('show')
    },
    add: function (event) {
      var _self = this
      if (common.getValidateResult($('#formA'))) {
        var workRow = {
          'userName': _self.userNameA,
          'name': _self.nameA,
          'mobile': _self.mobileA,
          'email': _self.emailA,
          'helpMark': _self.helpMarkA,
          'fullName': _self.fullNameA,
          'province': _self.provinceA,
          'city': _self.cityA,
          'region': _self.regionA,
          'address': _self.addressA,
          'contact': _self.contactA,
          'contactName': _self.contactNameA,
          'webSite': _self.webSiteA,
          'GPS': _self.GPSA
        }
        _self.$http.post('/api/basic/containerYardControl?method=add', workRow).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('insertRow', { index: 0, row: retData })
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
        _self.$http.post('/api/basic/containerYardControl?method=modify', { 'old': _self.oldRow, 'new': _self.currentRow }).then((response) => {
          var retData = response.json()['data']
          $('#table').bootstrapTable('updateByUniqueId', { id: retData.userID, row: retData })
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
        _self.$http.post('/api/basic/containerYardControl?method=delete', _self.currentRow).then((response) => {
          $('#table').bootstrapTable('remove', { field: 'userID', values: [_self.currentRow.userID] })
          common.dealSuccessCommon('删除成功')
          $('#modifyModal').modal('hide')
          console.log('delete success')
        }, (response) => {
          console.log('delete error')
          common.dealErrorCommon(this, response)
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

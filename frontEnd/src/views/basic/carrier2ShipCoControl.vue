<template>
  <section class="content-header">
    <h1>
      承运人堆场维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 系统管理</a></li>
      <li class="active">承运人堆场维护</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
    <div class="box box-success">
      <div class="box-body">
        <div id="toolbar" class="pull-right">
          <div class="form-inline" role="form">
            <div class="form-group">
              <label>承运人</label>
              <select class="form-control select2" style="width: 200px" name="carrierID" id="carrierID">
              </select>
            </div>
            <div class="form-group">
              <button id="modify" class="btn btn-success" v-on:click="modify" disabled>
                <i class="glyphicon glyphicon-saved"></i> 提交
              </button>
            </div>
          </div>
        </div>
        <table id="table"></table>
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

export default {
  data: function () {
    return {
      pagePara: '',
      tableData: ''
    }
  },
  name: 'carrier2YardControl',
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

    function initTable () {
      $table.bootstrapTable({
        height: common.getTableHeight(),
        columns:
        [
          {
            field: 'state',
            checkbox: true
          },
          {
            field: 'yardID',
            align: 'center',
            visible: false
          },
          common.BTRowFormat('name', '名称'),
          common.BTRowFormat('helpMark', '简称'),
          common.BTRowFormatWithFormatter('fullName', '全称', common.remarkFormatter),
          common.BTRowFormatWithFormatter('vAdress', '地址', common.remarkFormatter)
        ],
        idField: 'yardID',
        uniqueId: 'yardID',
        toolbar: '#toolbar',
        clickToSelect: true,
        striped: true,
        locale: 'zh-CN'
      })
      setTimeout(function () {
        $table.bootstrapTable('resetView')
      }, 200)
      common.changeTableClass($table)
    }

    function initPage () {
      _self.$http.post('/api/basic/carrier2YardControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        for (let i = 0; i < retData.yardInfo.length; i++) {
          retData.yardInfo[i]['state'] = false
        }
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2SingleWithSearch($('#carrierID'), retData['carrierInfo'])
        $('#table').bootstrapTable('load', {
          data: retData.yardInfo
        })
        console.log('init success')
      }, (response) => {
        console.log('init error')
        common.dealErrorCommon(_self, response)
      })
    }

    function getCheckData () {
      var carrierID = $('#carrierID').val()
      _self.$http.post('/api/basic/carrier2YardControl?method=searchCheck', { 'carrierID': carrierID }).then((response) => {
        var retData = response.json()['data']
        console.log(retData)
        var yardInfo = $.extend(true, [], _self.pagePara.yardInfo)
        for (let i = 0; i < retData.carrierYard.length; i++) {
          for (let j = 0; j < yardInfo.length; j++) {
            if (retData.carrierYard[i] === yardInfo[j].userID) {
              yardInfo[j]['state'] = true
            }
          }
        }
        _self.tableData = $.extend(true, [], yardInfo)
        $('#table').bootstrapTable('load', {
          data: yardInfo
        })
      }, (response) => {
        // error callback
        console.log('get data error')
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      initPage()
      common.initControlSize()
      initTable()
      $('#carrierID').on('select2:select', function (evt) {
        getCheckData()
        $('#modify').prop('disabled', false)
      })
    })
  },
  methods: {
    modify: function (event) {
      var carrierID = $('#carrierID').val()
      console.log(carrierID)
      if (!carrierID) {
        common.dealPromptCommon('未选定承运人')
      } else {
        var yardData = $('#table').bootstrapTable('getSelections')

        this.$http.post('/api/basic/carrier2YardControl?method=modify', { 'carrierID': carrierID, 'yardData': yardData }).then((response) => {
          common.dealSuccessCommon('更新成功')
        }, (response) => {
          // error callback
          console.log('get data error')
          common.dealErrorCommon(this, response)
        })
      }
    }
  }
}

</script>
<style>
</style>

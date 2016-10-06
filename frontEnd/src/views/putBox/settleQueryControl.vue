<template>
  <section class="content-header">
    <h1>
      财务结算查询
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">财务结算查询</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar" class="pull-right">
            <div class="form-inline" role="form">
              <div class="form-group">
                <div class="input-group">
                  <div class="input-group-addon">
                    <i class="fa fa-calendar"></i>
                  </div>
                  <input type="text" class="form-control pull-right" style="width: 230px" id="daterange">
                </div>
              </div>
            </div>
          </div>
          <table id="table"></table>
        </div>
      </div>
    </div>
  </section>
  <!-- DetailModal -->
  <div class="modal fade" id="detail-modal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document" style="width: 950px;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>详细信息</h4>
        </div>
        <div class="modal-body">
          <div class="box-body">
            <table id="detail-table"></table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- DetailModal -->
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
import moment from 'moment'
var common = require('commonFunc')
let currentCarrierID
let currentRow

function getData (obj) {
  // console.log(_self.searchDate)
  var carManagerID = $('#carManagerID').val()
  if (!carManagerID) { return }
  obj.$http.post('/api/putbox/settleQueryControl?method=search', { 'stDate': obj.stDate, 'edDate': obj.edDate }).then((response) => {
    var retData = response.json()['data']
    obj.tableData = $.extend(true, {}, retData)
    $('#table').bootstrapTable('load', {
      data: retData
    })
    obj.$compile(obj.$el)
  }, (response) => {
    // error callback
    common.dealErrorCommon(obj, response)
  })
}

export default {
  data: function () {
    return {
      pagePara: '',
      stDate: moment().subtract(9, 'days').format('YYYY-MM-DD'),
      edDate: moment().format('YYYY-MM-DD'),
      currentSettle: ''
    }
  },
  name: 'settleQueryControl',
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
    function imagesFormatter (value, row) {
      var retString = '<div class="btn-group">'
      for (var key in value) {
        retString += '<div style="height:30;width:30px;float:left;"><a data-lightbox="image-1" href="' + value[key] + '" > <img class="img-responsive" src="' + value[key] + '"> </a></div>'
      }
      retString += '</div>'
      return retString
    }
    function operateFormatter (value, row, index) {
      var updateRowId = row.uid
      return [
        '<a class="update" v-on:click="showdetail(\'' + updateRowId + '\')" title="展示">',
        '<i class="glyphicon glyphicon-pencil"></i>',
        '</a>'
      ].join('')
    }
    function initTable () {
      $('#table').bootstrapTable({
        height: common.getTableHeight(),
        columns:
        [
          common.BTRowFormatWithFormatter('mtype', '类型', mTypeFormatter),
          common.BTRowFormat('uid', '财务流水号'),
          common.BTRowFormat('settleDate', '结算日期'),
          common.BTRowFormat('bgDate', '开始日期'),
          common.BTRowFormat('edDate', '结束日期'),
          common.BTRowFormat('receivables', '应收金额'),
          common.BTRowFormat('proceeds', '实收金额'),
          common.BTRowFormatWithFormatter('status', '状态', statusFormatter),
          common.BTRowFormatWithFormatter('remark', '备注', common.remarkFormatter),
          common.BTRowFormatWithFormatter('images', '图片', imagesFormatter),
          {
            field: 'act',
            formatter: operateFormatter,
            align: 'center',
            valign: 'middle'
          }
        ],
        idField: 'uid',
        uniqueId: 'uid',
        toolbar: '#toolbar',
        search: true,
        showRefresh: true,
        striped: true,
        locale: 'zh-CN',
        onRefresh: function () {
          getData(_self)
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)
    }

    function mTypeFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['putMoneyType'].length; i++) {
        if (_self.pagePara['putMoneyType'][i].id === value) {
          return _self.pagePara['putMoneyType'][i].text
        }
      }
      return ''
    }

    function statusFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['putSettleStatusInfo'].length; i++) {
        if (_self.pagePara['putSettleStatusInfo'][i].id === value) {
          return '<span class="label ' + _self.pagePara['putSettleStatusInfo'][i].style + '">' + _self.pagePara['putSettleStatusInfo'][i].text + '</span>'
        }
      }
      return ''
    }

    function initPage () {
      _self.$http.post('/api/putbox/settleQueryControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        console.log('init success')
      }, (response) => {
        console.log('init error')
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      common.initControlSize()
      initPage()
      initTable()
      $('#daterange').daterangepicker({
        startDate: _self.stDate,
        endDate: _self.edDate,
        timePicker: false,
        dateLimit: { days: 30 },
        ranges: {
          '最近7日': [moment().subtract(6, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')],
          '最近14日': [moment().subtract(13, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')],
          '最近30日': [moment().subtract(29, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')]
        },
        locale: common.daterangepickerlocale
      }, function (start, end, label) { // 格式化日期显示框
        _self.stDate = start.format('YYYY-MM-DD')
        _self.edDate = end.format('YYYY-MM-DD')
        getData(_self)
      })
    })
  },
  methods: {
    showdetail: function (uid) {
      var row = $('#table').bootstrapTable('getRowByUniqueId', uid)
      var _self = this
      function initDetailTable () {
        $('#detail-table').bootstrapTable({
          height: 600,
          columns:
          [
            common.BTRowFormat('trunkListID', '流水号'),
            common.BTRowFormat('maketime', '申请日期'),
            common.BTRowFormat('billLodingNo', '提单号'),
            common.BTRowFormat('containerStuffingCharge', '提箱费'),
            common.BTRowFormat('logisticsHitCharge', '打单费'),
            common.BTRowFormat('serviceCharge', '服务费'),
            common.BTRowFormat('otherFee', '其他'),
            common.BTRowFormat('subfee', '总金额'),
            common.BTRowFormatWithFormatter('remark', '备注', common.remarkFormatter)
          ],
          idField: 'trunkListID',
          uniqueId: 'trunkListID',
          search: true,
          formatNoMatches: function () {
            return
          }
        })
        setTimeout(function () {
          $('#table').bootstrapTable('resetView')
        }, 200)
      }
      function getDetailData (row) {
        var carManagerID = $('#carManagerID').val()
        if (!carManagerID) { return }
        _self.$http.post('/api/putbox/settleControl?method=searchDetail', { 'carManagerID': carManagerID, 'uid': row.uid }).then((response) => {
          var retData = response.json()['data']
          $('#detail-table').bootstrapTable('load', {
            data: retData
          })
        }, (response) => {
          common.dealErrorCommon(_self, response)
        })
      }

      initDetailTable()
      getDetailData(row)
      $('#detail-modal').modal('show')
    }
  }
}
</script>
<style>
</style>

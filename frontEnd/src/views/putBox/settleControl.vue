<template>
  <section class="content-header">
    <h1>
      财务结算
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">财务结算</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar" class="pull-right">
            <div class="form-inline" role="form">
              <div class="form-group">
                <label>用箱人</label>
                <select class="form-control select2" style="width: 200px" name="carManagerID" id="carManagerID">
                </select>
              </div>
              <div class="form-group">
                <div class="input-group">
                  <div class="input-group-addon">
                    <i class="fa fa-calendar"></i>
                  </div>
                  <input type="text" class="form-control pull-right" style="width: 230px" id="daterange">
                </div>
              </div>
              <div class="form-group">
                <button id="settleM" class="btn btn-info" v-on:click="settleM" disabled>
                  <i class="glyphicon glyphicon-saved"></i> 结算
                </button>
              </div>
              <div class="form-group">
                <button id="settleC" class="btn btn-success" v-on:click="settleC" disabled>
                  <i class="glyphicon glyphicon-check"></i> 款项结清
                </button>
              </div>
            </div>
          </div>
          <table id="table"></table>
        </div>
      </div>
    </div>
  </section>
  <!-- STModal -->
  <div class="modal fade" id="STModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document" style="width: 950px;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>结算</h4>
        </div>
        <div class="modal-body">
            <div id="STtoolbar" class="pull-right">
              <div class="form-inline" role="form">
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-calendar"></i>
                    </div>
                    <input type="text" class="form-control pull-right" style="width: 230px" id="STdaterange">
                  </div>
                </div>
                <div class="form-group">
                  <div class="form-group">
                    <button id="settle" class="btn btn-success" v-on:click="settle" disabled>
                      <i class="glyphicon glyphicon-saved"></i> 提交
                    </button>
                  </div>
                </div>
                <div class="form-group" style="margin-left: 20px">
                  <label>总金额:</label>
                  <div style="margin-left: 10px; display: inline;">{{ sumMoney | currency }}</div>
                </div>
              </div>
            </div>
            <div class="box-body">
              <table id="STtable"></table>
            </div>
        </div>
      </div>
    </div>
  </div>
  <!-- STModal -->
  <!-- CLModal -->
  <div class="modal fade" id="CLModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document" style="width: 800px;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>款项结清</h4>
        </div>
        <div class="modal-body" id="deskForm">
          <div class="form-group">
            <label>财务流水号</label>
            <input class="form-control" v-model="currentSettle.uid" disabled>
          </div>
          <div class="form-group">
            <label> 结算日期</label>
            <input class="form-control" v-model="currentSettle.settleDate" disabled>
          </div>
          <div class="form-group">
            <label> 日期区间</label>
            <input class="form-control" v-model="currentSettle.bgDate + ' -- ' + currentSettle.edDate" disabled>
          </div>
          <div class="form-group">
            <label> 应收金额</label>
            <input class="form-control" v-model="currentSettle.receivables" disabled>
          </div>
          <div class="form-group">
            <label> 实收金额</label>
            <input class="form-control" v-model="currentSettle.proceeds" name="proceeds">
          </div>
          <div class="form-group">
            <label> 备注</label>
            <textarea rows="3" class="form-control" v-model="currentSettle.remark"></textarea>
          </div>
          <div class="form-group">
            <label>相关图像</label>
            <div>
              <settle-img-upload v-bind:urls.sync="urls"></settle-img-upload>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" v-on:click="clear">确定</button>
        </div>
      </div>
    </div>
  </div>
  <!-- CLModal -->
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
import settleImgUpload from '../../components/putBox/settleImgUpload'
import moment from 'moment'
var common = require('commonFunc')
let currentCarrierID
let currentRow

function getData (obj) {
  // console.log(_self.searchDate)
  var carManagerID = $('#carManagerID').val()
  if (!carManagerID) { return }
  obj.$http.post('/api/putbox/settleControl?method=search', { 'carManagerID': carManagerID, 'stDate': obj.stDate, 'edDate': obj.edDate }).then((response) => {
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

function sumMoney (obj) {
  var sum = 0.00
  for (let i = 0; i < obj.STtableData.length; i++) {
    if (obj.STtableData[i].ckstate === true) {
      sum += parseFloat(obj.STtableData[i].subfee)
    }
  }
  obj.sumMoney = sum
  if (sum > 0.009) {
    $('#settle').prop('disabled', false)
  } else {
    $('#settle').prop('disabled', true)
  }
}

function getSTData (obj) {
  var carManagerID = $('#carManagerID').val()
  if (!carManagerID) { return }
  obj.$http.post('/api/putbox/settleControl?method=searchST', { 'carManagerID': carManagerID, 'stDate': obj.STstDate, 'edDate': obj.STedDate }).then((response) => {
    var retData = response.json()['data']
    for (let i = 0; i < retData.length; i++) {
      retData[i]['ckstate'] = true
    }
    obj.STtableData = $.extend(true, [], retData)
    sumMoney(obj)
    $('#STtable').bootstrapTable('load', {
      data: retData
    })
  }, (response) => {
    common.dealErrorCommon(obj, response)
  })
}

export default {
  data: function () {
    return {
      pagePara: '',
      stDate: moment().subtract(9, 'days').format('YYYY-MM-DD'),
      edDate: moment().format('YYYY-MM-DD'),
      STstDate: moment().subtract(9, 'days').format('YYYY-MM-DD'),
      STedDate: moment().format('YYYY-MM-DD'),
      tableData: '',
      STtableData: '',
      currentSettle: '',
      sumMoney: 0.00,
      urls: []
    }
  },
  name: 'settleControl',
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
    settleImgUpload
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
          {
            align: 'center',
            valign: 'middle',
            field: 'state',
            radio: true
          },
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
        clickToSelect: true,
        locale: 'zh-CN',
        onRefresh: function () {
          getData(_self)
        },
        onCheck: function (row) {
          if (row.status === '0') {
            $('#settleC').prop('disabled', false)
          } else {
            $('#settleC').prop('disabled', true)
          }
          _self.currentSettle = $.extend(true, {}, row)
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

    function initValidators () {
      $('#deskForm').bootstrapValidator({
        container: 'tooltip',
        fields: {
          proceeds: common.BVMoney
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/settleControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = $.extend(true, {}, retData)
        common.initSelect2SingleWithSearch($('#carManagerID'), retData['carManagerInfo'])
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
      initValidators()
      $('#carManagerID').on('select2:select', function (evt) {
        getData(_self)
        $('#settleM').prop('disabled', false)
      })
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
    },
    settle: function (event) {
      var _self = this
      common.dealConfrimCommon('提交结算', function () {
        var sData = {}
        sData['carManagerID'] = $('#carManagerID').val()
        sData['stDate'] = _self.STstDate
        sData['edDate'] = _self.STedDate
        sData['sumMoney'] = _self.sumMoney
        sData['ids'] = []
        for (let i = 0; i < _self.STtableData.length; i++) {
          if (_self.STtableData[i].ckstate) {
            sData['ids'].push(_self.STtableData[i].trunkListID)
          }
        }
        _self.$http.post('/api/putbox/settleControl?method=settle', sData).then((response) => {
          var retData = response.json()['data']
          getSTData(_self)
          getData(_self)
          common.dealSuccessCommon('结算成功')
        }, (response) => {
          common.dealErrorCommon(_self, response)
        })
      })
    },
    clear: function (event) {
      var _self = this
      if (common.getValidateResult()) {
        $('#CLModal').modal('hide')
        common.dealConfrimCommon('款项结清', function () {
          var sData = {}
          sData['carManagerID'] = $('#carManagerID').val()
          sData['uid'] = _self.currentSettle.uid
          sData['settleDate'] = _self.currentSettle.settleDate
          sData['receivables'] = _self.currentSettle.receivables
          sData['proceeds'] = _self.currentSettle.proceeds
          sData['remark'] = _self.currentSettle.remark
          sData['images'] = _self.urls
          _self.$http.post('/api/putbox/settleControl?method=clear', sData).then((response) => {
            var retData = response.json()['data']
            $('#table').bootstrapTable('updateByUniqueId', { id: retData.uid, row: retData })
            $('#settleC').prop('disabled', true)
            common.dealSuccessCommon('结款成功')
          }, (response) => {
            common.dealErrorCommon(_self, response)
          })
        })
      }
    },
    settleM: function (event) {
      var _self = this
      function initSTTable () {
        $('#STtable').bootstrapTable({
          height: 600,
          columns:
          [
            {
              align: 'center',
              valign: 'middle',
              field: 'ckstate',
              checkbox: true
            },
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
          toolbar: '#STtoolbar',
          search: true,
          showRefresh: true,
          striped: true,
          clickToSelect: true,
          formatNoMatches: function () {
            return
          },
          onRefresh: function () {
            getSTData(_self)
          },
          onPreBody: function (data) {
            for (let i = 0; i < data.length; i++) {
              for (let j = 0; j < _self.STtableData.length; j++) {
                if (data[i].trunkListID === _self.STtableData[j].trunkListID) {
                  data[i].ckstate = _self.STtableData[j].ckstate
                }
              }
            }
          },
          onCheck: function (row) {
            for (let i = 0; i < _self.STtableData.length; i++) {
              if (row.trunkListID === _self.STtableData[i].trunkListID) {
                _self.STtableData[i].ckstate = row.ckstate
              }
            }
            sumMoney(_self)
          },
          onUncheck: function (row) {
            for (let i = 0; i < _self.STtableData.length; i++) {
              if (row.trunkListID === _self.STtableData[i].trunkListID) {
                _self.STtableData[i].ckstate = row.ckstate
              }
            }
            sumMoney(_self)
          },
          onCheckAll: function (rows) {
            for (let i = 0; i < _self.STtableData.length; i++) {
              _self.STtableData[i].ckstate = true
            }
            sumMoney(_self)
          },
          onUncheckAll: function (rows) {
            for (let i = 0; i < _self.STtableData.length; i++) {
              _self.STtableData[i].ckstate = false
            }
            sumMoney(_self)
          }
        })
        setTimeout(function () {
          $('#table').bootstrapTable('resetView')
        }, 200)
      }

      initSTTable()
      $('#STdaterange').daterangepicker({
        startDate: _self.STstDate,
        endDate: _self.STedDate,
        timePicker: false,
        dateLimit: { days: 60 },
        ranges: {
          '最近7日': [moment().subtract(6, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')],
          '最近14日': [moment().subtract(13, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')],
          '最近30日': [moment().subtract(29, 'days').format('YYYY-MM-DD'), moment().format('YYYY-MM-DD')]
        },
        locale: common.daterangepickerlocale
      }, function (start, end, label) { // 格式化日期显示框
        _self.STstDate = start.format('YYYY-MM-DD')
        _self.STedDate = end.format('YYYY-MM-DD')
        getSTData(_self)
      })
      getSTData(_self)
      $('#STModal').modal('show')
    },
    settleC: function (event) {
      $('#CLModal').modal('show')
    }
  }
}
</script>
<style>
</style>

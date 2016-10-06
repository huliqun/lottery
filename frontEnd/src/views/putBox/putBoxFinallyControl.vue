<template>
  <section class="content-header">
    <h1>
      对单&退关&退单
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">对单&退关&退单</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar" class="pull-right">
            <div class="form-inline" role="form">
              <div class="form-group">
                <button id="match" class="btn btn-success" style="background-color: #993300; border-color: #993333;" disabled>
                  <i class="glyphicon glyphicon-check"></i> 对单
                </button>
              </div>
              <div class="form-group">
                <button id="shutout" class="btn btn-danger" style="background-color: #CC9933; border-color: #CC9900;" disabled>
                  <i class="glyphicon glyphicon-repeat"></i> 退关
                </button>
              </div>
              <div class="form-group">
                <button id="chargeback" class="btn btn-danger" style="background-color: #515151; border-color: #4D4D4D;" disabled>
                  <i class="glyphicon glyphicon-arrow-left"></i> 退单
                </button>
              </div>
              <div class="form-group" style="margin-left:15px;">
                <input name="searchDate" v-model="searchDate" class="form-control" id="searchDate">
              </div>
            </div>
          </div>
          <table id="table"></table>
        </div>
      </div>
    </div>
  </section>
  <!-- Modal Edit -->
  <div class="modal fade" id="rowEditModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" v-on:click="clear"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="rowEditModalLabel"><i class="fa fa-pencil-square-o big-blue"></i>放箱修改</h4>
          </div>
          <div class="modal-body">
            <div class="form-horizontal">
              <div class="box-body">
                <div class="form-group">
                  <label class="col-sm-2 control-label">用箱人</label>
                  <div class="col-sm-10">
                    <input class="form-control" v-model="currentRow.carManagerInfo.name" disabled="disabled">
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">放箱人</label>
                  <div class="col-sm-10">
                    <select class="form-control select2" multiple style="width:100%" id="modal_putter" name="modal_putter" disabled="disabled">
                    </select>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">船代</label>
                  <div class="col-sm-10">
                    <select class="form-control select2" multiple style="width:100%" id="modal_carrier" name="modal_carrier">
                    </select>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">船舶信息</label>
                  <div class="col-sm-10">
                    <div class="nav-tabs-custom " style="cursor: move;">
                      <ul class="nav nav-tabs pull-right ui-sortable-handle">
                        <li class="active"><a href="#select-ship" data-toggle="tab" aria-expanded="true">选择</a></li>
                        <li class=""><a href="#input-ship" data-toggle="tab" aria-expanded="false">填充</a></li>
                      </ul>
                      <div class="tab-content no-padding">
                        <!-- Morris chart - Sales -->
                        <div class="chart tab-pane active " id="select-ship" style="position: relative;">
                          <div class="col-sm-8" style="padding-left:0px">
                            <select class="select2 " multiple id="modal_EDIExportShipID" name="modal_EDIExportShipID"></select>
                          </div>
                          <div class="col-sm-4" style="padding-right:0px">
                            <select class="select2 " multiple id="modal_transitPortId" name="modal_transitPortId"></select>
                          </div>
                        </div>
                        <div class="chart tab-pane" id="input-ship" style="position: relative;">
                          <div>
                            <label>船名</label>
                            <input type="text" class="form-control" v-model="currentRow.shipName" name="modal_shipName">
                          </div>
                          <div>
                            <label>航次</label>
                            <input type="text" class="form-control" v-model="currentRow.voyageNo" name="modal_voyageNo">
                          </div>
                          <div>
                            <label>中转港</label>
                            <input type="text" class="form-control" v-model="currentRow.transportationHub" name="modal_transitPort">
                          </div>
                        </div>
                      </div>
                      <div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">箱型箱量</label>
                  <div class="col-sm-3">
                    <select class="form-control select2" multiple id="modal_containerSize" name="modal_containerSize">
                    </select>
                  </div>
                  <div class="col-sm-3">
                    <select class="form-control select2" multiple id="modal_containerType" name="modal_containerType">
                    </select>
                  </div>
                  <label for="code" class="col-sm-1 control-label">X</label>
                  <div class="col-sm-3">
                    <input class="form-control" type='number' min='1' v-model="currentRow.containerCount" name="modal_containerCount">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-2 control-label">堆场</label>
                  <div class="col-sm-10">
                    <table id="containerCountYard_table" class="table table-no-bordered" style="margin-bottom:0">
                      <thead>
                        <tr>
                          <th style="text-align: center; width: 30%; " data-field="containerCount" tabindex="0"><div class="th-inner " style="font-weight:normal;">数量</div><div class="fht-cell"></div></th>
                          <th style="text-align: center; width: 60%; " data-field="containerYard" tabindex="0"><div class="th-inner " style="font-weight:normal;">堆场</div><div class="fht-cell"></div></th>
                          <th style="text-align: center; width: 10%; " data-field="3" tabindex="0"><div class="th-inner "></div><div class="fht-cell"></div></th>
                        </tr>
                      </thead>
                      <tbody>
                      </tbody>
                    </table>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">费用</label>
                  <div class="col-sm-10">
                    <table id="fee_table" class="table table-no-bordered" style="margin-bottom:0">
                      <thead>
                        <tr>
                          <th style="text-align: center; width: 25%; " tabindex="0"><div class="th-inner " style="font-weight:normal;">提箱费</div><div class="fht-cell"></div></th>
                          <th style="text-align: center; width: 25%; " tabindex="0"><div class="th-inner " style="font-weight:normal;">打单费</div><div class="fht-cell"></div></th>
                          <th style="text-align: center; width: 25%; " tabindex="0"><div class="th-inner " style="font-weight:normal;">服务费</div><div class="fht-cell"></div></th>
                          <th style="text-align: center; width: 25%; " tabindex="0"><div class="th-inner " style="font-weight:normal;">其他</div><div class="fht-cell"></div></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td style="text-align: center; width: 25%;"><input class="form-control" v-model="currentRow.containerStuffingCharge" name="modal_containerStuffingCharge"></td>
                          <td style="text-align: center; width: 25%;"><input class="form-control" v-model="currentRow.logisticsHitCharge" name="modal_logisticsHitCharge"></td>
                          <td style="text-align: center; width: 25%;"><input class="form-control" v-model="currentRow.serviceCharge" name="modal_serviceCharge"></td>
                          <td style="text-align: center; width: 25%;"><input class="form-control" v-model="currentRow.otherFee" name="modal_otherFee"></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">备注</label>
                  <div class="col-sm-10">
                    <textarea rows="3" class="form-control" v-model="currentRow.remark" name="modal_remark"></textarea>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal" v-on:click="clear">关闭</button>
            <button type="button" class="btn btn-primary" v-on:click="modify">保存</button>
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
var selections = []
let currentRow
let currentRowIndex
let containerCountYardNum // showdetail用 堆场数量发番

function modalClean (obj) {
  obj.currentRow = {}
  $('#rowEditModal').bootstrapValidator('resetForm', true)
  $('#containerCountYard_table tbody tr').remove()
}

export default {
  data: function () {
    return {
      pagePara: '',
      searchDate: common.DateFormat(new Date(), 'yyyy-MM-dd'),
      currentRow: {}
    }
  },
  name: 'putBoxFinallyControl',
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
      // console.log(_self.searchDate)
      _self.$http.post('/api/putbox/putBoxFinallyControl?method=search', { 'searchDate': _self.searchDate }).then((response) => {
        var retdata = response.json()['data']
        $('#table').bootstrapTable('load', {
          data: retdata
        })
        $('.bs-checkbox').css({ 'text-align': 'center', 'vertical-align': 'middle' })
        _self.$compile(_self.$el)

        $('[data-toggle="popover"]').each(function () {
          $(this).popover()
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
        columns:
        [
          {
            align: 'center',
            valign: 'middle',
            field: 'state',
            checkbox: true
          },
          common.BTRowFormatWithFormatter('carManagerID', '用箱人', carManagerFormater),
          common.BTRowFormatWithFormatter('putterID', '放箱人', putterFormater),
          common.BTRowFormatWithFormatter('requirment', '要求', common.remarkFormatter),
          common.BTRowFormatWithFormatter('status', '状态', statusFormatter),
          common.BTRowFormat('billLodingNo', '关单号'),
          common.BTRowFormatWithFormatter('carrierID', '承运人', carrierFormater),
          common.BTRowFormat('shipv', '船信息'),
          common.BTRowFormat('containerInfo', '箱信息'),
          common.BTRowFormatWithFormatter('yardID', '堆场', yardIdFormater),
          common.BTRowFormat('transportationHub', '中转港'),
          common.BTRowFormatWithFormatter('bookingConfirmStatus', '预配状态', bookingConfirmStatusFormater),
          common.BTRowFormat('containerStuffingCharge', '提箱费'),
          common.BTRowFormat('logisticsHitCharge', '打单费'),
          common.BTRowFormat('serviceCharge', '服务费'),
          common.BTRowFormat('otherFee', '其它'),
          common.BTRowFormatWithFormatter('remark', '备注', common.remarkFormatter),
          {
            field: 'act',
            formatter: operateFormatter,
            align: 'center',
            valign: 'middle'
          },
          {
            field: 'trunkListID',
            title: '申请编号',
            align: 'center',
            valign: 'middle',
            visible: false
          },
          {
            field: 'modifytime',
            title: '末次更新日期',
            align: 'center',
            valign: 'middle',
            visible: false
          }
        ],
        idField: 'trunkListID',
        uniqueId: 'trunkListID',
        toolbar: '#toolbar',
        showRefresh: true,
        showColumns: true,
        clickToSelect: true,
        striped: true,
        locale: 'zh-CN',
        onRefresh: function () {
          getData()
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)

      $('#table').on('check.bs.table uncheck.bs.table ' + 'check-all.bs.table uncheck-all.bs.table', function () {
        $('#match').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
        $('#shutout').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
        $('#chargeback').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
      })
    }

    function yardIdFormater (value, row, index) {
      var yardName
      if (value) {
        var yard = $.parseJSON(value.replace(new RegExp('\'', 'gm'), '"'))
        if (yard.length > 1) {
          yardName = '多个堆场'
        } else {
          $(_self.pagePara['containerYard']).each(function () {
            if (this.userID === yard[0].containerYard) {
              yardName = this.name
              return false
            }
          })
        }
      }
      return yardName
    }

    function bookingConfirmStatusFormater (value, row, index) {
      var bookingConfirmClass = ''
      if (row.sameFlag === '1') {
        bookingConfirmClass = '<span class="label label-success">&nbsp;&nbsp;&nbsp;</span>'
      } else {
        bookingConfirmClass = '<span class="label label-warning">&nbsp;&nbsp;&nbsp;</span>'
      }

      var carrierBName, carrierName
      $(_self.pagePara['carrierInfo']).each(function () {
        if (this.id === row.carrierID) {
          carrierName = this.text
          return false
        }
      })
      if (row.carrierIDB) {
        $(_self.pagePara['carrierInfo']).each(function () {
          if (this.id === row.carrierIDB) {
            carrierBName = this.text
            return false
          }
        })
      } else {
        carrierBName = carrierName
      }

      return [
        '<a tabindex="putter' + index + '" role="button" data-toggle="popover" data-trigger="hover" data-placement="right" data-html="true" data-content="' +
        '<div class=&quot;table-responsive&quot;>' +
          '<table class=&quot;table table-bordered table-striped responsive-utilities&quot;>' +
            '<thead>' +
              '<tr>' +
                '<th style=&quot;text-align: center; vertical-align: middle; width:30%;&quot;></th>' +
                '<th style=&quot;text-align: center; vertical-align: middle; &quot;width:35%;>申请信息</th>' +
                '<th style=&quot;text-align: center; vertical-align: middle; &quot;width:35%;>预配信息</th>' +
              '</tr>' +
            '</thead>' +
            '<tbody>' +
              '<tr>' +
                '<th>船代</th>' +
                '<td>' + carrierBName + '</td>' +
                '<td>' + carrierName + '</td>' +
              '</tr>' +
              '<tr>' +
                '<th>船名/航次</th>' +
                '<td>' + row.shipv + '</td>' +
                '<td>' + row.shipvWeb + '</td>' +
              '</tr>' +
              '<tr>' +
                '<th>中转港</th>' +
                '<td>' + row.transportationHub + '</td>' +
                '<td>' + row.transportationHubWeb + '</td>' +
              '</tr>' +
              '<tr>' +
                '<th>箱型箱量</th>' +
                '<td>' + row.containerInfo + '</td>' +
                '<td>' + row.containerInfoWeb + '</td>' +
              '</tr>' +
            '</tbody>' +
          '</table>' +
        '</div>">' + bookingConfirmClass + '</a>'
      ].join('')
    }

    function statusFormatter (value, row, index) {
      var rtnClass = ''
      $(_self.pagePara['statusInfo']).each(function () {
        if (this.id === value) {
          rtnClass = '<span class="label ' + this.style + '">' + this.text + '</span>'
          return false
        }
      })
      return rtnClass
    }

    function operateFormatter (value, row, index) {
      var updateRowId = row.trunkListID
      return [
        '<a class="update" v-on:click="showdetail(\'' + updateRowId + '\')" title="修改">',
        '<i class="glyphicon glyphicon-pencil"></i>',
        '</a>'
      ].join('')
    }

    function carrierFormater (value, row, index) {
      var carrierName = ''
      $(_self.pagePara['carrierInfo']).each(function () {
        if (this.id === value) {
          carrierName = this.text
          return false
        }
      })
      return carrierName
    }

    function carManagerFormater (value, row, index) {
      return [
        '<a tabindex="carManager' + index + '" role="button" data-toggle="popover" data-trigger="hover" data-placement="right" data-html="true" data-content="' +
        '<div class=&quot;box&quot;>' +
          '<div class=&quot;box-body&quot;>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>联系人:</label>' +
              '<div class=&quot;&quot;><span>' + row.carManagerInfo.contact + '</span></div>' +
            '</div>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>手机号:</label>' +
              '<div class=&quot;&quot;><span>' + row.carManagerInfo.mobile + '</span></div>' +
            '</div>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>传真:</label>' +
              '<div class=&quot;&quot;><span>' + row.carManagerInfo.fax + '</span></div>' +
            '</div>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>地址:</label>' +
              '<div class=&quot;&quot;><span>' + row.carManagerInfo.address + '</span></div>' +
            '</div>' +
          '</div>' +
        '</div>">' + row.carManagerInfo.name + '</a>'
      ].join('')
    }

    function putterFormater (value, row, index) {
      var putterRow
      if (value === '') {
        return '<div style="color:#D12E2E">未分配</div>'
      }
      for (let i = 0; i < _self.pagePara['putterInfo'].length; i++) {
        if (_self.pagePara['putterInfo'][i].userID === value) {
          putterRow = _self.pagePara['putterInfo'][i]
          break
        }
      }
      return [
        '<a tabindex="putter' + index + '" role="button" data-toggle="popover" data-trigger="hover" data-placement="right" data-html="true" data-content="' +
        '<div class=&quot;box&quot;>' +
          '<div class=&quot;box-body&quot;>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>联系人:</label>' +
              '<div class=&quot;&quot;><span>' + putterRow.name + '</span></div>' +
            '</div>' +
            '<div class=&quot;form-group&quot;>' +
              '<label class=&quot;control-label&quot;>手机号:</label>' +
              '<div class=&quot;&quot;><span>' + putterRow.mobile + '</span></div>' +
            '</div>' +
          '</div>' +
        '</div>">' + putterRow.name + '</a>'
      ].join('')
    }

    function containerTypeFormatter (value, row, index) {
      var containerTypeValue = ''
      $(_self.pagePara['containerTypeInfo']).each(function () {
        if (this.code === value) {
          containerTypeValue = this.value
          return false
        }
      })
      return containerTypeValue
    }

    function containerSizeFormatter (value, row, index) {
      var containerSizeValue = ''
      $(_self.pagePara['containerSizeInfo']).each(function () {
        if (this.code === value) {
          containerSizeValue = this.value
          return false
        }
      })
      return containerSizeValue
    }

    function getIdSelections () {
      return $.map($('#table').bootstrapTable('getSelections'), function (row) {
        return row.trunkListID
      })
    }

    function actIconFormatter (value, row, index) {
      if (index > 0) {
        return [
          '<a class="add" v-on:click="delete(\'' + index + '\')" title="删除">',
          '<i class="glyphicon glyphicon-minus"></i>',
          '</a>'
        ].join('')
      } else {
        return [
          '<a class="delete" v-on:click="add()" title="增加">',
          '<i class="glyphicon glyphicon-plus"></i>',
          '</a>'
        ].join('')
      }
    }

    function yardFormatter (value, row, index) {
      var yardName
      $(_self.pagePara['containerYard']).each(function () {
        if (this.userID === value) {
          yardName = this.name
          return false
        }
      })
      return yardName
    }

    function initValidators () {
      $('#rowEditModal').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
          valid: 'glyphicon glyphicon-ok',
          invalid: 'glyphicon glyphicon-remove',
          validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
          modal_EDIExportShipID: common.BVNotEmput('请选择船只'),
          modal_shipName: common.BVNotEmput('船名不能为空'),
          modal_voyageNo: common.BVNotEmput('航次不能为空'),
          modal_containerSize: common.BVNotEmput('请选择尺寸'),
          modal_containerType: common.BVNotEmput('请选择箱型'),
          modal_containerCount: {
            validators: {
              notEmpty: {
                message: '请输入数量'
              },
              integer: {
                message: '请输入正确数量'
              }
            }
          }
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/putBoxFinallyControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = retData
        common.initSelect2($('#modal_putter'), retData['putterInfo'])
        common.initSelect2($('#modal_carrier'), retData['carrierInfo'])
        common.initSelect2($('#modal_EDIExportShipID'), retData['shipInfo'])
        $('#modal_EDIExportShipID').on('change', function () {
          if ($('#modal_EDIExportShipID').val()) {
            var shipId = $('#modal_EDIExportShipID').val()[0]

            $('#modal_transitPortId').val(null).trigger('change')
            $('#modal_transitPortId').html('')
            $(_self.pagePara['shipInfo']).each(function () {
              if (this.id === parseInt(shipId)) {
                common.initSelect2($('#modal_transitPortId'), this.transitPort)
                return false
              }
            })
          } else {
            $('#modal_transitPortId').val(null).trigger('change')
            $('#modal_transitPortId').html('')
          }
        })
        common.initSelect2($('#modal_containerType'), retData['containerTypeInfo'])
        common.initSelect2($('#modal_containerSize'), retData['containerSizeInfo'])
        console.log('init success')
      }, (response) => {
        console.log('init error')
        common.dealErrorCommon(_self, response)
      })
    }

    function modifyStatus (ids, method) {
      _self.$http.post('/api/putbox/putBoxFinallyControl?method=' + method, { 'ids': ids }).then((response) => {
        var retData = response.json()['data']
        $(retData).each(function () {
          $('#table').bootstrapTable('updateByUniqueId', { id: this.trunkListID, row: this })
        })
        $('.bs-checkbox').css({ 'text-align': 'center', 'vertical-align': 'middle' })

        $('[data-toggle="popover"]').each(function () {
          $(this).popover()
        })
        _self.$compile(_self.$el)
      }, (response) => {
        console.log(method + ' error')
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      common.initControlSize()
      initPage()
      initTable()
      common.changeTableClass($('#table'))
      getData()
      initValidators()
      $('#searchDate').datepicker({
        language: 'zh-CN',
        autoclose: true,
        todayHighlight: true,
        format: 'yyyy-mm-dd'
      }).on('changeDate', function (e) {
        var dateTime = common.DateFormat(e.date, 'yyyy-MM-dd')
        _self.searchDate = dateTime
        $('#table').bootstrapTable('refresh')
      })
      // 对单
      $('#match').click(function () {
        var rows = $('#table').bootstrapTable('getSelections')
        var ids = []
        $(rows).each(function () {
          if (this.status === '3') {
            ids.push(this.trunkListID)
          } else {
            common.dealWarningCommon('只有已放箱状态能够对单')
            return false
          }
        })
        if (ids.length === rows.length) {
          modifyStatus(ids, 'match')
        }
      })
      // 退关
      $('#shutout').click(function () {
        var rows = $('#table').bootstrapTable('getSelections')
        var ids = []
        $(rows).each(function () {
          if (this.status === '3' || this.status === '4') {
            ids.push(this.trunkListID)
          } else {
            common.dealWarningCommon('只有已放箱或者已对单状态能够退关!')
            return false
          }
        })
        if (ids.length === rows.length) {
          modifyStatus(ids, 'shutout')
        }
      })
      // 退单
      $('#chargeback').click(function () {
        var rows = $('#table').bootstrapTable('getSelections')
        var ids = []
        $(rows).each(function () {
          if (this.status === '3' || this.status === '4') {
            ids.push(this.trunkListID)
          } else {
            common.dealWarningCommon('只有已放箱或者已对单状态能够退单!')
            return false
          }
        })
        if (ids.length === rows.length) {
          modifyStatus(ids, 'chargeback')
        }
      })
    })
  },
  methods: {
    showdetail: function (trunkListID) {
      var _self = this
      containerCountYardNum = 0

      var row = $('#table').bootstrapTable('getRowByUniqueId', trunkListID)
      this.currentRow = $.extend(true, {}, row)
      currentRow = $.extend(true, {}, row)
      currentRowIndex = trunkListID
      $('#modal_putter').val(row.putterID).trigger('change')
      $('#modal_carrier').val(row.carrierID).trigger('change')
      if (row.EDIExportShipID === '') {
        $('#select-ship').removeClass('active')
        $('#input-ship').addClass('active')
        $('#modal_EDIExportShipID').val(null).trigger('change')
        $('#modal_transitPortId').val(null).trigger('change')
      } else {
        $('#select-ship').addClass('active')
        $('#input-ship').removeClass('active')
        $('#modal_EDIExportShipID').val(row.EDIExportShipID).trigger('change')
        $('#modal_transitPortId').val(row.transportationHub).trigger('change')
      }
      $('#modal_containerType').val(row.containerType).trigger('change')
      $('#modal_containerSize').val(row.containerSize).trigger('change')

      if (row.yardID) {
        var containerCountYard = $.parseJSON(row.yardID.replace(new RegExp('\'', 'gm'), '"'))
        $(containerCountYard).each(function () {
          containerCountYardNum += 1
          _self.addContainerCountYard()
        })
        $('#containerCountYard_table tbody tr').each(function (index) {
          $(this).find('td:eq(0) input').val(containerCountYard[index].containerCount)
          $(this).find('td:eq(1) select').val(containerCountYard[index].containerYard).trigger('change')
        })
      }
      _self.$compile(_self.$el)

      $('#rowEditModal').modal({ backdrop: 'static', keyboard: false })
    },
    addContainerCountYard: function () {
      var icons
      if (containerCountYardNum === 1) {
        icons = '<a class="form-control" v-on:click="addContainerCountYard2" title="增加"><i class="glyphicon glyphicon-plus"></i></a>'
      } else {
        icons = '<a class="form-control" v-on:click="deleteContainerCountYard(\'' + containerCountYardNum + '\')" title="删除"><i class="glyphicon glyphicon-minus"></i></a>'
      }
      var tr = '<tr data-index="' + containerCountYardNum + '">' +
                 '<td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="1" name="ContainerCount"></input></td>' +
                 '<td style="text-align: center; width: 60%;"><select id="yardselect' + containerCountYardNum + '" name="ContainerYardName" class="form-control select2" multiple></select></td>' +
                 '<td style="text-align: center; width: 10%;">' + icons + '</td>' +
               '</tr>'
      $('#containerCountYard_table tbody').append(tr)

      common.initSelect2($('#yardselect' + containerCountYardNum), this.pagePara['containerYard'])

      this.$compile(this.$el)
    },
    addContainerCountYard2: function () {
      containerCountYardNum += 1
      var icons = '<a class="form-control" v-on:click="deleteContainerCountYard(\'' + containerCountYardNum + '\')" title="删除"><i class="glyphicon glyphicon-minus"></i></a>'

      var tr = '<tr data-index="' + containerCountYardNum + '">' +
                 '<td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="1" value="1" name="ContainerCount"></input></td>' +
                 '<td style="text-align: center; width: 60%;"><select id="yardselect' + containerCountYardNum + '" name="ContainerYardName" class="form-control select2" multiple></select></td>' +
                 '<td style="text-align: center; width: 10%;">' + icons + '</td>' +
               '</tr>'
      $('#containerCountYard_table tbody').append(tr)

      common.initSelect2($('#yardselect' + containerCountYardNum), this.pagePara['containerYard'])

      this.$compile(this.$el)
    },
    deleteContainerCountYard: function (trIndex) {
      $('#containerCountYard_table tbody tr[data-index=\'' + trIndex + '\']').remove()
    },
    modify: function (event) {
      // 堆场验证
      var yzFlag = false
      $('select[name="ContainerYardName"]').each(function () {
        if (!$(this).val()) {
          yzFlag = true
          common.dealPromptCommon('堆场不能为空, 请确认!')
          return false
        }
      })
      if (yzFlag) {
        return
      }

      var containerCountModal = 0
      $('input[name="ContainerCount"]').each(function () {
        containerCountModal += parseInt($(this).val())
      })
      if (!(parseInt(this.currentRow['containerCount']) === containerCountModal)) {
        common.dealPromptCommon('箱量不匹配，请确认堆场输入数量与箱型箱量处数量是否一致！')
        return
      }

      this.currentRow['putterID'] = $('#modal_putter').val()[0]
      this.currentRow['carrierID'] = $('#modal_carrier').val()[0]
      if ($('#select-ship').hasClass('active')) {
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_EDIExportShipID', true)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_shipName', false)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_voyageNo', false)
        this.currentRow['EDIExportShipID'] = $('#modal_EDIExportShipID').val()[0]
        this.currentRow['transportationHub'] = $('#modal_transitPortId').val()[0]
      } else if ($('#input-ship').hasClass('active')) {
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_EDIExportShipID', false)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_shipName', true)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_voyageNo', true)
        this.currentRow['EDIExportShipID'] = ''
        this.currentRow['transportationHub'] = $('#modal_transitPort').val()
      }
      this.currentRow['containerSize'] = $('#modal_containerSize').val()[0]
      this.currentRow['containerType'] = $('#modal_containerType').val()[0]
      var yardId = []
      $('#containerCountYard_table tbody tr').each(function () {
        var containerCount = $(this).find('td input').val()
        var containerYard = $(this).find('td select').val()[0]
        yardId.push({ 'containerCount': containerCount, 'containerYard': containerYard })
      })
      this.currentRow['yardID'] = yardId

      if (common.getValidateResult($('#rowEditModal'))) {
        this.$http.post('/api/putbox/putBoxFinallyControl?method=modify', { 'old': currentRow, 'new': this.currentRow }).then((response) => {
          var row = response.json()['data']
          // this.currentRow = $.extend(true, {}, row)
          // currentRow = $.extend(true, {}, row)
          $('#table').bootstrapTable('updateByUniqueId', { id: this.currentRow.trunkListID, row: row })

          $('.bs-checkbox').css({ 'text-align': 'center', 'vertical-align': 'middle' })

          $('[data-toggle="popover"]').each(function () {
            $(this).popover()
          })
          this.$compile(this.$el)
          console.log('modify success')
          $('#rowEditModal').modal('hide')

          modalClean(this)
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(this, response)
        })
      }
    },
    delete: function (event) {
      this.$http.post('/api/putbox/putBoxFinallyControl?method=delete', currentRow).then((response) => {
        $('#table').bootstrapTable('remove', { field: 'userID', values: [currentRow.userID] })
        console.log('delete success')
      }, (response) => {
        console.log('delete error')
        common.dealErrorCommon(this, response)
      })
    },
    clear: function (event) {
      modalClean(this)
    }
  }
}
</script>
<style>
.popover {
  max-width: 400px;
}
.popover-content {
    padding: 9px 24px;
}
</style>

<template>
  <section class="content-header">
    <h1>
      用箱申请
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 用箱管理</a></li>
      <li class="active">用箱申请</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar">
            <div class="form-inline" role="form">
              <div class="form-group">
                <button id="apply" class="btn btn-block btn-primary">
                    <i class="glyphicon glyphicon-save"></i> 申请放箱
                </button>
              </div>
              <div class="form-group" style="display:none;">
                <button id="cancel" class="btn btn-danger" disabled>
                  <i class="glyphicon glyphicon-remove"></i> 取消放箱
                </button>
              </div>
              <div class="form-group">
                <input name="searchDate" v-model="searchDate" class="form-control" id="searchDate" placeholder="查询日期">
              </div>
            </div>
          </div>
          <table id="table"></table>
        </div>
      </div>
    </div>
  </section>
  <div class="modal" id="applyModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" v-on:click="clear"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="rowEditModalLabel"><i class="fa fa-pencil-square-o big-blue"></i>申请放箱</h4>
          </div>
          <div class="modal-body">
            <div id="scroll-desk">
              <div id="deskForm">
                <div class="hidden">{{ actGroup }}</div>
                <div class="hidden">{{ modifyTime }}</div>
                <div class="form-group">
                  <label>船代</label>
                  <select class="form-control select2" multiple style="width:100%" id="carrier" name="carrier">
                  </select>
                </div>
                <div class="nav-tabs-custom" style="cursor: move;">
                  <ul class="nav nav-tabs pull-right ui-sortable-handle">
                    <li class="active"><a href="#select-ship" data-toggle="tab" aria-expanded="true">选择</a></li>
                    <li class=""><a href="#input-ship" data-toggle="tab" aria-expanded="false">填充</a></li>
                    <li class="pull-left" style="line-height: 41px;font-weight: 700;"> 船名 / 航次</li>
                  </ul>
                  <div class="tab-content no-padding">
                    <!-- Morris chart - Sales -->
                    <div class="chart tab-pane active" id="select-ship" style="position: relative;">
                      <select class="select2" multiple style="width:100%" id="EDIExportShipID" name="EDIExportShipID">
                      </select>
                    </div>
                    <div class="chart tab-pane" id="input-ship" style="position: relative;">
                      <div class="form-group">
                        <label>船名</label>
                        <input type="text" class="form-control" v-model="shipName" name="shipName">
                      </div>
                      <div class="form-group">
                        <label>航次</label>
                        <input type="text" class="form-control" v-model="voyageNo" name="voyageNo">
                      </div>
                    </div>
                  </div>
                  <div>
                  </div>
                </div>
                <div class="form-group">
                  <label>提单号</label>
                  <input type="text" class="form-control" v-model="billLodingNo" name="billLodingNo">
                </div>
                <div class="form-group hidden" id="putBoxNoDiv">
                  <label>放箱号</label>
                  <input type="text" class="form-control" v-model="putBoxNo" name="putBoxNo">
                </div>
                <div class="form-group">
                  <label>提箱要求</label>
                  <textarea rows="3" class="form-control" v-model="requirment" name="requirment"></textarea>
                </div>
                <div class="form-group">
                  <table id="container_Table" class="table table-no-bordered" style="margin-bottom:0">
                    <thead>
                      <tr>
                        <th style="text-align: center; width: 30%; "><div class="th-inner ">尺寸</div><div class="fht-cell"></div></th>
                        <th style="text-align: center; width: 30%; "><div class="th-inner ">箱型</div><div class="fht-cell"></div></th>
                        <th style="text-align: center; width: 30%; "><div class="th-inner ">数量</div><div class="fht-cell"></div></th>
                        <th style="text-align: center; width: 10%; "><div class="th-inner "></div><div class="fht-cell"></div></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr data-index="0">
                        <td style="text-align: center; width: 30%;"><select class="form-control select2" id="containerSize" name="containerSize"></select></td>
                        <td style="text-align: center; width: 30%;"><select class="form-control select2" id="containerType" name="containerType"></select></td>
                        <td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="1" value="1" id="containerCount"></td>
                        <td style="text-align: center; width: 10%;"><a class="form-control" style="padding-right:12px;" v-on:click="addContainerInfo" title="增加"><i class="glyphicon glyphicon-plus"></i></a></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" v-on:click="add"><i class="fa fa-fw fa-save"></i>提交</button>
          <button type="button" class="btn btn-success" v-on:click="clear"><i class="fa fa-fw fa-trash"></i>清空</button>
        </div>
      </div>
    </div>
</div>
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
import moment from 'moment'
var common = require('commonFunc')
let containerInfoNum

function shipID2Name (obj, value) {
  for (let i = 0; i < obj.pagePara['shipInfo'].length; i++) {
    if (obj.pagePara['shipInfo'][i].id === parseInt(value)) {
      return obj.pagePara['shipInfo'][i].text
    }
  }
  return ''
}
function desk2Json (obj) {
  var containerData = []
  $('#container_Table tbody tr').each(function () {
    var containerSimple = { 'containerSize': $(this).find('td:eq(0) select').val(),
                            'containerType': $(this).find('td:eq(1) select').val(),
                            'containerCount': $(this).find('td:eq(2) input').val() }
    containerData.push(containerSimple)
  })
  var containerDisplay = ''
  $(containerData).each(function () {
    containerDisplay += containerSizeFormatter(obj, this.containerSize) + containerTypeFormatter(obj, this.containerType) + ' X ' + this.containerCount + ','
  })
  if ($('#select-ship').hasClass('active')) {
    return {
      'carrier': $('#carrier').val()[0],
      'EDIExportShipID': $('#EDIExportShipID').val()[0],
      'shipv': shipID2Name(obj, $('#EDIExportShipID').val()[0]),
      'shipName': '',
      'voyageNo': '',
      'billLodingNo': obj.billLodingNo,
      'requirment': obj.requirment,
      'putBoxNo': obj.putBoxNo,
      'status': '1',
      'containerData': containerData,
      'containerDisplay': containerDisplay.substring(0, containerDisplay.length - 1)
    }
  } else if ($('#input-ship').hasClass('acrow = SysUtil.schema2Json(tkList)tive')) {
    return {
      'carrier': $('#carrier').val()[0],
      'EDIExportShipID': '',
      'shipv': obj.shipName + ' / ' + obj.voyageNo,
      'shipName': obj.shipName,
      'voyageNo': obj.voyageNo,
      'billLodingNo': obj.billLodingNo,
      'requirment': obj.requirment,
      'putBoxNo': obj.putBoxNo,
      'status': '1',
      'containerData': containerData,
      'containerDisplay': containerDisplay.substring(0, containerDisplay.length - 1)
    }
  }
}
function deskClean (obj) {
  $('#carrier').val(null).trigger('change')
  $('#EDIExportShipID').val(null).trigger('change')
  obj.shipName = ''
  obj.voyageNo = ''
  obj.billLodingNo = ''
  obj.requirment = ''
  obj.putBoxNo = ''
  obj.modifyTime = ''
  $('#containerSize').val(null).trigger('change')
  $('#containerType').val(null).trigger('change')
  $('input[id=containerCount]').val('1')
  $('#container_Table tbody tr[data-index!=0]').remove()
  $('#deskForm').data('bootstrapValidator').updateStatus('billLodingNo', 'NOT_VALIDATED')
  $('#deskForm').data('bootstrapValidator').updateStatus('carrier', 'NOT_VALIDATED')
  $('#deskForm').data('bootstrapValidator').updateStatus('EDIExportShipID', 'NOT_VALIDATED')
  containerInfoNum = 0
}
function containerTypeFormatter (obj, value) {
  for (let i = 0; i < obj.pagePara['containerTypeInfo'].length; i++) {
    if (obj.pagePara['containerTypeInfo'][i].id === value) {
      return obj.pagePara['containerTypeInfo'][i].text
    }
  }
  return ''
}
function containerSizeFormatter (obj, value) {
  for (let i = 0; i < obj.pagePara['containerSizeInfo'].length; i++) {
    if (obj.pagePara['containerSizeInfo'][i].id === value) {
      return obj.pagePara['containerSizeInfo'][i].text
    }
  }
  return ''
}
export default {
  data: function () {
    return {
      pagePara: '',
      searchDate: moment().format('YYYY-MM-DD'),
      carrierID: '',
      shipName: '',
      voyageNo: '',
      billLodingNo: '',
      requirment: '',
      putBoxNo: ''
    }
  },
  name: 'boxApplyControl',
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
    function getData () {
      _self.$http.post('/api/putbox/boxApplyControl?method=search', { 'searchDate': _self.searchDate }).then((response) => {
        var retData = response.json()['data']
        $('#table').bootstrapTable('load', {
          data: retData
        })
        $('[data-toggle="popover"]').each(function () {
          $(this).popover()
        })
      }, (response) => {
        // error callback
        console.log('get data error')
        common.dealErrorCommon(_self, response)
      })
    }

    function carrierFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['carrierInfo'].length; i++) {
        if (_self.pagePara['carrierInfo'][i].id === value) {
          return _self.pagePara['carrierInfo'][i].text
        }
      }
      return ''
    }
    function containerTypeFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['containerTypeInfo'].length; i++) {
        if (_self.pagePara['containerTypeInfo'][i].id === value) {
          return _self.pagePara['containerTypeInfo'][i].text
        }
      }
      return ''
    }
    function containerSizeFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['containerSizeInfo'].length; i++) {
        if (_self.pagePara['containerSizeInfo'][i].id === value) {
          return _self.pagePara['containerSizeInfo'][i].text
        }
      }
      return ''
    }

    function statusFormatter (value, row) {
      for (let i = 0; i < _self.pagePara['statusInfo'].length; i++) {
        if (_self.pagePara['statusInfo'][i].id === value) {
          return '<span class="label ' + _self.pagePara['statusInfo'][i].style + '">' + _self.pagePara['statusInfo'][i].text + '</span>'
        }
      }
      return ''
    }

    function initTable () {
      $('#table').bootstrapTable({
        height: common.getTableHeight(),
        columns: [{
          field: 'state',
          align: 'center',
          valign: 'middle',
          checkbox: true
        }, {
          field: 'trunkListID',
          align: 'center',
          valign: 'middle',
          title: '申请编号',
          visible: false
        },
        common.BTRowFormat('maketime', '申请时间'),
        common.BTRowFormatWithFormatter('carrierID', '船代', carrierFormatter),
        common.BTRowFormat('shipv', '船名 / 航次'),
        common.BTRowFormat('billLodingNo', '关单号'),
        common.BTRowFormat('containerInfo', '箱信息'),
        common.BTRowFormat('containerStuffingCharge', '提箱费'),
        common.BTRowFormat('logisticsHitCharge', '打单费'),
        common.BTRowFormat('serviceCharge', '服务费'),
        common.BTRowFormat('otherFee', '其他费用'),
        common.BTRowFormatWithFormatter('requirment', '要求', common.remarkFormatter),
        common.BTRowFormatWithFormatter('remark', '备注', common.remarkFormatter),
        common.BTRowFormatWithFormatter('status', '状态', statusFormatter), {
          field: 'putBoxNo',
          align: 'center',
          valign: 'middle',
          title: '放箱号',
          visible: false
        }, {
          field: 'modifytime',
          align: 'center',
          valign: 'middle',
          title: '末次更新日期',
          visible: false
        }
      ],
        idField: 'trunkListID',
        toolbar: '#toolbar',
        search: true,
        showRefresh: true,
        showColumns: true,
        striped: true,
        showFooter: false,
        locale: 'zh-CN',
        onRefresh: function () {
          getData()
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)
      $('#table').on('check.bs.table uncheck.bs.table check-all.bs.table uncheck-all.bs.table', function () {
        $('#cancel').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
      })
    }

    function initValidators () {
      $('#deskForm').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
          valid: 'glyphicon glyphicon-ok',
          invalid: 'glyphicon glyphicon-remove',
          validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
          carrier: {
            validators: {
              notEmpty: {
                message: '请选择承运人'
              }
            }
          },
          shipName: {
            validators: {
              notEmpty: {
                message: '请输入船名'
              }
            }
          },
          voyageNo: {
            validators: {
              notEmpty: {
                message: '请输入航次'
              }
            }
          },
          billLodingNo: {
            validators: {
              notEmpty: {
                message: '请输入提单号'
              }
            }
          }
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/boxApplyControl?method=init', {}).then((response) => {
        var retData = response.json()['data']
        _self.pagePara = retData
        common.initSelect2($('#carrier'), retData['carrierInfo'])
        common.initSelect2($('#EDIExportShipID'), retData['shipInfo'])
        common.initSelect2Single($('#containerSize'), retData['containerSizeInfo'])
        common.initSelect2Single($('#containerType'), retData['containerTypeInfo'])
        console.log('init success')
      }, (response) => {
        common.dealErrorCommon(_self, response)
      })
    }

    $(function () {
      common.initControlSize()
      initPage()
      initTable()
      common.changeTableClass($('#table'))
      common.initDatepicker($('#useContainerDate'))
      getData()
      initValidators()
      $('#apply').click(function () {
        containerInfoNum = 0
        $('#applyModal').modal('show')
      })

      $('#cancel').click(function () {
        var rows = $('#table').bootstrapTable('getSelections')
        var ids = []
        for (let i = 0; i < rows.length; i++) {
          if (rows[i].status !== '1') {
            common.dealWarningCommon('只有已提交状态能够取消')
            break
          } else {
            ids.push(rows[i].trunkListID)
          }
        }
        if (ids.length === rows.length) {
          _self.$http.post('/api/putbox/boxApplyControl?method=delete', { 'cancelids': ids }).then((response) => {
            $('#table').bootstrapTable('remove', {
              field: 'trunkListID',
              values: ids
            })
            $('[data-toggle="popover"]').each(function () {
              $(this).popover()
            })
            console.log('delete success')
          }, (response) => {
            console.log('delete error')
            common.dealErrorCommon(this, response)
          })
        }
      })

      $('#carrier').change(function () {
        if ($('#carrier option:selected').text().trim() === 'COSCO-中远') {
          if ($('#putBoxNoDiv').hasClass('hidden')) {
            $('#putBoxNoDiv').removeClass('hidden')
          }
        } else {
          if (!$('#putBoxNoDiv').hasClass('hidden')) {
            $('#putBoxNoDiv').addClass('hidden')
            _self.putBoxNo = ''
          }
        }
      })

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
    })
  },
  methods: {
    add: function (event) {
      var _self = this
      var yzFlag = false
      $('select[name="containerSize"]').each(function () {
        if (!$(this).val()) {
          yzFlag = true
          common.dealPromptCommon('尺寸不能为空, 请确认!')
          return false
        }
      })
      if (yzFlag) {
        return
      }
      $('select[name="containerType"]').each(function () {
        if (!$(this).val()) {
          yzFlag = true
          common.dealPromptCommon('箱型不能为空, 请确认!')
          return false
        }
      })
      if (yzFlag) {
        return
      }

      if (common.getValidateResult($('#deskForm'))) {
        var workRow = desk2Json(this)
        common.dealConfrimCommon('申请信息： 提单号:' + workRow.billLodingNo + ' 箱型箱量：' + workRow.containerDisplay, function () {
          _self.$http.post('/api/putbox/boxApplyControl?method=add', workRow).then((response) => {
            var retdata = response.json()['data']['serviceReData']
            for (let i = 0; i < retdata.length; i++) {
              $('#table').bootstrapTable('insertRow', { index: 0, row: retdata[i] })
            }
            $('[data-toggle="popover"]').each(function () {
              $(this).popover()
            })
            deskClean(_self)
          }, (response) => {
            console.log('add error')
            common.dealAlertCommon(this, response)
          })
        })
      }
    },
    clear: function (event) {
      deskClean(this)
      console.log('clear success')
    },
    addContainerInfo: function () {
      containerInfoNum += 1
      var icons = '<a class="form-control" style="padding-right:12px;" v-on:click="deleteContainerInfo(\'' + containerInfoNum + '\')" title="删除"><i class="glyphicon glyphicon-minus"></i></a>'

      var tr = '<tr data-index="' + containerInfoNum + '">' +
                 '<td style="text-align: center; width: 30%;"><select id="containerSize' + containerInfoNum + '" name="containerSize" class="form-control select2"></select></td>' +
                 '<td style="text-align: center; width: 30%;"><select id="containerType' + containerInfoNum + '" name="containerType" class="form-control select2"></select></td>' +
                 '<td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="1" value="1" name="containerCount"></td>' +
                 '<td style="text-align: center; width: 10%;">' + icons + '</td>' +
               '</tr>'
      $('#container_Table tbody').append(tr)

      common.initSelect2Single($('#containerSize' + containerInfoNum), this.pagePara['containerSizeInfo'])
      common.initSelect2Single($('#containerType' + containerInfoNum), this.pagePara['containerTypeInfo'])

      this.$compile(this.$el)
    },
    deleteContainerInfo: function (trIndex) {
      $('#container_Table tbody tr[data-index=\'' + trIndex + '\']').remove()
    }
  }
}
</script>
<style>
</style>

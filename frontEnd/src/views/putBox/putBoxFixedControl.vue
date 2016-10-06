<template>
  <section class="content-header">
    <h1>
      日放箱汇总
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">日放箱汇总</li>
    </ol>
  </section>
  <section class="content connectedSortable ui-sortable">
    <div class="col-lg-12">
      <div class="box box-info">
        <div class="box-body">
          <div id="toolbar" class="pull-right">
            <div class="form-inline" role="form">
              <div class="form-group">
                <button id="send" class="btn btn-primary" disabled>
                  <i class="fa fa-share"></i> 下发
                </button>
              </div>
              <div class="form-group">
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
                    <select class="form-control select2" multiple style="width:100%" id="modal_putter" name="modal_putter">
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
                    <div class="nav-tabs-custom" style="cursor: move;">
                      <ul class="nav nav-tabs pull-right ui-sortable-handle">
                        <li class="active"><a href="#select-ship" data-toggle="tab" aria-expanded="true">选择</a></li>
                        <li class=""><a href="#input-ship" data-toggle="tab" aria-expanded="false">填充</a></li>
                      </ul>
                      <div class="tab-content no-padding">
                        <!-- Morris chart - Sales -->
                        <div class="chart tab-pane active" id="select-ship" style="position: relative;">
                          <div class="col-sm-8" style="padding-left:0px">
                            <select class="select2 " multiple id="modal_EDIExportShipID" name="modal_EDIExportShipID"></select>
                          </div>
                          <div class="col-sm-4" style="padding-right:0px">
                            <select class="select2 " id="modal_transitPortId" name="modal_transitPortId"></select>
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
                    </div>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">箱型箱量</label>
                  <div class="col-sm-3">
                    <select class="form-control select2" id="modal_containerSize" name="modal_containerSize">
                    </select>
                  </div>
                  <div class="col-sm-3">
                    <select class="form-control select2" id="modal_containerType" name="modal_containerType">
                    </select>
                  </div>
                  <label for="code" class="col-sm-1 control-label">X</label>
                  <div class="col-sm-3">
                    <input class="form-control" type='number' min='1' v-model="currentRow.containerCount">
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
                        <tr data-index="0">
                          <td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="0" value="0" id="containerCount"></td>
                          <td style="text-align: center; width: 60%;"><select id="containerYardName0" class="form-control select2" multiple></select></td>
                          <td style="text-align: center; width: 10%;"><a class="form-control" style="padding-right:12px;" v-on:click="addContainerCountYard" title="增加"><i class="glyphicon glyphicon-plus"></i></a></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
                <div class="form-group">
                  <label for="code" class="col-sm-2 control-label">其他费用</label>
                  <div class="col-sm-10">
                    <input class="form-control" v-model="currentRow.otherFee" name="modal_otherFee">
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
  $('input[id=containerCount]').val('0')
  $('#containerYardName0').val(null).trigger('change')
  $('#container_Table tbody tr[data-index!=0]').remove()
  containerCountYardNum = 0
  $('#rowEditModal').bootstrapValidator('resetForm', true)
}

export default {
  data: function () {
    return {
      pagePara: '',
      searchDate: common.DateFormat(new Date(), 'yyyy-MM-dd'),
      currentRow: {}
    }
  },
  name: 'putBoxFixedControl',
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
      _self.$http.post('/api/putbox/putBoxFixedControl?method=search', { 'searchDate': _self.searchDate }).then((response) => {
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
      console.log(common.getTableHeight())
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
          common.BTRowFormatWithFormatter('remark', '备注', common.remarkFormatter),
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
          common.BTRowFormatWithFormatter('status', '状态', statusFormatter),
          {
            field: 'act',
            formatter: operateFormatter,
            align: 'center',
            valign: 'middle'
          }, {
            field: 'trunkListID',
            title: '申请编号',
            align: 'center',
            valign: 'middle',
            visible: false
          }, {
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
        search: true,
        showRefresh: true,
        showColumns: true,
        striped: true,
        clickToSelect: true,
        locale: 'zh-CN',
        onRefresh: function () {
          getData()
        },
        onAll: function () {
          $('[data-toggle="popover"]').each(function () {
            $(this).popover()
          })
          _self.$compile(_self.$el)
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)

      $('#table').on('check.bs.table uncheck.bs.table ' + 'check-all.bs.table uncheck-all.bs.table', function () {
        $('#send').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
        $('#remove').prop('disabled', !$('#table').bootstrapTable('getSelections').length)

        $('#back').prop('disabled', !$('#table').bootstrapTable('getSelections').length)
        // save your data, here just save the current page
        selections = getIdSelections()
        // push or splice the selections if you want to save all data selections
      })

      $('#remove').click(function () {
        var ids = getIdSelections()
        $('#table').bootstrapTable('remove', {
          field: 'trunkListID',
          values: ids
        })
        $('#remove').prop('disabled', true)
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
            if (this.userID === yard[0].yardId) {
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

    function initValidators () {
      $('#rowEditModal').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
          valid: 'glyphicon glyphicon-ok',
          invalid: 'glyphicon glyphicon-remove',
          validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
          modal_EDIExportShipID: {
            validators: {
              notEmpty: {
                message: '请选择船只'
              }
            }
          },
          modal_shipName: {
            validators: {
              notEmpty: {
                message: '船名不能为空'
              }
            }
          },
          modal_voyageNo: {
            validators: {
              notEmpty: {
                message: '航班号不能为空'
              }
            }
          },
          modal_containerSize: {
            validators: {
              notEmpty: {
                message: '请选择尺寸'
              }
            }
          },
          modal_containerType: {
            validators: {
              notEmpty: {
                message: '请选择箱型'
              }
            }
          // },
          // modal_containerCount: {
          //   validators: {
          //     notEmpty: {
          //       message: '请输入数量'
          //     },
          //     integer: {
          //       message: '请输入正确数量'
          //     }
          //   }
          }
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/putBoxFixedControl?method=init', {}).then((response) => {
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
                common.initSelect2Single($('#modal_transitPortId'), this.transitPort)
                return false
              }
            })
          } else {
            $('#modal_transitPortId').val(null).trigger('change')
            $('#modal_transitPortId').html('')
          }
        })
        common.initSelect2Single($('#modal_containerType'), retData['containerTypeInfo'])
        common.initSelect2Single($('#modal_containerSize'), retData['containerSizeInfo'])
        common.initSelect2($('#containerYardName0'), retData['containerYard'])
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
      $('#send').click(function () {
        var rows = $('#table').bootstrapTable('getSelections')
        var ids = []
        for (let i = 0; i < rows.length; i++) {
          if (rows[i].status !== '1') {
            common.dealWarningCommon('只有已提交状态能够下发')
            break
          } else {
            ids.push(rows[i].trunkListID)
          }
        }
        if (ids.length === rows.length) {
          _self.$http.post('/api/putbox/putBoxFixedControl?method=send', { 'ids': ids }).then((response) => {
            var retData = response.json()['data']
            for (let i = 0; i < retData.length; i++) {
              $('#table').bootstrapTable('updateByUniqueId', { id: retData[i].trunkListID, row: retData[i] })
            }
          }, (response) => {
            console.log('send error')
            common.dealErrorCommon(_self, response)
          })
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
    modify: function (event) {
      // 堆场验证
      var yzFlag = false
      $('#containerCountYard_table tbody tr').each(function () {
        var count = $(this).find('td:eq(0) input').val()
        var yardName = $(this).find('td:eq(1) select').val()
        var yardFlag = false
        if (yardName) {
          yardFlag = true
        }
        if (parseInt(count) > 0 && !yardFlag) {
          yzFlag = true
          common.dealPromptCommon('堆场不能为空, 请确认!')
          return false
        } else if (yardFlag && parseInt(count) === 0) {
          yzFlag = true
          common.dealPromptCommon('堆场存在的情况下,数量不能为0, 请确认!')
          return false
        }
      })
      if (yzFlag) {
        return
      }

      var containerCountModal = 0
      $('#containerCountYard_table tbody tr').each(function () {
        containerCountModal += parseInt($(this).find('td:eq(0) input').val())
      })
      if (containerCountModal > 0 && !(parseInt(this.currentRow['containerCount']) === containerCountModal)) {
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
        if ($('#modal_transitPortId').val()) {
          this.currentRow['transportationHub'] = $('#modal_transitPortId').val()
        }
      } else if ($('#input-ship').hasClass('active')) {
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_EDIExportShipID', false)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_shipName', true)
        $('#rowEditModal').data('bootstrapValidator').enableFieldValidators('modal_voyageNo', true)
        this.currentRow['EDIExportShipID'] = ''
        this.currentRow['transportationHub'] = $('#modal_transitPort').val()
      }

      this.currentRow['containerSize'] = $('#modal_containerSize').val()
      this.currentRow['containerType'] = $('#modal_containerType').val()

      var yardId = []
      $('#containerCountYard_table tbody tr').each(function () {
        var containerCount = $(this).find('td input').val()
        if (parseInt(containerCount) > 0) {
          var containerYard = $(this).find('td select').val()[0]
          yardId.push({ 'containerCount': containerCount, 'containerYard': containerYard })
        }
      })
      this.currentRow['yardID'] = yardId

      if (common.getValidateResult($('#rowEditModal'))) {
        this.$http.post('/api/putbox/putBoxFixedControl?method=modify', { 'old': currentRow, 'new': this.currentRow }).then((response) => {
          var row = response.json()['data']
          $('#table').bootstrapTable('updateByUniqueId', { id: this.currentRow.trunkListID, row: row })
          console.log('modify success')
          $('#rowEditModal').modal('hide')
        }, (response) => {
          console.log('modify error')
          common.dealErrorCommon(this, response)
        })
      }
    },
    clear: function (event) {
      modalClean(this)
    },
    addContainerCountYard: function () {
      containerCountYardNum += 1
      var icons = '<a class="form-control" style="padding-right:12px;" v-on:click="deleteContainerCountYard(\'' + containerCountYardNum + '\')" title="删除"><i class="glyphicon glyphicon-minus"></i></a>'

      var tr = '<tr data-index="' + containerCountYardNum + '">' +
                 '<td style="text-align: center; width: 30%;"><input class="form-control" type="number" min="1" value="1"></input></td>' +
                 '<td style="text-align: center; width: 60%;"><select id="containerYardName' + containerCountYardNum + '" class="form-control select2" multiple></select></td>' +
                 '<td style="text-align: center; width: 10%;">' + icons + '</td>' +
               '</tr>'
      $('#containerCountYard_table tbody').append(tr)

      common.initSelect2($('#containerYardName' + containerCountYardNum), this.pagePara['containerYard'])

      this.$compile(this.$el)
    },
    deleteContainerCountYard: function (trIndex) {
      $('#containerCountYard_table tbody tr[data-index=\'' + trIndex + '\']').remove()
    }
  }
}
</script>
<style>
.popover {
  max-width: 400px;
}
</style>

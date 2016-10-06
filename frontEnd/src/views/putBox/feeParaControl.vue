<template>
  <section class="content-header">
    <h1>
      费用参数维护
      <small>操作面板</small>
    </h1>
    <ol class="breadcrumb">
      <li><a href="#"><i class="fa fa-dashboard"></i> 放箱管理</a></li>
      <li class="active">费用参数维护</li>
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
                <div id="deskForm">
                  <label>服务费</label>
                  <input class="form-control" v-model="tableData.serviceCharge" type="text" name="serviceCharge">
                </div>
              </div>
              <div class="form-group">
                <button id="commit" class="btn btn-success" v-on:click="modify" disabled>
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
  <!-- LHModal -->
  <div class="modal fade" id="LHModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>打单费维护</h4>
        </div>
        <div class="modal-body">
          <div class="form-horizontal">
            <div class="box-body">
              <table id="LHtable"></table>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" data-dismiss="modal">确定</button>
        </div>
      </div>
    </div>
  </div>
  <!-- LHModal -->
  <!-- CSEdit -->
  <div class="modal fade" id="CSModal" tabindex="-1" role="dialog" aria-labelledby="rowEditModalLabel">
    <div class="modal-dialog" role="document" style="width: 800px;">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title"><i class="fa fa-pencil-square-o big-blue"></i>放箱费维护</h4>
        </div>
        <div class="modal-body">
          <div class="form-horizontal">
            <div class="box-body">
              <table id="CStable" data-detail-view="true"></table>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" data-dismiss="modal">确定</button>
        </div>
      </div>
    </div>
  </div>
  <!-- CSModal -->
</template>
<script>
import $ from 'jquery'
import vuexStore from 'vuexStore'
import { setError } from 'vuexActions'
var common = require('commonFunc')
let currentCarrierID
let currentRow
let currentRowIndex

function modalClean (obj) {
  obj.currentRow = {}
  $('#rowEditModal').bootstrapValidator('resetForm', true)
}

function getData (obj) {
  // console.log(_self.searchDate)
  var carManagerID = $('#carManagerID').val()
  if (!carManagerID) { return }
  obj.$http.post('/api/putbox/feeParaControl?method=search', { 'carManagerID': carManagerID }).then((response) => {
    var retData = response.json()['data']
    obj.tableData = $.extend(true, {}, retData)
    $('#table').bootstrapTable('load', {
      data: retData.carriers
    })
  }, (response) => {
    // error callback
    common.dealErrorCommon(obj, response)
  })
}

export default {
  data: function () {
    return {
      pagePara: '',
      tableData: ''
    }
  },
  name: 'feeParaControl',
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
    function initTable () {
      $('#table').bootstrapTable({
        height: common.getTableHeight(),
        columns:
        [
          common.BTRowFormatWithFormatter('carrierID', '承运人', carrierFormater),
          common.BTRowFormatWithFormatter('carrierID', '打单费', logisticsHitFormater),
          common.BTRowFormatWithFormatter('carrierID', '提箱费', containerStuffingFormater)
        ],
        toolbar: '#toolbar',
        search: true,
        showRefresh: true,
        // showToggle: true,
        striped: true,
        showFooter: false,
        pageList: [10, 25, 50, 100, 'ALL'],
        locale: 'zh-CN',
        onRefresh: function () {
          getData(_self)
        },
        onAll: function () {
          _self.$compile(_self.$el)
        }
      })
      setTimeout(function () {
        $('#table').bootstrapTable('resetView')
      }, 200)
    }

    function carrierFormater (value, row) {
      for (let i = 0; i < _self.pagePara['carrierInfo'].length; i++) {
        if (_self.pagePara['carrierInfo'][i].id === value) {
          return _self.pagePara['carrierInfo'][i].text
        }
      }
      return ''
    }

    function logisticsHitFormater (value, row) {
      return [
        '<a class="update" v-on:click="showLH(\'' + value + '\')" title="修改">',
        '<i class="glyphicon glyphicon-pencil"></i>',
        '</a>'
      ].join('')
    }

    function containerStuffingFormater (value, row) {
      return [
        '<a class="update" v-on:click="showCS(\'' + value + '\')" title="修改">',
        '<i class="glyphicon glyphicon-pencil"></i>',
        '</a>'
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

    function initValidators () {
      $('#deskForm').bootstrapValidator({
        fields: {
          serviceCharge: common.BVMoney
        }
      })
    }

    function initPage () {
      _self.$http.post('/api/putbox/feeParaControl?method=init', {}).then((response) => {
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
        $('#commit').prop('disabled', false)
      })
    })
  },
  methods: {
    showLH: function (carrierID) {
      var _self = this
      function initLHTable () {
        $('#LHtable').bootstrapTable({
          height: 200,
          columns:
          [
            {
              field: 'type',
              title: '类型',
              formatter: LHTypeFormater,
              align: 'center',
              valign: 'middle'
            },
            {
              field: 'money',
              title: '提箱费',
              editable: {
                type: 'text',
                title: 'Item Price',
                validate: function (value) {
                  value = $.trim(value)
                  if (!value) {
                    return '请输入费用金额'
                  }
                  if (!/^\d+\.\d{2}/.test(value)) {
                    return '请输入正确的金额格式如: 0.00.'
                  }
                  var data = $('#LHtable').bootstrapTable('getData')
                  var index = $(this).parents('tr').data('index')

                  for (let i = 0; i < _self.tableData.carriers.length; i++) {
                    if (_self.tableData.carriers[i].carrierID === carrierID) {
                      for (let j = 0; j < _self.tableData.carriers[i].logisticsHit.length; j++) {
                        if (_self.tableData.carriers[i].logisticsHit[j].type === data[index].type) {
                          _self.tableData.carriers[i].logisticsHit[j].money = value
                        }
                      }
                    }
                  }
                  return ''
                }
              },
              align: 'center',
              valign: 'middle'
            }
          ],
          formatNoMatches: function () {
            return
          },
          showFooter: false
        })
        setTimeout(function () {
          $('#table').bootstrapTable('resetView')
        }, 200)
      }

      function LHTypeFormater (value, row) {
        for (let i = 0; i < _self.pagePara['LHTypeInfo'].length; i++) {
          if (_self.pagePara['LHTypeInfo'][i].id === value) {
            return _self.pagePara['LHTypeInfo'][i].text
          }
        }
        return ''
      }

      initLHTable()
      var LHData = []
      for (let i = 0; i < _self.tableData.carriers.length; i++) {
        if (_self.tableData.carriers[i].carrierID === carrierID) {
          LHData = $.extend(true, [], _self.tableData.carriers[i].logisticsHit)
        }
      }
      $('#LHtable').bootstrapTable('load', {
        data: LHData
      })
      $('#LHModal').modal('show')
    },
    showCS: function (carrierID) {
      var _self = this

      function expandTable ($detail, carrierID, yardID) {
        var $el = $detail.html('<table></table>').find('table')
        var columns = []
        var data = []

        function feeChange (field, row, oldValue, $el) {
          for (let i = 0; i < _self.tableData.carriers.length; i++) {
            if (_self.tableData.carriers[i].carrierID === row.carrierID) {
              for (let j = 0; j < _self.tableData.carriers[i].yards.length; j++) {
                if (_self.tableData.carriers[i].yards[j].yardID === row.yardID) {
                  for (let k = 0; k < _self.tableData.carriers[i].yards[j].types.length; k++) {
                    if (row.type === _self.tableData.carriers[i].yards[j].types[k].typeID) {
                      for (let l = 0; l < _self.tableData.carriers[i].yards[j].types[k].sizes.length; l++) {
                        if (field === _self.tableData.carriers[i].yards[j].types[k].sizes[l].sizeID) {
                          _self.tableData.carriers[i].yards[j].types[k].sizes[l].money = row[field]
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }

        function containerTypeFormatter (value, row, index) {
          var containerTypeValue = ''
          $(_self.pagePara['containerTypeInfo']).each(function () {
            if (this.id === value) {
              containerTypeValue = this.text
              return false
            }
          })
          return containerTypeValue
        }

        columns.push({
          field: 'type',
          title: '类型',
          formatter: containerTypeFormatter,
          align: 'center',
          valign: 'middle'
        })
        for (let i = 0; i < _self.pagePara['containerSizeInfo'].length; i++) {
          columns.push({
            field: _self.pagePara['containerSizeInfo'][i].id,
            title: _self.pagePara['containerSizeInfo'][i].text,
            editable: {
              type: 'text',
              title: 'Item Price',
              validate: function (value) {
                value = $.trim(value)
                if (!value) {
                  return '请输入费用金额'
                }
                if (!/^\d+\.\d{2}/.test(value)) {
                  return '请输入正确的金额格式如: 0.00.'
                }

                return ''
              }
            },
            align: 'center',
            valign: 'middle'
          })
        }

        for (let z = 0; z < _self.pagePara['containerTypeInfo'].length; z++) {
          for (let i = 0; i < _self.tableData.carriers.length; i++) {
            if (_self.tableData.carriers[i].carrierID === carrierID) {
              for (let j = 0; j < _self.tableData.carriers[i].yards.length; j++) {
                if (_self.tableData.carriers[i].yards[j].yardID === yardID) {
                  for (let k = 0; k < _self.tableData.carriers[i].yards[j].types.length; k++) {
                    if (_self.pagePara['containerTypeInfo'][z].id === _self.tableData.carriers[i].yards[j].types[k].typeID) {
                      var lineData = {}
                      lineData['type'] = _self.tableData.carriers[i].yards[j].types[k].typeID
                      for (let l = 0; l < _self.tableData.carriers[i].yards[j].types[k].sizes.length; l++) {
                        lineData[_self.tableData.carriers[i].yards[j].types[k].sizes[l].sizeID] = _self.tableData.carriers[i].yards[j].types[k].sizes[l].money
                        lineData['carrierID'] = carrierID
                        lineData['yardID'] = yardID
                      }
                      data.push(lineData)
                    }
                  }
                }
              }
            }
          }
        }
        console.log(carrierID)
        console.log(data)
        $el.bootstrapTable({
          columns: columns,
          data: data,
          onEditableSave: feeChange
        })
      }

      function initCSTable () {
        $('#CStable').bootstrapTable({
          height: 700,
          columns:
          [
            {
              field: 'yardID',
              title: '堆场',
              formatter: YardFormater,
              align: 'center',
              valign: 'middle'
            }
          ],
          search: true,
          onExpandRow: function (index, row, $detail) {
            expandTable($detail, row.carrierID, row.yardID)
          },
          formatNoMatches: function () {
            return
          },
          showFooter: false
        })
        setTimeout(function () {
          $('#table').bootstrapTable('resetView')
        }, 200)
      }

      function YardFormater (value, row) {
        for (let i = 0; i < _self.pagePara['yardInfo'].length; i++) {
          if (_self.pagePara['yardInfo'][i].userID === value) {
            return _self.pagePara['yardInfo'][i].helpMark + '-' + _self.pagePara['yardInfo'][i].name
          }
        }
        return ''
      }

      initCSTable()
      var yardData = []
      for (let i = 0; i < _self.tableData.carriers.length; i++) {
        if (_self.tableData.carriers[i].carrierID === carrierID) {
          yardData = $.extend(true, [], _self.tableData.carriers[i].yards)
          for (let i = 0; i < yardData.length; i++) {
            yardData[i]['carrierID'] = carrierID
          }
        }
      }
      $('#CStable').bootstrapTable('load', {
        data: yardData
      })
      $('#CSModal').modal('show')
    },
    modify: function (event) {
      var _self = this
      if (common.getValidateResult()) {
        common.dealConfrimCommon('费用参数更新', function () {
          _self.$http.post('/api/putbox/feeParaControl?method=modify', _self.tableData).then((response) => {
            var retData = response.json()['data']
            getData(_self)
            common.dealSuccessCommon('更新成功')
          }, (response) => {
            common.dealErrorCommon(_self, response)
          })
        })
      }
    }
  }
}
</script>
<style>
.popover-content {
    padding: 9px 24px;
}
</style>

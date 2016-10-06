exports.baseMixin = {
  ready: function () {
  }
}

exports.daterangepickerlocale = {
  format: 'YYYY-MM-DD',
  applyLabel: '确定',
  cancelLabel: '取消',
  fromLabel: '起始时间',
  toLabel: '结束时间',
  customRangeLabel: '自定义',
  daysOfWeek: [ '日', '一', '二', '三', '四', '五', '六' ],
  monthNames: [ '一月', '二月', '三月', '四月', '五月', '六月',
          '七月', '八月', '九月', '十月', '十一月', '十二月' ],
  firstDay: 1
}

exports.clearStoreData = function (key, value) {
  store.clear()
}

exports.setStoreData = function (key, value) {
  store.set(key, value)
}

exports.getStoreData = function (key) {
  return store.get(key)
}

exports.removeStoreData = function (key) {
  store.remove(key)
}

exports.getValidateResult = function (obj) {
  obj.data('bootstrapValidator').validate()
  return obj.data('bootstrapValidator').isValid()
}

exports.dealErrorCommon = function(obj,response) {
  if (response.status > 699 && response.status < 800) {
    console.log('700 error')
    BootstrapDialog.show({
      title: '<i class= "fa fa-fw fa-info-circle"></i><strong>错误信息</strong>',
      cssClass: 'modal-danger',
      message: '<i class="text-warning fa fa-fw fa-warning" style="font-size: 40px"></i>' + response.data.description,
      buttons: [{
        label: '<i class= "fa fa-fw fa-close"></i>关闭',
        cssClass: 'btn-outline',
        action: function(dialogItself){
          dialogItself.close()
        }
      }]
    })
  } else if (response.status > 401) {
    obj.$router.go({ path: '/error401', replace: true })
  } else{
    console.log('else error')
    console.log(response.data)
    obj.setError(response.status,response.data.description)
    obj.$router.go({ path: '/error', replace: true })
  }
}

exports.dealAlertCommon = function(obj,response) {
  if (response.status > 699 && response.status < 800) {
    console.log('700 error')
    alert(response.data.description)
  } else if (response.status > 401) {
    obj.$router.go({ path: '/error401', replace: true })
  } else{
    console.log('else error')
    console.log(response.data)
    obj.setError(response.status,response.data.description)
    obj.$router.go({ path: '/error', replace: true })
  }
}

exports.dealConfrimCommon = function(message, callbackFunc) {
  BootstrapDialog.confirm({
    title: '<i class= "fa fa-fw fa-info-circle"></i><strong>确认信息</strong>',
    message: '<i class="text-warning fa fa-fw fa-question-circle" style="font-size: 40px"></i>' + message,
    cssClass: 'modal-primary',
    btnOKLabel: '<i class= "fa fa-fw fa-check"></i>确认',
    btnOKClass: 'btn-primary',
    btnCancelLabel: '<i class= "fa fa-fw fa-close"></i>取消',
    btnCancelClass: 'btn-warning',
    callback: function (result) {
      if (result) {
        callbackFunc()
      }
    }
  })
}

exports.dealSuccessCommon = function(message) {
  BootstrapDialog.show({
    title: '<i class= "fa fa-fw fa-info-circle"></i><strong>提示信息</strong>',
    cssClass: 'modal-success',
    message: '<i class="tex t-warning glyphicon glyphicon-ok" style="font-size: 40px"></i>' + message,
    buttons: [{
      label: '<i class= "fa fa-fw fa-close"></i>关闭',
      cssClass: 'btn-primary',
      action: function(dialogItself){
        dialogItself.close()
      }
    }]
  })
}

exports.dealPromptCommon = function(message) {
  BootstrapDialog.show({
    title: '<i class= "fa fa-fw fa-info-circle"></i><strong>提示信息</strong>',
    cssClass: 'msg-dialog',
    message: '<i class="text-warning fa fa-fw fa-warning" style="font-size: 40px"></i>' + message,
    buttons: [{
      label: '<i class= "fa fa-fw fa-close"></i>关闭',
      cssClass: 'btn-primary',
      action: function(dialogItself){
        dialogItself.close()
      }
    }]
  })
}

exports.dealWarningCommon = function(message) {
  BootstrapDialog.show({
    title: '<i class= "fa fa-fw fa-info-circle"></i><strong>警告信息</strong>',
    cssClass: 'modal-warning',
    message: '<i class="text-warning fa fa-fw fa-warning" style="font-size: 40px"></i>' + message,
    buttons: [{
      label: '<i class= "fa fa-fw fa-close"></i>关闭',
      cssClass: 'btn-outline',
      action: function(dialogItself){
        dialogItself.close()
      }
    }]
  })
}

exports.changeTableClass = function (tableObj) {
  tableObj.on('click-row.bs.table', function (e, row, $element) {
    $('.success').removeClass('success')
    $($element).addClass('success')
  })
}

exports.changeValidatorStatus = function (tableObj, columns, status) {
  for (var index = 0; index < columns.length; index++) {
    tableObj.data('bootstrapValidator').updateStatus(columns[index], status)
  }
}

exports.initControlSize = function () {
  var topOffset = 180
  var height = $(window).height()
  $('.wrapper').trigger( "resize" )
  height = height - topOffset
  if (height < 1) height = 1
  if (height > 0) {
    $('#box-body').height(height - 30)
    $('#table').bootstrapTable('resetView', {
      height: height - 20
    })
  }
}

exports.getTableHeight = function () {
  var topOffset = 164
  var height = $(window).height()
  height = height - topOffset
  return height
}

exports.initSelect2 = function (jqItem, sdata) {
  jqItem.select2({
    maximumSelectionLength: 1,
    language: 'zh-CN',
    tags: true,
    width: '100%',
    data: sdata
  })
}

exports.initSelect2Single = function (jqItem, sdata) {
  jqItem.select2({
    minimumResultsForSearch: Infinity,
    language: 'zh-CN',
    tags: true,
    width: '100%',
    data: sdata
  })
  jqItem.val(null).trigger('change')
}

exports.initSelect2SingleWithSearch = function (jqItem, sdata) {
  jqItem.select2({
    language: 'zh-CN',
    tags: true,
    data: sdata
  })
  jqItem.val(null).trigger('change')
}

exports.initDatepicker = function (jqItem) {
  jqItem.datepicker({
    language: 'zh-CN',
    autoclose: true,
    todayHighlight: true,
    format: 'yyyy-mm-dd'
  })
}


//两端去空格函数
String.prototype.trim = function() {    return this.replace(/(^\s*)|(\s*$)/g,""); }

exports.DateFormat = function (date, fmt) {
    var o = {
        "M+": date.getMonth() + 1, //月份
        "d+": date.getDate(), //日
        "h+": date.getHours(), //小时
        "m+": date.getMinutes(), //分
        "s+": date.getSeconds(), //秒
        "q+": Math.floor((date.getMonth() + 3) / 3), //季度
        "S": date.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
    if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}

exports.remarkFormatter = function (value, row, index) {
  if (value) {
    var displayName = (value.length > 3) ? (value.substring(0, 3) + '...') : value
    return [
      '<a role="button" data-toggle="popover" data-trigger="hover" data-placement="right" data-html="true" data-content="' +
      '<div class=&quot;box&quot;>' +
        '<div class=&quot;box-body&quot;>' +
          '<div class=&quot;form-group&quot;>' +
            '<div class=&quot;&quot;><span>' + value + '</span></div>' +
          '</div>' +
        '</div>' +
      '</div>">' + displayName + '</a>'
    ].join('')
  }
}

exports.imagesFormatter = function (value, row) {
  var retString = '<div class="tuto-thumbox-detail"><ul>'
  for (var key in value) {
    retString += '<li><a href="' + value[key] + '" > <img src="' + value[key] + '" alt=""></a></li>'
  }
  retString += '</ul></div>'
  return retString
}

exports.BTRowFormat = function (rowid,rowname) {
  return {
    field: rowid,
    title: rowname,
    align: 'center',
    valign: 'middle'
  }
}

exports.BTRowFormatWidth = function (rowid,rowname, width) {
  return {
    field: rowid,
    title: rowname,
    width: width,
    align: 'center',
    valign: 'middle'
  }
}

exports.BTRowFormatWithFormatter = function (rowid,rowname,rFormatter) {
  return {
    field: rowid,
    title: rowname,
    formatter: rFormatter,
    align: 'center',
    valign: 'middle'
  }
}
exports.BTRowFormatWithPhotoFormatter = function (rowid,rowname,rFormatter) {
  return {
    field: rowid,
    title: rowname,
    formatter: rFormatter,
    align: 'center',
    valign: 'middle',
    width: '60px'
  }
}

exports.BTRowFormatWithFormatterWidth = function (rowid,rowname,rFormatter,width) {
  return {
    field: rowid,
    title: rowname,
    formatter: rFormatter,
    width: width,
    align: 'center',
    valign: 'middle',
    width: '60px'
  }
}
// bootstrapValidator  检查公共方法
exports.BVUsername = {
  validators: {
    notEmpty: {
      message: '用户名不能为空'
    },
    regexp: {
      regexp: /^[a-zA-Z0-9_\.]+$/,
      message: '只能是数字和字母_.'
    },
    stringLength: {
      min: 6,
      max: 30,
      message: '用户名长度必须在6到30之间'
    }
  }
}

exports.BVEmail = {
  validators: {
    notEmpty: {
      message: '邮件不能为空'
    },
    emailAddress: {
      message: '请输入正确的邮件地址如：xxxx@abc.com'
    }
  }
}

exports.BVMobile = {
  validators: {
    notEmpty: {
      message: '手机不能为空'
    },
    phone: {
      country: 'CN',
      message: '请输入正确的手机号码'
    }
  }
}

exports.BVDate = {
  validators: {
    notEmpty: {
      message: '日期不能为空'
    },
    date: {
      format: 'YYYY-MM-DD',
      message: '日期类型是 YYYY-MM-DD'
    }
  }
}

exports.BVMoney = {
  validators: {
    notEmpty: {
      message: '请输入金额'
    },
    regexp: {/* 只需加此键值对，包含正则表达式，和提示 */
      regexp: /^\d+\.\d{2}/,
      message: '请输入正确的金额格式如: 0.00.'
    }
  }
}

exports.BVNotEmput = function (message) {
  return {
    validators: {
      notEmpty: {
        message: message
      }
    }
  }
}

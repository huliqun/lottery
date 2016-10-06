<template lang="pug">
  table(class="table table-hover text-center")
    thead
      tr
        th 图片
        th 大小
        th 进度
        th 状态
    tbody
      tr(v-for='file in files')
        td
          a(href="{{file.fileUrl}}", data-lightbox="image-1", data-title="My caption")
            img( :src='file.fileUrl' class="img-responsive center-block")
        td(v-text='file.size')
        td(v-text='file.progress')
        td(v-html='onStatus(file)')
  div
    file-upload(class='btn btn-primary',
      v-bind:url='url',
      v-bind:method='method',
      v-bind:files.sync = 'files',
      v-bind:urls.sync = 'urls',
      v-bind:auto-upload = 'true',
      v-bind:events = 'cbEvents',
      v-bind:filters = "filters",
      v-bind:request-options = "reqopts"
      )
</template>
<script>
import $ from 'jquery'
var Store = require('store')
import FileUpload from '../fileUpload/fileUpload'
function getToken () {
  var token = Store.get('token')
  return token
}
export default {
  props: {
    urls: {
      type: Array,
      default: () => {
        return []
      },
      twoWay: true
    }
  },
  data () {
    return {
      url: '/api/putbox/settleControl?method=upload',
      files: [],
      method: 'RESOURCE',
      filters: [
        {
          name: 'imageFilter',
          fn (file) {
            var type = '|' + file.type.slice(file.type.lastIndexOf('/') + 1) + '|'
            return '|jpg|png|jpeg|bmp|gif|'.indexOf(type) !== -1
          }
        }
      ],
      cbEvents: {
        onCompleteUpload: (file, response, status, header) => {
          console.log('finish upload;')
        }
      },
      reqopts: {
        responseType: 'json',
        withCredentials: false
      }
    }
  },
  methods: {
    onStatus (file) {
      if (file.isSuccess) {
        return '<span class="badge bg-green">成功</span>'
      } else if (file.isError) {
        return '<span class="badge bg-red">失败</span>'
      } else if (file.isUploading) {
        return '<div id="loading" class="loading"></div> '
      } else {
        return '<span class="badge bg-yellow">等待</span>'
      }
    }
  },
  components: {
    FileUpload
  }
}
</script>

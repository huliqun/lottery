<template>
  <div class="navbar-default sidebar" role="navigation" id="side-control">
    <div class="sidebar-nav navbar-collapse">
      <ul class="nav" id="side-menu">
        <li class="sidebar-search">
          <div class="input-group custom-search-form">
            <input type="text" class="form-control" placeholder="Search...">
            <span class="input-group-btn">
              <button class="btn btn-default" type="button">
                <i class="fa fa-search"></i>
              </button>
            </span
          </div>
          <!-- /input-group -->
        </li>
        <template v-for="item in userinfo['menulist']">
          <li>
            <template v-if="item.menuType === '01'">
              <a v-link="item.menuPath"><i class="fa {{ item.menuIcon }} fa-fw"></i> {{ item.menuName }}</a>
            </template>
            <template v-if="item.menuType === '00'">
              <a href="#"><i class="fa {{ item.menuIcon }} fa-fw"}></i> {{ item.menuName }}<span class="fa arrow"></span></a>
              <ul class="nav nav-second-level">
                <template v-for="sItem in item.subMenu">
                  <li>
                    <a v-link="sItem.menuPath">{{ sItem.menuName }}</a>
                  </li>
                </template>
              </ul>
            </template>
          </li>
        </template>
      </ul>
    </div>
    <!-- /.sidebar-collapse -->
  </div>
  <!-- /.navbar-static-side -->
</template>
<script>
import $ from 'jquery'
var common = require('commonFunc')
export default {
  name: 'mainMenu',
  data: function () {
    return {
      userinfo: common.getStoreData('userinfo')
    }
  },
  ready: function () {
    console.log('mainMenu created!')
    $(function () {
      $('#side-control').BootSideMenu({
        side: 'left', // left or right
        autoClose: false // auto close when page loads
      })
      $('#side-menu').metisMenu()
      $(window).bind('load live resize', function () {
        var topOffset = 50
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width
        if (width < 768) {
          $('div.navbar-collapse').addClass('collapse')
          topOffset = 100 // 2-row-menu
        } else {
          $('div.navbar-collapse').removeClass('collapse')
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1
        height = height - topOffset
        if (height < 1) height = 1
        if (height > topOffset) {
          $('#page-wrapper').css('min-height', (height) + 'px')
        }
      })

      var url = window.location
      var element = $('ul.nav a').filter(function () {
        return this.href === url || url.href.indexOf(this.href) === 0
      }).addClass('active').parent().parent().addClass('in').parent()
      if (element.is('li')) {
        element.addClass('active')
      }
    })
  }
}
</script>
<style>
</style>

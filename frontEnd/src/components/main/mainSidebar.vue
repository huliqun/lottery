<template>
  <!-- Left side column. contains the logo and sidebar -->
  <aside class="main-sidebar">
    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar">
      <!-- Sidebar user panel -->
      <div class="user-panel">
        <div class="pull-left image">
          <img src="/img/user2-160x160.jpg" class="img-circle" alt="User Image">
        </div>
        <div class="pull-left info">
          <p>Alexander Pierce</p>
          <a href="#"><i class="fa fa-circle text-success"></i> Online</a>
        </div>
      </div>
      <!-- search form -->
      <form action="#" method="get" class="sidebar-form">
        <div class="input-group">
          <input type="text" name="q" class="form-control" placeholder="Search...">
          <span class="input-group-btn">
            <button type="submit" name="search" id="search-btn" class="btn btn-flat"><i class="fa fa-search"></i>
            </button>
          </span>
        </div>
      </form>
      <!-- /.search form -->
      <!-- sidebar menu: : style can be found in sidebar.less -->
      <ul class="sidebar-menu">
        <li class="header">主菜单</li>
        <template v-for="item in userinfo['menulist']">
          <li class="treeview">
            <template v-if="item.menuType === '01'">
              <a v-link="item.menuPath">
                <i class="fa {{ item.menuIcon }}"></i> <span>{{ item.menuName }}</span>
                <span class="pull-right-container">
                  <small class="label pull-right bg-green">new</small>
                </span>
              </a>
            </template>
            <template v-if="item.menuType === '00'">
              <a href="#">
                <i class="fa {{ item.menuIcon }} "></i> <span> {{ item.menuName }}</span>
                <span class="pull-right-container">
                  <i class="fa fa-angle-left pull-right"></i>
                </span>
              </a>
              <ul class="treeview-menu">
                <template v-for="sItem in item.subMenu">
                  <li><a v-link="sItem.menuPath"><i class="fa fa-circle-o"></i> {{ sItem.menuName }}</a></li>
                </template>
              </ul>
            </template>
          </li>
        </template>
        <li class="header">LABELS</li>
        <li><a href="#"><i class="fa fa-circle-o text-red"></i> <span>Important</span></a></li>
        <li><a href="#"><i class="fa fa-circle-o text-yellow"></i> <span>Warning</span></a></li>
        <li><a href="#"><i class="fa fa-circle-o text-aqua"></i> <span>Information</span></a></li>
      </ul>
    </section>
    <!-- /.sidebar -->
  </aside>
</template>
<script>
import $ from 'jquery'
var Store = require('store')
export default {
  name: 'mainMenu',
  data: function () {
    return {
      userinfo: Store.get('userinfo')
    }
  },
  ready: function () {
    console.log('mainMenu created!')
  }
}
</script>
<style>
</style>

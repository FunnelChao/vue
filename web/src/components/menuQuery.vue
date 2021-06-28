<!--  -->
<template>
  <el-menu :router=true :default-active="$route.name" unique-opened=true>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-chicken"></i>高校类型</template>
            <el-menu-item-group v-for="(value, key, index) in elData" :key='index'>
              <el-menu-item :index="value.path" @click="getData(value)">{{value.name}}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-chicken"></i>所在地区</template>
            <el-menu-item-group v-for="(value, key, index) in elPlaceData" :key='index' >
              <el-menu-item index="" @click="getPlaceData(value)" v-on:="">{{value.name}}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
</template>

<script>
import Bus from '../bus'
export default {
  data() {
    return {
      elData: [{
        path: '',
        name: '一流学校'
      },
      {
        path: '',
        name: '一流学科'
      },
      {
        path: '',
        name: '985高校'
      },
      {
        path: '',
        name: '211高校'
      }
      ],
      elPlaceData:[
        {
          name: '北京市'
        },
        {
          name: '四川省'
        },
        {
          name: '天津市'
        },
        {
          name: '河北省'
        },
        {
          name: '山西省'
        },
        {
          name: '内蒙古自治区'
        },
        {
          name: '辽宁省'
        },
        {
          name: '吉林省'
        },
        {
          name: '黑龙江省'
        },
        {
          name: '上海市'
        },
        {
          name: '江苏省'
        },
        {
          name: '浙江省'
        },
        {
          name: '安徽省'
        },
        {
          name: '福建省'
        },
        {
          name: '江西省'
        },
        {
          name: '山东省'
        },
        {
          name: '河南省'
        },
        {
          name: '湖北省'
        },
        {
          name: '湖南省'
        },
        {
          name: '广东省'
        },
        {
          name: '广西壮族自治区'
        },
        {
          name: '海南省'
        },
        {
          name: '重庆市'
        },
        {
          name: '贵州省'
        },
        {
          name: '云南省'
        },
        {
          name: '西藏自治区'
        },
        {
          name: '陕西省'
        },
        {
          name: '甘肃省'
        },
        {
          name: '青海省'
        },
        {
          name: '宁夏回族自治区'
        },
        {
          name: '新疆维吾尔自治区'
        },
      ]
    }
  },
  methods: {
    getData(value){
      if(value.name == '一流学校')
      {
        Bus.$emit('name', '一流大学')
      }
      else if(value.name == '985高校'){
        Bus.$emit('name', '985')
      }
      else if(value.name == '211高校'){
        Bus.$emit('name', '211')
      }
      else
      {
        Bus.$emit('name', value.name)
      }
      Bus.$emit('yemian_page', 1)
    },
    getPlaceData(value){
      Bus.$emit('place', value.name)
      Bus.$emit('yemian_page', 1)
    }
  },
}
</script>
<style>
</style>
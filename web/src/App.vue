<template>
  <div id="app" >
    <table  width="80%" style="text-align:center;margin:0 auto;background-color: #F2F8FE;filter:brightness(1);">
      <tr><td style="text-align:left;">教育部全国高校名单（截止2020-06-30</td> <td style="width= 15%; ">  <span @click="changeSchool()"><router-link to="">按高校查询</router-link></span>   | <span @click="changePlace()"><router-link to="">按地区查询</router-link></span>  </td> </tr>
    </table>
    <add/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script>
import SchoolQuery from './components/schoolQuery.vue' 
import Bus from './bus'
export default {
  data() {
    return {
      show : true,
      elData: [{
        path: '/',
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
  components:{
    Add:SchoolQuery
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
    },
    getPlaceData(value){
      Bus.$emit('place', value.name)
    },
    changePlace(){
      Bus.$emit('show', true)
    },
    changeSchool(){
      Bus.$emit('show', false)
    }
  },
  
}
</script>
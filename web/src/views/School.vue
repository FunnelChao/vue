<template>
<div>
  
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column
      type="index"
      :index="indexMethod" label="序号" width="124">
    </el-table-column>
    <el-table-column v-for="(val, key) in tableLabel" :key="key" :prop="key" :label="val" width="124"></el-table-column>
    </el-table>
    <el-pagination v-if="show" background  layout="prev, pager, next" :total="total" :current-page="yemian_page" :page-size="20" @current-change="changerPage">
</el-pagination>
</div>
</template>

<script>
import Bus from '../bus'
  export default {
    data() {
      return {
        total:42,
        page: 0,
        yemian_page:1,
        show: true,
        val_flag: '一流大学',
        placeList:'北京市四川省天津市河北省山西省内蒙古自治区辽宁省吉林省黑龙江省上海市江苏省浙江省安徽省福建省江西省山东省河南省湖北省湖南省广东省广西壮族自治区海南省重庆市贵州省云南省西藏自治区陕西省甘肃省青海省新疆维吾尔自治区',
        schoolList:['一流学校','一流学科','985高校','211高校'],
        tableData: [],
        tableLabel: {
          code: '学校标识码',
          schoolname: '学校名称',
          province: '所在地区',
          city: '城市',
          department: '主管部门',
          level: '办学层次',
          type: '办学类型'
        }
      }
    },
    created() {
      Bus.$on('yemian_page', val=> {
        this.yemian_page = val
        this.show = false;//让分页隐藏
        this.$nextTick(() => {//重新渲染分页
          this.show = true
        })
      })
      Bus.$on('name', val => {
        this.val_flag = val
        this.$http('http://localhost:8001/user/first?type='+this.val_flag+'&page='+this.page).then(res => {
            this.tableData = res.data
        })
        this.$http('http://localhost:8001/user/countPlace?type='+this.val_flag).then(res => {
            this.total = res.data
        })
      })
      Bus.$on('place', val =>{
        this.val_flag = val
        this.$http('http://localhost:8001/user/second?province='+this.val_flag+'&page='+this.page).then(res => {
            this.tableData = res.data
          })
        this.$http('http://localhost:8001/user/countProvince?province='+this.val_flag).then(res => {
            this.total = res.data
          })
      })
      Bus.$on('page', val=>{
        this.page = val
        if(this.placeList.indexOf(this.val_flag) > -1){
          this.$http('http://localhost:8001/user/second?province='+this.val_flag+'&page='+this.page).then(res => {
            this.tableData = res.data
          })
        }
        else if(this.schoolList.indexOf(this.val_flag) > -1){
          this.$http('http://localhost:8001/user/first?type='+this.val_flag+'&page='+this.page).then(res => {
            this.tableData = res.data
        })
        }
      })
    },
    mounted () {
      this.$http('http://localhost:8001/user/first?type='+this.val_flag+'&page='+this.page).then(res => {
        this.tableData = res.data
      })
    },
    methods: {
      indexMethod(index) {
        return index + 1;
      },
      changerPage(page){
        Bus.$emit('page', page-1)
      }
    },
    
  }
</script>
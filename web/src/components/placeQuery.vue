<!--  -->
<template>
  <el-form :inline="true" class="demo-form-inline" style="display:block;">
    <el-input v-model="place"  placeholder="地区" style="width: 120px"></el-input>
  <el-form-item>
    <el-button type="primary" @click="onSubmit" style="display:block;"> <router-link to="">查询</router-link> </el-button>
  </el-form-item>
</el-form>
</template>

<script>
import Bus from '../bus'
  export default {
    data() {
      return {
        place: ''
      }
    },
    methods: {
      onSubmit() {
        Bus.$emit('place', this.place)
      }
    }
  }
</script>
<style>
</style>
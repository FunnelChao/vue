package com.example.demo.controller;

import com.example.demo.bean.user;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("user")
@CrossOrigin
public class userController {
    @Resource
    com.example.demo.mapper.userMapper userMapper;
    @RequestMapping("all")
    public List<user> findAll(){
        return userMapper.findAll();
    }
    @RequestMapping("first")
    public List<user> findAllFromFirstSchool(String type,int page){
        int pageCount = 20;
        System.out.println(page);
        return userMapper.findAllFromFirst(type,page,pageCount);
    }
    @RequestMapping("second")
    public List<user> findAllFromSecond(String province,int page){
        System.out.println(111);
        System.out.println(province);
        System.out.println(2222);
        System.out.println(page);
        System.out.println(3333);
        int pageCount = 20;
        return userMapper.findAllFromSecond(province,page,pageCount);}
    @RequestMapping("countPlace")
    public int countPlace(String type){
        return userMapper.countPlace(type);
    }
    @RequestMapping("countProvince")
    public int countProvince(String province){
        System.out.println(province);
        return userMapper.countProvince(province);
    }
}

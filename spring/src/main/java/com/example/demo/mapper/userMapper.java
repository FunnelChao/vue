package com.example.demo.mapper;

import com.example.demo.bean.user;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface userMapper {
    @Select("select * from schooldb")
    List<user> findAll();
    @Select("select * from schooldb where type like \"%\" #{type} \"%\" limit #{page}, #{pageCount}")
    List<user> findAllFromFirst(String type, int page, int pageCount);
    @Select("select * from schooldb where province like \"%\" #{province} \"%\" limit #{page},#{pageCount} ")
    List<user> findAllFromSecond(String province, int page, int pageCount);
    @Select("SELECT count(*) FROM schooldb where type like \"%\" #{type} \"%\"")
    int countPlace(String type);
    @Select("SELECT count(*) FROM schooldb where province like \"%\" #{province} \"%\"")
    int countProvince(String province);
}

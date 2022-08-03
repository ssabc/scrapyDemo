 //引入mongoose.js文件
 var mongoose = require("./mongoose.js")
 //定义schema
 var schema = mongoose.Schema
 const blog=new schema({
     //这里是数据库自己创建的属性名：他的属性类型   如：
     'name' : {type : String , require : true},
     'img' : {type : String , require : true}
 })
 //导出
 module.exports = blog;

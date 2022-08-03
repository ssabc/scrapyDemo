 //引入mongoose.js 文件
 var mongoose = require("./mongoose");
 //引入schema.js 文件
 var schema = require("./schema");
 //定义模型 表名为jingtians
 var appModel = mongoose.model("jingtian", schema);
 //导出
 module.exports = appModel;

/*
 * @Author: zhaoshan
 * @Date: 2022-07-30 11:03:10
 * @LastEditTime: 2022-08-03 16:27:35
 * @LastEditors: zhaoshan
 * @Description: 
 */
var express = require('express');
var router = express.Router();
var appModel = require("../lib/appMode");

/* GET users listing. */
router.get('/', async function(req, res, next) {
  const resData = {
    code: '000000',
    data: [], //await
  }
  appModel.find().exec(function(err, data) {
    if (!err) {
      console.log('----', data);
      resData.data = data
      res.send(resData);
    }
  });
});

module.exports = router;

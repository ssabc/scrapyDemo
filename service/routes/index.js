/*
 * @Author: zhaoshan
 * @Date: 2022-07-30 11:03:10
 * @LastEditTime: 2022-08-03 11:44:18
 * @LastEditors: zhaoshan
 * @Description: 
 */
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  const resData = {
    code: '000000',
    data: []
  }
  res.send(resData);
});

module.exports = router;

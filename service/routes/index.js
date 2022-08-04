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

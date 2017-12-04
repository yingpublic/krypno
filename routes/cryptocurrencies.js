var express = require('express');
var router = express.Router();

/* GET cryptocurrencies listing. */
router.get('/', function(req, res, next) {
  res.send('Here is a listing of the most popular cryptocurrencies!');
});

module.exports = router;

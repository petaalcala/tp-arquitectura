const express = require('express');
const app = express();
const resources = require('./resources.json');

app.get('/', function(req, res) {
  res.send("Hi, I'm root");
});

app.use('/static', express.static(__dirname + '/static/files'));

app.get('/resources/:resource_id', function(req, res) {
  const resource_id = req.params.resource_id;
  res.send(resources[resource_id]);
});

app.listen(3000, function () {
  console.log('listening on port 3000!')
})
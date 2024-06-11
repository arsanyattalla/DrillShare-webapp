const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient } = require('mongodb');

const app = express();

const mongoClient = new MongoClient("mongodb+srv://drillshare:DrillShare101@drillshare.pmlbx.mongodb.net/DrillShare")

mongoClient.connect((err, client) => {
  const testDB = mongoClient.db('Drillshare');
  app.use(bodyParser.json());

  app.post('/test/postListing', (req, res) => {
    testDB.collection('test').insertOne({data: req.body.message})
      .then(() => console.log('db insert worked'))
      .catch((e) => console.log(e));
  });

  app.get('/test/getListings', (req, res) => {
    testDB.collection('test').find({}).toArray()
      .then((result) => {
        res.send(result.map(r => r.data));
      })
      .catch((e) => console.log(e));
  });

  client.close();
});
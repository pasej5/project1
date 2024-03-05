const express = require('express');
const axios = require('axios');
const cors = require('cors');
const Redis = require('redis');

const redisClient = Redis.createClient();

const DEFAULT_EXPIRATION = 3600;

const app = express();
// app.use(cors());

app.get('/photos', async (req, res) => {
  const albumId = req.query.albumId;
  redisClient.get('photos', async (error, photos) => {
    if (error) console.error(error);
    if (photos != null) {
      return res.json(JSON.parse(photos));
    } else {
      const { data } = await axios.get(
        'https://jsonplaceholder.typicode.com/photos',
        { params: { albumId } }
      );
      redisClient.setex('photos', DEFAULT_EXPIRATION, JSON.stringify(data));
    }
  });

  res.json(data);
});

app.get('/photos/:id', async (req, res) => {
  const { data } = await axios.get(
    `https://jsonplaceholder.typicode.com/photos/${req.params.id}`
  );
  res.json(data);
});

app.listen(3000);

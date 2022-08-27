const redis = require('redis');
const cl = redis.createClient();

cl.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

cl.on('connect', function() {
  console.log('Redis client connected to the server');
});

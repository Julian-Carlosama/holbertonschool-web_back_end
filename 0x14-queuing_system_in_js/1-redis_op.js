const redis = require('redis');
const cl = redis.createClient();

cl.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

cl.on('connect', function() {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  cl.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  cl.get(schoolName, function(err, res) {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

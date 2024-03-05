const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
  console.log(req.url, req.method);
});

// Start the server on port 3000
server.listen(3000, '127.0.0.1', () => {
  console.log('listening for ports on port 3000');
});

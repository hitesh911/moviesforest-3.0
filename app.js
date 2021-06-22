const http = require('http');

const hostname = '0.0.0.0';
const port = 3333;

const MY_MESSAGE = process.env.MY_MESSAGE

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end(MY_MESSAGE);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

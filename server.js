const http = require("http");
http.createServer((req, res) => { res.end(process.version); }).listen(8080);

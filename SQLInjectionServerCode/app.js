var http = require('http');
var fs = require('fs');
var sqlite3 = require('sqlite3').verbose();
//look at sqlite3 node package - how to do prepared statements
var exec = require('child_process').exec;

// Connect to the database
var db = new sqlite3.Database('./sql_inj_test.sqlite');

function handlePostData(req, res, callback) {
    var body = '';
    // http://stackoverflow.com/questions/4295782/how-do-you-extract-post-data-in-node-js
    // collect all of the POST data
    req.on('data', function (data) {
        body += data;
        // Too much POST data, kill the connection!
        if (body.length > 1e6) {
            request.connection.destroy();
            res.writeHead(413, {'Content-Type': 'text/html'});
            res.end('failure: POST data too large');
            return console.error('POST data too large');
        }
    });
    // when the data collection is done, pull out each parameter and unencode it, then pass it on to the
    // callback function
    req.on('end', function () {
        var data = {};
        var parameters = body.split('&');
        for (var index = 0; index < parameters.length; ++index) {
            var parameter = parameters[index].split('=');
            data[parameter[0]] = decodeURIComponent(parameter[1].replace(/\+/g, '%20'));
        }
        callback(res, data);
    });
}

var server = http.createServer(function (req, res) {
    // first handle the CSS and JavaScript files
    if (req.method === 'POST') {
        handlePostData(req, res, function (res, data) {
            var username = data['username'];
            var password = data['password'];

            //var query = 'SELECT username, password FROM users WHERE username="' + username + '"';
            //NOTE: the ? means that whatever the user has inputed will not be run as code bc it is compiled after the select
            var query = 'SELECT username, password FROM users WHERE username= ?';
            //make sure it just gets the username that it has already found from the database
            db.get(query, username, function(err, row) {
                if (err) {
                    res.writeHead(500, {'Content-Type': 'text/html'});
                    res.end('Database error');
                    console.error(err);
                } else {
                    if (row && row.password === password) {
                        res.writeHead(200, {'Content-Type': 'text/html'});
                        res.end(fs.readFileSync('instructions.html', 'utf8'));
                    }
                    else {
                        res.writeHead(200, {'Content-Type': 'text/html'});
                        res.end(fs.readFileSync('login.html', 'utf8'));
                    }
                }
            });
        });
    }
    else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(fs.readFileSync('login.html', 'utf8'));
    }
});

// start the server
exec("id -u", (error, stdout, stderr) => {
    if (error) {
        console.error("Could not get uid to set port number.");
        console.error(stderr);
    } else {
        var port = 3000 + parseInt(stdout);
        console.log("Listening on port " + port);
        server.listen(port);
    }
});

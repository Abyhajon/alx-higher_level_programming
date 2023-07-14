#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Read the URL from the command line arguments
const filePath = process.argv[3]; // Read the file path from the command line arguments

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
});

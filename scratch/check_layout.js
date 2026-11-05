const http = require('http');
const { execSync } = require('child_process');

// We have CDP running or let's inspect via chrome headless
console.log("Checking layout...");

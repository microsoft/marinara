// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello from the node server running inside Azure Linux NodeJS distroless container.');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

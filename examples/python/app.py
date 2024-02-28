# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from the python server running in Azure Linux Python distroless container.'

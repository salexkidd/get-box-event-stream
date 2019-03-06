#!/usr/bin/env python
"""get_token.py

Usage:
  get_token.py <CLIENT_ID> <CLIENT_SECRET>
"""
import pprint
import requests
import webbrowser
from docopt import docopt
from flask import Flask, request, redirect

TOKEN_URL = "https://api.box.com/oauth2/token"
AUTHORIZATION_URL = "https://account.box.com/api/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_url}&state={client_secret}"

app = Flask(__name__)
arguments = docopt(__doc__)

@app.route("/")
def get_start():
    return redirect(
        AUTHORIZATION_URL.format(
            client_id=arguments["<CLIENT_ID>"],
            client_secret = arguments["<CLIENT_SECRET>"],
            redirect_url="http://localhost:8000/authorization"
        )
    )

@app.route('/authorization')
def get_authoirization():
    code = request.args.get("code", "")
    state = request.args.get("state", "")

    if code and state:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": arguments["<CLIENT_ID>"],
            "client_secret": arguments["<CLIENT_SECRET>"]
        }

        response = requests.post(TOKEN_URL, data, verify=False)
        json_data = pprint.pformat(response.json())
        return json_data
    else:
        return "Failed to get token."

if __name__ == '__main__':
    app.run(port=8000)

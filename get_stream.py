#!/usr/bin/env python
"""get_stream.py

Usage:
  get_token.py <TOKEN>
"""
import requests
from docopt import docopt
from pprint import pprint

API_URL = 'https://api.box.com/2.0/events?stream_type=admin_logs&event_type=COLLABORATION_INVITE'

arguments = docopt(__doc__)


def main():
    ...
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer {}'.format(arguments["<TOKEN>"])
    }
    response = requests.get(API_URL, headers=headers, verify=False)
    pprint(response.json())

main()


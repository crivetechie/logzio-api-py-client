#!/usr/bin/env python3

import requests
import argparse


# usage example:
# ./logzio.py --accountid=12345 --createuser --apitoken="aabbcc-ddee-ffgg-1122-002211" --username=joe.doe@example.com --fullname="Joe Doe"


API_URL = 'https://api.logz.io/v1/'
EP_USERS = 'user-management'

DATA_CREATE_USER = """{{
  "username": "{username}",
  "fullName": "{fullname}",
  "accountID": {accountId},
  "roles": [
    {roles}
  ]
}}"""


def logzio_get(apitoken, endpoint):
    headers = {'X-API-TOKEN': apitoken}
    r = requests.get('{}/{}'.format(API_URL, endpoint), headers=headers)
    r.status_code
    print(r.json())

def logzio_post(apitoken, endpoint, data):
    headers = {'X-API-TOKEN': apitoken}
    r = requests.post('{}/{}'.format(API_URL, endpoint), headers=headers, data=data)
    r.status_code
    print(r.json())

def get_users(apitoken):
    logzio_get(apitoken, EP_USERS)

def create_user(accountid, apitoken, username, fullname, roles):
    data = DATA_CREATE_USER.format(accountId=accountid, username=username, fullname=fullname, roles=roles)
    print(data)
    logzio_post(apitoken, EP_USERS, data)

def validate_user_params(args):
    return args.accountid is not None and args.username is not None and args.fullname is not None and args.roles is not None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apitoken', required=True, action='store', help='the logz.io api key')
    parser.add_argument('--accountid', action='store', help='the target logz.io account id')
    parser.add_argument('--createuser', action='store_true', help='creates a user')
    parser.add_argument('--username', action='store', help='The username, ie: joe.doe@example.com')
    parser.add_argument('--fullname', action='store', help='The full name, ie: Joe Doe')
    parser.add_argument('--roles', default="2", help='For admin access, 3. For user access, 2')
    args = parser.parse_args()

    if args.createuser:
        if validate_user_params(args):
            create_user(accountid=args.accountid, apitoken=args.apitoken,  username=args.username, fullname=args.fullname, roles=args.roles)
        else:
            print("Missing one or more required parameters.")
  
if __name__== "__main__":
  main()
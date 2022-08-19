import argparse
import time
import requests
import base64
import json
from datetime import datetime

base_dev_url = 'https://dev-api.axil.ai/axil/enterprise-objects'
base_prod_url = 'https://api.axil.ai/axil/enterprise-objects'


def get_auth0_token(client_id_, client_secret_):
    print(f'get_auth0_token :: starting')
    payload = {
        'client_id': client_id_,
        'client_secret': client_secret_,
        'audience': 'https://api.axil.ai',
        'grant_type': 'client_credentials'
    }
    headers = {'content-type': 'application/json'}

    req_resp = requests.post(
        'https://axil.auth0.com/oauth/token',
        headers=headers,
        json=payload,
    )
    if req_resp.status_code != requests.codes.ok:
        raise Exception('Error occurred getting Bearer token')
    print(f'get_auth0_token :: completed\n')
    return req_resp.json()


def get_asset(bearer_token_, base_url_, asset_id_):
    print(f'get_asset :: starting')
    record_url = f'{base_url_}/assets/{asset_id_}'
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {bearer_token_}'
    }
    req_resp = requests.get(url=record_url, headers=headers,)
    if req_resp.status_code != requests.codes.ok:
        raise Exception(f'Error occurred calling API; {req_resp.json()}')
    rec_ = req_resp.json()
    name = ''
    if 'name' in rec_:
        name = rec_['name']
    print(f'get_asset :: {name} asset was found :: completed\n')
    return rec_


def search_asset(bearer_token_, base_url_, search_term_):
    print(f'search_asset :: starting')
    record_url = f'{base_url_}/assets?search={search_term_}'
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {bearer_token_}'
    }
    req_resp = requests.get(url=record_url, headers=headers,)
    if req_resp.status_code != requests.codes.ok:
        raise Exception(f'Error occurred calling API; {req_resp.json()}')
    recs_ = req_resp.json()
    print(f'search_asset :: {len(recs_["assets"])} assets were found :: completed\n')
    return recs_


if __name__ == '__main__':
    print(f'main :: Hello World')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-e', '--environment',
        help='The environment to be used',
        choices=['dev', 'prod'],
        default='dev',
    )
    parser.add_argument('-c', '--clientId', help='Auth0 Client Id', required=True)
    parser.add_argument('-s', '--clientSecret', help='Auth0 Client Secret', required=True)
    parser.add_argument('-a', '--assetId', help='The Asset Id that is to be looked up')
    parser.add_argument('-t', '--search', help='Search term to search against')
    args = parser.parse_args()

    token_obj = get_auth0_token(args.clientId, args.clientSecret)
    bearer_token = token_obj['access_token']
    if args.environment == 'prod':
        base_url = base_prod_url
    else:
        base_url = base_dev_url

    if args.assetId:
        rec = get_asset(bearer_token, base_url, args.assetId)
        filename = f'rec-{datetime.now().isoformat()}.json'
        with open(filename, 'w') as outfile:
            json.dump(rec, outfile)
    else:
        recs = search_asset(bearer_token, base_url, args.search)
        filename = f'recs-{datetime.now().isoformat()}.json'
        with open(filename, 'w') as outfile:
            json.dump(recs, outfile)

    print(f'main :: Goodbye World')

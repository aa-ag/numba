############------------ IMPORTS ------------############
from re import sub
from sys import pycache_prefix
import requests
from time import time, sleep
from numba.core.decorators import njit
from settings import token, email
from pprint import pprint


############------------ GLOBAL VARIABLE(S) ------------############
zd_token = token
zd_email_address = email
instance_url = 'https://z3n-platformdev-aaron.zendesk.com'


############------------ FUNCTION(S) ------------############
def get_tickets():
    get_tickets_endpoint = instance_url + '/api/v2/tickets'
    get_headers = {'Accept': 'application/json'}
    tickets = {'tickets': []}
    while get_tickets_endpoint:
        print(get_tickets_endpoint)
        response = requests.get(
                            get_tickets_endpoint,
                            auth=(zd_email_address+'/token', zd_token),
                            headers=get_headers
                        )

        if response.status_code == 429:
            sleep(int(response.headers['retry-after']))

        if response.status_code != 200:
            print(f'Status: {response.status_code}\n')
            print(response.text)
            exit()

        data = response.json()
        tickets['tickets'].append(data['tickets'])
        get_tickets_endpoint = data["next_page"]

    return tickets


def manipulate_tickets(tickets):
    pprint(tickets)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    tickets = get_tickets()
    start_time = time()
    manipulate_tickets(tickets)
    print(f"took: {time() - start_time} seconds")
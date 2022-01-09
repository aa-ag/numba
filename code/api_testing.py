############------------ IMPORTS ------------############
import requests
from time import time, sleep
from numba.core.decorators import njit
from settings import token, email


############------------ GLOBAL VARIABLE(S) ------------############
zd_token = token
zd_email_address = email
instance_url = 'https://z3n-platformdev-aaron.zendesk.com'


############------------ FUNCTION(S) ------------############
def count_tickets():
    count_tickets_endpoint = instance_url + '/api/v2/tickets/count'
    get_headers = {'Accept': 'application/json'}

    response = requests.get(
                        count_tickets_endpoint,
                        auth=(zd_email_address+'/token', zd_token),
                        headers=get_headers
                    )

    print(response.status_code)



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    count_tickets()
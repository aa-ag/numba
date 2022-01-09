############------------ IMPORTS ------------############
from time import time, sleep
from numba.core.decorators import njit
from .secrets import token, email


############------------ GLOBAL VARIABLE(S) ------------############
zd_token = token
zd_email_address = email
instance_url = 'https://z3n-platformdev-aaron.zendesk.com/'


############------------ FUNCTION(S) ------------############
def count_tickets():
    count_tickets_endpoint = '/api/v2/tickets/count'



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    count_tickets()
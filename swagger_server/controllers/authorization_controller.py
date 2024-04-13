from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_Basic(username, password, required_scopes):
    return {'test_key': 'test_value'}

def check_OAuth2(token):
    return {'scopes': ['accesslink.read_all', 'accesslink.write_all'], 'uid': 'test_value'}

def validate_scope_OAuth2(required_scopes, token_scopes):
    print(set(required_scopes).issubset(set(token_scopes)))
    print(required_scopes)
    print(token_scopes)
    return set(required_scopes).issubset(set(token_scopes))



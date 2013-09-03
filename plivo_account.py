import plivo


auth_id = ""
auth_token = ""

p = plivo.RestAPI(auth_id, auth_token)

# Get account
response = p.get_account()


# Delete subaccount
params = {
        'subauth_id': 'XXXXXXXXXXXXXXXXXX',
        }
response = p.delete_subaccount(params)


# Modify Account
params = {
        'name': 'Alice',
        'city': 'Wonderland',
        'address':'Rabbit hole'
        }
response = p.modify_account(params)




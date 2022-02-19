#!/usr/bin/python3
import sys
from twilio.rest import Client

#----------functions start----------

def get_account_information(sid, auth_token):
    account_sid = sid
    auth_token  = auth_token
    client = Client(account_sid, auth_token)
    return client

def send_text_message(client, to_number, account_number, message):
    try:
        message = client.messages.create(
            to=str(to_number), 
            from_=str(account_number),
            body=str(message))
        print('sent!')
    except:
        print('error')

    
#----------functions end----------

your_account_number = "YOUR ACCOUNT NUMBER HERE EX. +11111111111"
your_account_sid = "YOUR ACCOUNT SID EX. Feiakdj29e"
your_auth_token  = "YOUR AUTH TOKEN EX. Feakdjfie842k"
send_to = "TEXT TO NUMBER"


#---------get text message body from command line--------
arg_content = sys.argv[1:]
stringed_arg = ' '.join(arg_content)


#--------start of program------------
try:
    my_client_info = get_account_information(your_account_sid, your_auth_token)
    send_text_message(my_client_info, send_to, your_account_number, stringed_arg)
except:
    print('OOP Something went wrong, make sure your account number, sid, auth_token and sent to number are right')











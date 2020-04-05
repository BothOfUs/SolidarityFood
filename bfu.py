import os, slackclient
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_USER_TOKEN = os.environ.get('SLACK_USER_TOKEN')

# initialize slack client
SolidarityFood_client = slackclient.SlackClient(SLACK_BOT_TOKEN)
fsc = slackclient.SlackClient(SLACK_USER_TOKEN)

# check if everything is alright
print(SLACK_BOT_TOKEN)
print('Dayo')
is_ok = SolidarityFood_client.api_call("users.list").get('ok')
mem = SolidarityFood_client.api_call("users.list").get('members')
if(is_ok):
    for user in mem:
        
        usName = user.get('name')
        if (usName == 'food_bot_ish'):
            usId = user.get('id')
            print(usName, usId)
print(is_ok)

#SolidarityFood_client.api_call("chat.postMessage", channel="food_test", text="Dayo is the best")
#SolidarityFood_client.api_call("chat.postMessage", channel="general", text=" Thank you!")
history = fsc.api_call("groups.history", channel="food_test")
for message in history['messages']:
    print(message)
    if '/pool' in message:
        message=message.split(" ")
        del message[0]
        poolname=message
        text="Please! Give more details of the pool"
            SolidarityFood_client.api_call("chat.postMessage", channel="food_test", text=(poolname,text))

    #need to assign to the next coming message
    pooldes=message
    SolidarityFood_client.api_call("chat.postMessage", channel="food_test", text=("Pool",poolname,"has been created - ",pooldes))
    SolidarityFood_client.api_call("chat.postMessage", channel="food_test", text=(("Your pool is almost ready: Go to your specific pool page on, ",poolurl,"to add a catalogue and see the pool order recap."))
def excel():
    df = pd.read_excel('Book1.xlsx')    
    print(df)
    print(df['Name'])
    print(df['Price'])

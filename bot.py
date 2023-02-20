import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
import datetime
current_time = datetime.datetime.now()
logging.basicConfig(filename= current_time.strftime("%m-%d_%H-%M-%S") + ".log", format='%(asctime)s %(levelname)s %(message)s ', filemode='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
token= "#PUT_YOUR_TOKEN_HERE"
client = WebClient(token=token)
users= [ "person1", "person2", "person3", "person4"]
counter= 0
number_of_users= len(users)

while counter<number_of_users:
    try:
        user_name = user_name = "@" + str(users[counter])
        result = client.chat_postMessage(channel=user_name, text="")
        counter++1
        logger.info(user_name + "sent")
        time.sleep(0.5)
    except SlackApiError as e:
        logger.error(f"Error posting message: {e} to {user_name}")
        counter++1
        continue
        # print(f"Error posting message: {e} to {user_name}")
        # break

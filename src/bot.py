################## Library Area###############
import sys
import configparser
import requests
from urllib.parse import urlencode
##############################################
# Create config variable and call function sections()
config = configparser.ConfigParser()
config.sections()

#Read config file
config.read('../control/config.ini')

#Create and assign LINE_ACCESS_TOKEN variable from configuration file
LINE_ACCESS_TOKEN = config['credentials']['LINE_ACCESS_TOKEN']

# Create headers variable it will be used for Basic Authentication
headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Authorization' : 'Bearer ' + LINE_ACCESS_TOKEN
}

# Create msgTosend variable, it is a message will be sent to Line group
#msgTosend = sys.argv[1]
msgTosend = "ข้อความทดสอบ"

# Create msgTosend variable, it is just a format for send a message to Line
payLoad = {
            'message' : msgTosend,
            'stickerPackageId':'11538',
            'stickerId':'51626496'
}

#Call function urlencode() from from urllib.parse to encode before send to URL
payLoadEncoded = urlencode(payLoad)

# Create and assign endpoint variable from configuration file
# This is https://notify-api.line.me/api/notify
endpoint = config['endpoint']['url']

# Send all information to the endpoint by requests function
# It is basic HTML requests function
line_resp = requests.post(endpoint, headers=headers, data=payLoadEncoded)

# Check response from Line.
if line_resp.status_code == 200:
    print ("Notification has been sent on Line")
    print(str(line_resp.status_code)+" "+line_resp.text[:300])
else:
    print ("Could not send Message")
    print(str(line_resp.status_code)+" "+line_resp.text[:300])







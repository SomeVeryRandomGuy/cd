import tkinter
import requests
from datetime import datetime

TRACKING_NUMBER = "1LSCXM616219940"

response = requests.get(url=f"https://t.lasership.com/Track/1LSCXM616219940/json")

data = response.json()

now = datetime.now()
date_time_day = now.strftime("%a %m/%d/%Y %H:%M:%S %p")

order_num = data["OrderNumber"]
o_city = data["Origin"]["City"].capitalize()
o_state = data["Origin"]["State"]
o_zip = data["Origin"]["PostalCode"]
o_country = data["Origin"]["Country"]

ord = data["ReceivedOn"]
edd = data["EstimatedDeliveryDate"]

ord = ord[:10]
ord = ord.replace('-','/')

y = ord[:4]
ord = ord[5:10]

ord = ord+'/'+y

edd = edd[:10]
edd = edd.replace('-','/')

z = edd[:4]
edd = edd[5:10]

edd = edd+'/'+z

d_city = data["Destination"]["City"].capitalize()
d_state = data["Destination"]["State"]
d_zip = data["Destination"]["PostalCode"]
d_country = data["Destination"]["Country"]

item_info = data["Pieces"][0]

weight = item_info["Weight"]
unit = item_info["WeightUnit"]

tnum = item_info["TrackingNumber"]

tracking_file = open("tracking.txt", "w")
tracking_file.write(f'''Order Number: {order_num}
Tracking Number: {tnum}

Origin City: {o_city}
Origin State: {o_state}
Origin Zip Code: {o_zip}
Origin Country: {o_country}

Destination City: {d_city}
Destination State: {d_state}
Destination Zip Code: {d_zip}
Destination Country: {d_country}

Weight: {weight}{unit}

ESTIMATED DELIVERY DATE: {edd}
Order Recieved: {ord}

Last Updated: {date_time_day}

Order Summary: An order was recived from Nike on {ord} from {d_city}, {d_state}, {d_zip}. The item is currently in {o_city}, {o_state}, {o_zip} and will be delivered to {d_city}, {d_state}, {d_zip}. The item weighs {weight}{unit}. The estimated delivery date of this item is {edd}. This message was last updated at {date_time_day}. 
''')

tracking_file.close()
tracking_file = open("tracking.txt", "r")
print(tracking_file.read())
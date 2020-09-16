# time module for utility server
# returns user's time based on IPv4 address as well as time zone
# this API is slow at times, but easy to implement
# as a result it is possible to be off by a few seconds - not very desirable

from datetime import datetime
import urllib.request
import json

def current_time(**kwargs):
    ip_address = kwargs["ip_address"]
    source = urllib.request.urlopen(f'https://worldtimeapi.org/api/ip{ip_address}').read()
    time_data = json.loads(source)

    # this is the only data we need from the JSON response
    time_dict = {
        "time" : time_data['datetime'],
        "timezone" : time_data['timezone']
    }

    # make a datetime object from a slice of the datetime entry
    # in the JSON response and format it appropriately
    time_object = datetime.strptime(time_dict["time"][11:19], "%H:%M:%S")
    current_time = f"{time_object:%H:%M:%S}"

    return f"Current time {current_time}. Timezone: {time_dict['timezone']}."
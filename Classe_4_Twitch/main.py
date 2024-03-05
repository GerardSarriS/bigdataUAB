from twitchAPI.twitch import Twitch
import json
import time

# TWITCH API VERSION 2.5.7.1
# pip install twitchAPI==2.5.7.1
# DOCS https://pytwitchapi.readthedocs.io/en/v2.5.7/modules/twitchAPI.twitch.html

public = "xlq8lnzy1pc55rs3titydpvsgrygs6"
secret = "aw9jjj4tfqesrwt5nu8ct4jyaiewyc"

twitch = Twitch(public, secret)
after = None
loop=0
def get_live_streams(after,loop):
    results = twitch.get_streams(language="es", after=after, first = 100 )
    print(len(results["data"]))

    with open(f"{loop}.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    try:
        after = results["pagination"]["cursor"]
        print("hi ha nova pàgina")
        loop = loop+1
        time.sleep(2)
        get_live_streams(after,loop)

    except:
        print("final")
        pass



get_live_streams(after,loop)





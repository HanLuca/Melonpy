from melonapi import scrapeMelon
import json

dd= json.loads(scrapeMelon.getList('LIVE').decode()) # string -> dic
print(dd["1"])

# https://github.com/ko28/melon-api/blob/master/README.md
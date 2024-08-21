from melonapi import scrapeMelon
import json

MelonChart = json.loads(scrapeMelon.getList('LIVE').decode()) # string -> dic

for i in range(1, 101):
    print(
        MelonChart[str(i)],
        end= '\n'
    )


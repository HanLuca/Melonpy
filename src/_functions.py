from melonapi import scrapeMelon
import json

def listedMelonChart():
    MelonChart = json.loads(scrapeMelon.getList('LIVE').decode()) # string -> dic
    ListedMelonChart = []

    for i in range(1, 101):
        ListedMelonChart.append(MelonChart[str(i)])

    return ListedMelonChart

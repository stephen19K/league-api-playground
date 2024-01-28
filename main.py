from itertools import count
import cassiopeia as cass
from cassiopeia.cassiopeia import get_champion
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from cassiopeia import Summoner, Patch, Champions, Match, MatchHistory, Lane
from cassiopeia.data import Continent

"""
1. Get match history with date and time
    - can use DataFrame.from_dict()
    - cols: match_id, datetime, result(w/l)
        - additional cols that can derived: day_of_week, hour_of_day
2. Heatmap with x-axis: day of week | y-axis: time of day | intensity: # of matches

dataframe schema
     match_id    date    time    result(w/l)
    0
    1
    .
    .
"""
def main():
    API_KEY = "RGAPI-c9474098-f1de-497d-88c1-1a03efc96e05"
    NA = "NA"
    cass.set_riot_api_key(API_KEY)
    # all_champions = Champions(region="NA")
    # teemo = all_champions["Teemo"]
    platapierule = Summoner(name="platapierule", region=NA)
    mh = cass.get_match_history(puuid=platapierule.puuid, count=100, continent=Continent.americas
)
    # print(type(mh))
    # print(len(mh))
    # print(mh.start_time)
    match_history_dict = {}
    match_history_dict["match_id"] = []
    match_history_dict["start"] = []
    match_history_dict["result"] = []
    match_history_dict["day"] = []
    match_history_dict["hour"] = []
    recent = mh

    for match in recent:
        print(match.start, match.start.humanize())
        champion_played = match.participants[platapierule].champion
        print(champion_played, cass.get_champion(key=champion_played, region=NA))
        print("WINNNN???" + str(match.participants[platapierule].team.win))
        match_history_dict["match_id"].append(match.id)
        arrow = match.start.to('US/Pacific')
        match_history_dict["start"].append(arrow)
        match_history_dict["day"].append(arrow.format('dddd'))
        match_history_dict["hour"].append(arrow.format('H'))
        match_history_dict["result"].append(str(match.participants[platapierule].team.win))


    print(match_history_dict)
    match_data = pd.DataFrame.from_dict(match_history_dict) #.pivot(index="time_of_day", columns="day", values="count")
    pivot_match_data = match_data.pivot_table(index="hour", columns="day", values="match_id", aggfunc="count")
    # match_data['month'] = match_data.start.month
    print(match_data)
    print(pivot_match_data)

    seaborn.heatmap(pivot_match_data, annot=True)
    plt.show()


if __name__ == "__main__":
    main()

from itertools import count
import cassiopeia as cass
from cassiopeia.cassiopeia import get_champion
import pandas as pd
from cassiopeia import Summoner, Patch, Champions, Match, MatchHistory, Lane
from cassiopeia.data import Continent

"""
1. Get match history with date and time
2. Heatmap with x-axis: day of week | y-axis: time of day | intensity: # of matches

dataframe schema
     match_id    date    time    result(w/l)
    0
    1
    .
    .
"""
def main():
    API_KEY = "RGAPI-42f1303d-57b2-47ab-ad6a-e33923f1b699"
    NA = "NA"
    cass.set_riot_api_key(API_KEY)
    # all_champions = Champions(region="NA")
    # teemo = all_champions["Teemo"]
    platapierule = Summoner(name="platapierule", region=NA)
    mh = cass.get_match_history(puuid=platapierule.puuid, count=5, continent=Continent.americas
)
    # print(type(mh))
    # print(len(mh))
    # print(mh.start_time)
    recent = mh
    for match in recent:
        print(match.start)
        for p in match.participants:
            if p.summoner.name == "platapierule":
                print(p.champion, p.lane)
                # print(get_champion(key=p.champion.id, region=NA))

    # first_match = mh[0]
    # get match date
    # print(
    #     first_match.start,
    #     first_match.duration,
    #     first_match.blue_team.bans,
    #     first_match.continent,
    #     first_match.blue_team.win)
    # print(first_match)



if __name__ == "__main__":
    main()

from riotwatcher import LolWatcher, ApiError
import pandas as pd

# global vars
api_key= 'RGAPI-6134ca46-b79f-4c06-83a1-1a17d8961b81'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Bearly')
print(me)
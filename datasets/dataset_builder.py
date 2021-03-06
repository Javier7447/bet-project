from features.feature_factory import FeatureFactory
import pandas as pd
from datasets.game_dataset import game_dataset_builder
if __name__=='__main__':
#[TODO] PASS DF FOR EACH GAME WITH THE BASIC INFO: HOME-AWAY TEAM, MATCHWEEK, SEASON, COMPETITION 
    keys = ['home_team', 'away_team', 'season'
            , 'date', 'competition']
    matchhistorical = pd.read_pickle('files/match_historical_data_v2.pkl')
    df_games = game_dataset_builder()
    features =  FeatureFactory
    
    df = features.get_concrete('match win loss').calculate(matchhistorical, df_games)
    df = df_games.merge(df, on=keys, how='left')
    
    df_games = df_games.merge(features.get_concrete('probs end season')\
                            .calculate(matchhistorical, df_games)\
                            , on=keys, how='left')


    print(1)
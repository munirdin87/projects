# this is a simple code to get google search numbers for a word.

# import packages

from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# define a function for this simple task

def get_searches ( key_word, state, time_frame ):
    
    pytrends = TrendReq(hl = 'en-US', tz = 360)
    pytrends.build_payload([key_word], cat= 0, timeframe= '{}'.format(time_frame),
                           gprop='', geo='US-{}'.format(state))
    df = pytrends.interest_over_time()
    print(df.head())

    sns.set()
    df['timestamp'] = pd.to_datetime(df.index)
    sns.lineplot(df['timestamp'], df[key_word])

    plt.title("Normalized search for {} in {}".format(key_word, state))
    plt.xlabel("Date")
    plt.ylabel("Number of search ")
    plt.show()


# here you can put search word, State code and time frame
# time frame should be in this format 'YYYY-MM-DD YYYY-MM-DD'

get_searches('Corona', 'NY', '2020-03-01 2020-03-30') 

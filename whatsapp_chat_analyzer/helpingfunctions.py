import re
import pandas as pd
from collections import Counter
import emoji

def general_stats(df):
    
    t_msg = df.shape[0] #total messages of selected user

    words = [] #total words typed
    links = [] #links send
    for message in df['message']:
        words.extend(message.split())
        url = re.findall('(?P<url>https?://[^\s]+)', message)
        links.extend(url)

    numfmedia = df[df['message'] == '<Media omitted>'].shape[0]

    return t_msg, len(words), len(links), numfmedia

def monthly_timeline(df):
    monthdf = df.groupby('month').count()['message'].reset_index()
     
    return monthdf

def daily_activity(df):
    daily_df = df.groupby('dateOnly').count()['message'].reset_index()

    return daily_df

def activity_map(df):
    days_of_week = df['day'].unique().tolist()
    msg_on_day = []
    for day in days_of_week:
        unidadf = df[df['day'] == day].shape[0]
        msg_on_day.append(unidadf)

    return days_of_week, msg_on_day
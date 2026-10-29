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

def plot_heatmap(df):
    heatmapdf = df.pivot_table(index='day', columns='period', values='message', aggfunc='count').fillna(0)

    return heatmapdf

def filterWords(df):
    msg = " ".join(df.message).lower()
    stopword = open(r".\stop_hinglish.txt").read()

    for word in msg.lower().split():
        if word in stopword:
            msg.replace(word,"")
    split_txt = msg.split()
    counter = Counter(split_txt)
    freq_wrd = counter.most_common(8)

    return msg, freq_wrd

def most_busy_user(df):
    mbudf = df.groupby('users').count().sort_values(by=['message'], ascending=False)['message'].reset_index()
    return mbudf

def emoji_counter(df):
    emojilist = df['message'].apply(lambda x: ' '.join([e for e in x if e in emoji.EMOJI_DATA]))
    emojistr = ' '.join([e for e in emojilist if e != " "])
    counter = Counter(emojistr.split())
    common_emjsdf = pd.DataFrame(counter.most_common(5))

    return common_emjsdf
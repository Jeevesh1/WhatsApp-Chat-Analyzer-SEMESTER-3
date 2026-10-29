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
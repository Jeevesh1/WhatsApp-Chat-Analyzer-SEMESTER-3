
import re
import pandas as pd

def preprocessor(data):
    #patter for separating d_np and messages from data(whatsapp file)
    messagesFind_pattern = r"\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}:\d{1,2}\s[APap][Mm]\]\s"

    # To extract just the date-time string:
    dateFind_pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}:\d{1,2}\s[APap][Mm]"

    messages_np = re.split(messagesFind_pattern, data)[1:]
    d_np = re.findall(dateFind_pattern, data)
    
    #creating a dataframe
    df = pd.DataFrame({'m_np': messages_np, 'd_np': d_np})
    df['d_np'] = pd.to_datetime(df['d_np'], format="%m/%d/%y, %I:%M:%S %p") #converting d_np to datetime datatype

    #extracting users and messages from m_np column and adding to df
    users = []
    messages = []
    for message in df['m_np']:
        processed = re.split("([\w\W]+?):\s", message)
        if len(processed) > 1:
            users.append(processed[1])
            messages.append(processed[2])
        else:
            users.append("group notification")
            messages.append(processed[0])
    
    df['users'] = users
    df['message'] = messages
    df['message'] = df['message'].apply(lambda x: x.replace("\n", '')) 

    #adding some more required columns to df
    df['year'] = df['d_np'].dt.year
    df['month'] = df['d_np'].dt.month_name()   #--> to get full names of the month
    df['date'] = df['d_np'].dt.day
    df['hour'] = df['d_np'].dt.hour
    df['minute'] = df['d_np'].dt.minute
    df['dateOnly'] = df['d_np'].dt.date
    df['day'] = df['dateOnly'].apply(lambda x: pd.Timestamp(x).day_name())
    df['period'] = df['hour'].apply(lambda x: f"{str(x)}-{str(x+1)}" if x!=24 else "")

    return df
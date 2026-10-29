import streamlit as st
import filePreprocessor
from helpingfunctions import *
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


with st.sidebar:
    st.title("Whatsapp Chat Analyzer")
    upload_file = st.file_uploader("Upload File")

if upload_file is not None:
    #read upload_file
    data = upload_file.getvalue().decode("utf-8")
    df = filePreprocessor.preprocessor(data)

    #extracting all users
    user_list = df['users'].unique().tolist()
    
    try: 
        user_list.remove('group notification')
    except Exception as e:
        pass
    user_list.insert(0, 'All Users')
    selected_user = st.sidebar.selectbox(user_list[0], user_list)
    bt = st.sidebar.button("Show Analysis")
    
    # data presentation
    if bt:
        if selected_user != 'All Users':
            df = df[df['users'] == selected_user]
        else:
            df = df.drop(df[df['users'] == 'group notification'].index)

        t_msg, t_words, t_links, t_media = general_stats(df)
        
        col1, col2, col3, col4 = st.columns(4) #creating 4 columns

        #writing data in columns
        with col1:
            st.title('Total Messages')
            st.header(str(t_msg))
        with col2:
            st.title('Total Words')
            st.header(str(t_words))
        with col3:
            st.title("Links Shared")
            st.header(str(t_links))
        with col4:
            st.title('Media Shared')
            st.header(str(t_media))

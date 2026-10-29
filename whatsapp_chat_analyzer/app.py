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

        # Plotting monthly Timeline graph
        st.title('Monthly Timeline')
        monthdf = monthly_timeline(df)
        fig = plt.figure()
        plt.plot(monthdf['month'], monthdf['message'])
        st.pyplot(fig)

        # Plotting Daiyly Timeline
        st.title('Daily Timeline')
        dailydf = daily_activity(df)
        fig = plt.figure()
        plt.plot(dailydf['dateOnly'], dailydf['message'])
        fig.autofmt_xdate()
        st.pyplot(fig)
        
        # Plotting activity map
        st.title('Activity Map')
        days_of_week,msg_on_day = activity_map(df)
        col1,col2 = st.columns(2)
        with col1:
            st.subheader('Busy Days')
            fig = plt.figure()
            plt.bar(days_of_week, msg_on_day)
            fig.autofmt_xdate()
            st.pyplot(fig)
        with col2:
            st.subheader('Busy Months')
            fig = plt.figure()
            plt.bar(monthdf['month'], monthdf['message'])
            fig.autofmt_xdate()
            st.pyplot(fig)

        # Plotting timewise heatmap according to day
        st.title('Weekly Activity Map')
        fig = plt.figure(figsize=(10,5))
        heatmapdf = plot_heatmap(df)
        sns.heatmap(heatmapdf)
        st.pyplot(fig)

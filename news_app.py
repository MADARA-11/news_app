import streamlit as st
import json
import requests

# Hyper Text Markup Language

st.title("Daily news Application📰📰🗞️")

api_key = "4782dcab85cd41bab6a109e323a3ce03"

topic = st.text_input("Enter any news topic: ")
page = st.number_input('how many articles do you need ?',min_value=1)
base_url =f"https://newsapi.org/v2/everything?q={topic}&apiKey=4782dcab85cd41bab6a109e323a3ce03"

p = {

    'q': topic,
    "apikey":api_key,
    "pageSize": page
}


if st.button("Display News"):
    response = requests.get(base_url,params=p)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        st.subheader("Headlines")


        for articles in articles:
            title = articles["title"]
            url = articles["url"]
            desc = articles["description"]
            image = articles["urlToImage"]


            html_code = f"""
            <div class = "news">
            <h2>{title}</h2>
            <p> link to the article : <a href = "{url}">{url}</a> </p>
            <p> {desc} </p>
            <img src = "{image}">
            </div>
            
            """


            css_code = """
            <style>
            .news{
              background-color : #fa9605;
              # height : 400px;
              width : 700px;
              border-radius : 15px;
              border-left : 7px solid black;
              padding : 10px;
              margin : 40px;
            }
            </style>
            
            
            
            
            """

            st.markdown(html_code,unsafe_allow_html=True)
            st.markdown(css_code,unsafe_allow_html=True)

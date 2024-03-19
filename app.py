import streamlit as st
import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="WikiStream", page_icon="ℹ️")

st.markdown("<h3 style='color: #22ebff;'>Wiki-Fetch</h3>", unsafe_allow_html=True)


st.write('---')

def load_lottier(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

img_link = load_lottier('https://lottie.host/b8bcd790-53ce-43fa-b9f5-216e2bf63c71/5Bwne8xCwL.json')

def magic():
    st.toast("woah......!🎉")
    time.sleep(0.1)
    st.toast("This is not chatGPT,info is from wiki😁")
    time.sleep(0.2)
    st.toast("this will only generate 200 words from wiki,stay tune for more updates.....")
    

prompt = st.chat_input("Enter the Topic: ")

def generate_link(prompt):
    if prompt:
        return "https://www.google.com/search?q=" + prompt.replace(" ", "+") + "+wiki"
    else:
        return None

link = generate_link(prompt)

def generating_wiki_link(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    for sp in soup.find_all("div"):
        try:
            link = sp.find('a').get('href')
            if 'en.wikipedia.org' in link:
                actual_link = link[7:].split('&')[0]
                return scraping_data(actual_link)
                break
        except:
            pass

def scraping_data(link):
    actual_link = link
    res = requests.get(actual_link)
    soup = BeautifulSoup(res.text, 'html.parser')
    corpus = ""
    for i in soup.find_all('p'):
        corpus += i.text
        corpus += '\n'
    corpus = corpus.strip()
    for i in range(1, 500):
        corpus = corpus.replace('['+str(i)+']', " ")

    word_count = 0
    for word in corpus.split():
        if word.lower() == "i":
            yield "I "
        else:
            yield word + " "
        word_count += 1
        if word_count >= 200:
            break
        time.sleep(0.2)


if img_link and not link:  
    with st.container():
        st_lottie(img_link, height=350, width=350, key="centered_img")

if link:
    with st.container(border=True):
       with st.chat_message('assistant'):
           
           magic()
           st.write(generating_wiki_link(link))
           

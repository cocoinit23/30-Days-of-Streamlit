import datetime
import time

import altair as alt
import numpy as np
import pandas as pd
import requests
import streamlit as st

st.set_page_config(layout="wide")
st.title("how to lay out your streamlit app")

with st.expander("about this app"):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header("input")
user_name = st.sidebar.text_input("what is your name?")
user_emoji = st.sidebar.selectbox("choose an emoji", ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?',
                                 ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header("output")
col1, col2, col3 = st.columns(3)

with col1:
    if user_name != "":
        st.write(f"hello {user_name}")
    else:
        st.write("please enter your **name**")

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')

with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')

st.write("hello world!")

st.header("st.button")

if st.button("say hello"):
    st.write("why hello there")
else:
    st.write("goodbye")

st.header("st.write")

st.write('hello *world* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [11, 22, 33, 44]
})
st.write(df)

st.write('below is a df:', df, 'above is a df')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)

st.header('st.slider')

st.subheader('slider')

age = st.slider('how old are you?', 0, 130, 25)
st.write("I'm", age, 'years old')

st.subheader('range slider')

values = st.slider(
    'select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('values:', values)

st.subheader('range time slider')

appointment = st.slider(
    'schedule your appointment:',
    value=(datetime.time(11, 30), datetime.time(12, 45))
)
st.write("you are scheduled for:", appointment)

st.subheader("datetime slider")

start_time = st.slider(
    "when do you start?",
    value=datetime.datetime(2020, 1, 1, 9, 30),
    format="YY/MM/DD - hh:mm"
)
st.write("start time:", start_time)

st.header("line chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=list("abc")
)

st.line_chart(chart_data)

st.header("st.selectbox")

option = st.selectbox(
    "what is your favourite color?",
    ('blue', 'red', 'green')
)
st.write("your favourite color is ", option)

st.header("st.multiselect")

options = st.multiselect(
    "what are your favourite colors",
    ["green", "yellow", "red", "blue"],
    ["yellow", "red"]
)

st.write("you selected:", options)

st.header("st.checkbox")

st.write("what would you like to order?")

icecream = st.checkbox("ice cream")
coffee = st.checkbox("coffee")
cola = st.checkbox("cola")

if icecream:
    st.write("here's some more icecream")

if coffee:
    st.write("here's some coffee")

if cola:
    st.write("here you go cola")

st.header("st.latex")

st.latex(r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     """)

st.title("st.file_uploader")

st.subheader("input csv")
uploaded_file = st.file_uploader("choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("dataframe")
    st.write(df)
    st.subheader("descriptive statistics")
    st.write(df.describe())
else:
    st.info("upload a csv file")

st.title("st.progress")

with st.expander("about this app"):
    st.write("you can now display the progress")

my_bar = st.progress(0)

for i in range(100):
    # time.sleep(0.01)
    my_bar.progress(i + 1)
# st.balloons()

st.header("1. example of using 'with' notation")
st.subheader("coffee machine")

with st.form("my_form"):
    st.subheader("**order your coffee**")

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

st.header("2. example of object notation")

form = st.form("my_form_2")
selected_val = form.slider("select a balue")
form.form_submit_button("submit")

st.write("selected value: ", selected_val)

st.title("st.cache")

a0 = time.time()
st.subheader("using st.cache")


@st.cache_data
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=list("abcde")
    )
    return df


st.write(load_data_a())
a1 = time.time()
st.info(a1 - a0)

b0 = time.time()
st.subheader("not using st.cache")


def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=list("abcde")
    )
    return df


st.write(load_data_b())
b1 = time.time()
st.info(b1 - b0)

st.title("st.session_state")


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.lbs * 2.2046


st.header("input")

col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("ponds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilogram = st.number_input("kilograms:", key="kg", on_change=kg_to_lbs)

st.header("output")
st.write("st.session_state object:", st.session_state)

st.title("Bored API app")
selected_type = st.sidebar.selectbox('Select an activity type',
                                     ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation",
                                      "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
    with st.expander("about this app"):
        st.write("This app is powered by the Bored API")
with c2:
    with st.expander("JSON data"):
        st.write(suggested_activity)

st.header("suggested activity")
st.info(suggested_activity["activity"])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="number of participants", value=suggested_activity["participants"])
with col2:
    st.metric(label="type of activity", value=suggested_activity["type"])
with col3:
    st.metric(label="price", value=suggested_activity["price"])
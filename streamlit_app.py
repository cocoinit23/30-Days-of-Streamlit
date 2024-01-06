from datetime import time, datetime

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

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
    value=(time(11, 30), time(12, 45))
)
st.write("you are scheduled for:", appointment)

st.subheader("datetime slider")

start_time = st.slider(
    "when do you start?",
    value=datetime(2020, 1, 1, 9, 30),
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
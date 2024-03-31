import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))


# 1. Display text
st.write('Hello world')

# 2. Display a title and some text to the app:
st.write('''
# This is the document title
This is some _markdown_.
''')

# 3. Display the dataframe
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
st.write(df) 

# 4. Display the string 'x' and then the value of x
x = 10
st.write('x', x)

# 5. Display Matplotlib chart
y = np.random.normal(0, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(y, bins=20)

st.write(fig)


def section_1():
    st.header("Section 1")
    st.write("This is the content of section 1.")
    # Add more content for section 1 as needed

def section_2():
    st.header("Section 2")
    st.write("This is the content of section 2.")
    # Add more content for section 2 as needed

def section_3():
    st.header("Section 3")
    st.write("This is the content of section 3.")
    # Add more content for section 3 as needed

st.title("Multi-Section Streamlit App")

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Section 1", "Section 2", "Section 3"])
# Display selected section
if selection == "Section 1":
    section_1()
elif selection == "Section 2":
    section_2()
elif selection == "Section 3":
    section_3()
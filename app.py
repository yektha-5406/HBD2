import streamlit as st

# Page config
st.set_page_config(page_title="Birthday Wishes 🎂", page_icon="🎉")

# Custom CSS (like your Flask styling)
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, pink, purple);
    }
    .title {
        text-align: center;
        color: white;
        font-size: 40px;
    }
    .wish {
        text-align: center;
        color: white;
        font-size: 35px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1 class="title">🎉 Birthday Wishes App 🎉</h1>', unsafe_allow_html=True)

# Input
name = st.text_input("Enter your friend's name")

# Button
if st.button("Send Wish 🎂"):
    if name:
        st.markdown(
            f'<h1 class="wish">🎂 Happy Birthday {name}! 🎉</h1>',
            unsafe_allow_html=True
        )
        st.write("💖 Wishing you lots of happiness and success!")
    else:
        st.warning("Please enter a name!")

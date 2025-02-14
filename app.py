import streamlit as st
import datetime
import time
import PIL


# Page configuration
st.set_page_config(page_title="Yap Queen", page_icon="🗣️", layout="centered")

# Header with animation
st.title("Hi Sam, Happy Valentine's Day! ")
st.title("To My Yap Queen ")

# Section 1: The Place Where It All Started
st.markdown(" **The Place Where It All Started**")
st.markdown("""
<div class='card'>
    <p><b>Place:</b> In front of Christ University Yeshwantpur Campus</p>
    <p>That day we ended up going to Chin Lung! It was so fun, and whatever happened the second time in that volleyball ground XD</p>
</div>
""", unsafe_allow_html=True)

# Section 2: Photo Album with Interactive Dropdown
st.header(" **Our Moments Together**")
photos = {
    "Photo 1": "photos/photo1.jpg",  # Replace these paths with actual image paths
    "Photo 2": "photos/photo2.jpg",
    "Photo 3": "photos/photo3.jpg",
    "Photo 4": "photos/photo4.jpg",
    "Photo 5": "photos/photo5.jpg"
}

# Dropdown for selecting a photo
selected_photo_caption = st.selectbox(
    "Scroll through our favorite memories",
    list(photos.keys())
)

selected_photo = photos[selected_photo_caption]
st.image(selected_photo, caption=selected_photo_caption, use_column_width=True)

# Button to start slideshow
if st.button("Start Slideshow"):
    st.write("Enjoy the slideshow! ")
    for caption, photo in photos.items():
        st.image(photo, caption=caption, use_column_width=True)
        time.sleep(2)

# Section 3: Voice Note
st.header(" **A Message from Me to You**")
st.markdown("Click below to hear my special Valentine’s Day message for you:")
st.audio("voice_note.mp3")  # Replace with the actual file path to your voice note

# Section 4: Thank You Note
st.header(" **Thank You for the Flowers**")
st.markdown("""
<div class='card'>
    <p>I keep the flowers by my desk all day.  Let’s not forget about the hair tie hehehe!</p>
    <p>You have the most thoughtful and kind heart, and I’m so lucky to yap with you every single day!</p>
</div>
""", unsafe_allow_html=True)

# Footer with personal touch
st.write("I will see you soon! ")
st.markdown("<div class='footer'>Made with love, you know who heheheh</div>", unsafe_allow_html=True)

st.write("We need to watch The Departed Movie and get Whiskey n beer.")

st.text("© 2025 Yap Queen Certified. All rights reserved. ")

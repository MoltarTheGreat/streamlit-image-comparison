from PIL import Image
import streamlit as st
from streamlit_image_comparison import image_comparison


IMAGE_TO_URL = {
    "sample_image_1": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",
    "sample_image_2": "https://user-images.githubusercontent.com/34196005/143309867-42841f5a-9181-4d22-b570-65f90f2da231.jpg",
}


st.set_page_config(
    page_title="Streamlit Image Comparison",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="auto",
)


st.write("## Image Comparison Tool")
st.write("Upload two images and use a slider to compare them.")

def load_image(image_file):
	img = Image.open(image_file)
	return img

with st.form(key="Streamlit Image Comparison"):
    # image one inputs
    col1, col2 = st.sidebar.columns([3, 1])
    img1_url = IMAGE_TO_URL["sample_image_1"]
    with col1:
        img1 = st.sidebar.file_uploader("Left Image", type=["png", "jpg", "jpeg"])
    with col2:
        img1_text = st.sidebar.text_input("Left Label:", value="Original")
    
    if img1 is not None:
        img1_url = Image.open(img1)

    # image two inputs
    col1, col2 = st.sidebar.columns([3, 1])
    img2_url = IMAGE_TO_URL["sample_image_2"]
    with col1:
        img2 = st.sidebar.file_uploader("Right Image", type=["png", "jpg", "jpeg"])
    with col2:
        img2_text = st.sidebar.text_input("Right Label:", value="Enhanced")

    if img2 is not None:
        img2_url = Image.open(img2)
        
    # continious parameters
    col1, col2 = st.sidebar.columns([1, 1])
    with col1:
        starting_position = st.sidebar.slider(
            "Starting position of the slider:", min_value=0, max_value=100, value=50
        )
    with col2:
        width = st.sidebar.slider(
            "Component width:", min_value=400, max_value=1000, value=700, step=100
        )

    # boolean parameters
    col1, col2 = st.sidebar.columns([1, 1])
    with col2:
        show_labels = st.sidebar.checkbox("Show labels", value=True)

static_component = image_comparison(
    img1=img1_url,
    img2=img2_url,
    label1=img1_text,
    label2=img2_text,
    width=width,
    starting_position=starting_position,
    show_labels=show_labels,
    make_responsive=False,
    in_memory=False,
)

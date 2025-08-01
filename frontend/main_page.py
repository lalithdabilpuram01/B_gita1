
import streamlit as st
import sys
import os
import base64




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))



try:
    from codeB import ask_gita

except ImportError as e:
    st.error(f"Import error: {e}.")

def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

#  Provide the path to your local image
image_path =  "images/gita_bg2.jpg"  # ✅ Change this to your image file name
encoded_image = get_base64_of_image(image_path)

#  Inject CSS with the encoded image
st.markdown(
    f"""
    <style>
    /*  Set background image with 40% brightness */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(data:image/jpeg;base64,{encoded_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }}

    /*  White floating cards with slight transparency for contrast */
    .card {{
        background: rgba(255, 255, 255, 0.9);  /* Slightly transparent white */
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }}

    /*  Title vibrant and bold with high contrast */
    h1 {{
        color: #ffd700;  /* Vibrant gold for title */
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
        text-align: center;
        font-size: 50px;
        font-weight: bold;
    }}

    /* ✍ Subheaders and text with vibrant colors */
    h2, .stMarkdown, .stTextInput label {{
        color: #ffffff;  /* White text for high contrast */
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.7);
    }}

    /*  Textareas bright and clear */
    textarea, .stTextInput input {{
        background: #ffffff !important;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        color: #000000;
        border: 2px solid #28a745;  /* Vibrant green border */
    }}

    /*  Buttons vibrant and bold */
    .stButton>button {{
        background-color: #ff4500;  /* Vibrant orange-red */
        color: white;
        font-weight: bold;
        font-size: 16px;
        padding: 12px 20px;
        border-radius: 8px;
        border: none;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
        transition: background-color 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: #e63900;  /* Darker orange-red on hover */
    }}

    /*  Ensure text output is vibrant and readable */
    .stWrite, .stMarkdown p {{
        color: #f0f0f0;  /* Light gray for readability */
        font-size: 16px;
        font-weight: 500;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }}
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("<h1 style='text-align: center; font-size: 50px; font-weight: bold;'>Get Answers From Bhagavad Gita</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)




if 'answer' not in st.session_state :
    st.session_state.answer = ""

if 'question' not in st.session_state:
    st.session_state.question = ""

with col1 :

    st.subheader(" Question.")
    st.session_state.question = st.text_input("Enter Your Question " , value= st.session_state.question)
    if st.button("Submit") :
        st.session_state.answer = ask_gita(st.session_state.question)

    st.markdown('</div>', unsafe_allow_html=True)
with col2 :

    st.subheader("Answer from Bagavad gita ")
    st.write(st.session_state.answer if st.session_state.answer else "Your answer will appear here.")
    st.markdown('</div>', unsafe_allow_html=True)
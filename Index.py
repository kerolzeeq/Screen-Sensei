import streamlit as st
from streamlit_chat import message as st_message
import openai

@st.experimental_singleton
def load_model():
    openai.api_key = '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'
    
load_model()

with st.columns(3)[1]:
     st.image('Sensei Screen Logo2.png')
     

st.markdown("<h2 style='text-align: center; color: white;'>Welcome to Sensei Screen!</h2>", unsafe_allow_html=True)

messages = [
        {"role": "system", "content": "You are an expert assistant in movies and films"}
    ]


if "history" not in st.session_state:
    st.session_state.history = []



# history = [
#     {
#         "message": "My message",
#         "is_user": False
#     },
#     {
#         "message": "Hello bot",
#         "is_user": True
#     }
# ]

def generate_answer():

    user_message = st.session_state.input_text
    
    if user_message:
        messages.append(
            {"role": "system", "content": user_message}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    bot_message = chat.choices[0].message.content
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": bot_message, "is_user": False})
    messages.append({"role": "assistant", "content": bot_message})

st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat) #unpacking

def restart_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

if st.button('Restart the session'):
        restart_session()
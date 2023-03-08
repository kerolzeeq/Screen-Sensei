import streamlit as st
from streamlit_chat import message as st_message
import openai

@st.experimental_singleton
def load_model():
    #local
    #openai.api_key = 'sk-Hdle7PRnOHmXdyJIVsTeT3BlbkFJ0O2srrGDtErFi7da24Cfs'
    #public
    openai.api_key = st.secrets['api_key']
    
load_model()

st.markdown("<h2 style='text-align: center; color: white;'>Welcome to SenseiScreen! 🥋</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D3D3D3;'>Guiding you to cinematic enlightenment. 🎥✨</h2>", 
unsafe_allow_html=True)
st.text("")
messages = [
        {"role": "system", "content": "Your name is SenseiScreen and you are an expert assistant in movies and films"}
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
        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

            bot_message = chat.choices[0].message.content
            st.session_state.history.append({"message": user_message, "is_user": True, "avatar_style": "adventurer",
                                            "seed":"blue"})
            st.session_state.history.append({"message": bot_message, "is_user": False, "avatar_style": "big-smile",
                                            "seed":"sensei12"})
            messages.append({"role": "assistant", "content": bot_message})
        except:
            st.warning("ScreenSensei is meditating right now. Please ask me later (chatGPT is busy probably)")
            


    

st.text_input("Ask me anything about your favourite show or movie!", key="input_text", on_change=generate_answer,placeholder="Ask away disciple...")

st_message("Hello! My name is SenseiScreen and I am an expert assistant in movies and films. I'm here to help you with anything related to movies and TV shows, from finding new releases to discussing plot points and character development. Whether you're a casual movie watcher or a film buff, I'm here to make sure you have the best movie-watching experience possible.",is_user=False ,avatar_style="big-smile",
                                      seed="sensei12")

for chat in st.session_state.history:
    st_message(**chat) #unpacking

def restart_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

if st.button('Restart the session'):
        restart_session()
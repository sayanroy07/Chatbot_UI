import streamlit as st
import random
import time

#Sidebar Details
with st.sidebar:
    st.markdown('''
    # Description:
    The purpose of this application is to be able to let the user select the type of LLM they want to use: 
    - Streamlit - https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
    - My Github Link - https://github.com/sayanroy07
    ''')
    st.write("Developed by Sayan Roy - 🤓")
def gpt():
    response = """Implementing a Chat Bot using GPT follows certain steps 
    including, having access to OpenAI account followed by using OpenAI
     Embeddings & eventually create an api_key & use it with any gpt model
    
    """
    for word in response.split():
        yield word + " "
        time.sleep(0.1)


def llama():
    response = """Implementing a Chat Bot using Llama-2 follows certain steps 
    including, having access to HuggingFace account followed by downloading a quantized version of the model.
    We can use either CTransformer/CPP-PYTHON as wrapper & HuggingFace Embeddings & 
    & use it within langchain

    """
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

def others():
    response = """There are multiple free tier/open source LLMs availabe within HuggingFace, use them accordingly
    """
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

st.title("💻 Sample Chat Bot Interface 💻")
st.title(' ☑ ')
option = st.selectbox('Which LLM would you prefer:',('<Select>','GPT', 'Llama-2', 'Let me Select'))
if option is not '<Select>':
    if option is "GPT":
        st.write("Please use this Link to get GPT related informations")
        st.write("▶ https://openai.com/")



        # Streamed response emulator
        def response_generator():
            response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            for word in response.split():
                yield word + " "
                time.sleep(0.05)


        st.title("Simple chat")

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask me Anything?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(gpt())
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            #st.write_stream(gpt())
    elif option is "Llama-2":
        st.write("Please use this Link to get Llama-2 related informations")
        st.write("▶ https://llama.meta.com/")



        # Streamed response emulator
        def response_generator():
            response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            for word in response.split():
                yield word + " "
                time.sleep(0.05)


        st.title("Simple chat")

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask me Anything?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(llama())
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            #st.write_stream(llama())
    else:
        st.write("Please visit Huggingface & select as per your need - https://huggingface.co/models")



        # Streamed response emulator
        def response_generator():
            response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            for word in response.split():
                yield word + " "
                time.sleep(0.05)


        st.title("Simple chat")

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask me Anything?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(others())
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            #st.write_stream(others())


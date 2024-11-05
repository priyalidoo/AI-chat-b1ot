import streamlit as st
import chatbot_backend as demo

st.title("Hi, this is chatbot Priya 😎")

# Initialize memory and chat history in session state if not present
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])

# Get user input
input_text = st.chat_input("What is up?")
if input_text:
    # Display user input in chat
    with st.chat_message("user"):
        st.markdown(input_text)
    # Append user input to chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Generate and display chatbot response
    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)
    with st.chat_message("assistant"):
        st.markdown(chat_response)
    # Append chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})

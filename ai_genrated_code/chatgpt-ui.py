import streamlit as st
from datetime import datetime

def format_message(sender, message, timestamp):
    return f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {sender}: {message}"

def main():
    st.title("ChatGPT Demo")
    st.sidebar.title("Settings")

    with st.sidebar:
        st.subheader("User Settings")
        user_name = st.text_input("Your Name", "User")

    messages = []
    chat_input = st.text_area("Type a message...", key="input_field")
    if st.button("Send"):
        if chat_input.strip() != "":
            current_time = datetime.now()
            messages.append(format_message(user_name, chat_input, current_time))
            st.session_state.input_field = ""
    
    if messages:
        st.markdown("---")
        st.text("\n\n".join(messages))

if __name__ == "__main__":
    main()

import streamlit as st

# Streamlit app initialization
st.set_page_config(page_title="Gemini AI Chatbot", layout="wide")
st.title("Gemini AI Chatbot 🤖")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to get dummy response
def get_dummy_response(query):
    # Dummy responses based on the input query
    dummy_responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm a bot, but I'm functioning as expected! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    # Return the response based on the query, or a default response
    return dummy_responses.get(query.lower(), "I'm not sure how to respond to that.")

# Display chat history above input
st.subheader("Chat History")
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['query']}")
    st.markdown(f"**Bot:** {chat['response']}")
    st.markdown("---")

# Text input for user queries
st.subheader("Your Message")
user_input = st.text_input("Type your message here:")

# Button to send the query
if st.button("Send"):
    if user_input:
        # Get response from dummy data
        response = get_dummy_response(user_input)
        
        # Append query and response to chat history
        st.session_state.chat_history.append({"query": user_input, "response": response})
        
        # Clear input box after submission
        st.session_state["user_input"] = ""
        st.experimental_rerun()  # Automatically refresh to clear input field

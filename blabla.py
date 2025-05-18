import nltk
from nltk.chat.util import Chat, reflections
import streamlit as st
import speech_recognition as sr
import random
import re

# ✨ SMART pattern cleaner (no re.escape)
def clean_pattern(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text)     # normalize whitespace
    return text

# 🔄 Load dialogue pairs from empress.txt in "User: ... || Bot: ..." format
def load_dialogue_pairs(filepath):
    pairs = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Match User and Bot parts
            if "||" not in line:
                continue
            user_part, bot_part = line.split("||", 1)
            
            # Extract text after "User:" and "Bot:" respectively, strip and clean user input
            user_text_match = re.match(r"User:\s*(.*)", user_part.strip(), re.I)
            bot_text_match = re.match(r"Bot:\s*(.*)", bot_part.strip(), re.I)
            
            if user_text_match and bot_text_match:
                user_text = clean_pattern(user_text_match.group(1))
                bot_text = bot_text_match.group(1).strip()
                if user_text and bot_text:
                    pattern = rf"^{user_text}"
                    pairs.append((pattern, [bot_text]))
    return pairs

# 🎤 Speech-to-text
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        st.error("Could not request results from the speech recognition service.")
        return ""

# 🔮 Special keyword triggers for Empress chatbot
def check_special_keywords(user_input):
    keyword_responses = {
        "empress": "Ah, my glorious Empress, your reign shines brighter than a thousand suns!",
        "kingdom": "Every kingdom listens to your command, wise and powerful.",
        "sun": "Like the sun, your light guides us through darkness.",
        "help": "Fear not, for I am here to assist you with all the kingdom's mysteries.",
        "secret": "Ah, a secret whispered... only the worthy shall hear it.",
        "unknown": "When the unknown calls, your wisdom shall lead the way.",
    }
    cleaned = clean_pattern(user_input)
    for keyword, reply in keyword_responses.items():
        if keyword in cleaned:
            return reply
    return None

# 🧠 Chatbot with fallback
def create_chatbot(pairs):
    fallback = [(r".*", ["Hmm... I don't quite get that. Try saying something else?"])]
    valid_pairs = []
    for pattern, responses in pairs:
        try:
            re.compile(pattern)
            valid_pairs.append((pattern, responses))
        except re.error:
            continue
    return Chat(valid_pairs + fallback, reflections)

# 🌐 Web app
def main():
    st.title("🌞 Empress Ruler of All Kingdoms Chatbot")
    st.write("Speak your mind, and the Empress shall respond with wisdom and grace.")

    dialogue_pairs = load_dialogue_pairs("empress.txt")
    random.shuffle(dialogue_pairs)
    chatbot = create_chatbot(dialogue_pairs[:1000])

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "response" not in st.session_state:
        st.session_state.response = ""

    input_type = st.radio("Choose your input type:", ("Text", "Speech"))

    if input_type == "Text":
        st.session_state.user_input = st.text_input("Type your message:", value=st.session_state.user_input)
    else:
        if st.button("🎤 Speak Now"):
            st.session_state.user_input = transcribe_speech()

    if st.session_state.user_input:
        special_reply = check_special_keywords(st.session_state.user_input)
        if special_reply:
            response = special_reply
        else:
            cleaned_input = clean_pattern(st.session_state.user_input)
            response = chatbot.respond(cleaned_input)
            if response is None:
                response = "Hmm... I don't quite get that. Try saying something else?"
        st.session_state.response = response

    st.text_area("Empress says:", value=st.session_state.response, height=150)

    if st.session_state.user_input:
        st.write(f"🗣️ You said: {st.session_state.user_input}")

if __name__ == "__main__":
    main()

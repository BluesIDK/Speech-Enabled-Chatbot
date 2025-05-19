# 🎙️ Speech-Enabled Chatbot

— a simple yet powerful voice-interactive AI assistant built with Python.  
It listens to your voice, thinks, and talks back.

---

## 🌟 What is this?

This project brings together **speech recognition**, a basic **chatbot logic**, and (optionally) **text-to-speech**, to create a real-time conversational AI.

---

## 🧠 How it works (Like, actually)

1. **You speak**: Your voice is captured via your microphone.
2. **Speech Recognition**: The voice is converted into text using Python’s `speech_recognition` library.
3. **Chatbot Engine**: The text is fed to a chatbot system. This could be a rule-based bot, a GPT-powered bot (e.g., via OpenAI), or something custom.
4. **Text-to-Speech (Optional)**: The chatbot’s reply is spoken aloud using `pyttsx3`.

- ⚙️ **Custom Prompts**: All responses and prompt logic are editable via `empress.txt`.

## ✍️ Custom Response Style via `empress.txt`

Right now, this chatbot doesn’t use any pre-trained AI like GPT or fancy machine learning.  
Instead, **all of its responses are defined by me** — inside the `empress.txt` file.

That file is where the chatbot looks for its lines, its tone, and its knowledge. It’s 100% handcrafted.  
Because i chose to build a bot that speaks in my own style — not some generic chatbot fluff.

Every line inside `empress.txt` is a reflection of my mind, humor, mood, and rules.


## 🧠 Why It’s Not “Advanced” (Yet)

This is a conscious design decision.

The chatbot is **not trying to guess** what you mean using AI.  
It only responds based on what's written in `empress.txt`.

It’s simple. Transparent. Personal.  
But with time, i will expand the file and make it smarter, deeper, even funnier.  
i will add more lines, expressions, and responses — and watch it grow with my vision.

---

## 🧪 Example

Let’s say you say:

> "how are you?"

If you’ve written this in `empress.txt`:

```txt
how are you: As long as the Empress lives, I live. I am always operational.


## 🛠️ Future Ideas

i might later integrate GPT or other APIs.

i could add fallback logic when no match is found.

i might include randomness, moods, or context awareness.

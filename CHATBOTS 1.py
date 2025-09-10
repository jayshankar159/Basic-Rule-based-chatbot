import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!"]],
    [r"how are you ?", ["I'm fine, thanks. How are you?"]],
    [r"what is your name ?", ["I'm a Python chatbot."]],
    [r"(.*) your creator ?", ["I was created by a Python programmer."]],
    [r"quit", ["Bye! Take care."]]
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hi, I'm your chatbot! Type 'quit' to exit.")
chatbot.converse()
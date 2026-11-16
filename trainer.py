# importing cleaner from clean_corpus function
# also chatterbot for chatbot >>

from chatterbot import ChatBot
from cleaner import clean_corpus
from chatterbot.trainers import ListTrainer


# instance of file data.txt
CORPUS_FILE = "data.txt"

# another instances >>
chatbot = ChatBot("Chatbot")
trainer = ListTrainer(chatbot)

cleaned_corpus = clean_corpus(CORPUS_FILE)

# now train data >>
trainer.train(cleaned_corpus)
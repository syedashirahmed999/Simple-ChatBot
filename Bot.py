# importing chatterbot which gives a chatbot with untrained data >>>
# also importing Listtrainer to train data manually >>

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# creating an instance of chatbot >>
chatbot = ChatBot('Chatbot')

# creating an instamce of list tranier to train data >>
trainer = ListTrainer(chatbot)

# training data >>
trainer.train(
    [
        "Hi",
        "Yo Student, What to Learn Today? 🤗"
    ]
)

trainer.train(
    [
        "Bye",
        "Bye Student, Don't Come Tomorrow. 🤗"
    ]
)

trainer.train(
    [
        "Are you a student",
        "No, I am A Gen-Z Teacher"
    ]
)

# exit conditions of chatbot>>
exit_conditions = ("quit","q",":q","clear","exit","nikal")

# loop of bot unless you type exit conditions >>
while True:

    query = input("=> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        if response.confidence >= 0.50:
            print(f"[Teacher]: {response}")
            print(f"Confidence: {response.confidence:.2f}")
        else:
            print("[Teacher]: Yo, Bro Didn't Understand Much, Can you rephrase It?")


# TRACEBACK ERROR AFTER RUNNING IN FIRST TIME >>>>>

# Traceback (most recent call last):
# ...
# chatterbot.chatterbot.ChatBot.ChatBotException: Setup error:
# The Spacy model for "English" language is missing.
# Please install the model using the command:
# python -m spacy download en_core_web_sm
# See https://spacy.io/usage/models for more information about available models.

    # If you bump into this, then go ahead and run the suggested command to install the missing language model:
    # python -m spacy download en_core_web_sm

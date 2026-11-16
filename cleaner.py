
# importing re(regular expression) for cleaning data >>
import re


# cleaning all metedata >>>
def remove_chat_metadata(export_file):

    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)" # 01/12/2026, 19:00
    dash_whitespace = r"(\s-\s)"  # " - "
    username = r"([\w\s]+)"  # Teacher
    meta_data = r"(:\s)"  # ": " 

    pattern = date_time + dash_whitespace + username + meta_data

    # opening data.txt and cleaning the data using re >>

    with open(export_file,"r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern,"",content)
    return tuple(cleaned_corpus.split("\n"))

# removing the blank lines, and unecessary lines >>
def remove_non_msgs_text(export_text_lines):

    filter_out_messages = ("<Media omitted>")

    return tuple(
        [
            msg for msg in export_text_lines
            if msg.strip()
            and not msg.strip().startswith("⮑")
            and "Messages and calls are end-to-end encrypted." not in msg
            and msg.strip() != filter_out_messages    
        ]
)

# clean corpus function which we can use in our trainer.py file to effectively use in our db.sqlite3 file >>
def clean_corpus(export_file):
    messages_corpus = remove_chat_metadata(export_file)
    cleaned_corpus = remove_non_msgs_text(messages_corpus)
    return cleaned_corpus

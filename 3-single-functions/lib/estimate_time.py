
def estimate_time(text):
    if text == "":
        raise Exception("You can't read what is not there.")
    word_count = len(text.split())
    time = word_count / 200
    return time
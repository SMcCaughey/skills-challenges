# takes a string as an argument and returns the first five words 
# and then a '...' if there are more than that.

def snippet(string):
    if len(string.split(" ")) <= 5:
        return string
    long_string = string.split(" ")
    return " ".join(long_string[0:5]) + "..."
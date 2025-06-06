class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        word_count = self.contents.split()
        return len(word_count)

    def reading_time(self, wpm):
        word_count = self.contents.split()
        return float(len(word_count)/wpm)

    def reading_chunk(self, wpm, minutes):
        word_count = self.contents.split()
        reading_time = float(len(word_count)/wpm)
        if reading_time <= minutes:
            return self.contents
        percentage_completion = float(minutes/reading_time)
        readable_words_count = int(len(word_count)*percentage_completion)
        chunk = " ".join(word_count[:readable_words_count])
        return chunk
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

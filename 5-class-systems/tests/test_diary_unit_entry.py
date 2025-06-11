from lib.diary_multi_class import DiaryEntry

def test_entry_creation_and_count():
    day1 = DiaryEntry("Day 1", "I found a diary lying around.")
    assert day1.count_words() == 6
    
def test_count_3000_words():
    day2 = DiaryEntry("Day 2", "The diary compels me to scribe. "*500)
    assert day2.count_words() == 3000

def test_reading_time_300_words_at_200_wpm():
    day3 = DiaryEntry("Day 3", "legere "*300)
    assert day3.reading_time(200) == 1.5

def test_readable_chunk_of_500_words_at_200wpm_in_2_minutes():
    day4 = DiaryEntry("Day 4", "Time is of the essence. "*100)
    assert day4.reading_chunk(200, 2) == ("Time is of the essence. "*80).strip()
    
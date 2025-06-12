from lib.diary_multi_class import *

def test_diary_creation_and_entry():
    diary = Diary()
    day1 = DiaryEntry("Day 1", "I found a diary lying around.")
    day2 = DiaryEntry("Day 2", "The diary compels me to scribe")
    diary.add(day1)
    diary.add(day2)
    assert diary.all() == [day1, day2]
    
def test_diary_word_count_6():
    diary = Diary()
    day1 = DiaryEntry("Day 1", "I found a diary lying around.")
    diary.add(day1)
    assert diary.count_words() == 6
    
def test_diary_word_count_12():
    diary = Diary()
    day1 = DiaryEntry("Day 1", "I found a diary lying around.")
    day2 = DiaryEntry("Day 2", "The diary compels me to scribe")
    diary.add(day1)
    diary.add(day2)
    assert diary.count_words() == 12
    
def test_reading_time_300_words_at_200_wpm():
    diary = Diary()
    day3 = DiaryEntry("Day 3", "legere "*300)
    day4 = DiaryEntry("Day 4", "legere "*300)
    diary.add(day3)
    diary.add(day4)
    assert diary.reading_time(200) == 3.0
    
def test_best_reading_entry_for_2_minutes_at_200wpm():
    diary = Diary()
    day3 = DiaryEntry("Day 3", "legere "*200)
    day4 = DiaryEntry("Day 4", "legere "*400)
    day5 = DiaryEntry("Day 5", "legere "*600)
    day6 = DiaryEntry("Day 6", "legere "*800)
    day7 = DiaryEntry("Day 7", "legere "*1000)
    diary.add(day3)
    diary.add(day4)
    diary.add(day5)
    diary.add(day6)
    diary.add(day7)
    assert diary.find_best_entry_for_reading_time(200, 2.0) == day4
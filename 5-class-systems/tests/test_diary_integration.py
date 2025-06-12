from lib.diary_multi_class import Diary, DiaryEntry

def test_add_and_retrieve_entries_integration():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "Today was sunny.")
    entry2 = DiaryEntry("Day 2", "It rained all day.")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

def test_count_words_across_entries_integration():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "Hello world")
    entry2 = DiaryEntry("Day 2", "Python is fun")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5

def test_reading_time_across_entries_integration():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "one two three four five")
    entry2 = DiaryEntry("Day 2", "six seven eight nine ten")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(5) == 2.0

def test_find_best_entry_for_reading_time_integration():
    diary = Diary()
    entry1 = DiaryEntry("Short", "one two")
    entry2 = DiaryEntry("Medium", "one two three four")
    entry3 = DiaryEntry("Long", "one two three four five six")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    # Can read up to 4 words (keep this as a small test)
    best = diary.find_best_entry_for_reading_time(2, 2)
    assert best == entry2
    # Can read up to 60 words (more realistic)
    entry4 = DiaryEntry("Epic", " ".join(["word"] * 50))
    diary.add(entry4)
    best = diary.find_best_entry_for_reading_time(30, 2)
    assert best == entry4
    # Can read up to 120 words (even more realistic)
    entry5 = DiaryEntry("Novel", " ".join(["word"] * 100))
    diary.add(entry5)
    best = diary.find_best_entry_for_reading_time(60, 2)
    assert best == entry5
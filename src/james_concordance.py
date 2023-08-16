import json

class GreekWord:

    def __init__(self, greek_word, english_text, chapter, verse, word_index, fisher_teaching, strongs_number, strongs_word, strongs_data):
        """
         Creates a Greek Word using data available from the james.json plus dictionary file.
         """
        self.greek_word = greek_word
        self.english_text = english_text
        self.chapter = chapter
        self.verse = verse
        self.word_index = word_index
        self.fisher_teaching = fisher_teaching
        self.strongs_number = strongs_number
        self.strongs_word = strongs_word
        self.strongs_data = strongs_data

    def __repr__(self):
        return f"{self.greek_word} - {self.english_text} ({self.chapter}:{self.verse}.{self.word_index}) T{self.fisher_teaching}"


def main():
    print("James Concordance")
    all_words = load_james()

    find_matches(all_words, ["τέλ", "τελ"])


def load_james():
    james_json_file = open("james.json")

    verse_maps = json.load(james_json_file)
    greek_words = []

    for single_verse in verse_maps:
        current_chapter = int(single_verse["id"][2:5])
        current_verse = int(single_verse["id"][5:])
        current_fisher_teaching = get_fisher_teaching(current_chapter, current_verse)
        words = single_verse["verse"]

        for json_word in words:
            greek_word = json_word["word"]
            english_text = json_word["text"]
            # chapter = chapter
            # verse = verse
            word_index = json_word["i"]
            # fisher_teaching = fisher_teaching
            strongs_number = json_word["number"]
            # strongs_word = strongs_word
            # strongs_data = strongs_data
            greek_word = GreekWord(greek_word, english_text, current_chapter, current_verse, word_index, current_fisher_teaching, strongs_number, None, None)
            greek_words.append(greek_word)

    james_json_file.close()
    return greek_words


def find_matches(all_words: list[GreekWord], regex_matches, print_only=True):
    greek_word_matches = []
    hits = 1
    for word in all_words:
        found = False
        for match in regex_matches:
            if match in word.greek_word:
                found = True
        if found:
            if print_only:
                print(f"{hits}. {word}")
                hits += 1
            else:
                greek_word_matches.append(word)
    return greek_word_matches


def get_fisher_teaching(chapter, verse):
    if chapter == 1:
        if verse == 1:
            return 0.1
        elif verse <= 4:
            return 1.1
        elif verse <= 8:
            return 1.2
        elif verse <= 12:  # Previously 11
            return 1.3
        elif verse <= 18:
            return 1.4
        elif verse <= 21:
            return 2.1
        elif verse <= 25:
            return 2.2
        else:
            return 2.3
    elif chapter == 2:
        if verse <= 13:
            return 3.1
        else:
            return 3.2
    elif chapter == 3:
        if verse <= 12:
            return 3.3
        else:
            return 3.4
    elif chapter == 4:
        if verse <= 10:
            return 4.1
        elif verse <= 12:
            return 4.2
        else:
            return 4.3
    elif chapter == 5:
        if verse <= 11:
            return 5.1
        elif verse == 12:
            return 5.2
        elif verse <= 18:
            return 5.3
        else:
            return 5.4


main()

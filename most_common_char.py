'''
Write a function named getTwoMostCommonCharacters that takes a filename as a parameter,
and returns the 2 most common characters and their occurrences in the file's content.
Python: return with a dict, example:
{
  "e": 6,
  "l": 4
}
If the file does not exist throw an exception with the following message: "File does not exist!"
'''
def getTwoMostCommonCharacters(filename):
    def count_characters(text):
        character_count = {}
        for line in text:
            for character in str(line):
                character_count[character] = character_count.get(character, 0) + 1
        return sorted(character_count.items(), key=lambda x: x[1], reverse = True)

    if not isinstance(filename, str):
        raise TypeError("Input filename as string e.g. sample.txt")
    try:
        with open(filename, "r") as text:
            most_common = {key : value for key, value in count_characters(text)[0:2]}
        return most_common
    except FileNotFoundError:
        return "File does not exist!"


print(getTwoMostCommonCharacters("sample2.txt"))

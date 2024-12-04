def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.lower().split()
        word_count = len(word_list)
        character_list = []
        character_count = {}
        temp_var = ""
        for word in word_list:
            temp_var = list(word)
            character_list += temp_var
        for character in character_list:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
        print("\n")
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("\n")
        for character in character_count:
            print(f"The {character} was found {character_count[character]} times")
        print("\n")
        print("--- End report ---")
        print("\n")


if __name__=="__main__":
    main()
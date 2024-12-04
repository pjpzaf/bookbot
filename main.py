def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.lower().split()
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
        print(character_count)
    

if __name__=="__main__":
    main()
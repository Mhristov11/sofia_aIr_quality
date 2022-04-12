text= input().split(" | ")
dictionary= dict()
for words in text:
    if ":" in words:
        word_and_description= words.split(": ")
        word = word_and_description[0]
        description = word_and_description[1]
        if word not in dictionary:
            dictionary[word]= [description]
        else:
            dictionary[word].append(description)

test_words= input().split(" | ")

command= input()

if command == "Test":
    for current_word in test_words:
        if current_word in dictionary:
            print(f"{current_word}:")
            for value in dictionary[current_word]:
                print(f"-{value}")
elif command== "Hand Over":
    for key in dictionary:
            print(key, end=" ")

#2:15:00- 30m.
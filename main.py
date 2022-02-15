with open('wordlist.txt') as f:
    word_list = f.readlines()[0].split(',')

print(word_list[242])
counter = 0
for word in word_list:
    counter += 1
    print("Wordle " + str(counter) + " - " + word)

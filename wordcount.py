# put your code here.

opened_file = open('test.txt')

poem_words = {}

words = []

for line in opened_file:
    words = line.rstrip().split( )
    for word in words:
        # if word not in poem_words:
        #     poem_words[word] = 1
        # else:
        #     poem_words[word] += 1
        poem_words[word] = poem_words.get(word, 0) +1

# if word != poem_words[word]:
for word, count in poem_words.items():
    print word, count


# 'test.txt'.close()

# # print poem_words



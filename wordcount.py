# put your code here.

opened_file = open('test.txt')

poem_words = {}

words = []

for line in opened_file:
    words = line.split( )
    for word in words:
        if word not in poem_words:
            poem_words[word] = 1
        else:
            poem_words[word] += 1
# if word != poem_words[word]:


print poem_words



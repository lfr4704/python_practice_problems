import sys

n= "my code"
def my_function(s):
    if s == "my code":
        return True

print(my_function(n))


#Given a maximum number of characters in a line followed by a list of words,
#return a collection of strings where each line contains as many words as possible
#concatenated by a space. The length of each string should not exceed the maximum length.

line_length= 6
words = ["The", "fox", "is", "hungry"]

def print_board(words):
    words.append("and")
    words.append("thirsty")
    # return words
print_board(words)

words =" ".join(words)

def wrapLines(line_length, words):

    for i in range(0,len(words), line_length):
        yield words[i:i+line_length] #https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

#add list() to work with generator

wrapped_words = list(wrapLines(line_length, words))

print("\n".join(wrapped_words))





# expected result:
# The
# fox is
# hungry

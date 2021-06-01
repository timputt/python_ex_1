# part 3
# Task: 
# - break s into a list of words (i.e. now separated by space)
# - print out the word list (with a loop) so that every 2. word is in full uppercase.
# - optionally remove all periods and commas
# result:
# Python
# IS
# an
# INTERPRETED
# high-level
# GENERAL-PURPOSE
# programming
# LANGUAGE
print("start of part 3") # set breakpoint here
# your code here

#My first pass without removing punctuation.

s = "Python is an interpreted, high-level, general-purpose programming language."
capwords = s.upper()
print(capwords)
word_lst = capwords.split(" ")
for e in word_lst:
    print(e)

# This is only 50% correct b/c you effectively upper() all chars first and then make words
# you need some way of doing upper() only to every 2. word




#Removing punctuation - FAIL :(
s = "Python is an interpreted, high-level, general-purpose programming language."
capwords = s.upper()
print(capwords)
punc = ","
word_lst = capwords.split(" ")
for e in word_lst:                 
    if e in punc:
        word_lst = word_lst.replace(e,"") 
    print(*word_lst, sep = "\n") # Fancy list unrollerado!

# You could use replace(e, "") instead of remove but should do it on s first, then split s:
s = "Python is an interpreted, high-level, general-purpose programming language."
p_chars = ",."
for p in p_chars:
    s = s.replace(p, "")
print(s)

words = s.split(" ")





print("end of 3") # set breakpoint here 




























# solution 3
# version 1 - using 1/-1
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = -1  # we start with 1 for normal print-out, then flip -1 for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == 1:
        print(w.upper())
    else:
        print(w)
    make_upper *= -1 # flip from 1 to -1 or vice versa

# version 2 - using 
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = False  # we start with False for normal print-out, then flip to True for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == True:
        print(w.upper())
        make_upper = False # it's currently True, so set to False
    else:
        print(w)
        make_upper = True # it must currently be False, so set to True

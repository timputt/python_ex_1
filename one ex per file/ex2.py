# part 2
# Task: Break s into sentences (which end in a .), count them and print them out using a loop:
# result: (I truncated them with ...)
# there are 4 sentences:
# Python is an interpreted, high-level, general-purpose programming language
#  Created by Guido van Rossum and first released in 1991, Python ...
#  Its language constructs and object-oriented approach aim to help programmers ...
print("start of part 2") # set breakpoint here
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."


#First attempt that works, but did NOT use loop.

print("Tim's first try at here") 
period_count = s.count(".")
print(period_count, "periods were counted.\n\n") #to confirm how many sentences end in a period.
sentence_str = s.split(". ",-1) #maxsplit is automatically -1
print(sentence_str)
# CH using ". " and not just "." is actually a pretty elegant way of getting a proper human sentence separtion. 
# No need to use -1, though, if you don't want to limit your split, just omit the second arg and it'll default to -1
# s.split(". ") 


print("Sentence 1:\n",sentence_str[0], "\n\nSentence 2:\n",sentence_str[1], "\n\nSentence 3:\n",sentence_str[2])
# CH this is amateurish b/c you should NEVER rely on hardcoding the number of any collection. Always either use
# len() or let the for loop do its magic. Just print(sentence_str) would also be OK, but a bit ugly

print("end of 2") # set breakpoint here 

#Second attempt after taking a brief peek below.
print("\n\n\n\nTim's second try at here -- after BRIEFLY looking at the solution below and realizing I didn't loop.")
sentence_lst = s.split(".")
print(len(sentence_lst),"total sentences")
for e in sentence_lst:
    print(e)


'''

























s = "Python is an interpreted, high-level, general-purpose programming language."
sentence_list = s.split('.')
print("there are", len(sentence_list), "sentences:")
for e in sentence_list:
    print(e)
'''
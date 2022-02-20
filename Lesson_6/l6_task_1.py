#Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys
# and the number of occurrences as values


#So we have some text in string value
some_string = "SQL (pronounced “ess-que-el”) stands for Structured Query Language. SQL is used to communicate " \
              "with a database. According to ANSI (American National Standards Institute), it is the standard " \
              "language for relational database management systems. SQL statements are used to perform tasks " \
              "such as update data on a database, or retrieve data from a database. Some common relational " \
              "database management systems that use SQL are: Oracle, Sybase, Microsoft SQL Server, Access, " \
              "Ingres, etc. Although most database systems use SQL, most of them also have their own additional " \
              "proprietary extensions that are usually only used on their system. However, the standard SQL " \
              "commands such as “Select”, “Insert”, “Update”, “Delete”, “Create”, and “Drop” can be used to " \
              "accomplish almost everything that one needs to do with a database. This tutorial will provide " \
              "you with the instruction on the basics of each of these commands as well as allow you to put " \
              "them to practice using the SQL Interpreter."
# and we define some empty dict.
some_dict = {}

# we split string into separate words using "whitespace" separator
some_list = some_string.split(' ')
#print(some_list) #remove hash to print separated string

#define variable that contains extra sybols: dot, comma etc.
symbols_to_del = ',.()[]{}"\'!@#$%^&*_+='
#here we delete all extra symbols in each string-element by replacing each by epty string ''
for index, word in enumerate(some_list):
    for symbol in symbols_to_del:
        word = word.replace(symbol, '')
    #after itareting and deleting extra symbols we replace each iterated string in our list
    some_list[index] = word.lower() #all words must be lower to avoid dublicates

#check if there are empty strings and remove them if they are exist
if '' in some_list:
    some_list.remove('')

#checking each word in our list. If it's not exist in our dict it's attached to our dict as key
# and for that key adding initial value '1', but if the word is exist in dict, value increments by '1'
for word in some_list:
    if word in some_dict:
        some_dict[word] += 1
    else:
        some_dict[word] = 1

#here we sort dict. by value decrease
#key and value as arguments in sorted dcit
#functrion sorted get list  with tuples inside as elements getted from .items()
# #each tuple contains two values inside, getted from our dict
#so we need to use key parameter to to make it clear whether to sort by key or by value
some_dict = {key: val for key, val in sorted(some_dict.items(), key=lambda item: item[1], reverse=True)}

#and printing in a mostly (:D) usability view, but i'm not sure for such loooong text
for key, val in some_dict.items():
    print(f"Word \"{key.upper()}\" has {val} occurrence(s)")



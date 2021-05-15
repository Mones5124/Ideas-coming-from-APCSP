
"""Code for Ceaser Cipher Breaker"""

#input ybodbk qbze hkfdeqp
#output Bergen Tech Knights

#words = "ybodbk qbze hkfdeqp"
#words = "SKKZ NKXK"
words = "Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar"
#words = "TRVJRI TZGYVIJ RIV HLZKV VRJP KF TIRTB"

words = words.lower()
#not working now

alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

original_num = []

print()
print(words)
print()

from datetime import datetime, timedelta
t = int(str(datetime.time(datetime.now()))[-6:])
#converts to a string to be able to subscript it and then converts to integer for the rest of the code
#print(t)
# do some stuff

def convert_to_num(original):
    """original is the original list of words (must be minimized)"""
    nums = []
    for letter in original:
        #print(letter)
        for x in range (0, 27):
            if alphabet[x] == letter:
                nums.append(x)
                #print(x)
                break
            #print(x)
    return nums

def move_letters(n_list, change):
    """moves the list of numbers by a certain number of digits"""
    new_list = []
    for number in n_list:
        change1 = change
        if number == 0:
            new_list.append(0)
        else:
            if (number+change >= 26):
                change1 -= 26
            new_list.append(number+change1)
    
    #print(new_list)
    return new_list

def convert_to_words(n_list):
    """changes the numbers list back into a word list"""
    word_list = []
    for n in n_list:
        word_list.append(alphabet[n])
    #print(word_list)
    str1 = ""
    t = str1.join(word_list)
    sentence = t
    #print(sentence)
    #testing_word = t.split(" ")
    #print(testing_word)
    vowels = ["a", "e", "i", "o", "u"]
    #print(t.split(" "))
    bad = 0
    for word in t.split(" "): #splits by the space
        good = False
        #print(len(vowels)-1)
        for v in vowels:
            if str(v) in word: #vowels[v]
                #print("Yes")
                good = True
            #print(v)
        if good == False:
            #print("No")
            bad += 1

    #print(good)
    if (bad == 0 and good):
        #print(t)
        return sentence
    else:
        return
    #try to test to make sure each word has a vowel
    return sentence
    
vowels = ["a", "e", "i", "o", "u"]
#vowels so I can try to filter the results a little bit

for x in range(1, 2):
    to_num = convert_to_num(words)
    #print(to_num)
    total_word_list = []
    for i in range(1, 25): # 25
        new_num_list = move_letters(to_num, i)
        word_list = convert_to_words(new_num_list)
        #print(word_list)
        total_word_list.append(word_list)

#print(to_num)
#print(len(total_word_list))
#print(total_word_list)

#filter to delete nones
L = [n for n in total_word_list if n != None]
#L = filter(None, total_word_list)
#print(len(total_word_list))
print(L)

later_time = int(str(datetime.time(datetime.now()))[-6:])
print("Total time: "+ str(later_time-t))

print()

# sum of each digit in a number
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total


print digit_sum(232999999999323493849832)


# if x=3 | x=3*2*1
def factorial(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
        print x
        print total
    return total


print factorial(20)


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True


print is_prime(10831)


def reverse(text):
    word = ""
    count = len(text) - 1
    while count >= 0:
        word = word + text[count]
        count -= 1
    return word


print reverse('Whatever you want! #*#(898)')


def anti_vowel(text):
    word = ""
    vowels = "ieaouIEAOU"
    for char in text:
        for v in vowels:
            if char == v:
                char = ""
            else:
                char = char
        word += char
    return word


print anti_vowel("I dont like this")

# key:value scoring
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    total = 0
    word = word.lower()
    for char in word:
        total += score[char]
    return total


print scrabble_score('homopqgeznius')


# choose your own censor
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)

    return result


print censor('bla f in bla bla ', 'bla')


# counts number of times something shows up in a list
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count


print count([5, 5, 5, 4, 5, 4, 4, 4, 5, 5], 5)


# filters a list
def purify(number_list):
    even_list = []
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


# this returns a list of even numbers
print purify([1, 2, 3, 4, 5, 5, 6, 7, 7767, 745, 67546754, 674, 324534])


# multiplies a list of numbers
def product(list):
    total = 1
    for num in list:
        total = total * num
    return total


print product([1, 5, 2, 2])  # 1*5*2*2


# return only one if multiplies
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
# Sort the input list from low to high
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted
# input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    return outputlist


print remove_duplicates([1, 4, 5, 2, 3, 1, 3, 1, 4, 2, 3, 5, 5])

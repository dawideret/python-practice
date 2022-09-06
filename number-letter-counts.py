import math

number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
                "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

word_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def zero_till_99(num):
    if num <= 19:
        return number_words[num]
    if 20 <= num <= 99:
        x = int(math.floor(num / 10))
        xx = word_tens[x - 2]
        if num % 10 != 0:
            xx += number_words[num - (x * 10)]
        return xx
    else:
        return num


def number_to_word(num):
    if num <= 19:
        return number_words[num]

    if 20 <= num <= 99:
        return zero_till_99(num)

    if 100 <= num <= 999:
        ret = ""
        hun = int(num / 100)
        ret += number_words[hun]
        ret += "hundred"
        if num % 100 != 00:
            ret += "and"
            ret += zero_till_99(int(num - (hun * 100)))
        return ret
    if num == 1000:
        return "onethousand"


fin_string = ""
for nums in range(1, 1001):
    fin_string += number_to_word(nums)

print(len(fin_string))
while True:
    print(number_to_word(int(input("Enter a Number: "))))

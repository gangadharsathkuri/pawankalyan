input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
index = 0

while index < len(input_string):
    char = input_string[index]
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    index += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

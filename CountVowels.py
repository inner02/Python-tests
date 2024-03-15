def count_vowels(word):
    vowels = 'aeiouAEIOU'  
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))

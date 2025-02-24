def count_vowels_in_sentence(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count +=1
    return count
sentence = input("Enter a sentence:")
print("number of vowels:",count_vowels_in_sentence(sentence)) 

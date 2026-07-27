#Tells user to unput tex
text = input("Input: ")

#This function declares the vowels to strip and .lowers the capitals
def strip_vowel(text):
    vowels = "aeiouAEIOU"
    result = text
    for v in vowels:
        result = result.replace(v, "")
    return result.lower()

#Calls fucntion output
output = strip_vowel(text)

print(output)

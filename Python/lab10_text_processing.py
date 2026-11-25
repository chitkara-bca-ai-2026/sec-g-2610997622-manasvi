print("=" * 45)
print("          TEXT PROCESSING TOOL")
print("=" * 45)

# Accept a sentence
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# String Indexing
position = int(input("Enter position for indexing: "))
print("Character at position", position, ":", sentence[position])

# String Slicing
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print(f"Sliced string [{start}:{end}] :", sentence[start:end])

# Uppercase
print("Uppercase                :", sentence.upper())

# Lowercase
print("Lowercase                :", sentence.lower())

# Replace a word
old_word = input("Enter word to replace    : ")
new_word = input("Enter replacement word   : ")

new_sentence = sentence.replace(old_word, new_word)
print("After replace            :", new_sentence)

# Length of sentence
print("Length of sentence       :", len(sentence))

print("\n" + "=" * 45)
print("           Analysis Complete!")
print("=" * 45)
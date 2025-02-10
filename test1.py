#1: Have your program check the word 'coronavirus' itself and report what unique letters it contains.

word = ('coronavirus')
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
for unqique_letter in letters:
    if unqique_letter in word:
        print(unqique_letter)

#for unique_letter in word:
 #   print(letter)

#2: Generate a series of questions of the form, "Can X treat Y?"
#where X is the following list of medications: remdesivir, hydroxychloroquine, kaletra, favipiravir
#and Y is the following list of diseases: coronavirus, hepatitis, malaria, influenza

medications = ['remdesivir', 'hydroxychloroquine', 'kaletra', 'favipiravir']
diseases = ['coronavirus', 'hepatitis', 'malaria', 'influenza']
for x in medications:
    for y in diseases:
        print('Can', x, 'treat', y, '?')

#3: In this step, your program will search for common letters in some words that were uncommon before the coronavirus outbreak.
#Take each letter in the word 'coronavirus' and report whether each letter also exists in each medication from the list of medications in step 2 above.

for letter in letters:
    if letter in word:
        for med in medications:
            if letter in med:
                print(letter, 'is in', word, 'and also in', med)
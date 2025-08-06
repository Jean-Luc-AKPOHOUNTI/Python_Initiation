# 1. Supprimer les doublons d’une liste en conservant l'ordre d'apparition des éléments.
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result


# Test de la fonction
table = [3, 5, 2, 3, 8, 5, 9, 2]
print("Liste d'origine :", table)
print("Liste sans doublons 👀 :", remove_duplicates(table))


# 2. Vérifier si un mot est un palindrome
def is_palindrome(word):
    # word = word.lower()
    # return word == word[::-1]
    word = word.lower()
    return word == ''.join(reversed(word))


# Test de la fonction
word = "Radar"
print(f"Le mot '{word}' est un palindrome ? 🤔 {is_palindrome(word)}")


# 3. Compter les occurrences d’un élément dans une liste
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


# Test de la fonction
print(f"Le nombre d'occurrences de '4' dans la liste est :{count_occurrences([1, 4, 2, 4, 5, 4, 7], 4)}")

# Simple Name Matching System
print("Hi there")

# --------- Example ---------
NAMES_DB = [
    # Geeta variations
    "Geetha", "Geeta", "Gita", "Gitu", "Githa", "Geetha Devi",

    # Sita variations
    "Sita", "Seeta", "Seetha", "Sitha",

    # Rita variations
    "Rita", "Reeta", "Ritha",

    # Anita / Sunita group
    "Anita", "Anitha", "Sunita", "Suneeta", "Sunitha",

    # Lata variations
    "Lata", "Leeta", "Latha",

    # Meena variations
    "Meena", "Mina", "Meenakshi",

    # Nita variations
    "Nita", "Neeta", "Neetha",

    # Others commonly confused
    "Pooja", "Puja",
    "Kavita", "Kavitha",
    "Savita", "Sravita"
]

user_input = input("Enter a name: ")


import Levenshtein

def similarity_score_lib(s1, s2):
    # Returns similarity between 0 and 1
    return Levenshtein.ratio(s1.lower(), s2.lower())


results = [(name, similarity_score_lib(user_input, name)) for name in NAMES_DB]
results.sort(key=lambda x: x[1], reverse=True)

print("Best Match:", results[0])
print("Other Matches:", results[:5])


import itertools


def leetspeak(word):
    replacements = {
        "a": ["a", "@", "4"],
        "e": ["e", "3"],
        "i": ["i", "1"],
        "o": ["o", "0"],
        "s": ["s", "$", "5"],
        "t": ["t", "7"]
    }

    variations = [""]

    for char in word.lower():
        if char in replacements:
            variations = [
                prefix + repl
                for prefix in variations
                for repl in replacements[char]
            ]
        else:
            variations = [prefix + char for prefix in variations]

    return variations


def generate_wordlist(name, pet, dob, keyword):
    base_words = [name, pet, keyword]

    all_words = set()

    # Generate variations for each base word
    for word in base_words:
        if word:
            variations = leetspeak(word)

            for v in variations:
                all_words.add(v)
                if dob:
                    all_words.add(v + dob)

    # Combine base words together
    for combo in itertools.permutations(base_words, 2):
        if all(combo):
            combined = combo[0] + combo[1]
            variations = leetspeak(combined)

            for v in variations:
                all_words.add(v)
                if dob:
                    all_words.add(v + dob)

    # Save to file
    with open("custom_wordlist.txt", "w") as file:
        for word in sorted(all_words):
            file.write(word + "\n")

    return len(all_words)
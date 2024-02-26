def recursive_levenshtein_distance(s, t):
    if len(s) == 0:
        return len(t)
    
    if len(t) == 0:
        return len(s)
    
    if s[0] == t[0]:
        return recursive_levenshtein_distance(s[1:], t[1:])
    
    return 1 + min(
        recursive_levenshtein_distance(s[1:], t),      # inserted
        recursive_levenshtein_distance(s, t[1:]),      # deleted
        recursive_levenshtein_distance(s[1:], t[1:]),  # substituted
    )
    
    
def iterative_levenshtein_distance(s, t):
    if len(s) < len(t):
        return iterative_levenshtein_distance(t, s)

    if len(t) == 0:
        return len(s)

    previous_row = range(len(t) + 1)
    for i, char_s in enumerate(s):
        current_row = [i + 1]
        for j, char_t in enumerate(t):
            current_row.append(min(
                previous_row[j + 1] + 1,                # inserted
                current_row[j] + 1,                     # deleted
                previous_row[j] + (char_s != char_t)    # substituted
            ))
        previous_row = current_row

    return previous_row[-1]

def levenshtein_distance(s, t, recursive=False):
    if recursive:
        return recursive_levenshtein_distance(s, t)
    return iterative_levenshtein_distance(s, t)

if __name__ == "__main__":
    iterValue = levenshtein_distance("kitten", "sitting", recursive=False)
    recurValue = levenshtein_distance("kitten", "sitting", recursive=True)
    print(f"Iterative result={iterValue} ::: Recursive result={recurValue}")
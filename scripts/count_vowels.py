z = 1

def count_vowels(filename):
    """This function counts the vowels in the given file."""
    with open(filename) as f:
        file_contents = f.read()
    vowels = 'aeiou'
    total_vowel_count = 0
    for char in file_contents:
        if char in vowels:
            total_vowel_count += 1
    return total_vowel_count


x = [t for t in range(10)]

if __name__ == '__main__':
    print(count_vowels('README.md'))

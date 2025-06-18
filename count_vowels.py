

# This function counts the vowels in the given file
def count_vowels(filename):
    with open(filename) as f:
        t = f.read()
    vowels = 'aeiou'
    x = 0
    for c in t:
        if c in vowels:
            x += 1
    return x


if __name__ == '__main__':
    print(count_vowels('README.md'))

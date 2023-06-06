class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def find_palindromes(self):
        words = self.text.split()
        palindromes = []

        for word in words:
            if word == word[::-1]:
                palindromes.append(word)

        return palindromes

    def find_unique_words(self):
        words = self.text.split()
        unique_words = set(words)

        return list(unique_words)

# Example usage
text = "radar sees madam and level kayak"
analyzer = TextAnalyzer(text)

# Using class method
palindromes = analyzer.find_palindromes()
unique_words = analyzer.find_unique_words()

print("Palindromes:", palindromes)
print("Unique Words:", unique_words)

# Using string methods
palindromes_str = [word for word in text.split() if word == word[::-1]]
unique_words_str = list(set(text.split()))

print("Palindromes (String method):", palindromes_str)
print("Unique Words (String method):", unique_words_str)

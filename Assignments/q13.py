class TextAnalyser:
    def __init__(self, text):
        self.text = text
    
    def __len__(self):
        return len(self.text)
    
    def repetitive_words_length(self):
        words = self.text.split()
        word_counts = {}
        repetitive_words = []
        
        for word in words:
            if len(word) > 1 and word:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        
        for word, count in word_counts.items():
            if count > 1:
                repetitive_words.append({word : count})
        
        return repetitive_words
    

    def most_repetitive_word(self):
        words = self.text.split()
        word_counts = {}
        
        
        for word in words:
            if len(word) > 1 and word:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        
        val, ans = 0, ""
        for word in words : 
            if(word_counts[word] > val) : 
                val = word_counts[word]
                ans = word
        
        return ans



text = "Hello Welcome Hello Bye Good Morning Good Night Bye Bye Pen Pencil Paper Pencil"
analyzer = TextAnalyser(text)

print(len(analyzer))
print(analyzer.repetitive_words_length())
print(analyzer.most_repetitive_word())
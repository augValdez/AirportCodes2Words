# Augustine Valdez
# partner: Preston McIllece
# Sept 18, 19


# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found. 
import pygtrie as trie  

# read codes of airport
codes = []
path_to_code_file = 'airports_code.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []
path_to_word_file = 'words_nine_letters.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using words
t = trie.CharTrie()
for word in words:
    t[word] = True

# search codes from the trie
results = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:
for code in codes:
    if t.has_subtrie(code):
        for code2 in codes:
            if t.has_subtrie(code + code2):
                for code3 in codes:
                    if t.has_key(code + code2 + code3):
                        print(code, code2, code3)
                        results.append(code + code2 + code3)
print(len(results))

## write results into results.txt
with open('results2.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 
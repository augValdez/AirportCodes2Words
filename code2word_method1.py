# Augustine Valdez
# partner: Preston McIllece

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

# build a trie using codes
t = trie.CharTrie()
for code in codes:
    t[code] = True

# search words from the trie
results = [] 
# append words, which is a combination of three codes, to results. 
# Your code goes here:

for word in words: 
    piece1 = word[0:3]
    piece2 = word[3:6]
    piece3 = word[6:9]
    if (t.has_key(piece1) == True) and (t.has_key(piece2) == True) and (t.has_key(piece3) == True):
        print(word)
        print(piece1,piece2,piece3)
        print("has_key (", piece1, "): ", t.has_key(piece1))
        print("has_key (", piece2, "): ", t.has_key(piece2))
        print("has_key (", piece3, "): ", t.has_key(piece3))   
        results.append(word)     
print(len(results))

## write results into results.txt
with open('results1.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 
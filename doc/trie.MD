# TRIE

- We have a ```TrieNode``` class that represents each node in the ```Trie```. Each node contains a dictionary called children to keep track of its child nodes for each character, and a boolean ```is_end_of_word``` to indicate whether the node represents the end of a word.
- We have a ```Trie``` class which contains methods to insert a word, search for a word, and check if there's any word in the ```Trie``` that starts with a given prefix.
- The ```insert``` method starts at the root and iterates through the characters of the word, creating new nodes as necessary.
- The ```search``` method starts at the root and iterates through the characters of the word, returning False if a character isn't found.
- The ```starts_with``` method is similar to ```search```, but returns True as soon as the prefix is found, without requiring the word to be complete.
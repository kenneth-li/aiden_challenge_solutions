# aiden_challenge_solutions
solutions to Challenge 1a and 1b


I settled on creating the Number to Word Mnemonic Converter with
the Mnemonic Major System, as implemented in http://numzi.com/numzi/
and as explained in https://en.wikipedia.org/wiki/Mnemonic_major_system

I first looked into how language processing tools, and installed the
Natural Language Toolkit (NLTK)* to give me access to a wide range of
corpus, one of which was the Carnegie Mellon University Pronouncing
Dictionary, which contains information on word pronunciations.

*because I installed NLTK, num_to_word.py will not work on your computers
without nltk installed. http://www.nltk.org/install.html has instructions
for installation

The cmudict, which can be accessed with nltk, allows for lookup of word
pronunciation given in the Arpabet, a phonetic alphabet like IPA.

My program takes an input number, splits it into pairs, and finds words
that match each pair according to the Mnemonic Major System. It then returns
the top 5 most common words that match each pair. The commonality of each
word was determined by calculating frequencies of words from the Brown Corpus,
which is also why my program is relatively slow/inefficient. It would be great
if I had found a corpus that maps words to word frequency in modern English,
which would be the difference between iteration millions (size of Brown corpus)
and tens of thousands (number of English words) of times.

An additional feature I would have liked to implement is word commonality
optimization with number place-holders. What I mean by this is that I'd like
my program to iterate over possible splittings of the input number, including
iterations with certain numbers not translated into words, and find the splitting
and number holding that has the most common words. This is based on the assumption
that common words are easier to remember (which may not be entirely true - keywords
like Lebron and MJ may not be common according to some corpus' but are actually
easy to remember because they are sports figures).

That would allow my program to input a number like 32662318120 and return

3 "inch" "chin" 1 "foot" "nose"

3   26    623   1   81     20





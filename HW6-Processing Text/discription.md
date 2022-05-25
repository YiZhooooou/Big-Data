Quiz 7: Processing Text


This assignment does not require any GCP resources. Some questions do require PySpark but they are intended to be done using Google Colab. The instructions for incorporating PySpark within the notebooks are included.

Q1. Sentence Similarity [50 pts]

You are given three documents:
doc1 = 'Life is suffering'
doc2 = 'Suffering builds character'
doc3 = 'Character is the essence of life'
 
[20 points] Write a function shingles(doc, n) that would return a set of n-character shingles. Before doing its work, this function should remove stop words and join the remaining words with spaces. For n = 2, the function should result in a set of 2-character shingles, for example {'li’, ‘if’, ‘fe’, ‘e ‘, …}. 
[15 points] Write a function jaccard(sh_set_1, sh_set_2) that would return the Jaccard distance between two sets of shingles.
[15 points] Calculate the distances between doc1&doc2, doc2&doc3 and doc3&doc1.

Q2. Frequent Itemset Mining [100]
The Frequent Itemset Mining assignment is here. The corresponding questions are in the linked notebook.
[15 pts] Interpreting association rules. This interpretation will require some research on your part. The slides don’t provide the answer.
[10 pts] Interpreting the new association rules.
[5 pts] Association Rules for an Online Retail Dataset
[30 pts] Connecting Online Retail Data to FP-Growth
[20 pts] Fine-tuning FP-Growth runs
[20 pts] Final Association Rules
Q3. NLTK [60 pts]

The text of a short Elizabeth Alexander poem, Boston Year, is available here. 

Convert all words to lowercase,
Use NLTK to break the poem into sentences & sentences into tokens. Here is the code for doing that, after you set the variable paragraph to hold the text of the poem.

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
sent_text = nltk.sent_tokenize(paragraph) # this gives us a list of sentences
# now loop over each sentence and tokenize it separately
all_tagged = [nltk.pos_tag(nltk.word_tokenize(sent)) for sent in sent_text]
Tag all remaining words in the poem as parts of speech using the Penn POS Tags. This SO answer shows how to obtain the POS tag values. Create and print a dictionary with the Penn POS Tags as keys and a list of words as the values.
[50 points] The main point of this exercise is to set up a PySpark DataFrame as a structure for analyzing large numbers of such poems. This structure is designed such that hundreds of Spark workers can be deployed to do similar analysis for different poems in parallel.

Each column row will represent a poem. The rows columns will be as follows:
The text of the poem,
Two-letter prefixes of each tag, for example NN, VB, RB, JJ etc.and the words belonging to that tag in the poem. 

Even though only one poem has been provided, your code is expected to work for as many poems as the user wishes to analyze. You may want to get more poems for testing. 

Show your code and also show the tag rows, at least for the one poem.
Q4. LDA: (Women's E-Commerce Clothing Reviews) [90 pts]

We have a corpus of reviews from a Women's E-Commerce Clothing site. 
A Jupyter notebook for using LDA for analyzing the reviews is provided here. 
The notebook also includes links to the corpus. 
There are 6 parts to this question, each worth 15 points. Please make your own copy of the notebook to work on it. When complete, print the notebook as a PDF and submit it into Gradescope.

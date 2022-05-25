poem = "My first week in Cambridge a car full of white boys tried to run me off the road, and spit through the window, open to ask directions. I was always asking directions and always driving: to an Armenian market in Watertown to buy figs and string cheese, apricots, dark spices and olives from barrels, tubes of paste with unreadable Arabic labels. I ate stuffed grape leaves and watched my lips swell in the mirror. The floors of my apartment would never come clean. Whenever I saw other colored people in bookshops, or museums, or cafeterias, I'd gasp, smile shyly, but they'd disappear before I spoke. What would I have said to them? Come with me? Take me home? Are you my mother? No. I sat alone in countless Chinese restaurants eating almond cookies, sipping tea with spoons and spoons of sugar. Popcorn and coffee was dinner. When I fainted from migraine in the grocery store, a Portuguese man above me mouthed: No breakfast. He gave me orange juice and chocolate bars. The color red sprang into relief singing Wagner's Walküre. Entire tribes gyrated and drummed in my head. I learned the samba from a Brazilian man so tiny, so festooned with glitter I was certain that he slept inside a filigreed, Fabergé egg. No one at the door: no salesmen, Mormons, meter readers, exterminators, no Harriet Tubman, no one. Red notes sounding in a grey trolley town."
import nltk

poem = poem.lower()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.data import load
from collections import defaultdict
# nltk.download()
tagdict = load('help/tagsets/upenn_tagset.pickle')

sent_text = nltk.sent_tokenize(poem) # this gives us a list of sentences
# now loop over each sentence and tokenize it separately
all_tagged = [nltk.pos_tag(nltk.word_tokenize(sent)) for sent in sent_text]


data ={k : set() for k in tagdict.keys()}

for itemset in all_tagged:
    for item in itemset:
        data[item[1]].add(item[0])

print(data)

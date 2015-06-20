import nltk
from nltk.corpus import brown

for category in brown.categories():
    words = brown.words(categories = category)
    fdist = nltk.FreqDist([w.lower() for w in words])
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    print category + ' '
    for m in modals:
        print m + ":", fdist[m],
    print "\n"

import nltk
from nltk.corpus import udhr

languages = ['Chinanteco-Ajitlan-Latin1', 'Chinanteco-UTF8', 'Chinese_Mandarin-GB2312']

cfd = nltk.ConditionalFreqDist((lang, len(word)) for lang in languages for word in udhr.words(lang))
cfd.plot(cumulative = True)

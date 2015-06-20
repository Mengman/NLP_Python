import nltk
from nltk.corpus import brown

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# genre = ['news', 'romance']

cfd = nltk.ConditionalFreqDist((gener, word) for gener in ['news', 'romance'] for word in brown.words(categories = gener) if word.lower() in days )
cfd.tabulate()

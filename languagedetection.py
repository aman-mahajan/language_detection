import nltk
from nltk.tokenize import PunktSentenceTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
from collections import defaultdict
import matplotlib.pyplot as plt


#tokenize sentences
def process_content(text):

    tokenizer = RegexpTokenizer(r'\w+') 
    words = nltk.word_tokenize(text)
    print words
    return words

#count number of stopwords for each language. Select max for detecting langauge
def detect_lang(words):
	count = {}
	for language in languages:
		stop_words = set(stopwords.words(language))
		text_stopwords = set(words)
		common = text_stopwords.intersection(stop_words)
		count[language] = len(common)
	detected = max(count, key=count.get)
	return detected

#count stopword frequency histogram
def hist(words, detected):
	if detected == 'English':
		sw = stopwords.words('English')
	elif detected == 'French':
		sw = stopwords.words('French')
	elif detected == 'German':
		sw = stopwords.words('German')
	elif detected == 'Spanish':
		sw = stopwords.words('Spanish')
	else:
		print 'language not valid'
	count_dict = defaultdict(int)
	for word in words:
		if word in sw:
			count_dict[word]+=1
	plot_hist(count_dict)

#plot histogram
def plot_hist(dict):
	plt.bar(range(len(dict.values())), dict.values(), align='center')
	plt.xticks(range(len(dict.values())), dict.keys(), size='small', rotation=90)
	plt.ylabel('Word Frequency')
	plt.xlabel('Stopwords')
	plt.show()


if __name__ == '__main__':

	#sample texts
	text = u"The Minister found herself in an happy situation when the House unprecedentedly voted her to continue to be in power. this is a joke!"

	text2 = u"Hamburg - Der Weltklimarat (IPCC) hat in Kopenhagen eine Debatte über die Zusammenfassung aller drei Teile seines neuen großen Klimaberichts begonnen. Bis zum Freitag ringen Wissenschaftler und Regierungsvertreter um den Wortlaut wichtiger Kernaussagen des sogenannten Synthesis-Report, den Uno-Generalsekretär Ban Ki Moon und IPCC-Chef Rajendra Pachauri am Sonntag präsentieren wollen. Die drei einzelnen Teile des Reports hatte das Gremium im September 2013 sowie im März und April 2014 vorgestellt. Die neue Zusammenfassung solle ein Fahrplan für politische Entscheidungsträger sein, anhand derer sie den Weg zu einem globalen Abkommen zum Klimaschutz finden könnten, sagte Pachauri am Montag zum Auftakt der Diskussionen in der dänischen Hauptstadt."

	text3 = u"mi casa su casa"

	words = process_content(text3)
	languages = ['English', 'French', 'German', 'Spanish']
	detected = detect_lang(words)
	print detected + ' Detected\n'
	hist(words, detected)
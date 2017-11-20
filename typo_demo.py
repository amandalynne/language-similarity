import typology


def demo(language):
    print "The most similar language to "+ language + " is: "
    print typology.get_similar_langs(language)[0]
#demo('Kannada')
#demo('Telugu')
#demo('Urdu')

demo('Persian')
demo('German')
demo('Korean')
#demo('Turkish')
#demo('Russian')
#demo('Polish')
#demo('Japanese')

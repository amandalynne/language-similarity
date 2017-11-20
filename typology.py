# -*- mode: Python; coding: utf-8 -*-

"""Typological similarity of languages using cosine similarity"""

import csv, numpy as np, scipy.spatial.distance as ssd
from mapping import Mapping
from collections import defaultdict

language_data = []

with open('language.csv') as inf:
    reader = csv.reader(inf)
    top_row = reader.next()
    for row in reader:
        language_data.append(row)

features = dict((feat, set()) for feat in top_row[8:])
feature_mapping = Mapping(top_row[8:])

#print feature_mapping.item(0)
#print feature_mapping.item(1)

values = defaultdict(set) 
languages = []
language_values = defaultdict(list)
for language_row in language_data:
    languages.append(language_row[3])
    features = language_row[8:]
    for i in range(len(features)):
        if features[i]:
            values[feature_mapping.item(i)].add(features[i])
            language_values[language_row[3]].append(feature_mapping.item(i)+": "+features[i])

language_mapping = Mapping(languages)

# all possible feature / value combos in a 1-D vector.

mega_vector = []
mega_table = []

for i in range(len(feature_mapping)):
    feature_name = feature_mapping.item(i)
    mega_vector.extend(sorted(list(values[feature_name])))
    mega_table.append(sorted(list(values[feature_name])))


#print mega_table[0]

feature_vector = []
for item in feature_mapping.keys():
    for value in sorted(list(values[item])):
        feature_vector.append(item+": "+value)

feat_val_mapping = Mapping(feature_vector)
#print feat_val_mapping.item(0)
#print feat_val_mapping.item(2)

#print feat_val_mapping.item((len(feature_vector)-1))

#print language_values['English']
#print language_mapping['English']


languages_table = np.zeros((len(languages),len(feature_vector)))
feat_val_counts = np.zeros(len(feature_vector))
for language in languages:
    for feature in language_values[language]:
        index = feat_val_mapping[feature]
        languages_table[language_mapping[language]][index] += 1
        feat_val_counts[index] +=1


languages_table/=feat_val_counts

# print feat_val_counts CORRECT
# scores are dot product of components divided by square crap
# find the one with the highest score somehow (get index of max score? but not the lang itself)
def get_lang_tab():
    return languages_table


def scores(language):
    lang_vector = languages_table[language_mapping[language]]
    scores = np.zeros(len(languages))
    cos_scores = np.zeros(len(languages))
    for lang in languages:
        if lang == language:
            cos_scores[lang_index] = -1
        else:
            lang_index = language_mapping[lang]
            lang_2_vec = languages_table[lang_index]
    #        try:
            scores[lang_index] = np.dot(lang_vector, lang_2_vec)
            sum_squares_1 = np.sum(lang_vector*lang_vector)
            sum_squares_2 = np.sum(lang_2_vec*lang_2_vec) 
            if sum_squares_1 != 0 and sum_squares_2 != 0:
                cos_scores[lang_index] = scores[lang_index] / (sum_squares_1 * sum_squares_2)
            else:
                cos_scores[lang_index] = -1


#        scores[lang_index] = ssd.cosine(lang_vector, lang_2_vec)
 #       except:
            
    return scores

    
def get_similar_langs(language, top=5):
    cos_scores = scores(language)
    english_index = language_mapping['English']
    print cos_scores[english_index]
    #get indices of maxes
    max_indices = np.argwhere(cos_scores == np.amax(cos_scores)).flatten().tolist()
    score = np.amax(cos_scores)
    lang_list = []
    for index in max_indices:
        lang_list.append(language_mapping.item(index))
    print score 
    return lang_list


'''
print get_similar_langs('English')    
print get_similar_langs('French')
print get_similar_langs('German')
print get_similar_langs('Kwomtari')
'''    





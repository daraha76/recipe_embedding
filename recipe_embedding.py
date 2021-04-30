import gensim.models
from gensim.models import FastText
from gensim.models import KeyedVectors
import csv
import os

recipe_sentences = []
direction = 'recipe_data/'
print(os.listdir(direction))
recipe_folder = os.listdir(direction)
for i, folder in enumerate(recipe_folder):
    csv_filepath = os.listdir(direction + folder)
    print(csv_filepath)
    for j, csv_file in enumerate(csv_filepath):
        fi = open(direction+folder+'/'+csv_file)
        print(csv_file)
        rdr = csv.reader(fi)
        for k, row in enumerate(rdr):
            if k == 0:
                continue
            elif k % 2 == 0:
                recipe_sentences.append(row)
        fi.close()

print(len(recipe_sentences))


import os
from utils import get_tagged_df
from tqdm import tqdm
import pandas as pd
import concurrent.futures
from multiprocessing import Pool

FILES_DIR = '../../Dane/wiki_test/'

verb_tags = ('fin', 'bedzie', 'aglt', 'praet', 'impt', 'imps', 'inf', 'pcon', 'pant', 'ger', 'pact', 'ppas')

def part_of_speech(row):
    pos = None
    if row['tag'].startswith('subst'):
        pos = 'noun'
    elif row['tag'].startswith('adj'):
        pos = 'adjective'
    elif row['tag'].startswith(verb_tags):
        pos = 'verb'

    return pos

files = os.listdir(FILES_DIR)

def process(files):

    if type(files) is str:
        files = [files]

    for file_name in files:
        if file_name.endswith('.txt'):

            try:
                with open(FILES_DIR+file_name, 'r') as f:
                    text = f.read()
                for tager in ['morphoDita', 'wcrft2', 'krnnt']:
                    df = get_tagged_df(text, tager)
                    df['part'] = df.apply(part_of_speech, axis=1)
                    df.to_csv(FILES_DIR+file_name[:-4]+'_'+tager+'.csv')

            except Exception as e:
                print()
                print(e)
                print(tager, file_name)
    print(file_name)

# process(files)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(process, files)

with Pool() as p:
    p.map(process, files)
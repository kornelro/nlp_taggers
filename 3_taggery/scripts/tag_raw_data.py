import pandas as pd
from tqdm import tqdm
from utils import get_tagged_df


with open('../../Dane/test-raw.txt', 'r') as f:
    test_raw = f.read()

test_raw = test_raw.splitlines()

morhpodita_df = pd.DataFrame(columns=['base', 'tag'])
wcrft2_df = pd.DataFrame(columns=['base', 'tag'])
krnnt_df = pd.DataFrame(columns=['base', 'tag'])

i = 0

for text in tqdm(test_raw):

    try:
        morhpodita_df = morhpodita_df.append(
            get_tagged_df(text, 'morphoDita')
        )

        wcrft2_df = wcrft2_df.append(
            get_tagged_df(text, 'wcrft2')
        )

        krnnt_df = krnnt_df.append(
            get_tagged_df(text, 'krnnt')
        )
        
        i += 1

    except Exception as e:
        print()
        print(e)
        print(text)

print('Tagged '+str(i)+' texts.')

morhpodita_df.to_csv('../tagged/morhpodita_tags.csv')
wcrft2_df.to_csv('../tagged/wcrft2_tags.csv')
krnnt_df.to_csv('../tagged/krnnt_tags.csv')
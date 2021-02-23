import json
import requests
import time
from xml.dom import minidom
import xml.etree.ElementTree as ET
import pandas as pd
from tqdm import tqdm

clarinpl_url = "http://ws.clarin-pl.eu/nlprest2/base"
user_mail = "demo2019@nlpday.pl"


def morphoDita_tagger(text, display=False):
    url = clarinpl_url + "/process"
    lpmn = "morphoDita"
    
    payload = {'text': text, 'lpmn': lpmn, 'user': user_mail}
    headers = {'content-type': 'application/json'}
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    ccl = r.content.decode('utf-8')
    
    
    if display:
        print(ccl)
        
    return ccl
        
        
def wcrft2_tagger(text, display=False):
    url = clarinpl_url + "/process"
    lpmn = "wcrft2"
    
    payload = {'text': text, 'lpmn': lpmn, 'user': user_mail}
    headers = {'content-type': 'application/json'}
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    ccl = r.content.decode('utf-8')
    
    if display:
        print(ccl)
    
    return ccl


def krnnt_tagger(text, display=False):
    url = "http://127.0.0.1:9003/"

    r = requests.post(url, data=text.encode('utf-8'))
    ccl = r.content.decode('utf-8')
    
    if display:
        print(ccl)
        
    return ccl


def tree_to_base_tags(tree):
    d = []
    for tok in tree.iter('tok'):
        lex = list(filter(lambda el: el.get('disamb') == '1', tok))[0]
        d.append((lex.find('./base').text, lex.find('./ctag').text))

    return d


def ccl_to_bases_tags(ccl):
    tree = ET.fromstring(ccl)
    return tree_to_base_tags(tree)


def ccl_to_bases_tags_krnnt(ccl):
    bases_tags = []
    
    for line in ccl.splitlines():
        if line.endswith('disamb'):
            line = list(line.split('\t'))
            bases_tags.append((line[1], line[2]))
            
    return bases_tags


def get_tagged_df(text, tagger):
    result = None

    if tagger == 'morphoDita':
        result = pd.DataFrame(
            ccl_to_bases_tags(morphoDita_tagger(text)),
            columns=['base', 'tag']
        )
    elif tagger == 'wcrft2':
        result = pd.DataFrame(
            ccl_to_bases_tags(wcrft2_tagger(text)),
            columns=['base', 'tag']
        )
    elif tagger == 'krnnt':
        result = pd.DataFrame(
            ccl_to_bases_tags_krnnt(krnnt_tagger(text)),
            columns=['base', 'tag']
        )
    else:
        raise Exception('Wrong tagger name! Select: morphoDita, wcrft2 or krnnt.')

    return result

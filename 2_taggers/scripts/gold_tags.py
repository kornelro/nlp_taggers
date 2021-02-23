import xml.etree.ElementTree as ET
import pandas as pd
from utils import tree_to_base_tags

tree = ET.parse('../../Dane/gold-task-c.xml')
tags = tree_to_base_tags(tree)

df = pd.DataFrame(
        tags,
        columns=['base', 'tag']
    )

df.to_csv('../tagged/gold_tags.csv')

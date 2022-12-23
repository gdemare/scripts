#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import glob
import re
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pandas as pd

dossier = r'C:/Users/Guigui/GitHub/gdemare.github.io/'
data = pd.DataFrame(columns = ['chemin', 'fichier', 'extension'] )
dossAide = dossier + 'aide-memoire/'

for root, dirs, files in os.walk(dossAide):
    for file in files:
        if file.endswith('.md'):
            chemin = root[len(dossAide):]
            if file.endswith('_r.md'):
                ext = 'r'
                fichier = file[:-5]
            elif file.endswith('_sas.md'):
                ext = 'sas'
                fichier = file[:-7]
            elif file.endswith('_py.md'):
                ext = 'py'
                fichier = file[:-6]
            else :
                fichier = file[:-3]
                ext = 'general'
            data.loc[len(data)] = [chemin, fichier, ext]


# In[5]:


tabcroi = pd.pivot_table(data, columns='extension', index=['fichier'], aggfunc='count')
tab = tabcroi.reset_index()
tab.fillna(0,inplace=True)
tab.columns = ['fichier', 'general', 'py', 'r', 'sas'] 
tab[[ 'general', 'py', 'r', 'sas']] = tab[[ 'general', 'py', 'r', 'sas']].astype(int)

label = data[["chemin", "fichier"]].drop_duplicates(keep='last')
jointure = pd.merge(label, tab, how = "left", on = "fichier")
jointure = jointure


# In[6]:


texte = ""
col = jointure.columns
print(col)
for i, row in jointure.iterrows():
    texte = texte + "{ chemin: '" + row[col[0]] + "/" + row[col[1]] + "', general: " + str(row[col[2]])
    texte = texte + ", r: " + str(row[col[4]]) + ", sas:" + str(row[col[5]])  + ", py:" + str(row[col[3]])  + "},\n"


# In[ ]:


tex = '// dossier ; sous dossier; chemin; general; r; sas; python\nfichiers = [' + str(texte)[0:-2] + '];'

with open(dossier + 'js/data.js', 'w') as f:
    sys.stdout = f
    print(tex)
    sys.stdout = original_stdout


# In[ ]:





# In[ ]:





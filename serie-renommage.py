#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import re
from tkinter import Tk
from tkinter.filedialog import askdirectory


# In[ ]:


dossier = askdirectory(title='Select Folder')
serie = re.search(r'((?!(/|\\)).)*$' , dossier).group(0)
os.chdir(dossier)
for i in os.listdir(dossier):
    if "mkv" in i:
        episode = re.search( "[S|s][0-9]{2}[E|e][0-9]{2}", i ).group(0)
        nvnom = serie + ' ' +episode + i[-4:]
        print(i)
        print(nvnom)
        os.rename(i, nvnom)


# In[ ]:





# In[ ]:





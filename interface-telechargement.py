import tkinter as tk
import os
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import date
import html
import re
from datetime import datetime

dossier = "C:\\Users\\Guigui\\Downloads\\"

def htmlPage (url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content.decode('UTF-8'), 'html.parser')
    return soup

def lien (url) : 
    adresse = re.match(r'(.)*//(.)*(\.fr|\.com)', str(url))
    return adresse.group(0)

### Trovuer des liens mp3
def audioLien (url) :
    soup = htmlPage(url)
    texte = str(soup)
    lien = re.search(r'https.[\S]*((?<!\").).mp3' , texte).group(0)
    nom = re.search(r'((?!/).)*$',url).group(0)
    return lien, nom

#### Télécharge le fichier trouvé
def download (fichier, url) :
    myfile = requests.get(url)
    open(fichier, 'wb').write(myfile.content)

## Radio france
#### renvoie un tableau avec les émissions et leur lien
def rfListe (url) :
    adresse = lien(url)
    soup = htmlPage(url)
    contenu = soup.findAll(class_='ConceptTitle')
    liste = []
    for i in contenu :
        liste.append(adresse+i.find('a', href=True)['href'])
    return liste

def rfFichier (url, titre):
    date = re.search(r'[0-9]{2}.[0-9]{2}.[0-9]{4}',url).group(0)
    date = datetime.strptime(date, '%d.%m.%Y')
    date = date.strftime('%Y-%m-%d')
    fichier = dossier + date + '_'+ titre +'.mp3'
    return fichier

## 

def ytvideo(url):
    ytid = url[len("https://www.youtube.com/watch?v="):]
    print(url)
    os.system(f"yt-dlp -P {dossier} {ytid}")

def radioFrance (url):
    liste = rfListe(url)
    if rfListe(url)==[]:
        liste.append(url)
    print(f"{len(liste)} épisodes trouvés" )
    for i in liste:
        mp3, titre = audioLien(i)
        print( rfFichier(mp3, titre) )
        download( rfFichier(mp3, titre), mp3)

##-----------------------Interface------------------------
root = tk.Tk()

textEntry = tk.StringVar()

saisie = tk.Entry(root, textvariable = textEntry, width=50)
saisie.grid(row=1, padx=20,  pady=10, column=0)
tk.Button(root, text="Blanc", command=lambda: ytvideo(saisie.get()), width=10 ).grid(row=1, column=1, padx=15)
tk.Button(root, text="Youtube vidéo", command=lambda: ytvideo(saisie.get()), width=30).grid(row=3)
tk.Button(root, text="Radio france", command=lambda: radioFrance(saisie.get()), width=30).grid(row=4)

root.mainloop()
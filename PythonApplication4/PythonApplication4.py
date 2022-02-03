from tkinter import *
from tkinter.messagebox import*
sonastik = {}
file=open("riigid_pealinnad.txt",'r')
for line in file:
    k, v=line.strip().split('-')
    sonastik[k.strip()]=v.strip()

print(sonastik)

from tkinter import *
from tkinter.font import Font
def failist_sonastikusee():
    tund_kirjeldus={}
    file=open("riigid_pealinnad.txt",'r')
    for line in file:
        tund_kirjeldus=Line.strip().split(':')
        tund_kirjeldus[tund.strip()]=kirjeldus.strip()
    print(tund_kirjeldus)
    return tund_kirjeldus

def kirjeldus_aknasse(t):

tund_kirjeldus=failist_sonastikusee()


for i in range(11):
    tn=Label(aken,text=str(i)+"\n"+kell[i],relief="solid").grid
    (row=0,column=i+1,sticky=N+S+W+E)
    command=lambda:kirjeldus=aknasse("Programeerimise")

    
def kirjeldus_aknasse(t:str):
    if(askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_aken=TopLevel()
        lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t].pack())
    else:
        showinfo("Vastus","Kui ei taha siis ei taha!")

    print(tund_kirjeldus[t])


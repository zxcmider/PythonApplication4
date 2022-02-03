from tkinter import *
aken=Tk()
aken.geometry("1680x1050")
aken.title("Tunniplaan")
p=["Esmaspäev","Tesipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
	Ep=Label(aken,text=p[j],relief="groove",font="Arial",height=6).grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
	j+=1


for i in range(11):
	tn="t"+str(i)
	tn=Label(aken,text=i,relief="groove",font="Arial",width=8,height=2).grid(row=0,column=i+1,sticky=N+S+W+E)
Ep=Label(aken,text="Esmaspäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=2,column=0,rowspan=2,sticky=N+S+W+E)
Tp=Label(aken,text="Teisipäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=4,column=0,rowspan=2,sticky=N+S+W+E)
Kp=Label(aken,text="Kolmapäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=6,column=0,rowspan=2,sticky=N+S+W+E)
Np=Label(aken,text="Neljapäev",relief="groove",font="Arial 10",width=10,height=4).grid(row=8,column=0,rowspan=2,sticky=N+S+W+E)
Rp=Label(aken,text="Reede",relief="groove",font="Arial 10",width=10,height=1).grid(row=10,column=0,rowspan=2,sticky=N+S+W+E)

t0=Label(aken,text="0",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=1,sticky=N+S+W+E)
t1=Label(aken,text="1",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=2,sticky=N+S+W+E)
t2=Label(aken,text="2",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=3,sticky=N+S+W+E)
t3=Label(aken,text="3",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=4,sticky=N+S+W+E)
t4=Label(aken,text="4",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=5,sticky=N+S+W+E)
t5=Label(aken,text="5",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=6,sticky=N+S+W+E)
t6=Label(aken,text="6",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=7,sticky=N+S+W+E)
t7=Label(aken,text="7",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=8,sticky=N+S+W+E)
t8=Label(aken,text="8",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=9,sticky=N+S+W+E)
t9=Label(aken,text="9",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=10,sticky=N+S+W+E)
t10=Label(aken,text="10",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=11,sticky=N+S+W+E)

k1=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=2,column=2,columnspan=2,sticky=N+S+W+E)
ks=Button(aken,text="   ",relief="groove",font="Arial 20",width=10,height=4).grid(row=3,column=4,sticky=N+S+W+E)
k2=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=2,column=5,columnspan=3,sticky=N+S+W+E)
k0=Button(aken,text="Rühmajuhataja tund",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=2,column=8,rowspan=2,sticky=N+S+W+E)
k3=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=3,column=2,columnspan=3,sticky=N+S+W+E)
k4=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=3,column=5,columnspan=2,sticky=N+S+W+E)

h1=Button(aken,text="Inglise Keel",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
h2=Button(aken,text="Inglise Keel",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=5,column=2,columnspan=2,sticky=N+S+W+E)
h3=Button(aken,text="Operatsioonisüsteemide alused",relief="groove",font="Arial 20",bg="#f603a3",width=10,height=4).grid(row=4,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
h4=Button(aken,text="    ",relief="groove",font="Arial 20",width=10,height=4).grid(row=4,column=6,rowspan=2,sticky=N+S+W+E)
h5=Button(aken,text="Kehaline kasvatus",relief="groove",font="Arial 20",bg="#f603a3",width=10,height=4).grid(row=4,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
h6=Button(aken,text="Eesti keel",relief="groove",font="Arial 20",bg="#8e7cc3",width=10,height=4).grid(row=4,column=9,rowspan=1,columnspan=1,sticky=N+S+W+E)
h7=Button(aken,text="Eesti keel",relief="groove",font="Arial 20",bg="#3e3530",width=10,height=4).grid(row=5,column=9,rowspan=1,columnspan=1,sticky=N+S+W+E)
h8=Button(aken,text="Geograafia",relief="groove",font="Arial 20",bg="#f8ac6a",width=10,height=4).grid(row=4,column=10,rowspan=2,sticky=N+S+W+E)

y1=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
y2=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=7,column=2,columnspan=3,sticky=N+S+W+E)
y3=Button(aken,text="    ",relief="groove",font="Arial 20",width=10,height=4).grid(row=6,column=5,rowspan=2,sticky=N+S+W+E)
y4=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
y5=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=7,column=6,columnspan=3,sticky=N+S+W+E)
y6=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",width=4,height=1,bg="#424983").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
y7=Button(aken,text="Kunstiained",relief="groove",font="Arial 20",width=4,height=1,bg="#424983").grid(row=6,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

g1=Button(aken,text="Andmebaasisüsteemide alused",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=2,columnspan=5,sticky=N+S+W+E)
g2=Button(aken,text="Geograafia",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=7,columnspan=1,rowspan=2,sticky=N+S+W+E)
g3=Button(aken,text="",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=8,columnspan=1,sticky=N+S+W+E)
g4=Button(aken,text="Eesti Keel",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=9,column=8,columnspan=1,sticky=N+S+W+E)
g5=Button(aken,text="Eesti Keel",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=9,column=8,columnspan=1,sticky=N+S+W+E)

aken.mainloop()

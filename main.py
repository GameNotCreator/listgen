
from tkinter import * 
from tkinter import messagebox as ms
import random

def btnClickFunction():
    global Output, OutputField, sortedList, label4, label5
    
    iMin, iMax, n = getInputBoxValue()
    
    if is_valid_input(iMin) and is_valid_input(iMax) and is_valid_input(n):
        int(iMin)
        int(iMax)
        int(n)

        liste = generateList(iMin, iMax, n)
        print(liste)

        label4 = Label(root, text = "Liste générée", font=["Times New Roman", 12], padx=10, pady=10)
        label4.place(relx=0.5, rely=0.73,anchor=CENTER, height=30)

        Output = Text(root, height=1.5, width=50)
        Output.insert(END, str(liste))
        Output.place(relx=0.5, rely=0.83, anchor=CENTER, height=30)

        e = element(liste)

        OutputField = Label(root, text=e[0], font=["Times New Roman", 10], padx=10, pady=10)
        OutputField.place(relx=0.5, rely=0.77,anchor=CENTER, height=20)

        label5 = Label(root, text = "Liste triée", font=["Times New Roman", 12], padx=10, pady=10)
        label5.place(relx=0.5, rely=0.90,anchor=CENTER, height=30)

        sortedList = Text(root, height=1.5, width=50)
        sortedList.insert(END, str(e[1]))
        sortedList.place(relx=0.5, rely=0.95,anchor=CENTER, height=30)

    else:
        ms.showerror(title="Error", message="Tu dois remplir tout les champs avec des entiers positifs")

def is_valid_input(value):
    return value.isdigit() and value != ""

def element(liste):
    mini = liste[0]
    maxi = liste[0]
    somme = 0
    n = len(liste)

    for i in liste:
        if mini > i:
            mini = i
        if maxi < i:
            maxi = i
        somme = somme + i
    
    moyenne = round(somme / n, 1)

    for j in range(len(liste)):
        for k in range(len(liste)):
            if liste[j] < liste[k]:
                liste[j], liste[k] = liste[k], liste[j]


    if n % 2 == 1:
        mediane = liste[n // 2]
    else:
        mediane = (liste[n // 2 - 1] + liste[n // 2]) / 2

    return ("Minium : " + str(mini) + " | Maximum : " + str(maxi) + " | Moyenne : " + str(moyenne) + " | Mediane : " + str(round(mediane)), liste)

def getInputBoxValue():
    iMin = RangeMin.get()
    iMax = RangeMax.get()
    n = N.get() 
    return iMin, iMax, n

def generateList(iMin, iMax, n):
    return [random.randint(int(iMin), int(iMax)) for i in range(int(n))]
        
root = Tk()

titre = Label(root, text = "Generateur de liste", font=["Times New Roman", 20], padx=10, pady=10)
titre.place(relx=0.5, rely=0.07,anchor=CENTER, height=30)

btn = Button(root, text='Generer la liste', bg='#808080', font=["Times New Roman", 14], command=btnClickFunction, padx=10, pady=10)
btn.place(relx=0.5, rely=0.62, width=200, anchor=CENTER, height=30)

label1 = Label(root, text = "Range minimum", font=["Times New Roman", 14], padx=10, pady=10)
label1.place(relx=0.5, rely=0.15,anchor=CENTER, height=30)

RangeMin = Entry(root)
RangeMin.place(relx=0.5, rely=0.20, width=200, anchor=CENTER, height=30)

label2 = Label(root, text = "Range maximum", font=["Times New Roman", 14], padx=10, pady=10)
label2.place(relx=0.5, rely=0.30,anchor=CENTER, height=30)

RangeMax=Entry(root)
RangeMax.place(relx=0.5, rely=0.35, width=200, anchor=CENTER, height=30)

label3 = Label(root, text = "Taille de la liste", font=["Times New Roman", 14], padx=10, pady=10)
label3.place(relx=0.5, rely=0.45,anchor=CENTER, height=30)

N = Entry(root)
N.place(relx=0.5, rely=0.50, width=200, anchor=CENTER, height=30)



def update_widget_backgrounds(color):
    titre.config(bg=color, fg='white')
    btn.config(bg='#FF0000', fg='white')
    label1.config(bg=color, fg='white')
    label2.config(bg=color, fg='white')
    label3.config(bg=color, fg='white')
    RangeMin.config(bg=color, fg='white')
    RangeMax.config(bg=color, fg='white')
    N.config(bg=color, fg='white')
    
    if 'Output' in globals():
        Output.config(bg=color, fg='white')
        OutputField.config(bg=color, fg='white')
        sortedList.config(bg=color, fg='white')
        label4.config(bg=color, fg='white')
        label5.config(bg=color, fg='white')
    
def update_color():
    global index, transition
    c1, c2 = colors[index], colors[(index + 1) % len(colors)]
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    rgb = (int(r1 + (r2 - r1) * transition), int(g1 + (g2 - g1) * transition), int(b1 + (b2 - b1) * transition))
    color = '#{0:02x}{1:02x}{2:02x}'.format(rgb[0], rgb[1], rgb[2])
    root.configure(background=color)
    update_widget_backgrounds(color)  
    transition += 0.05
    if transition >= 1.0:
        transition = 0.0
        index = (index + 1) % len(colors)
    root.after(200, update_color)
    
colors = ['#F62992', '#6B0AB8', '#340DA4', '#476AED', '#50CFEF']
index, transition = 0, 0.0

update_color()
root.geometry('500x500')
root.maxsize(500, 500)
root.minsize(500, 500)
root.configure(background='#F0F8FF')
root.title('Generateur de liste')


root.mainloop()






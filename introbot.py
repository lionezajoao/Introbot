import datetime
import random

def gerar(path):
    template = open(path+"template.txt", "r")
    valor = open(path+"valor.txt", "r")
    t1 = template.readlines()
    val = valor.readlines()


    t = random.choice(t1)
    v1 = random.choice(val)
    v2 = random.choice(val)
    v3 = random.choice(val)

    for i in range(len(t1)):
        if t == t1[i]:
            id1 = i+1

    for i in range(len(val)):
        if v1 == val[i]:
            id2 = i+1
        if v2 == val[i]:
            id3 = i+1
        if v3 == val[i]:
            id4 = i+1
    

    idt = "Last.fm ID: %d, %d, %d, %d." %(id1, id2, id3, id4)
    ct = t + " "+ v1+ ", " + v2 + ", " + v3 + "."

    c = ct.replace('\n', '')
    dia = datetime.date.today().strftime("%A")  
    diat = datetime.date.today().strftime("%d/%m/%y")
    if dia == "Wednesday":
        diat = datetime.date.today().strftime("%d/%m/%y")+"\nIt's Wednesday, my dudes!!!"

    valcomp = "\n```%s\n\n%s\n\nRegistro feito em: %s```\n" %(c, idt, diat)
    template.close()
    valor.close()
    return valcomp

def recriar(path, aux):
    valores = list(map(int, aux.split()))
    template = open(path+"template.txt", "r")
    valor = open(path+"valor.txt", "r")
    t1 = template.readlines()
    val = valor.readlines()
    valcomp = ''
    for index, i in enumerate(t1):
        if valores[0] - 1 == index:
            valcomp += "```"+i
    for i in range(len(valores)-1):
        i += 1
        for index, j in enumerate(val):
            if valores[i] - 1 == index:
                valcomp += ", "+j
    valcomp += "."+"```"
    return valcomp.replace("\n", '')
#PP
path = "/home/d4rthbodus/Repositorios/introbot-420/"
bc = open(path+"backup.txt", "a+")

backup = gerar(path)
bc.write(backup.replace("`", ''))
bc.close()
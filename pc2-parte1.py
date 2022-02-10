from subprocess import call
import sys
import os

#### PARTE 1: DESPLIEGUE DE LLA APLICACIÓN EN MÁQUINA VIRTUAL PESADA ####

os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
os.system("pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")


## Cambio de título 
os.environ['GROUP_NUMBER'] = 'Grupo 20'

try:
    fhin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
    fhout = open("html.html", "w")

    for line in fhin :
        if '''{% block title %}Simple Bookstore App{% endblock %}''' in line :
            fhout.write('''{% block title %}'''+ os.environ[ 'GROUP_NUMBER' ] +'''{% endblock %}''')
        else:
            fhout.write(line)
    
    fhin.close()
    fhout.close()
except:
    print("Error cambiando el título")

try:
    fhin2 = open("html.html", "r")
    fhout2 = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w")

    for line in fhin2 :
        fhout2.write(line)
    
    fhin2.close()
    fhout2.close()
except: 
    print("Error en la copia del html")

try:
    os.system("rm html.html")
except:
    print("Error eliminando auxiliar html")

 ##

os.system("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080")

#http://<ip-publica>:9080/productpage
#### FIN PARTE 1 ####

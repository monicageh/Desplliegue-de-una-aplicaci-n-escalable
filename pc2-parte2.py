from subprocess import call
import sys
import os

#### PARTE 2: DESPLIEGUE DE UNA APLICACION MONOLITICA USANDO DOCKER ####

os.chdir('practica_creativa2/bookinfo/src/productpage')

# Creación del Dockerfile

fhin = open("Dockerfile", "w")
fhin.write("FROM python:3.7.7-slim\n")
fhin.write("\n")
fhin.write("WORKDIR /practica_creativa2/bookinfo/src/productpage\n")
fhin.write("\n")
fhin.write("COPY requirements.txt . ./\n")
fhin.write("COPY productpage_monolith.py . ./\n")
fhin.write("COPY templates/productpage.html . /templates/\n")
fhin.write("COPY templates/index.html . /templates/\n")
fhin.write("\n")
fhin.write("RUN apt-get update\n")
fhin.write("RUN apt-get -y install python3\n")
fhin.write("RUN apt-get -y install python3-pip\n")
fhin.write("RUN pip3 install -r requirements.txt\n")
fhin.write("\n")
fhin.write("EXPOSE 9080\n")
fhin.write("\n")
fhin.write("ENV GROUP_NUMBER = 'Grupo 20'\n")
fhin.write("\n")
fhin.write('CMD [ "python3", "productpage_monolith.py", "9080" ]\n')
fhin.close()

os.system("sudo docker build -t 'g20/productpage' .") 
os.system("sudo docker run --name g20-productpage -p 80:9080 -e GROUP_NUMBER=20 -d g20/productpage")

#http://<ip-publica>/productpage
#### FIN PARTE 2 ####

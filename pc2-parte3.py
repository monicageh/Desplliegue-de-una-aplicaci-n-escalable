from subprocess import call
import sys
import os

#### PARTE 3: SEGMENTACIÓN DE UNA APLICACIÓN MONOLÍTICA EN MICROSERVICIOS UTILIZANDO DOCKER-COMPOSE ####

## Borramos la imagen y paramos y borramos el contenedor de la parte 2

os.system("sudo docker stop g20-productpage")
os.system("sudo docker rm g20-productpage")
os.system("sudo docker rmi g20/productpage")

## Definimos los Dockerfiles

# DOCKERFILE PRODUCTPAGE
os.chdir('practica_creativa2/bookinfo/src/productpage')

fhin = open("Dockerfile", "r")
fhout = open("aux", "w")
for line in fhin :
    if 'CMD [ "python3", "productpage_monolith.py", "9080" ]' in line :
        fhout.write('CMD [ "python3", "productpage.py", "9080" ]')
    else :
        fhout.write(line)

fhin.close()
fhout.close()

fhin2 = open("aux", "r")
fhout2 = open("Dockerfile", "w")

for line in fhin2 :
    fhout2.write(line)
    
fhin2.close()
fhout2.close()

os.system("rm aux")

#Creamos la imagen
os.system("sudo docker build -t 'g20/productpage' .") 

# DOCKERFILE DETAILS

os.chdir('..')
os.chdir('details')

fhin = open("Dockerfile", "w")
fhin.write("FROM ruby:2.7.1-slim\n")
fhin.write("\n")
fhin.write("WORKDIR /opt/microservices\n")
fhin.write("\n")
fhin.write("COPY details.rb . /opt/microservices/\n")
fhin.write("\n")
fhin.write("EXPOSE 9080\n")
fhin.write("\n")
fhin.write("ENV SERVICE_VERSION = v1\n")
fhin.write("ENV ENABLE_EXTERNAL_BOOK_SERVICE = true\n")
fhin.write("\n")
fhin.write('CMD [ "ruby", "details.rb", "9080"]\n')
fhin.close()

#Creamos la imagen
os.system("sudo docker build -t 'g20/detailsv1' .") 

# DOCKERFILE REVIEWS

os.chdir('..')
os.chdir('reviews')

os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')

os.chdir('reviews-wlpcfg')
#Creamos la imagen
os.system("sudo docker build -t 'g20/reviews' .") 

# DOCKERFILE RATINGS

os.chdir('../..')
os.chdir('ratings')

fhin = open("Dockerfile", "w")
fhin.write("FROM node:12.18.1-slim\n")
fhin.write("\n")
fhin.write("WORKDIR /opt/microservices\n")
fhin.write("\n")
fhin.write("COPY package.json . /opt/microservices/\n")
fhin.write("COPY ratings.js . /opt/microservices/\n")
fhin.write("\n")
fhin.write("RUN npm install\n")
fhin.write("\n")
fhin.write("EXPOSE 9080\n")
fhin.write("\n")
fhin.write("ENV SERVICE_VERSION = v1\n")
fhin.write("ENV ENABLE_EXTERNAL_BOOK_SERVICE = true\n")
fhin.write("\n")
fhin.write('CMD [ "node", "ratings.js", "9080" ]\n')
fhin.close()

#Creamos la imagen
os.system("sudo docker build -t 'g20/ratingsv1' .") 

# DOCKER-COMPOSE

os.chdir('..')

fhin = open("docker-compose.yml", "w")
fhin.write("version:  '3.3'\n")
fhin.write("\n")
fhin.write("services:\n")
fhin.write("\n")
fhin.write("  productpage:\n")
fhin.write("    container_name: g20-productpage\n")
fhin.write("    image: g20/productpage\n")
fhin.write("    ports:\n")
fhin.write('      - "9080:9080"\n')
fhin.write("    links:\n")
fhin.write('      - "details"\n')
fhin.write('      - "reviews"\n')
fhin.write("\n")
fhin.write("  details:\n")
fhin.write("    container_name: g20-detailsv1\n")
fhin.write("    image: g20/detailsv1\n")
fhin.write("    expose:\n")
fhin.write("      - 9080\n")
fhin.write("\n")
fhin.write("  reviews:\n")
fhin.write("    container_name: g20-reviews\n")
fhin.write("    image: g20/reviews\n")
fhin.write("    expose:\n")
fhin.write("      - 9080\n")
fhin.close()

os.system("sudo docker-compose up")
####
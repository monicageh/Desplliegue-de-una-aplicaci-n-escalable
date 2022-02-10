from subprocess import call
import sys
import os

#MODIFICAMOS LOS DOCKERFILE PARA V1

# Dockerfile Details

os.chdir('practica_creativa2/bookinfo/src/details')

fhin = open("Dockerfile", "r")
fhout = open("aux", "w")

for line in fhin :
    if "ENV SERVICE_VERSION = v2" in line :
        fhout.write("ENV SERVICE_VERSION = v1\n")
    elif "ENV SERVICE_VERSION = v3" in line :
        fhout.write("ENV SERVICE_VERSION = v1\n")
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
os.system("sudo docker build -t 'g20/detailsv1' .")

# Dockerfile Ratings

os.chdir('..')
os.chdir('ratings')

fhin = open("Dockerfile", "r")
fhout = open("aux", "w")

for line in fhin :
    if "ENV SERVICE_VERSION = v2" in line :
        fhout.write("ENV SERVICE_VERSION = v1\n")
    elif "ENV SERVICE_VERSION = v3" in line :
        fhout.write("ENV SERVICE_VERSION = v1\n")
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
os.system("sudo docker build -t 'g20/ratingsv1' .") 


# MODIFICAMOS EL DOCKER-COMPOSE PARA V1

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
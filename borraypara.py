from subprocess import call
import sys
import os

# BORRAMOS Y PARAMOS LOS CONTENEDORES DE LA PARTE 3

os.system("sudo docker stop g20-productpage")
os.system("sudo docker rm g20-productpage")
os.system("sudo docker stop g20-reviews")
os.system("sudo docker rm g20-reviews")
os.system("sudo docker stop g20-detailsv1")
os.system("sudo docker rm g20-detailsv1")
os.system("sudo docker stop g20-detailsv2")
os.system("sudo docker rm g20-detailsv2")
os.system("sudo docker stop g20-detailsv3")
os.system("sudo docker rm g20-detailsv3")
os.system("sudo docker stop g20-ratingsv1")
os.system("sudo docker rm g20-ratingsv1")
os.system("sudo docker stop g20-ratingsv2")
os.system("sudo docker rm g20-ratingsv2")
os.system("sudo docker stop g20-ratingsv3")
os.system("sudo docker rm g20-ratingsv3")
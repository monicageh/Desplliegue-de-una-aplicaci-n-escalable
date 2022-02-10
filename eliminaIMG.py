from subprocess import call
import sys
import os

## ELIMINAMOS LAS IMAGENES DE LA PARTE 3

os.system("sudo docker rmi g20/productpage")
os.system("sudo docker rmi g20/reviews")
os.system("sudo docker rmi g20/detailsv1")
os.system("sudo docker rmi g20/detailsv2")
os.system("sudo docker rmi g20/detailsv3")
os.system("sudo docker rmi g20/ratingsv1")
os.system("sudo docker rmi g20/ratingsv2")
os.system("sudo docker rmi g20/ratingsv3")
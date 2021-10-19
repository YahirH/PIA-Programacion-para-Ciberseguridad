#Descripción
#1.Archivo usado para importar pipreq, verificar si esta instalado e instalarlo o no.
#2.Tambien se usara para utilizar pipreq para instalar los modulos de requirements.txt

#importar modulos
import sys, subprocess, pkg_resources
import logging
import os
import requests
from lxml import html
from bs4 import BeautifulSoup


logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)s %(message)s')


def pireq():
  try:
    required = {'pipreqs'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    logging.info('Se busca si esta instalado pipreqs en su equipo')

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *required], stdout=subprocess.DEVNULL)
        subprocess.check_call([python, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        logging.info('Se instalo pipreqs')

    else:
        print('PIPREQS INSTALADO')
        print('Modulos en requirements instalados')
        logging.info('pipreqs ya estaba instalado')

  except FileNotFoundError:
    print ('Archivo requirements.txt no encontrado')
    logging.warning('Verifique si se encuentra pipreqs en el sitio correcto, de otra forma ubicarlo')


#WEB SCRAPING 
url = input("Ingrese url para aplicar el WebScraping : ")


#import urlparse

class Scraping:
    
				
    def scrapingImages(self,url):
        print("\nObteniendo imagenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src')

            print ('Imagenes %s encontradas' % len(images))
    
            #create directory for save images
            os.system("mkdir images")
            logging.info('Se creo un folder')
            
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                logging.info('Se descargo imagen con dirreccion al folder creado')
                f.close()
                
        except Exception as e:
                print (e)
                print ("Error conexion con " + url)
                logging.warning('URL ingresada no existente o no disponible')
                exit()
              
          
            
    def scrapingPDF(self,url):
        print("\nObteniendo pdfs de la url:"+ url)

        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
    
            #create directory for save pdfs
            if len(pdfs) >0:
                os.system("mkdir pdfs")
                logging.info('Se creo un folder con para los pdfs')
        
            print ('Encontrados %s pdf' % len(pdfs))
                
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)
                    
                # descarga pdfs
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                logging.info('se agregaron los pdfs encontrados')
                f.write(r.content)
                f.close()
    
        except Exception as e:
            print(e)
            print("Error conexion con " + url)
            logging.warning('Hubo error de conexion con la url')
            pass
    
   
    
scraping = Scraping()
scraping.scrapingImages(url)
scraping.scrapingPDF(url)



  #bloque de obtencion de metadata


from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta():
    ruta = input("Ruta de imágenes: ")
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            input()
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print ("\n")
                logging.info('Se encontro metadata')
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
                logging.warning('Hubo error de conexion con la url')
                
printMeta()

from PyPDF2 import PdfFileReader, PdfFileWriter
#import os

def metaPDF():
  ruta=input("ruta de PDF's: ")
  os.chdir(ruta)
  for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
      ext = name.lower() .rsplit(".", 1)[-1]
      if ext in ['pdf']:
        print ("[+] Metadata for file: %s " %(ruta+os.path.sep+name))
        pdfFile= PdfFileReader(open(ruta+os.path.sep+name,'rb'))
        print("Tipo: ", type(docInfo))
        for metaItem in docInfo:
          print('[+] ' + metaItem + ' :' + docInfo[metaItem])
        print("\n")

metaPDF()
      

if __name__ == "__main__":
  #imports
  import argparse
  import a


  #argparser
  parser = argparse.ArgumentParser()
  parser.add_argument("--op", dest="op", help='Opción A - WebScrapping/ | Opción B - Escaneo de Puertos')
  parser.add_argument('--url', dest='url', help='Dirección o Pagina Web Para WebScrapping')
  parser.add_argument('--carp', dest='carp', help='Dirección de guardado de archivos generados')
  args = parser.parser_args()


  #Instalación de Funciones
  #instalacion de pipreq y modulos en req.txt}
  a.pireq()
  

  #ejecucion de funciones
  def opc (op,url,carp,ip,port):
    if op == 'A' or op == 'a':
      a.scrap(url,carp)
    else:
      a.scan(ip,port,carp)
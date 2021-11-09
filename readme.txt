=======================================
PIA - PROGRAMACIÓN PARA CIBERSEGURIDAD
=======================================
DESCRIPCIÓN DEL PROGRAMA:
-Serie de scripts para uso de WebScrapping, Obtención de Metadatos, Envió de Correos, Verificación de Correos, Escaneo de Puertos.
-Uso Automatizado sin Intervención entre Procesos.
=======================================
MODO DE USO:
-Inicie CMD con dirección el directorio en el que esta el proyecto.
-NOTA: (Puede Utilizar main.py -h o main.py --help para ver los parametros a utilizar).     
-Escoja una opción disponible y agregue los parametros necesarios para su funcionamiento.

-IMPORTANTE:Si hace uso de la opcion de Api de verificación de correos es necesario registrarse en el siguiente url:
     |----------------> https://rapidapi.com/Top-Rated/api/e-mail-check-invalid-or-disposable-domain/pricing
     Despues de registrarse seleccionar el plan GRATUITO y listo puede usar sin obstáculos nuestra herramienta.
     
 Tipo de Opciones:
     -op A     En esta opcion se hace WebScrap a una url dada, se obtienen imágenes, Pdfs, se descargan en su debido folder, se obtienen sus metadatos, después los 
                    metadatos se codifican en base64 y se manda un correo con éstos reportes obtenidos hacia un correo dado.
                    
     -op B     En esta opcion se hace una peticion a una API llamada E-mail Check Invalid or Disposable Domain API Documentation, donde es necesario el registro mencionado
                    con anterioridad y un email dado que pueda verficiar.
                    
     -op C     En esta opcion lo que se hace es enlazar python con PowerShell, para poder ver las reglas de Bloqueo del Firewall
     
     -op D     En esta opcion solo se obtiene el FQDN un nombre de dominio completo que incluye el nombre de la computadora y el nombre de                           dominio  asociado a ese equipo. 

     -op E     En esta última opcion lo que se hace es obtener un Universally Unique IDentifier. -saber mas sobre uuid                                                                                                                          en:https://www.significados.com/uuid/


-Verifique si los parametros son correctos, ya que si estos no lo son el Programa puede Interrumpirse (Se añadira Logs de Errores, Interrupciones, etc en una archivo txt)
-En el archivo app.log puede encontrar todo lo que esta pasando internamente, desde ver que se esta descargando, el codigo de aceptación de la pagina, la creación de folders,etc..
-NOTA: Puede copiar y pegar datos como Direcciónes de directorios o cadenas de texto sin problema alguno con el funcionamiento del script.
-De ENTER y automaticamente hará los procesos de la opción utilizada
=======================================

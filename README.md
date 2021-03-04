Readme

Abra CMD o GITBASH, ubique la ruta en la cual quiere que se descargue el proyecto, 
ya en la ruta ejecute el siguiente comando:
			git clone EL LINK
Enseguida se empezará a descargar, ábralo en VisualCode o desde CMD desde la ruta 
en la que descargó.
Acceda al directorio env con el comando:
			cd env 
En esta ruta entramos a la carpeta Scripts:
			cd Scripts
Activamos el entorno virtual con el siguiente comando:
			activate
Regresamos a la carpeta anterior env con:
			cd..
Entramos a la siguiente ruta:
			cd Control_escolar
Ejecutamos el servidor con el siguiente comando:
			python manage.py runserver 
Aparecerá una dirección IP, le da clic y se abrirá la página web
Si se presenta un error para ejecutar, es necesario que se encuentre en el 
directorio env, por ejemplo:
			(env)C:\Users\Rosa\Desktop\env>
Escriba el siguiente comando para descargar Django
			pip install django
Una vez descargado entre nuevamente a la carpeta de Control_escolar, ejemplo
			(env)C:\Users\Rosa\Desktop\Control Escolar\env\Control_escolar>
Volvemos a ejecutar el servidor con el comando:
			python manage.py runserver 
Y ahora mostrará la dirección IP que lo dirigirá a la página web

Preentrega numero 3.
Para esta comision, se ponen en practica los conocimientos adquiridos a traves de las clases que giran en torno a Django a traves del diseño de una pagina web con las siguientes caracteristicas:
Herencia de HTML. Punto cubierto a traves de la herencia del archivo "padre.html" al archivo "inicio.html" desde el cual se puede acceder a las diferentes vistas creadas.
Por lo menos 3 clases en models. Clases creadas (Usuario, Propietario, Departamento y Casa)
Un formulario para insertar datos a todas las clases de tu models. A traves del uso de forms.py y su respectiva vista HTML, se generan los formularios para agregar objetos de cada modelo anteriormente mencionado.
Un formulario para buscar algo en la BD. Utilizando vistas, se genera un formulario donde se pueden buscar elementos de tipo usuario, existentes en la base de datos.
Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades. Punto cubierto a traves de la redaccion de este documento.

Modo de uso:


Descargar el repositorio en formato zip
Extraer y abrir desde VSC la carpeta donde se encuentre el archivo manage.py
En la terminal ingresar el comando python manage.py runserver
El comando devolverá un link, el cual será accesible al presionar "CTRL + click", es importante agregar /Inmobiliaria al final del link para acceder a la pagina de inicio.
En la pagina de inicio se podrá acceder a los diferentes modulos, simplemente haciendo click sobre el formulario que se quiera revisar.
Una vez seleccionado el formulario, habrá que llenarlo de modo que al momento de dar click en el boton "Guardar" la informacion ingresada quede almacenada en la BD.
Este proceso se repite en cada formulario para revisar y confirmar su funcionamiento.

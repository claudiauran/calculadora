# calculadora

## Notas de Git

### Crear carpeta para el proyecto
mkdir proyecto

### Cambiarse a la carpeta del proyecfo
cd proyecto

### Creamos el archivo de codigo, sin utilizar espacios en el nombre

### Inicializar el repositorio
git init

### Para crear un archivo con un texto simple
echo "Texto simple" >> README.md

### Para agregar archivos. "archivos_de_codigo" se refiere a los archivos de codigo que hayas creado. Le debes poner el nombre del archivo que creas.
git add README.md archivos_de_codigo

### Para mirar los cambios pendientes
git status

### Para registrar/comitear nuevos cambios con un comentario significativo sobre lo que se ha hecho.
git commit -m "Renombrando archivo leeme a readme"

### Para enviar los cambios a la nube
git push -u origin main

### Para clonar un repositorio, ir a la pagina de git del repositorio y copiar el campo que se encuentra bajo el boton verde "Code". Por ejemplo, https://github.com/claudiauran/calculadora
git clone https://github.com/claudiauran/calculadora.git
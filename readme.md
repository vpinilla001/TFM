# Diseño e implementación de un chatbot para el software de IDbox
## Máster en Ciencia de Datos 2019/20

### Autora: Verónica Pinilla Gómez

## Descripción
En este repositorio se puede consultar todo el código desarrollado en Rasa expuesto a lo largo del trabajo. 

<a href="https://rasa.com/"><img width="150" height="100" src="https://www.spaceo.ca/wp-content/uploads/2019/12/rasa-framework.png"></a> 

## Instalación
Rasa se trata de una librería que se encuentra en constante desarrollo. Para la realizacicón de la memoria se ha utilizado la versión de Rasa 1.9.6 por lo que se recomienda utilizar esta ya que de lo contrario puede haber fragmentos del código que se hayan quedado obsoletos o den fallos. Se recomienda crear un entorno ya que no se está utilizando la versión más reciente y además la versión requiere utilizar paquetes que no están tampoco en su versión más actualizada. Existen varias alternativas para trabajar con entornos virtuales, la que se ha propuesto como ejemplo es utilizando Anaconda. La versión de Python utilizada ha sido la 3.7.7.

```bash
conda create --name IDbox_chatbot python=3.7.7 --no-default-packages #Crear el entorno
conda activate IDbox_chatbot #Activar el entorno
```

<img align="right" src="https://user-images.githubusercontent.com/56036131/81272037-34be7500-904d-11ea-9b3f-774b2cd1ce2e.png">

En primer lugar, hay que instalar [Visual C++ Build Tools](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/). Además, se tienen que marcar las casillas que aparecen en la imagen. Una vez instalado, hay que instalar la versión de Rasa mencionada anteriormente utilizando la siguiente línea de comando

```bash
pip install rasa==1.9.6
```

A la hora de instalar Rasa se instala una versión del paquete `rasa-sdk`, librería que proporciona las herramientas necesarias para escribir acciones personalizadas en python, que no es compatible con Rasa. Lo mismo ocurre con la librería `tensorflow-addons`. Esto se soluciona fácilmente desinstalando dichos paquetes e instalando la versiones deseadas.

```bash
pip uninstall rasa-sdk tensorflow-addons
pip install rasa-sdk==1.9.0 tensorflow-addons==0.9.1
```

Otros paquetes adicionales que se han utilizado y necesitan ser instalados son los siguientes

```bash
conda install flask pandas seaborn pathlib
```

También se ha adjuntado el modelo ya entrenado que se puede encontrar en la carpeta `/models`. Para hacer uso del bot simplemente hay que correr las siguientes líneas de comando en diferentes terminales.

```bash
#Para la impresión de las gráficas
python app.py
```

```bash
#Iniciar el servidor de las acciones
rasa run actions --actions actions
```

Para comenzar a hablar con el bot se puede hacer o bien desde la terminal mediante el comando

```bash
rasa shell --endpoints endpoints.yml
```

o utilizando la interfaz que proporciona la herramienta Rasa X. Para que no haya problemas de compatibilidad se utiliza la versión 0.28.1, la cual se puede encontrar dentro de la carpeta `rasax`.
```bash
pip install rasax/rasa-x-0.28.1.tar.gz
rasa x
```

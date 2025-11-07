# Algoritmo de Tarjan

## Descripción

Este proyecto ofrece una implementación y visualización didáctica del **Algoritmo de Tarjan**, desarrollado íntegramente en Python.

El Algoritmo de Tarjan es un procedimiento fundamental en la teoría de grafos, diseñado para encontrar los **componentes fuertemente conexos (SCC)** en un grafo dirigido. Un componente fuertemente conexo es un subgrafo en el que existe un camino desde cualquier vértice del subgrafo hacia cualquier otro vértice del mismo.

Esta implementación utiliza las bibliotecas `NetworkX` para la manipulación de las estructuras de datos del grafo y `Matplotlib` para la representación visual del mismo, facilitando la comprensión de cómo el algoritmo identifica dichos componentes.

## Primeros Pasos

A continuación, se describen los pasos necesarios para la configuración y ejecución del proyecto.

### Dependencias

El proyecto requiere las siguientes bibliotecas de Python:

* Python (versión 3.13 o superior)
* Tkinter (versión 3.10 o superior)
* Matplotlib (versión 3.10.1)
* NetworkX (versión 3.5)

### Instalación

**Instalación de Bibliotecas**: Es necesario tener instaladas las dependencias listadas. Puede instalarlas globalmente en su sistema utilizando `pip`.

* En Windows:
    ```cmd
    pip install networkx matplotlib
    ```
* En distribuciones basadas en GNU/Linux Debian:
    ```bash
    sudo apt-get install python3-networkx python3-matplotlib
    ```
    *O, si prefiere usar `pip` en Linux:*
    ```bash
    pip install networkx matplotlib
    ```

### Ejecución del Programa

1.  Descargue el archivo `algoritmo_tarjan_v3.py` y ubíquelo en un directorio de su elección.
2.  Abra una terminal o línea de comandos.
3.  Navegue hasta el directorio donde se encuentra el archivo del programa (utilizando el comando `cd`).
4.  Ejecute el script mediante el siguiente comando:

    ```bash
    python algoritmo_tarjan_v3.py
    ```

## Ayuda

A continuación, se listan algunos problemas comunes y sus posibles soluciones:

* **Error: `python: command not found` o `'python' no se reconoce...`**
    * **Causa**: Python no está instalado correctamente o no está agregado al PATH (variables de entorno) del sistema.
    * **Solución**: Asegúrese de haber instalado Python 3.13 o superior. Durante la instalación en Windows, marque la casilla "Add Python to PATH". Si ya está instalado, es posible que deba agregarlo manualmente a las variables de entorno.

* **Error: `ModuleNotFoundError: No module named 'networkx'` (o `'matplotlib'`)**
    * **Causa**: Las bibliotecas requeridas no se instalaron correctamente en el entorno de Python que está ejecutando el script.
    * **Solución**: Vuelva a ejecutar el comando de instalación de la sección "Instalación" (`pip install networkx matplotlib`). Asegúrese de que el `pip` que utiliza corresponde al `python` que ejecuta el script.

* **El script se ejecuta pero no muestra gráficos:**
    * **Causa**: Puede ser un problema con el *backend* de renderizado de Matplotlib en su sistema.
    * **Solución**: Verifique que su sistema tenga un entorno gráfico (GUI) disponible. Si está en un servidor o terminal remota sin GUI, es posible que la visualización no funcione.

## Autores

* Bañuelos Rodríguez Guillermo Saúl
* Domínguez Trejo Sergio Eduardo
* Pequeño Aguilera Myriam Elizabeth
* Puente Cruz Edgar Eduardo
* Rodríguez Domínguez Grecia Yarezy
* Torres Hernández Juan Vladimir

## Historial de Versiones

* **0.1**
    * Versión inicial.

## Agradecimientos

La estructura de este documento README se inspiró en las siguientes guías:

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

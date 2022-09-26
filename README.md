# José Luis López Bautista

El lenguaje de programación: 
- Python3

## Ejecución
Para ejecutar el programa se necesita:
- Python

Se descomprime el archivo de tipo ".zip" luego:
1. Dirigirse en la terminal a la carpeta src: 
```
JoseLuisLopez$
```
2. Ejecutar el comando 
```
python3 main.py
```
- Para probar con más ejemplos se debe de sustituir los archivos `.txt` por los deceado, pero se debe de manter el nombre. 

## Justificaión

Para la solución del problema se optó por implementar la clase vértice y gráfica, esto se realizó con listas de adyacencias. 
Luego se decidió implementar una clase gestor que se encargará de simular la búsqueda del conjunto independiente de la gráfica. 
En esta se decidió tener como atributos de clase un lista en la que almacenan los elementos que pertenecen al conjunto 
independiente, otra que almacena los vértices de la vecindad que se removió durante la ejecución y una que tendrá una copia de 
los ejemplares de gráfica cada que se removió la vecindad de un vértice.

Lo primero que se decidió fue implementar un método que resolviera los casos bases del teorema, es decir para un número de 
vértices menor o igual a tres, para esto se decidió dividir el problema en casos los cuales osn cuando no existen adyacencias, 
un caso particular para el ciclo del triángulo, y el resto. Para la selección del vértice que se remueve cuando no se está en 
el caso base, se decidió seleccionar de forma pseudoaleatoria haciendo uso de `Random`.

Ahora para el diseño del método que remueve una vecindad  lo que se hace es realizar una copia de la gráfica antes de remover 
la vecindad, esta se almacena en su atributo correspondientes. luego lo que se hace es remover de los vértices al que se 
seleccionó de forma aleatorio, de la misma forma se eliminar sus vértices adjacentes, si este no tiene lo único que se hace es 
eliminar el “apuntador” de los demás vértices al que se quita. Para el otro caso se quita de la lista a sus vecinos.

Después se tiene el método que se encarga de encontrar el conjunto independiente, para esto se hace uso de los método 
anteriores en el caso de que cumpla que el número de vértices es menor o igual a 3, se ejecuta el caso base y se obtienen los 
candidatos para el conjunto independiente. Si no es el caso base se selecciona uno de la gráfica, para después remover su 
vecindad y ejecutamos recursividad a la gráfica que se obtiene al eliminar la vecindad, hasta llegar al caso base. 

Luego al conjunto candidato y a la gráfica que se obtuvo tras aplicar el método anterior, se le agrega el último vértice que se 
removió, se verifica si alguno de los candidatos a conjunto independiente es adyacente al removido, si es asi no se agrega a 
los candidatos  en otro caso si, se ejecuta hasta vaciar la lista de los vértices removidos. Por último se tien un método que 
verificacion, es decir se revisa si uno de los candidatos del conjunto es adyacentes a un vértice de la gráfica inicial, si es 
asi se remueve del conjunto.


# José Luis López Bautista

## Num.Cuenta: 31719189-5

El lenguaje de programación: 
- Java

## Ejecución
Para ejecutar el programa se necesita:
- Java versión 8

Para su ejecución se descomprime el archivo de tipo ".zip".
1. Dirigirse en la terminal a la carpeta src: 
```
MergeTwoSortedLists$
```
2. Ejecutar el comando 
```
javac *.java
```
Después se ejecuta el siguiente comando
```
java Prueba
```

## Justificaión

Notemos que se tiene como precondición que las listas que se reciben están ordenadas de menor a mayor, y como postcondición que 
se regrese una lista ordenada de menor a mayor con las. Por lo que para resolverlo se  creó una lista vacía en la cual se irá 
llenando con los elementos de las otras dos, para esto se vieron los siguientes casos: primero se verifica si estas no están 
vacías en caso de ambas serlo se regresa `null`. Ahora si una de estas es vacía y la otra no se devuelve la que no lo está ya 
que como sabemos esta está ordenada se cumple la postcondición.
Por otro lado cuando ninguna de las dos está vacía, lo que hacemos es comparar nodo por nodo el valor de las listas, es decir, 
si el valor de la primera lista es menor o igual que el de la segunda a la lista que se creó se le asigna el valor de la lista 
uno, y esta apunta al nodo que se obtiene al hacer recursión la lista dos y con el nodo al que apunta la lista uno, por último 
tenemos el caso en que el valor del nodo de la lista dos es menor al uno, de manera similar al caso anterior se almacena en la 
lista creada el valor de la lista dos y este apunta al nodo que se obtiene al hacer recursión con la lista uno y el nodo al que 
apunta la lista dos. Al finalizar la ejecución se regresa la lista que se creó ordenada de menor a mayor.
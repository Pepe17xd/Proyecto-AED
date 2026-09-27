# Guion final v3 — Listas enlazadas

La narración acompaña cada acción visual. Las pausas se conservan en la
puntuación para que edge-tts mantenga un ritmo natural; la voz no se acelera.

## IntroduccionConcepto

VISUAL:
Se presenta el título «Listas Enlazadas», el subtítulo y un índice breve del
documental. Después aparece la pregunta «¿Por qué necesitamos listas
enlazadas?». Se muestra un arreglo de 100 000 elementos (representado con
seis celdas y una elipsis). Se pide insertar un dato al inicio: aparece la
celda nueva y, al insertarla, todo el arreglo se desplaza una posición
(las celdas se resaltan en naranja). Después se presenta la misma operación
con una lista enlazada: tres nodos 10 → 20 → 30. Se crea un nuevo nodo 5 a
la izquierda y solo se dibuja una flecha verde hacia el 10; ningún otro nodo
se mueve. Se cierra resaltando que cada nodo guarda un dato y una referencia
al siguiente.

NARRACIÓN:
Antes de hablar de nodos, pensemos en un problema real. Imagina un arreglo con cien mil elementos guardados uno junto a otro en memoria. Si queremos insertar un nuevo dato al inicio, cada uno de esos cien mil elementos debe desplazarse una posición. Ahora veamos la misma operación con una lista enlazada. Aquí cada elemento no vive pegado al siguiente: solo guarda una referencia hacia él. Para insertar el nuevo dato no movemos nada; simplemente creamos el nodo y agregamos una referencia. Así aparecen los nodos: cada uno guarda un dato y una conexión al siguiente. Ahora veamos la estructura de una lista enlazada, paso a paso.

DURACIÓN: 34–40 segundos.

## IntroduccionLista

VISUAL:
Tres celdas contiguas representan un arreglo. Se separan y el valor 10 se
convierte en el primer nodo; luego aparecen 20 y 30, con flechas amarillas y
un marco verde alrededor de la lista.

NARRACIÓN:
Ahora observemos la cadena con más detalle. Primero vemos tres datos guardados uno junto a otro, como en un arreglo. El diez se convierte en un nodo: conserva el dato y prepara una referencia. Después aparecen el veinte y el treinta. Las flechas amarillas conectan cada nodo con el siguiente. Así, los elementos no necesitan vivir juntos: forman una cadena que podemos recorrer.

DURACIÓN: 20–24 segundos.

## ReferenciasLista

VISUAL:
La lista 10 → 20 → 30 aparece completa. El nodo 20 se amplía, se señalan sus
dos partes y luego se inserta 15 cambiando las referencias.

NARRACIÓN:
Detengámonos en un nodo. A la izquierda vive el dato; aquí, el veinte. A la derecha está la referencia que permite continuar hacia el siguiente nodo. Cuando insertamos el quince, no movemos el veinte. Cambiamos la conexión de diez, y el nuevo nodo apunta a veinte. La información permanece; lo que cambia es el camino.

DURACIÓN: 20–24 segundos.

## InsercionEnLista

VISUAL:
Se solicita insertar 15 en la posición dos. El nodo nuevo aparece en verde,
se actualizan los enlaces y la lista queda 10 → 15 → 20 → 30.

NARRACIÓN:
Partimos de diez, veinte y treinta. La tarea es insertar el quince en la segunda posición. El nuevo nodo aparece antes de veinte. Primero, diez deja de apuntar directamente a veinte. Luego, diez apunta a quince, y quince continúa hacia veinte. La cadena queda completa sin desplazar todos los datos.

DURACIÓN: 18–22 segundos.

## EliminacionEnLista

VISUAL:
El nodo 20 se marca en rojo. Se actualiza la referencia de 15 para llegar a
30; después desaparece 20 y queda una cadena más corta.

NARRACIÓN:
Ahora eliminaremos el nodo veinte, marcado en rojo. Antes de retirarlo, conservamos la continuidad. El nodo quince deja de mirar a veinte y actualiza su referencia para llegar a treinta. Entonces el veinte puede desaparecer. El resultado es una cadena más corta, pero todavía conectada.

DURACIÓN: 18–22 segundos.

## VentajasLista

VISUAL:
Se muestra el crecimiento de la lista, una inserción local y la comparación
entre celdas contiguas y nodos conectados.

NARRACIÓN:
Esta estructura tiene ventajas visibles. Puede crecer agregando un nodo al final sin reservar un bloque completo desde el inicio. Insertar también requiere ajustar referencias cercanas. Y, a diferencia de un arreglo, los nodos pueden conectarse aunque estén en lugares distintos de la memoria.

DURACIÓN: 24–28 segundos.

## DesventajasLista

VISUAL:
Se compara el acceso directo de un arreglo con el recorrido de una lista y se
resaltan la referencia adicional y el riesgo de romper un enlace.

NARRACIÓN:
La flexibilidad también tiene un costo. En un arreglo podemos ir directamente a la tercera posición. En una lista debemos recorrer diez, después veinte y finalmente treinta. Además, cada nodo guarda una referencia extra. Las conexiones exigen cuidado: si un enlace queda mal actualizado, parte del recorrido puede perderse.

DURACIÓN: 24–28 segundos.

## VariantesLista

VISUAL:
Las flechas hacia adelante se complementan con flechas de regreso para formar
una lista doblemente enlazada. Después una flecha curva cierra el circuito.

NARRACIÓN:
La versión simple solo avanza: cada nodo conoce al siguiente. Si agregamos flechas de regreso obtenemos una lista doblemente enlazada; también podemos volver al nodo anterior, a cambio de más memoria. Finalmente, una flecha cierra el circuito. En una lista circular, el último nodo vuelve al primero, una idea útil para turnos y ciclos repetidos.

DURACIÓN: 24–28 segundos.

## AplicacionesLista

VISUAL:
Se muestran navegación anterior y siguiente, un reproductor musical y un
sistema de turnos con jugadores conectados en círculo.

NARRACIÓN:
Estas conexiones aparecen en productos cotidianos. Un navegador puede avanzar y retroceder entre páginas. Un reproductor enlaza la canción anterior, la actual y la próxima. Y en un sistema de turnos, el último jugador puede devolver el recorrido al primero. Son ejemplos distintos de la misma idea: decidir quién sigue mediante referencias.

DURACIÓN: 18–22 segundos.

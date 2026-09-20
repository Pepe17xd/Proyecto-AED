# Guion final v2 — Listas enlazadas

La locución está escrita para acompañar la acción; los puntos suspensivos y los
cambios de párrafo introducen pausas naturales al sintetizar la voz.

## IntroduccionLista

[Descripción visual]
El título abre el documental. Tres celdas contiguas representan un arreglo; se
separan y el valor 10 se convierte en el primer nodo. Después aparecen 20 y 30,
unidos por flechas amarillas, y un marco verde encierra la lista terminada.

[Tiempo aproximado]
18 a 22 segundos.

[Narración]
Primero vemos tres datos guardados uno junto a otro, como en un arreglo. Ahora los separamos. El diez se convierte en un nodo: guarda el dato y una referencia. Después aparecen el veinte y el treinta. Las flechas amarillas conectan cada nodo con el siguiente. Así, los elementos no necesitan vivir juntos: forman una cadena.

## ReferenciasLista

[Descripción visual]
La lista 10 → 20 → 30 aparece completa. El nodo 20 se amplía para señalar su
celda de dato y su celda de referencia. La lista vuelve y se inserta 15 entre
10 y 20; los textos muestran cómo cambian las referencias.

[Tiempo aproximado]
20 a 24 segundos.

[Narración]
Observemos un nodo de cerca. A la izquierda vive el dato, aquí el veinte. A la derecha está la referencia: la dirección que permite continuar hacia el siguiente nodo. Cuando insertamos el quince, no movemos el veinte. Cambiamos la conexión de diez, y el nuevo nodo apunta a veinte. La información permanece; lo que cambia es el camino.

## InsercionEnLista

[Descripción visual]
Se presenta la cadena 10 → 20 → 30. La instrucción pide insertar 15 en la
posición dos. El nuevo nodo aparece en verde sobre la cadena, se crean sus
enlaces y la lista se reacomoda como 10 → 15 → 20 → 30.

[Tiempo aproximado]
16 a 20 segundos.

[Narración]
Partimos de diez, veinte y treinta. La tarea es insertar el quince en la segunda posición. El nuevo nodo aparece antes de veinte. Primero, diez deja de apuntar directamente a veinte. Luego, diez apunta a quince, y quince continúa hacia veinte. La cadena queda completa otra vez, sin desplazar los datos como lo haría un arreglo.

## EliminacionEnLista

[Descripción visual]
La lista 10 → 15 → 20 → 30 aparece. El nodo 20 se marca en rojo. Se destaca
que 15 debe apuntar a 30, el nodo rojo desaparece y queda 10 → 15 → 30.

[Tiempo aproximado]
16 a 20 segundos.

[Narración]
Ahora eliminaremos el nodo veinte, marcado en rojo. Antes de retirarlo, debemos conservar la continuidad. El nodo quince deja de mirar a veinte y actualiza su referencia para llegar a treinta. Entonces el veinte puede desaparecer. El resultado es una cadena más corta, pero todavía conectada: diez, quince y treinta.

## VentajasLista

[Descripción visual]
Se muestran tres ventajas. Primero se añade 40 al final de una lista. Luego se
inserta 15 entre nodos cambiando enlaces. Finalmente se compara un arreglo de
celdas pegadas con una lista cuyos nodos se conectan por flechas.

[Tiempo aproximado]
24 a 30 segundos.

[Narración]
Esta estructura tiene tres ventajas visibles. Primero, puede crecer: el cuarenta se agrega al final sin reservar un bloque completo desde el inicio. Segundo, insertar el quince solo requiere ajustar referencias cercanas. Y tercero, observe la comparación final. El arreglo necesita celdas contiguas; la lista puede conectar nodos aunque estén en lugares distintos de la memoria.

## DesventajasLista

[Descripción visual]
Se contrasta el acceso directo de un arreglo con el recorrido 10, 20 y 30 de
la lista. Luego una celda simple se transforma en un nodo con puntero. Al final
se resaltan los enlaces que deben mantenerse correctos.

[Tiempo aproximado]
24 a 30 segundos.

[Narración]
La flexibilidad también tiene un costo. En el arreglo, podemos señalar de inmediato la tercera posición. En la lista, para llegar al treinta recorremos diez, después veinte y finalmente treinta. Además, cada nodo guarda una referencia extra. Por último, las conexiones exigen cuidado: si un enlace queda mal actualizado, la cadena puede perder parte de su recorrido.

## VariantesLista

[Descripción visual]
La lista simple muestra flechas hacia adelante. Después aparecen dos flechas
moradas de regreso para convertirla en doblemente enlazada. Por último, una
flecha curva verde conecta el último nodo de vuelta al primero y se muestran
usos de una lista circular.

[Tiempo aproximado]
22 a 28 segundos.

[Narración]
La versión simple solo avanza: cada nodo conoce al siguiente. Al agregar las flechas moradas de regreso obtenemos una lista doblemente enlazada. Ahora también podemos volver al nodo anterior, a cambio de más memoria. Finalmente, la flecha verde cierra el circuito. En una lista circular, el último nodo vuelve al primero, una idea útil para turnos y ciclos repetidos.

## AplicacionesLista

[Descripción visual]
Tres ejemplos aparecen en pantalla: navegación anterior/actual/siguiente,
reproductor musical y tres jugadores conectados en círculo para un sistema de
turnos.

[Tiempo aproximado]
16 a 20 segundos.

[Narración]
Estas conexiones aparecen en productos cotidianos. Un navegador puede avanzar y retroceder entre páginas. Un reproductor enlaza la canción anterior, la actual y la próxima. Y en un sistema de turnos, el último jugador puede devolver el recorrido al primero. Son ejemplos distintos de la misma idea: decidir quién sigue mediante referencias.

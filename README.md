# Documental visual de listas enlazadas con Manim e IA

Proyecto educativo que explica cómo se conectan los datos en memoria mediante
un documental animado. La narración parte del problema de almacenar y
reorganizar información, presenta el concepto de nodo y referencia, y muestra
las operaciones y variantes de una lista enlazada.

El proyecto combina Ollama local para apoyar la generación del guion,
edge-tts para producir la voz y Manim Community v0.21.0 para crear las
animaciones. Su objetivo es que una persona que no conoce el tema pueda seguir
visualmente el recorrido de los datos y entender por qué una lista enlazada
puede ser útil.

## Características

- Introducción conceptual al problema de organizar e insertar datos.
- Animación de listas enlazadas simples.
- Explicación visual de nodos, datos y referencias.
- Inserción de elementos y actualización de enlaces.
- Eliminación de elementos conservando la continuidad de la lista.
- Comparación de ventajas y desventajas frente a estructuras contiguas.
- Variantes doblemente enlazada y circular.
- Aplicaciones en navegación, reproducción multimedia y sistemas de turnos.
- Narración sincronizada por sección y soporte para música ambiental en la
  mezcla final.

## Pipeline de producción

1. **Guion:** Ollama se ejecuta localmente para generar o revisar el texto.
2. **Voz:** edge-tts convierte el guion de cada sección en una pista MP3.
3. **Animación:** Manim Community v0.21.0 renderiza el documental.
4. **Producción final:** se mezclan la narración y la música ambiental con el
   volumen de música reducido para mantener la voz al frente.

El documental utiliza una pista independiente para la introducción conceptual
(`concepto.mp3`) y para cada una de las ocho escenas educativas existentes.

## Instalación

Instala las dependencias del proyecto con:

```powershell
python -m pip install -r requirements.txt
```

Ollama debe estar instalado localmente para usar la generación de guion. Para
la mezcla final también se utiliza FFmpeg.

## Configuración

Las variables principales son:

- `OLLAMA_URL`: dirección del servicio local de Ollama. El ejemplo usa
  `http://localhost:11434`.
- `OLLAMA_MODEL`: modelo de Ollama que se utilizará para el guion. El ejemplo
  usa `llama3.2:latest`.
- `MANIM_NARRACION`: activa (`1`) o desactiva (`0`) la incorporación de las
  pistas de voz durante el render.

El archivo `.env.example` contiene la configuración base de Ollama. Crea un
archivo `.env` en la raíz copiando esos valores y añade `MANIM_NARRACION=1`
cuando quieras renderizar con narración:

```text
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:latest
MANIM_NARRACION=1
```

Las variables definidas directamente en la sesión tienen prioridad sobre las
del archivo `.env`. No publiques `.env` con credenciales o configuraciones
locales.

## Ejecución

Genera o revisa el guion con Ollama:

```powershell
python audio/generar_guion_ia.py
```

Genera las nueve pistas de narración definidas en el guion final:

```powershell
python audio/generar_audio.py
```

Para reemplazar pistas existentes, añade `--overwrite`.

Renderiza el documental completo:

```powershell
$env:MANIM_NARRACION="1"
manim -pqh main.py ListaEnlazadaDocumental
```

Para comprobar el montaje sin voz:

```powershell
$env:MANIM_NARRACION="0"
manim -pqh main.py ListaEnlazadaDocumental
```

Coloca una pieza instrumental en `audio/musica_ambiental.mp3` y ejecuta la
mezcla final con `produccion/mezclar_audio.py`. El script mantiene la narración
al 100 % y permite configurar la música entre 10 % y 15 %.

## Estructura del proyecto

```text
componentes/   # Elementos visuales reutilizables, como NodoVisual.
estructuras/   # Estructuras visuales y operaciones animables de la lista.
escenas/       # Introducción, escenas educativas, créditos y cierre.
audio/         # Guiones, pistas de voz y utilidades de generación y unión.
produccion/    # Orquestación del documental y mezcla de audio.
config/        # Paleta visual y configuración de producción.
main.py        # Punto de entrada de las escenas renderizables.
```

La escena `ListaEnlazadaDocumental` coordina las secciones sobre un mismo
lienzo y aplica las transiciones entre ellas. Los componentes y la estructura
de datos se reutilizan desde las escenas sin duplicar su lógica.

## Créditos

- Antony Yonel Rosales Esteban
- Jeseph Imanol Burgos Ochoa

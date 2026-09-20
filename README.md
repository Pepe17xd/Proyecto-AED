# Animaciones de listas enlazadas con Manim

Proyecto organizado para construir una serie didáctica sobre listas simplemente enlazadas.

## Estructura

```text
componentes/  # NodoLista y ListaEnlazadaVisual
config/       # Paleta, medidas y constantes de diseño
escenas/      # Una escena por concepto de la lección
estructuras/  # Estructuras visuales con operaciones animables
main.py       # Punto de entrada de las escenas renderizables
assets/       # Tipografías, imágenes o audio externos
media/        # Salida de Manim (no editar a mano)
```

Las escenas no dibujan flechas ni posiciones directamente: usan `ListaEnlazadaVisual`.
Esto permite reutilizar los componentes en eliminación, búsqueda e inserción final.

`NodoVisual` también puede usarse directamente en escenas personalizadas:

```python
origen = NodoVisual(10).shift(LEFT * 2)
destino = NodoVisual(20).shift(RIGHT * 2)
self.play(origen.animar_creacion(), destino.animar_creacion())
self.play(origen.animar_conexion(destino))
self.play(origen.animar_eliminacion())
```

## Renderizado

```powershell
manim -pqh main.py IntroduccionListasEnlazadas
manim -pqh main.py InsercionAlInicio
manim -pqh main.py RecorridoDeLista
```

Use `-pql` durante la iteración rápida.

## Lista enlazada animable

`estructuras.ListaEnlazadaVisual` gestiona nodos `NodoVisual` y usa posiciones
basadas en 1 (por ejemplo, `eliminar(2)` elimina el segundo nodo). Sus métodos
`insertar` y `eliminar` devuelven animaciones listas para `self.play`.

```powershell
manim -pql main.py PruebaListaSimple
```

## Producción del documental

La clase `ListaEnlazadaDocumental` encadena créditos, las ocho escenas
educativas y el cierre en un único vídeo. No modifica las escenas individuales:
las ejecuta sobre un mismo lienzo y realiza un fundido entre secciones.

```text
audio/       # MP3 de voz, guion_final.md y música ambiental
config/      # Estilo y configuración de producción
produccion/  # Orquestación del documental
escenas/     # Escenas educativas, créditos y cierre
```

### Instalación

Instale Python 3.11, FFmpeg y las dependencias del proyecto:

```powershell
python -m pip install -r requirements.txt
ffmpeg -version
```

### 1. Generar o revisar el guion IA

El guion de producción es [audio/guion_final_v2.md](audio/guion_final_v2.md).
Cada bloque incluye lo que se ve, duración prevista y una narración asociada a
una de las ocho escenas. Si se desea una variante con Ollama, el optimizador
sigue disponible y puede recibir el guion explícitamente:

```powershell
python audio/generar_guion_ia.py
```

### 2. Generar audio por escena

La voz predeterminada es `es-MX-JorgeNeural` a velocidad natural (`-2%`). Las
pausas están incorporadas mediante la puntuación y los cambios de idea del
guion; no se acelera la locución para encajarla en el video.

```powershell
python audio/generar_audio.py --overwrite
```

Se generan `intro.mp3`, `referencias.mp3` y las demás pistas en `audio/`.
`ListaEnlazadaDocumental` incorpora cada archivo al inicio de su escena y, si
la voz dura más que la animación, conserva el último plano hasta terminarla.

### 3. Vídeo completo sin audio

La narración está desactivada por defecto:

```powershell
$env:MANIM_NARRACION="0"
manim -pqh main.py ListaEnlazadaDocumental
```

### 4. Vídeo con narración sincronizada

Después de generar las pistas, active la narración antes de renderizar:

```powershell
$env:MANIM_NARRACION="1"
manim -pqh main.py ListaEnlazadaDocumental
```

Cada pista se inicia al comienzo de su sección. No se usa
`narracion_completa.mp3` durante el render: esto evita desfases acumulados.

### 5. Narración y música ambiental

Con el vídeo narrado generado y una pista libre de derechos en
`audio/musica_ambiental.mp3`, mezcle la música a volumen bajo (12 %) con FFmpeg
y genere el archivo final:

```powershell
ffmpeg -i media/videos/main/1080p60/ListaEnlazadaDocumental.mp4 -stream_loop -1 -i audio/musica_ambiental.mp3 -filter_complex "[1:a]volume=0.12[musica];[0:a][musica]amix=inputs=2:duration=first:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -shortest video_final_listas_enlazadas.mp4
```

Use `-pql` en lugar de `-pqh` para comprobar el montaje rápidamente.

## Pipeline automático de narración

El pipeline conserva las ocho pistas separadas para que Manim sincronice cada
una al inicio de su escena. Los scripts no modifican nodos, listas ni escenas.

### Dependencias de voz

```powershell
python -m pip install -r requirements.txt
```

### Configuración de Ollama

Instale Ollama para su sistema operativo y compruebe los modelos disponibles:

```powershell
ollama list
```

Descargue el modelo que quiera usar. El repositorio no asume que un modelo esté
instalado ni contiene un valor por defecto obligatorio:

```powershell
ollama pull llama3.2:latest
```

Configure las variables antes de generar el guion. `OLLAMA_URL` es opcional y
por defecto usa `http://localhost:11434`; `OLLAMA_MODEL` es obligatorio.

```powershell
# PowerShell
$env:OLLAMA_URL="http://localhost:11434"
$env:OLLAMA_MODEL="llama3.2:latest"
python audio/generar_guion_ia.py
```

```bash
# Linux/macOS
export OLLAMA_URL="http://localhost:11434"
export OLLAMA_MODEL="llama3.2:latest"
python audio/generar_guion_ia.py
```

`.env.example` muestra las variables requeridas. Los scripts cargan `.env`
automáticamente y también funcionan con las variables de entorno anteriores.

### Configuración local

Para desarrollo local, los scripts cargan automáticamente el archivo `.env` de
la raíz mediante `python-dotenv`. Las variables definidas en PowerShell, Linux o
macOS siempre tienen prioridad sobre ese archivo.

En Linux/macOS, cree su configuración local así:

```bash
cp .env.example .env
```

En Windows, cree manualmente un archivo `.env` en la raíz a partir de
`.env.example`. Un ejemplo mínimo es:

```text
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:latest
MANIM_NARRACION=1
```

`.env` está en `.gitignore`, por lo que no se publica. Después de configurar el
modelo con `ollama pull llama3.2:latest`, ejecute el pipeline sin exportar
variables manualmente.

### Flujo final

1. Revise `audio/guion_final_v2.md`. Si necesita una alternativa producida por
   Ollama, el script valida que el servicio, la variable `OLLAMA_MODEL` y el
   modelo estén disponibles; crea `audio/guion_optimizado.md`.

   ```powershell
   python audio/generar_guion_ia.py
   ```

2. Genere las ocho pistas MP3. La voz por defecto es `es-MX-JorgeNeural`, con
   ritmo natural y pausas guiadas por el texto.

   ```powershell
   python audio/generar_audio.py --overwrite
   python audio/generar_audio.py --voice es-MX-JorgeNeural --rate -2% --overwrite
   ```

3. Renderice el documental con las pistas generadas.

   ```powershell
   $env:MANIM_NARRACION="1"
   manim -pqh main.py ListaEnlazadaDocumental
   ```

4. Coloque una pieza instrumental libre de derechos en
   `audio/musica_ambiental.mp3` y mezcle música al 12 %, con la narración al
   100 %. El resultado es `video_final_listas_enlazadas.mp4`.

   ```powershell
   python produccion/mezclar_audio.py
   ```

Use `python audio/generar_audio.py --help` y `python produccion/mezclar_audio.py --help`
para configurar voz, ritmo, vídeo de origen, pista musical y volumen.

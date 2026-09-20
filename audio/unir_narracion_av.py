import av
from pathlib import Path


ARCHIVOS = [
    "intro.mp3",
    "referencias.mp3",
    "insercion.mp3",
    "eliminacion.mp3",
    "ventajas.mp3",
    "desventajas.mp3",
    "variantes.mp3",
    "aplicaciones.mp3",
]


CARPETA = Path("audio")
SALIDA = CARPETA / "narracion_completa.mp3"


def unir_audios():

    salida = av.open(str(SALIDA), mode="w")

    stream_salida = None

    for nombre in ARCHIVOS:

        ruta = CARPETA / nombre

        print(f"Procesando {nombre}")

        entrada = av.open(str(ruta))

        audio = entrada.streams.audio[0]

        if stream_salida is None:
            stream_salida = salida.add_stream(
                "libmp3lame",
                rate=audio.rate,
            )
            stream_salida.layout = audio.layout


        for frame in entrada.decode(audio):

            frame.pts = None

            for paquete in stream_salida.encode(frame):
                salida.mux(paquete)


        entrada.close()


    for paquete in stream_salida.encode():
        salida.mux(paquete)


    salida.close()

    print("\n✅ Narración completa creada:")
    print(SALIDA)


if __name__ == "__main__":
    unir_audios()
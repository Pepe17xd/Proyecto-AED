# Narración del documental

Coloca aquí los MP3 finales, usando exactamente estos nombres:

```text
intro.mp3
referencias.mp3
insercion.mp3
eliminacion.mp3
ventajas.mp3
desventajas.mp3
variantes.mp3
aplicaciones.mp3
```

Los archivos no se incluyen en el repositorio. Al habilitar `MANIM_NARRACION=1`,
la escena documental añade cada pista al inicio de su sección correspondiente.

Especificación recomendada para locución: voz masculina natural, español latino,
ritmo moderado, tono educativo y pausas breves entre ideas. Recorta cada voz para
que no supere la duración de su escena y no invada la sección siguiente.

Para música, coloca una pista instrumental libre de derechos en
`musica_ambiental.mp3`. Debe tener carácter tecnológico o cinematográfico y se
mezcla después con FFmpeg al 12 % (voz 100 %), no dentro de Manim.

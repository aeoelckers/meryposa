# Media para sección 6 meses

Si tus fotos están en Google Drive, este flujo es el más simple:

1. Descarga la carpeta desde Drive al computador.
2. Copia/pega todas las fotos y videos dentro de `media/6-meses/`.
3. Ejecuta:

```bash
python scripts/generate-6-meses-manifest.py
```

4. Listo: `events/6-meses.html` usará automáticamente los archivos detectados.


## ¿Carpeta o fotos separadas?

- **Déjalas como fotos/videos separados** dentro de `media/6-meses/`.
- No necesitas renombrar ni ordenar manualmente.
- **No uses subcarpetas** (por ejemplo `media/6-meses/viaje/`), porque el script solo lee archivos en el nivel principal de `media/6-meses/`.

Ejemplo correcto:
- `media/6-meses/IMG_0011.jpg`
- `media/6-meses/20260209_163247.jpg`
- `media/6-meses/IMG_0011.mov`

Luego ejecuta:

```bash
python scripts/generate-6-meses-manifest.py
```

## Formatos recomendados

### Fotos
- `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`

### Video
- `.mp4` (ideal), `.webm`, `.mov`

> Nota: archivos `.HEIC` normalmente no se muestran en navegador sin conversión. Conviene exportarlos a `.jpg`.

## Archivos generados
- `manifest.json` (lo crea/actualiza el script y contiene la lista de imágenes/video).

Si no hay media personalizada o falta algo, la página hace fallback a `FV/`.

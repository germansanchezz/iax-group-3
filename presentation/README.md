# Presentaciones de la Unidad 2

Se conservan las dos versiones anteriores y se añade la versión final revisada:

- `presentacion.tex` y `presentacion.pdf`: versión visual y más dinámica.
- `presentacion_formal.pdf`: versión académica anterior.
- `presentacion_final.tex` y `presentacion_final.pdf`: versión académica actualizada. La curva EBM está recortada de la salida del notebook y se incluye como `ebm_payment_to_bill_ratio.png`.
- `presentacion_natural.tex` y `presentacion_natural.pdf`: versión sencilla para exposición oral, con un árbol CART ramificado y la curva EBM real del notebook.
- `presentacion_beamer.tex` y `presentacion_beamer.pdf`: versión de estilo Beamer universitario tradicional, basada visualmente en las diapositivas interiores de `K_SVC.pdf`.
- `presentacion_beamer_nav.tex` y `presentacion_beamer_nav.pdf`: versión con navegación superior nativa de Beamer.
- `presentacion_beamer_nav_ebm.tex` y `presentacion_beamer_nav_ebm.pdf`: versión con dos curvas EBM de mayor importancia, extraídas de la figura del notebook; la imagen completa está en `ebm_top_functions_notebook.png`.

Para recompilar la versión final desde la raíz del repositorio en WSL:

```bash
pdflatex -jobname=presentacion_final -interaction=nonstopmode -halt-on-error -output-directory presentation presentation/presentacion_final.tex
```

Para compilar la versión sencilla:

```bash
pdflatex -jobname=presentacion_natural -interaction=nonstopmode -halt-on-error -output-directory presentation presentation/presentacion_natural.tex
```

Para compilar la versión basada en `K_SVC.pdf`:

```bash
pdflatex -jobname=presentacion_beamer -interaction=nonstopmode -halt-on-error -output-directory presentation presentation/presentacion_beamer.tex
```

Para compilar la versión con curvas EBM adicionales:

```bash
pdflatex -jobname=presentacion_beamer_nav_ebm -interaction=nonstopmode -halt-on-error -output-directory presentation presentation/presentacion_beamer_nav_ebm.tex
```

Requiere una instalación de LaTeX con Beamer, TikZ y las fuentes Latin Modern. En este entorno ya estaban disponibles, por lo que no fue necesario instalar dependencias.

# Plantilla de proyecto de IA Explicable

Plantilla LaTeX para redactar proyectos académicos del Máster en Inteligencia Artificial de la Universidad Politécnica de Madrid. La estructura es flexible y puede adaptarse a informes de investigación, prácticas o proyectos de asignatura.

## Estructura

- `images`: imágenes y documentos que se incorporen al informe.
- `include`: portada y preámbulo LaTeX.
- `plan-trabajo`: plantilla opcional para describir objetivos, tareas y planificación.
- `secciones`: capítulos de la memoria y datos editables de portada.
- `bibliography.bib`: referencias bibliográficas del proyecto.
- `report.tex`: documento principal.

## Uso

1. Edita `secciones/_DatosProyecto.tex` con el título, autores, asignatura, supervisión y fecha.
2. Sustituye los textos entre `<< >>` por el contenido del proyecto.
3. Añade o elimina capítulos desde `report.tex` según las necesidades del informe.
4. Compila con `pdflatex` y `biber` cuando uses bibliografía.

La estructura propuesta incluye resumen, introducción, estado del arte, desarrollo, impacto, resultados, conclusiones y anexos. No es necesario conservar todos los capítulos.

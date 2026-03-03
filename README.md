# lovande-shorts-analytics

Análisis de YouTube Shorts de Lovandé (últimos 180 días, desde exportes de YouTube Studio). Objetivo: identificar qué tipos de Shorts generan más suscriptores y comentarios, con limpieza de datos y ranking por performance.

## Qué hay en este repo

Este proyecto analiza Shorts de Lovandé en una ventana móvil de ~180 días (recortada desde un export de 365 días de YouTube Studio). El objetivo es identificar qué Shorts generan más **suscriptores** y **comentarios**.

### Outputs (carpeta `reports/`)
- `top20_subscribers.csv`: Top 20 Shorts por **suscriptores ganados** (ranking absoluto).
- `top20_comments.csv`: Top 20 Shorts por **comentarios** (ranking absoluto).
- `top20_subscribers_rate.csv`: Top 20 por **suscriptores por 1000 views** (eficiencia).
- `top20_comments_rate.csv`: Top 20 por **comentarios por 1000 views** (eficiencia).
- `top20_total_score.csv`: Top 20 por **score combinado** (suscriptores + comentarios normalizados).  
  Fórmula: `total_score = (subs / max_subs) + (comments / max_comments)`.

El script que genera estos outputs está en `notebooks/01_shorts_180d.py`. El CSV crudo no se sube al repo.

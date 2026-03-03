## Insights (Shorts, ~180 días)

### Objetivo
Identificar qué Shorts generan más **suscriptores** (prioridad) y, secundariamente, **comentarios**.

### Evidencia (outputs)
- `top20_subscribers.csv` (base de estos insights)
- `top20_comments.csv`
- `top20_total_score.csv`

### Patrones observados (con evidencia)

1) **Duración “pegada” al límite: 60s domina el Top**
   - Evidencia: 17 de 20 Shorts del Top tienen **60s** (solo 3 tienen 52s).
   - Ejemplos (60s): `27zn9VSuWek`, `qoeC4pf5ZbQ`, `NgXUWHuGvqA`
   - Ejemplos (52s): `SboZJ27VS-E`, `U-Sb9_N0PNg`, `DUszBoFDICE`

2) **Repetir el mismo hook/título funciona (no necesitas que cada Short sea “nuevo”)**
   - Evidencia: el título **“Sí, me voy pero no creas que es con la única intención de apartarme de ti”** aparece **9 veces** en el Top 20.
   - Ejemplos con 2 subs: `NgXUWHuGvqA`, `ZTlmvDxHR3U`, `6CWElxDzL4M`
   - Ejemplos con 1 sub: `iC5YF9_1sLk`, `qQ18ERDtjO0`, `hKjiiM6qXHc`, `Z4dHSP5Vj9s`, `vxgV7La3Nj0`, `EVm0G875y2M`

3) **Un hook específico destaca como “ganador” (subs + algo de conversación)**
   - Evidencia: variantes de **“Intentaré fingir…”** entran alto y además son de los pocos con comentarios.
   - Ejemplos:  
     - `SboZJ27VS-E` (3 subs, 1 comment)  
     - `U-Sb9_N0PNg` (2 subs, 1 comment)  
     - `DUszBoFDICE` (1 sub, 0 comments)

4) **Los hashtags no son requisito para generar suscriptores**
   - Evidencia: 15 de 20 títulos del Top **no tienen hashtags** y aun así rankean por subs.
   - Ejemplos sin hashtags: `SboZJ27VS-E`, `U-Sb9_N0PNg`, `NgXUWHuGvqA`
   - Ejemplos con hashtags: `27zn9VSuWek`, `qoeC4pf5ZbQ`, `C-NP4vghHZE`, `UAc4TaRrNu0`, `zz9qvL6r_s0`

5) **Comentarios son raros en los top por subs (si quieres comments, ojo: no es automático)**
   - Evidencia: solo **4 de 20** tienen `Comments added = 1`; la mayoría tiene 0.
   - Ejemplos con comments: `SboZJ27VS-E`, `U-Sb9_N0PNg`, `C-NP4vghHZE`, `dXlJSWf22bY`

### Notas / límites
- Estos patrones vienen del **Top 20 por suscriptores** (no de todos los Shorts). Sirven como “señales” para replicar, no como reglas universales.

### Insights específicos de comentarios (usando `top20_comments.csv`)

1) **El ranking de comentarios está dominado por empates**
   - Evidencia: en `top20_comments.csv`, 9/20 tienen `Comments added = 1` y 11/20 tienen `0`.
   - Lectura correcta: enfócate en los que tienen **1 comentario** (son los que realmente “activaron conversación”).

2) **Hook que más se repite entre los que sí comentan: “Intentaré fingir…”**
   - Evidencia (todos con 1 comment): `SboZJ27VS-E`, `U-Sb9_N0PNg`, `IRgVZ6tr8TU`, `C-YreVbr0mk`.
   - Lectura: ese tipo de frase/hook parece invitar respuesta (aunque no siempre maximice subs).

3) **Comentarios pueden aparecer incluso con pocas views (son más “espiky”)**
   - Evidencia: `Q0qAFl3_YF4` tiene 1 comment con muy pocas views.
   - Lectura: por eso comentarios en total pueden ser “ruidosos” en piezas con poco alcance (un solo comment cambia todo).

4) **Hay Shorts que generan comentarios pero 0 suscriptores**
   - Evidencia (1 comment, 0 subs): `vw6U8ETtW5c`, `IRgVZ6tr8TU`, `C-YreVbr0mk`, `b864lO2Bvrc`, `Q0qAFl3_YF4`.
   - Lectura: sirven como “shorts conversacionales”, aunque no sean los mejores para crecer en subs.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

REPORTS_DIR = Path("reports")
FIG_DIR = REPORTS_DIR / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

TOP_SUBS_PATH = REPORTS_DIR / "top20_subscribers.csv"
TOP_COMMENTS_PATH = REPORTS_DIR / "top20_comments.csv"

top_subs = pd.read_csv(TOP_SUBS_PATH)
top_comments = pd.read_csv(TOP_COMMENTS_PATH)


def hook_family(title: str) -> str:
    t = str(title).lower()

    if "intentare fingir" in t or "intentaré fingir" in t:
        return "Intentaré fingir..."
    if "sí, me voy" in t or "si, me voy" in t or "sí me voy" in t or "si me voy" in t:
        return "Sí, me voy..."
    if "cómo le digo a mamá" in t or "como le digo a mama" in t:
        return "Cómo le digo a mamá..."
    if "no puedo creer" in t:
        return "No puedo creer..."
    return "Otros"


# --- FIG 1: Duración (Top 20 por subs) ---
dur_counts = top_subs["Duration"].value_counts().sort_index()

plt.figure()
dur_counts.plot(kind="bar")
plt.title("Top 20 por suscriptores: distribución de duración (seg)")
plt.xlabel("Duración (seg)")
plt.ylabel("Cantidad de Shorts")
plt.tight_layout()
plt.savefig(FIG_DIR / "top_subs_duration.png", dpi=200)
plt.close()

# --- FIG 2: Familias de hook por título (Top 20 por subs) ---
top_subs["hook_family"] = top_subs["Video title"].apply(hook_family)
hook_counts = top_subs["hook_family"].value_counts()

plt.figure()
hook_counts.plot(kind="bar")
plt.title("Top 20 por suscriptores: familias de hook (por título)")
plt.xlabel("Familia")
plt.ylabel("Cantidad de Shorts")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(FIG_DIR / "top_subs_hook_families.png", dpi=200)
plt.close()

# --- FIG 3: Comentarios en el Top 20 por subs ---
comments_counts = top_subs["Comments added"].value_counts().sort_index()

plt.figure()
comments_counts.plot(kind="bar")
plt.title("Top 20 por suscriptores: distribución de comentarios")
plt.xlabel("Comentarios")
plt.ylabel("Cantidad de Shorts")
plt.tight_layout()
plt.savefig(FIG_DIR / "top_subs_comments_distribution.png", dpi=200)
plt.close()

# --- FIG 4 (opcional útil): ¿cuántos con 1 comentario en top_comments? ---
comments_counts_2 = top_comments["Comments added"].value_counts().sort_index()

plt.figure()
comments_counts_2.plot(kind="bar")
plt.title("Top 20 por comentarios: distribución de comentarios")
plt.xlabel("Comentarios")
plt.ylabel("Cantidad de Shorts")
plt.tight_layout()
plt.savefig(FIG_DIR / "top_comments_distribution.png", dpi=200)
plt.close()

print("OK: Figuras generadas en", FIG_DIR)
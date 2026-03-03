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


def save_hook_plot(df: pd.DataFrame, title: str, out_name: str) -> None:
    counts = df["Video title"].apply(hook_family).value_counts()

    plt.figure()
    counts.plot(kind="bar")
    plt.title(title)
    plt.xlabel("Familia")
    plt.ylabel("Cantidad de Shorts")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / out_name, dpi=200)
    plt.close()


# 1) Hooks en Top 20 por suscriptores
save_hook_plot(
    top_subs,
    "Top 20 por suscriptores: familias de hook (por título)",
    "top_subs_hook_families.png",
)

# 2) Hooks en Top 20 por comentarios
save_hook_plot(
    top_comments,
    "Top 20 por comentarios: familias de hook (por título)",
    "top_comments_hook_families.png",
)

print("OK: Figuras generadas en", FIG_DIR)
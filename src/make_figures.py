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


def save_hook_impact_plot(df: pd.DataFrame, metric: str, title: str, out_name: str) -> None:
    tmp = df.copy()
    tmp["hook_family"] = tmp["Video title"].apply(hook_family)

    impact = tmp.groupby("hook_family")[metric].sum().sort_values(ascending=False)

    plt.figure()
    impact.plot(kind="bar")
    plt.title(title)
    plt.xlabel("Hook (familia)")
    plt.ylabel(metric)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / out_name, dpi=200)
    plt.close()


# 1) Hooks vs SUSCRIPTORES (suma), usando top20_subscribers
save_hook_impact_plot(
    top_subs,
    metric="Subscribers gained",
    title="Top 20 por suscriptores: impacto por familia de hook (suma de suscriptores)",
    out_name="top_subs_hook_impact_subscribers.png",
)

# 2) Hooks vs COMENTARIOS (suma), usando top20_comments
save_hook_impact_plot(
    top_comments,
    metric="Comments added",
    title="Top 20 por comentarios: impacto por familia de hook (suma de comentarios)",
    out_name="top_comments_hook_impact_comments.png",
)

print("OK: Figuras generadas en", FIG_DIR)
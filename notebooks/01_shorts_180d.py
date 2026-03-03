import pandas as pd

# 1) Ruta esperada del CSV (NO lo subas a GitHub).
#    Guarda tu export localmente con este nombre:
#    data/raw/yt_table_365d.csv
DATA_PATH = "data/raw/yt_table_365d.csv"

# 2) Cargar
df = pd.read_csv(DATA_PATH)

# 3) Limpiar fila "Total"
df = df[df["Content"] != "Total"].copy()

# 4) Parsear fecha de publicación
df["Video publish time"] = pd.to_datetime(df["Video publish time"], errors="coerce")
df = df.dropna(subset=["Video publish time"])

# 5) Shorts-only (Duration está en segundos)
df = df[df["Duration"] <= 60].copy()

# 6) Filtrar últimos 180 días (tomando como fin la última fecha del dataset)
end_date = df["Video publish time"].max()
start_date = end_date - pd.Timedelta(days=180)
df = df[(df["Video publish time"] >= start_date) & (df["Video publish time"] <= end_date)].copy()

# 7) KPIs clave
df["Subscribers gained"] = df["Subscribers gained"].fillna(0).astype(int)
df["Comments added"] = df["Comments added"].fillna(0).astype(int)
df["Views"] = df["Views"].fillna(0)

# Columnas a mostrar en rankings
cols_show = [
    "Content",
    "Video title",
    "Video publish time",
    "Duration",
    "Views",
    "Subscribers gained",
    "Comments added",
]

# 7.1) Tasas por 1000 views (evitar división por cero)
df["subs_per_1000_views"] = df.apply(
    lambda r: (r["Subscribers gained"] / r["Views"] * 1000) if r["Views"] > 0 else 0,
    axis=1,
)

df["comments_per_1000_views"] = df.apply(
    lambda r: (r["Comments added"] / r["Views"] * 1000) if r["Views"] > 0 else 0,
    axis=1,
)

# 8) Rankings absolutos
top_subs = df.sort_values(
    ["Subscribers gained", "Comments added", "Views"], ascending=False
)[cols_show].head(20)

top_comments = df.sort_values(
    ["Comments added", "Subscribers gained", "Views"], ascending=False
)[cols_show].head(20)

# 9) Rankings por tasa
top_subs_rate = df.sort_values(
    ["subs_per_1000_views", "Subscribers gained", "Views"], ascending=False
)[cols_show + ["subs_per_1000_views"]].head(20)

top_comments_rate = df.sort_values(
    ["comments_per_1000_views", "Comments added", "Views"], ascending=False
)[cols_show + ["comments_per_1000_views"]].head(20)

print("Rango analizado:", start_date.date(), "->", end_date.date())
print("Shorts en el rango:", len(df))

print("\nTOP 20 por SUSCRIPTORES ganados")
print(top_subs.to_string(index=False))

print("\nTOP 20 por COMENTARIOS")
print(top_comments.to_string(index=False))

print("\nTOP 20 por SUSCRIPTORES por 1000 views")
print(top_subs_rate.to_string(index=False))

print("\nTOP 20 por COMENTARIOS por 1000 views")
print(top_comments_rate.to_string(index=False))

# 10) Guardar resultados para el repo (NO incluye data cruda)
top_subs.to_csv("reports/top20_subscribers.csv", index=False)
top_comments.to_csv("reports/top20_comments.csv", index=False)
top_subs_rate.to_csv("reports/top20_subscribers_rate.csv", index=False)
top_comments_rate.to_csv("reports/top20_comments_rate.csv", index=False)

with open("reports/summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Rango analizado: {start_date.date()} -> {end_date.date()}\n")
    f.write(f"Shorts en el rango: {len(df)}\n")
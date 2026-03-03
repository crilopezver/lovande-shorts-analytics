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

# 8) Rankings
cols_show = [
    "Content",
    "Video title",
    "Video publish time",
    "Duration",
    "Views",
    "Subscribers gained",
    "Comments added",
]

top_subs = df.sort_values(
    ["Subscribers gained", "Comments added", "Views"], ascending=False
)[cols_show].head(20)

top_comments = df.sort_values(
    ["Comments added", "Subscribers gained", "Views"], ascending=False
)[cols_show].head(20)

print("Rango analizado:", start_date.date(), "->", end_date.date())
print("Shorts en el rango:", len(df))

print("\nTOP 20 por SUSCRIPTORES ganados")
print(top_subs.to_string(index=False))

print("\nTOP 20 por COMENTARIOS")
print(top_comments.to_string(index=False))

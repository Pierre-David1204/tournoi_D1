import streamlit as st
import pandas as pd
from supabase import create_client

url = "https://yzupjrzhqmojefurpmrx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6dXBqcnpocW1vamVmdXJwbXJ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM0MTY0ODcsImV4cCI6MjA4ODk5MjQ4N30.4qYKmPfDagkicbC31aob3egY2msh7mzuk7ECRJ2-M1A"

supabase = create_client(url, key)

# sécurité connexion
if "equipe" not in st.session_state:
    st.switch_page("app.py")

equipe = st.session_state.equipe
poule_id = equipe["poule_id"]
mon_equipe = equipe["nom"]

st.title("📊 Classement de la poule")

# récupérer les équipes de la poule
data = supabase.table("d1_equipes") \
    .select("*") \
    .eq("poule_id", poule_id) \
    .execute()

df = pd.DataFrame(data.data)

# tri classement
df = df.sort_values(
    ["points", "score_total"],
    ascending=False
)

# ajouter position
df.insert(0, "#", range(1, len(df) + 1))

df = df.rename(columns={
    "nom": "Equipe",
    "points": "Pts",
    "victoires": "V",
    "nuls": "N",
    "defaites": "D",
    "score_total": "Score total"
})

df = df[[
    "#",
    "Equipe",
    "Pts",
    "V",
    "N",
    "D",
    "Score total"
]]

# mettre l'équipe en gras
def highlight_team(row):
    if row["Equipe"] == mon_equipe:
        return ["font-weight: bold"] * len(row)
    return [""] * len(row)

styled = df.style.apply(highlight_team, axis=1)

st.dataframe(styled, use_container_width=True)


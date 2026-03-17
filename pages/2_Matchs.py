import streamlit as st
import pandas as pd
from supabase import create_client

url = "https://yzupjrzhqmojefurpmrx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6dXBqcnpocW1vamVmdXJwbXJ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM0MTY0ODcsImV4cCI6MjA4ODk5MjQ4N30.4qYKmPfDagkicbC31aob3egY2msh7mzuk7ECRJ2-M1A"


supabase = create_client(url, key)

st.title("📅 Planning D1")

equipes_data = supabase.table("d1_equipes").select("*").execute()

equipes = {e["id"]:e["nom"] for e in equipes_data.data}

data = supabase.table("d1_matchs").select("*").execute()

df = pd.DataFrame(data.data)

df["Equipe1"] = df["equipe1"].map(equipes)
df["Equipe2"] = df["equipe2"].map(equipes)

for _,m in df.iterrows():

    heure = pd.to_datetime(str(m["heure"])).strftime("%H:%M")

    st.write(
        f"{heure} | Terrain {m['terrain']} | {m['Equipe1']} vs {m['Equipe2']}"
    )

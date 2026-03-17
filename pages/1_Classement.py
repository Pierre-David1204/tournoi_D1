import streamlit as st
import pandas as pd
from supabase import create_client

url = "https://yzupjrzhqmojefurpmrx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6dXBqcnpocW1vamVmdXJwbXJ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM0MTY0ODcsImV4cCI6MjA4ODk5MjQ4N30.4qYKmPfDagkicbC31aob3egY2msh7mzuk7ECRJ2-M1A"


supabase = create_client(url, key)

st.title("📊 Classement D1")

data = supabase.table("d1_equipes").select("*").execute()

df = pd.DataFrame(data.data)

df = df.sort_values(
    ["points","score_total"],
    ascending=False
)

df.insert(0,"#",range(1,len(df)+1))

st.dataframe(df[[
"#",
"nom",
"points",
"victoires",
"nuls",
"defaites",
"score_total"
]])

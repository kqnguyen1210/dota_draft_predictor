import pickle

import pandas as pd
import streamlit as st

# For hero names to be used in the multiselect
df_heroes = pd.read_csv("dota_heroes.csv")

all_heroes = df_heroes["Hero Name"].to_list()

with open("dota_rf_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

# HEADER
st.title("Dota 2 Oracle")
st.write("Predict match outcomes using a 10,000-match Random Forest model.")

# DRAFTING INTERFACE
st.subheader("Draft Your Teams")

col1, col2 = st.columns(2)

with col1:
    st.write("### Radiant Team")
    radiant_draft = st.multiselect(
        "Select 5 Heroes:",
        all_heroes,
        max_selections=5,
    )

with col2:
    st.write("### Dire Team")
    dire_draft = st.multiselect(
        "Select 5 Heroes:",
        all_heroes,
        max_selections=5,
    )

# COUNTER-PICK INTERFACE
st.subheader("Activate Synergies & Counters")
st.write("Select the known interactions you want the model to heavily weigh:")

available_interactions = [
    "Anti-Mage vs Medusa",
    "Earthshaker vs Meepo",
    "Axe vs Dazzle",
]

active_interactions = st.multiselect("Known Matchups:", available_interactions)

# PREDICT BUTTON
if st.button("Predict Match Outcome"):
    if len(radiant_draft) == 5 and len(dire_draft) == 5:
        st.success("Draft locked in! Running the Oracle...")
        for hero in radiant_draft:
            # We add a quick safety check to make sure the hero is actually in our dictionary
            if hero in draft_matrix:
            draft_matrix[hero] = 1
    else:
        st.error("Please select exactly 5 heroes for each team.")

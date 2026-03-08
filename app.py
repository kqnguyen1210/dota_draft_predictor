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
        key="radiant_draft_box",
    )

with col2:
    st.write("### Dire Team")
    dire_draft = st.multiselect(
        "Select 5 Heroes:", all_heroes, max_selections=5, key="dire_draft_box"
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

        model_columns = rf_model.feature_names_in_

        draft_matrix = {feature: 0 for feature in model_columns}

        for hero in radiant_draft:
            # We add a quick safety check to make sure the hero is actually
            # in our dictionary
            if hero in draft_matrix:
                draft_matrix[hero] = 1

        for hero in dire_draft:
            if hero in draft_matrix:
                draft_matrix[hero] = -1

        for interaction in available_interactions:
            if interaction in draft_matrix:
                draft_matrix[interaction] = -1

        single_match_df = pd.DataFrame([draft_matrix])

        win_probability = rf_model.predict_proba(single_match_df)[0][1]

        radiant_prob = float(win_probability)
        dire_prob = 1.0 - radiant_prob

        st.divider()
        st.subheader("🔮 Oracle Verdict")

        res_col1, res_col2 = st.columns(2)

        with res_col1:
            st.metric(
                label="🌟 Radiant Win Probability",
                value=f"{radiant_prob * 100:.1f}%",
            )
            st.progress(radiant_prob)

        with res_col2:
            st.metric(
                label="👹 Dire Win Probability", value=f"{dire_prob * 100:.1f}%"
            )
            st.progress(dire_prob)

        st.write("")

        if radiant_prob > 0.5:
            st.success("The Oracle heavily favors the Radiant draft.")
        else:
            st.error("The Oracle heavily favors the Dire draft.")

    else:
        st.error("Please select exactly 5 heroes for each team.")

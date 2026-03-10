Dota 2 Match Outcome Predictor ("Dota Oracle")

Overview

An end-to-end machine learning pipeline that harvests real-time match data from the OpenDota API to predict the outcome of professional-grade drafts. The project compares linear and non-linear models to identify which hero picks carry the most "weight" in the current meta.

Tech Stack: Python, Scikit-Learn, Pandas, Streamlit, Git, Streamlit Community Cloud

    Built and deployed a full-stack machine learning web application that predicts esports match outcomes based on team compositions and hero counter-picks.

    Engineered features from a 10,000-match dataset, utilizing Pandas to transform raw drafting data into formatted matrices for model ingestion.

    Trained and evaluated a Random Forest classifier using Scikit-Learn, extracting the underlying predictive logic to calculate dynamic win probabilities.

    Developed an interactive front-end user interface using Streamlit, allowing users to input live match drafts and toggle specific synergetic interactions.

    Deployed the application to the live web via Streamlit Community Cloud, establishing a continuous deployment pipeline synced directly to a GitHub repository.

Key Features

    Live Data Harvesting: Automated script to pull 10,000+ unique matches using API pagination.

    The Hero Matrix: A custom-engineered sparse matrix transforming categorical hero IDs into a +1/−1 feature set representing Radiant and Dire team compositions.

    Interpretability: Comparison of Logistic Regression coefficients and Random Forest feature importance to identify high-variance heroes like Pudge.
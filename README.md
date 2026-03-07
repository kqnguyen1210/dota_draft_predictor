Overview

An end-to-end machine learning pipeline that harvests real-time match data from the OpenDota API to predict the outcome of professional-grade drafts. The project compares linear and non-linear models to identify which hero picks carry the most "weight" in the current meta.

Technical Stack

    Data Ingestion: Requests (REST API), JSON, Time (Rate-limiting).

    Data Engineering: Pandas, NumPy, AST (Literal Evaluation).

    Machine Learning: Scikit-Learn (Random Forest, Logistic Regression).

    Visualization: Matplotlib (Feature Importance).

    DevOps: Pickle (Model Serialization)

Key Features

    Live Data Harvesting: Automated script to pull 10,000+ unique matches using API pagination.

    The Hero Matrix: A custom-engineered sparse matrix transforming categorical hero IDs into a +1/−1 feature set representing Radiant and Dire team compositions.

    Interpretability: Comparison of Logistic Regression coefficients and Random Forest feature importance to identify high-variance heroes like Pudge.

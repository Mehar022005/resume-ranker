import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

from utils.scorer import SKILL_KEYWORDS

def plot_scores(df):
    fig, ax = plt.subplots()
    sns.barplot(data=df, x="Score", y="Resume", ax=ax, palette="viridis")
    ax.set_title("Resume Scores")
    return fig

def show_heatmap(matrix, names):
    df = pd.DataFrame(matrix, index=names, columns=SKILL_KEYWORDS)
    st.subheader("🧠 Skill Match Heatmap")
    fig, ax = plt.subplots(figsize=(10, len(names) * 0.5))
    sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=False, linewidths=.5, ax=ax)
    st.pyplot(fig)

import streamlit as st
import pandas as pd
import sqlite3

# ---- Load Data ----
conn = sqlite3.connect('nextgen.db')
applicants = pd.read_sql("SELECT * FROM applicants;", conn)
interns = pd.read_sql("SELECT * FROM interns;", conn)
scores = pd.read_sql("SELECT * FROM hackathon_scores;", conn)

st.title("NextGenLearners - Program Performance Dashboard")

# ---- Domain Filter ----
domain_list = ['All'] + sorted(applicants['domain'].unique().tolist())
selected_domain = st.selectbox('Filter by Domain', domain_list)

if selected_domain != 'All':
    applicants_filtered = applicants[applicants['domain'] == selected_domain]
    interns_filtered = interns[interns['domain'] == selected_domain]
    scores_filtered = scores[scores['domain'] == selected_domain]
else:
    applicants_filtered = applicants
    interns_filtered = interns
    scores_filtered = scores

# ---- 1. Funnel: Applicants vs Interns ----
st.subheader("Applicant to Intern Funnel")
col1, col2 = st.columns(2)
col1.metric("Total Applicants", len(applicants_filtered))
col2.metric("Completed Interns", len(interns_filtered[interns_filtered['completion_status'] == 'Completed']))

# ---- 2. Completion Rate per Domain ----
st.subheader("Completed Interns per Domain")
completed_by_domain = interns[interns['completion_status'] == 'Completed']['domain'].value_counts()
st.bar_chart(completed_by_domain)

# ---- 3. Average Hackathon Score per Domain ----
st.subheader("Average Hackathon Score per Domain")
avg_score_by_domain = scores.groupby('domain')['score'].mean().round(2)
st.bar_chart(avg_score_by_domain)

# ---- 4. Leaderboard: Top 10 Performers ----
st.subheader("Top 10 Performers")
leaderboard = scores_filtered.merge(interns_filtered, on=['intern_id', 'domain'])
leaderboard = leaderboard.sort_values('score', ascending=False).head(10)
st.dataframe(leaderboard[['intern_id', 'domain', 'score']])
import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.formula.api as smf
st.title("Causal Inference Dashboard: Policy Impact")
st.write("Evaluating the impact of interventions using Difference-in-Differences (DiD)")
@st.cache_data
def load_data():
    return pd.read_csv('marketing_data.csv')
df=load_data()
st.sidebar.header("Model Settings")
treated_unit=st.sidebar.selectbox("Select Treaated Unit", df['State'].unique())
intervention_year=st.sidebar.slider("Select Intervention Year", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=2016)
df['is_treated_unit']=(df['State']==treated_unit).astype(int)
df['is_post_intervention']=(df['Year']>=intervention_year).astype(int)
model=smf.ols('Sales ~ is_treated_unit+is_post_intervention+is_treated_unit:is_post_intervention', data=df)
results=model.fit()
treatment_effect=results.params['is_treated_unit:is_post_intervention']
p_value=results.pvalues['is_treated_unit:is_post_intervention']
st.subheader("Causal Impact Estimates")

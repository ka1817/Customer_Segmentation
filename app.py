from sklearn import preprocessing
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the pre-trained model
filename = 'final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Load the clustered dataset
df = pd.read_csv("Clustered_Data.csv")

# Streamlit app setup
st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title("Customer Segmentaion")

# Input form
with st.form("my_form"):
    balance = st.number_input(label='Balance', step=0.001, format="%.6f")
    balance_frequency = st.number_input(label='Balance Frequency', step=0.001, format="%.6f")
    purchases = st.number_input(label='Purchases', step=0.01, format="%.2f")
    oneoff_purchases = st.number_input(label='OneOff Purchases', step=0.01, format="%.2f")
    installments_purchases = st.number_input(label='Installments Purchases', step=0.01, format="%.2f")
    cash_advance = st.number_input(label='Cash Advance', step=0.01, format="%.6f")
    purchases_frequency = st.number_input(label='Purchases Frequency', step=0.01, format="%.6f")
    oneoff_purchases_frequency = st.number_input(label='OneOff Purchases Frequency', step=0.1, format="%.6f")
    purchases_installment_frequency = st.number_input(label='Purchases Installments Frequency', step=0.1, format="%.6f")
    cash_advance_frequency = st.number_input(label='Cash Advance Frequency', step=0.1, format="%.6f")
    cash_advance_trx = st.number_input(label='Cash Advance Trx', step=1)
    purchases_trx = st.number_input(label='Purchases TRX', step=1)
    credit_limit = st.number_input(label='Credit Limit', step=0.1, format="%.1f")
    payments = st.number_input(label='Payments', step=0.01, format="%.6f")
    minimum_payments = st.number_input(label='Minimum Payments', step=0.01, format="%.6f")
    prc_full_payment = st.number_input(label='PRC Full Payment', step=0.01, format="%.6f")
    tenure = st.number_input(label='Tenure', step=1)

    # Create a data structure for prediction
    data = [[
        balance, balance_frequency, purchases, oneoff_purchases, installments_purchases, cash_advance,
        purchases_frequency, oneoff_purchases_frequency, purchases_installment_frequency, cash_advance_frequency,
        cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments, prc_full_payment, tenure
    ]]

    submitted = st.form_submit_button("Submit")

# Prediction and visualization
if submitted:
    clust = loaded_model.predict(data)[0]
    st.write(f'Data belongs to Cluster {clust}')

    # Filter the cluster data
    cluster_df1 = df[df['Cluster'] == clust]

    # Plot the histograms for each feature in the cluster
    st.write(f"Feature Distributions for Cluster {clust}")
    for c in cluster_df1.drop(['Cluster'], axis=1):
        fig, ax = plt.subplots()
        sns.histplot(data=cluster_df1, x=c, kde=True, ax=ax)
        plt.title(f'Distribution of {c} in Cluster {clust}')
        st.pyplot(fig)

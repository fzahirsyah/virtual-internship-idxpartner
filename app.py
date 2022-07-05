import streamlit as st
import pandas as pd
import pickle


st.title('Consumer Credit Risk Prediction')
st.markdown('''
    These web Application is for predicting costumer credit risk in the loan company

    the value below are for example data input
    ''')


num_select = ['inq_last_6mths','out_prncp','total_rec_prncp','recoveries','last_pymnt_amnt']
cat_select = ['initial_list_status','last_pymnt_d']
day_list = ['Jan-16', 'Apr-15', 'Dec-15', 'Mar-15', 'Jul-15', 'Mar-13',
       'Jan-11', 'Oct-15', 'Jul-14', 'Aug-15', 'Nov-12', 'Jul-12',
       'Jun-15', 'Oct-12', 'Jun-12', 'Jan-15', 'Feb-15', 'Nov-14',
       'Jun-13', 'Feb-14', 'Dec-12', 'Sep-15', 'May-15', 'Nov-15',
       'Apr-14', 'May-14', 'Dec-14', 'Mar-14', 'Oct-13', 'Feb-13',
       'Nov-13', 'Aug-14', 'Dec-13', 'Oct-14', 'May-13', 'Jul-13',
       'Jun-14', 'Feb-12', 'Aug-13', 'Sep-14', 'Sep-13', 'Jan-14',
       'May-12', 'Apr-12', 'Jul-11', 'Jan-12', 'Jan-13', 'Apr-13',
       'Oct-11', 'Apr-11', 'Feb-11', 'Mar-12', 'Sep-12', 'Sep-10',
       'Jun-10', 'Aug-08', 'Nov-10', 'Mar-11', 'Dec-10', 'Dec-11',
       'Nov-11', 'May-08', 'Feb-09', 'Aug-12', 'Sep-11', 'May-10',
       'May-11', 'Jul-10', 'Jun-11', 'Mar-10', 'Aug-11', 'Apr-08',
       'Jan-10', 'Oct-10', 'Jun-09', 'Dec-09', 'Oct-08', 'Apr-09',
       'Aug-10', 'Jul-08', 'Feb-10', 'Mar-09', 'May-09', 'Oct-09',
       'Nov-08', 'Aug-09', 'Apr-10', 'Jan-09', 'Sep-09', 'Dec-08',
       'Sep-08', 'Jun-08', 'Jul-09', 'Nov-09', 'Jan-08', 'Mar-08',
       'Feb-08', 'Dec-07']

col1,col2 = st.columns(2)
inq_last_6mths = col1.number_input('inqueries last 6 months',min_value=0,max_value=6,value=1,step=1)
out_prncp = col2.number_input('Payments received to date for total amount funded',min_value=0,max_value=100000,value=3000)
total_rec_prncp = col1.number_input('Number of finance trades',min_value=0,max_value=100000,value=3000)
recoveries = col2.number_input('Recoveries',min_value=0,max_value=100000,value=0)
last_payment_amount = col1.number_input('The number of months since the borrowers last delinquency.',min_value=0,max_value=100000,value=250)

initial_list_status = st.selectbox(options=['w','f'], index=0, label='Initial List Status')
last_pymnt_d = st.selectbox(options=day_list, index=0 , label='last payment date')

data_new = {
    'inq_last_6mths' : inq_last_6mths,
    'out_prncp' : out_prncp,
    'total_rec_prncp' : total_rec_prncp,
    'recoveries': recoveries,
    'last_pymnt_amnt': last_payment_amount,
    'initial_list_status' : initial_list_status,
    'last_pymnt_d': last_pymnt_d
}
data_new = pd.DataFrame([data_new])

with open("model/model_credit_score.pkl", "rb") as p:
    credit_score = pickle.load(p)

if st.button('predict'):
    predict_score = credit_score.predict(data_new)
    if predict_score == 1:
        st.subheader('Credit Score for this person is Bad')
        st.markdown(" we shouldn't give the person loans")
    elif predict_score == 2:
        st.subheader('Excelent')
        st.markdown('we can give the person loans without any worries')
    elif predict_score == 3:
        st.subheader('Good')
        st.markdown('we can give the person loans')
    elif predict_score == 4:
        st.subheader('Poor')
        st.markdown('''we can give the person loans but with caution because theres probability that the person can't paid loans on time.
        this person is high risk in credit scoring.
        ''')
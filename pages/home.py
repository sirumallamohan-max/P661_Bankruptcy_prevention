import streamlit as st
import pickle
import pandas as pd
import os
import time

# Load the model

    
def main():
    st.title('P661_Bankruptcy_Prevention')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)

    tab1, tab2 = st.tabs(["💾 About Project","🦸‍♂️ About Group"])
    
    with tab1:
          st.title('About Project')
          st.text('Project Is Designed by Group-5. For details, see in About group.')
          st.header(f"BANKRUPTCY APP")
          st.markdown('Business Objective: This is a classification project, since the variable to predict is binary bankruptcy or non-bankruptcy. The goal here is to model the probability that a business goes bankrupt from different features.')
          st.text('Variables affecting bankruptcy')
          st.markdown("""
          
          |Sr# |Variable |Description|
          |--|:------|:------- |
          |1.| industrial_risk| 0 = low risk, 0.5 = medium risk, 1 = high risk.|
          |2.| management_risk   | 0 = low risk, 0.5 = medium risk, 1 = high risk. |
          |3.| financial flexibility|0 = low flexibility,0.5 = medium flexibility, 1 = high flexibility.|
          |4.| credibility   |0 = low credibility, 0.5 = medium credibility, 1 = high credibility.|
          |5.| competitiveness|0 = low competitiveness, 0.5 = medium competitiveness, 1 = high competitiveness.|
          |6.| operating_risk   | 0 = low risk, 0.5 = medium risk, 1 = high risk. |
          |7.| class   |bankruptcy, non-bankruptcy (target variable).|
          """)

    with tab2:
          st.markdown("""
          #### Group Members
          * **Mohan Rajaram Sirumalla**
          * **Santhosh Kumar H N**
          * **MALLEMPATI SREE LAKSHMI SATHVIKA**
          * **Kandikonda Shashank**
          * **Pranav A**
          * **Devasath Anand**
          * **LOHIT SAI N**
          ***
          """)

if __name__ == '__main__':
    main()
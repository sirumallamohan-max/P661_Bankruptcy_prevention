import streamlit as st
import pickle
import pandas as pd
import os

# Load the model

    
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pickle_path = os.path.join(current_dir, '..', 'models', 'P661_Bankruptcy_Prevention_Group5.pkl')

    with open(pickle_path , 'rb') as file:
        loaded_model = pickle.load(file)
    # --- 1. SET PAGE CONFIG ---
    st.set_page_config(layout="wide", page_title="Bankruptcies & Prevention", page_icon="🏠")
    
    # Create two columns (Column 1: Prevention, Column 2: Bankruptcies)
    # You can adjust relative widths, e.g., st.columns([2, 1])
    col1, col2 = st.columns([0.3,0.7])
    
    # --- COLUMN 1: PREVENTION ---
    with col1:
        
        # st.subheader("🛡️ Prevention Strategies")
        st.image("assets/group5.png")
        st.markdown("💡 **Prevention Strategies**")
        st.markdown("\u2714 High Performance")
        st.markdown("\u2714 Mainain a healthy cash flow")
        st.markdown("\u2714 Reduce unnecessary operational expenses")
        st.markdown("\u2714 Improve financial flexibility")
        st.markdown("\u2714 Enchnage a buiness credibility to attract investors")
        st.markdown("\u2714 Monitor competitiveness in the market")


    
    # --- COLUMN 2: BANKRUPTCIES ---
    with col2:
        st.subheader("🛡️ Bankruptcy Prevention App")

        sub_col1, sub_col2 = st.columns(2)
    
        with sub_col1:
            # Use select_slider for fixed options
            feature_1 = st.select_slider(
            "industrial risk",
            options=[0, 0.5, 1],
            value=0.5, # Default value
            key="feature_1")

            # Use select_slider for fixed options
            feature_3 = st.select_slider(
            "financial_flexibility",
            options=[0, 0.5, 1],
            value=0.5, # Default value
            key="feature_3")
            
            # Use select_slider for fixed options
            feature_5 = st.select_slider(
            "competitiveness",
            options=[0, 0.5, 1],
            value=0.5, # Default value
            key="feature_5")
            
        with sub_col2:
            # Use select_slider for fixed options
            feature_2 = st.select_slider(
            "management_risk",
            options=[0, 0.5, 1],
            value=0.5, # Default value
            key="feature_2")

            # Use select_slider for fixed options
            feature_4 = st.select_slider(
            "credibility",
            options=[0, 0.5, 1],
            value=0.5, # Default value
            key="feature_4")
            
            # Use select_slider for fixed options
            feature_6 = st.select_slider(
            "operating_risk",
            options=[0,0.1,0.2,0.3,0.4, 0.5, 1],
            value=0.5, # Default value
            key="feature_6")
        


        # Create a DataFrame or array from inputs, matching the model's expected format
        user_input = pd.DataFrame({
            'industrial_risk':[feature_1],
            'imanagement_risk':[feature_2],
            'financial_flexibility':[feature_3],
            'credibility':[feature_4],
            'competitiveness':[feature_5],
            'operating_risk':[feature_6]        
        })

        # Make prediction
        if st.button("Run Bankruptcy Prediction"):
            prediction = loaded_model.predict(user_input)
            prediction_prob = loaded_model.predict_proba(user_input)
            # print(f"Probability of 'No': {prediction_prob[0][0] * 100}%")
            # print(f"Probability of 'Yes': {prediction_prob[0][1] * 100}%")
            if prediction[0] == 1 :
                result="Bankcruptcy"
                st.error(f"The predicted output is: {result} with {prediction_prob[0][1] * 100}%")
            else:
                result="Non Bankcruptcy"
                st.success(f"The predicted output is: {result} with {prediction_prob[0][0] * 100}%")
               
    
            
            
        
        # --- BOTTOM SECTION ---
        st.write("---")
        st.write("System Status: Operational")


if __name__ == '__main__':
    main()
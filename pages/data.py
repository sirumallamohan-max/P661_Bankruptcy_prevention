import streamlit as st
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt 

# This function will only run once and cache the result
@st.cache_data
def load_data(file_path):
    # Perform the expensive read operation
    df = pd.read_excel(file_path)
    return df

def main():
    st.set_page_config(layout="wide") # Optional: use the full width of the browser
    
    # Create a sample dataframe
    # df = pd.read_excel("data/data.xlsx")

    # Display a spinner while loading data
    with st.spinner('Loading data, please wait...'):
        # Replace with your actual data loading logic
        #time.sleep(3)  # Simulating a delay
        df = load_data("data/data.xlsx")
    
    st.title("Bankruptcy Analysis Dataset")
    my_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    
    tab1, tab2 = st.tabs(["Univariate Analysis📊" , "Multivariate Analysis📈"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.header('Exploratory Data Analysis -Univarite analysis')
            st.subheader('Univarite analysis')
            st.write('Univarite analysis explores each variable in a dataset separately.')
            options = ['industrial_risk', 'management_risk', 'financial_flexibility', 'credibility', 'competitiveness', 'operating_risk']
            
            #Describe The dataset
            st.write(df.describe())
            
            #Value_counts
            selected_option = st.selectbox('Select a variable to display value counts', options)
            st.write(df[selected_option].value_counts())
            
            #Histogram
            selected_option = st.selectbox('Select an option', options)
            fig, ax = plt.subplots()
            fig, ax = plt.subplots(figsize=(8, 6))
            df.hist(column=selected_option, by='class', ax=ax, stacked=True)
            ax.set_title("Histogram for {}".format(selected_option))
            ax.set_xlabel(selected_option)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)
            
            #Pie Charts
            selected_option = st.selectbox('Select a variable to create a pie chart', options)
            fig, ax = plt.subplots(figsize=(8, 8))
            df[selected_option].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
            ax.set_title("Pie chart for {}".format(selected_option))
            st.pyplot(fig)
            
            #Count Plots
            selected_option = st.selectbox('Select a variable to create a count plot', options)
            fig, ax = plt.subplots()
            sns.countplot(data=df, x=selected_option, ax=ax)
            ax.set_title("Count plot for {}".format(selected_option))
            ax.set_xlabel(selected_option)
            ax.set_ylabel('Count')
            st.pyplot(fig)
    
    # Define tab-2 for multivariate analysis
    with tab2:
        col1, col2 = st.columns(2)
    
        with col1:
            st.header("Exploratory Data Analysis - Multivariate Analysis")
            st.subheader('Multivariate Analysis')
            st.write('Multivariate analysis is based on observation and analysis of more than one statistical outcome variable at a time.')
        
            # Define options for visualizations
            options = ['Correlation Heatmap', 'Pairplot', 'Boxplot']
            selected_option = st.selectbox('Select a visualization', options)
            
            # Display Correlation Heatmap if selected
            if selected_option == 'Correlation Heatmap':
                st.subheader('Correlation between the Variables')
                corr_matrix = df.drop(columns='class').corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr_matrix, cmap="YlGnBu", annot=True, ax=ax)
                ax.set_title("Correlation Matrix")
                st.pyplot(fig)
            
            # Display Pairplot if selected
            elif selected_option == 'Pairplot':
                st.subheader('Pairplot')
                fig = sns.pairplot(data=df)
                st.pyplot(fig)
        
                # Display Boxplot if selected
            elif selected_option == 'Boxplot':
                st.subheader('Boxplot')
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.boxplot(data=df, ax=ax)
                ax.set_title("Boxplot")
                st.pyplot(fig)
    
if __name__ == '__main__':
    main()
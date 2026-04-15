import streamlit as st
import pandas as pd
import time
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
    
    st.title("Browse and Display Bankruptcy Analysis Dataset")
    
    # Use a sidebar for the multiselect widget
    with st.sidebar:
        st.header("Column Selection")
        # Get user selection of columns to display
        selected_columns = st.multiselect(
            "Select columns to display:",
            list(df.columns), # Pass all column names as options
            default=list(df.columns) # Display all columns by default
        )

    # # Define tab names
    # tab1, tab2, tab3 = st.tabs(["📈 Visualization", "🗃 Raw Data", "ℹ️ Info"])
    
    # # Content for Tab 1: Visualization
    # with tab1:
    #     st.header("Performance Chart")
    #     st.line_chart(df)
    
    # # Content for Tab 2: Raw Data
    # with tab2:
    #     st.header("Dataset Overview")
    #     st.write("Below is the sample data used for the chart:")
    #     st.dataframe(df)
    
    # # Content for Tab 3: Info (Alternative syntax)
    # tab3.header("About This App")
    # tab3.write("This app demonstrates how to use `st.tabs` to organize a dashboard.")
    # Display the filtered dataframe in the main area
    if selected_columns:
        st.subheader("Selected Data")
        # Display only the selected columns

        # Display a spinner while loading data
        with st.spinner('Loading data, please wait...'):
            # Replace with your actual data loading logic
            #time.sleep(3)  # Simulating a delay
            st.dataframe(df[selected_columns], use_container_width=True)
    else:
        st.warning("Please select at least one column to display.")
    
if __name__ == '__main__':
    main()
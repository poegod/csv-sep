import streamlit as st
import pandas as pd

# Title of the app
st.title("CSV/Excel Column Separator")

# File upload section
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Read the uploaded file
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Display a sample of the data
        st.write("Preview of your data:")
        st.dataframe(df.head())
        
        # Column selection
        selected_column = st.selectbox("Select the column to filter by:", df.columns)
        
        # Process button
        if st.button("Process"):
            # Split the file into two based on the selected column
            filled_df = df[df[selected_column].notna() & (df[selected_column] != '')]
            empty_df = df[df[selected_column].isna() | (df[selected_column] == '')]
            
            # Display results summary
            st.write(f"Rows with '{selected_column}' filled: {filled_df.shape[0]}")
            st.write(f"Rows with '{selected_column}' empty: {empty_df.shape[0]}")
            
            # Convert results to CSV for download
            filled_csv = filled_df.to_csv(index=False).encode('utf-8')
            empty_csv = empty_df.to_csv(index=False).encode('utf-8')
            
            # Download buttons
            st.download_button(
                label="Download Rows with Data",
                data=filled_csv,
                file_name="filled_rows.csv",
                mime="text/csv",
            )
            st.download_button(
                label="Download Rows without Data",
                data=empty_csv,
                file_name="empty_rows.csv",
                mime="text/csv",
            )
    except Exception as e:
        st.error(f"Error processing the file: {e}")

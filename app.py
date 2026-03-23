import streamlit as st

# MUST BE FIRST
st.set_page_config(
    page_title='Claim Prediction' ,
    layout='wide'
)

st.write("Claim Prediction")

st.sidebar.title('Streamlit Dashboard')
section = st.sidebar.radio(
    "Jump to section",
    ['Home', 'Text and Markdown', 'Layout Columns', 'File Upload', 'Forms', 'Sessions', 'Caching']
)

if section == 'Home':
    st.title("Claim Prediction")
    st.subheader(
        "Details on Claim Prediction",
        divider=True
    )
st.header('Streamlit Dashboard')

if section == 'Input widgets':
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('Basic Inputs')
        name = st.text_input("Enter Details")

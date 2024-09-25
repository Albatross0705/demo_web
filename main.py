import streamlit as st
import pandas as pd 

# st.title("Welcome to DataWizardryHub")
# st.header("Data Science Tutorial")
# st.subheader("learn with Akash")
# st.markdown("I love Data science and AI")
# st.code("""for i in range (1,5,1):
#         print ("hello")""")

# st.title("Cosmetics Data")
# dataset = pd.read_csv("C:/Users/akash/Downloads/Csv.Dataset/cosmetics.csv")

# st.dataframe(dataset)

name = st.text_input("Enter your name")
lname = st.text_input("Enter your last name")
adr = st.text_area("Enter the Address")
clasdata = st.selectbox("Enter the Class : ",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
                Name :{name}
                Last Name : {lname}
                 Address : {adr}
                 class : {clasdata}""")
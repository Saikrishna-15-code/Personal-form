import streamlit as st

st.set_page_config(page_title = "Personal Details form", layout = "wide")

st.title("GENERAL DETAILS") 


with st.form("general_details_form"):

   st.subheader("1.Name (IN CAPITAL LETTERS)")
   col1, col2, col3 = st.columns(3)
   with col1:
      first_name = st.text_input("First Name")
   with col2:
      middle_name = st.text_input("Middle Name")
   with col3:
      last_name = st.text_input("Last Name") 

   st.subheader("2.Date Of Birth")
   dob = st.date_input("Select Date")   

   st.subheader("3.Education Details")
   col1, col2, col3 = st.columns(3)
   with col1:
      degree = st.text_input("Degree")
   with col2:
      college = st.text_input("College/University")
   with col3:
      yop = st.date_input("Year Of Passing")   

   st.subheader("4.Family Details")   
   fam_col1, fam_col2 = st.columns(2)
   with fam_col1:
      father_name = st.text_input("Father Name")   
      mother_name = st.text_input("Mother_name")
   with fam_col2:
      father_occ = st.text_input("Father Occupation")
      mother_occ = st.text_input("Mother Occupation")

   st.subheader("5.Contact Details")
   tel = st.text_input("Telephone Number")
   phone = st.text_input("Phone Number")
   emg = st.text_input("Emergency Contact Number")

   st.subheader("Address")
   addr_1 = st.text_area("Address for Communication (WITH PIN CODE IN CAPITAL LETTERS)")
   addr_2 = st.text_area("Permanent Address")

   st.subheader("Identification Details")
   pan = st.text_input("PAN Number")
   aadhar = st.text_input("Aadhar Number")

   submitted = st.form_submit_button("Submit")

if submitted:
   st.success("Form submitted Successfully")
   st.write("Submitted Data")
   st.json({
      "First Name": first_name,
      "Middle Name": middle_name,
      "Last Name": last_name,
      "Date Of Birth": dob,
      "Degree": degree,
      "College": college,
      "Year Of Passing": yop,
      "Father Name": father_name,
      "Mother Name": mother_name,
      "Phone Number": phone,
      "Address": addr_1,
      "Permanent Address": addr_2,
      "PAN Number": pan,
      "Aadhar Number": aadhar
   })   

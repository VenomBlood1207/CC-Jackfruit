import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Employee & Staff Form", layout="centered")

st.title("📋 Add New Employee and Staff (Unified Form)")

with st.form("combined_form"):
    st.subheader("🧾 Common Form for Employee & Staff")

    # Common fields
    name = st.text_input("Full Name")
    first_name, last_name = "", ""
    if name:
        parts = name.strip().split()
        if len(parts) > 1:
            first_name = parts[0]
            last_name = " ".join(parts[1:])
        else:
            first_name = name
            last_name = ""

    user_id = st.text_input("User ID (UUID)")
    department_id = st.text_input("Department ID (UUID)")
    employee_id = st.text_input("Employee ID")
    role = st.text_input("Role / Position")
    specialization = st.selectbox("Specialization", ["badminton", "volleyball", "basketball"])
    date_of_birth = st.date_input("Date of Birth")
    hire_date = st.date_input("Hire Date")
    contact_number = st.text_input("Contact Number")
    email = st.text_input("Email")
    address = st.text_area("Address")
    is_active = st.checkbox("Is Active?", value=True)
    years_of_experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)

    submitted = st.form_submit_button("🚀 Submit")

    if submitted:
        # Prepare employee data
        emp_payload = {
            "user_id": user_id,
            "department_id": department_id,
            "employee_id": employee_id,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": str(date_of_birth),
            "hire_date": str(hire_date),
            "position": role,
            "contact_number": contact_number,
            "address": address,
        }

        # Prepare staff data
        staff_payload = {
            "name": name,
            "role": role,
            "specialization": specialization,
            "contact_number": contact_number,
            "email": email,
            "is_active": is_active,
            "years_of_experience": years_of_experience
        }

        # Send to Employee API
        try:
            emp_response = requests.post("http://10.14.147.239:3001/api/employees", json=emp_payload)
            if emp_response.status_code in [200, 201]:
                st.success("✅ Employee added successfully!")
            else:
                st.error(f"❌ Employee API error: {emp_response.text}")
        except Exception as e:
            st.error(f"🚨 Error connecting to Employee API: {e}")

        # Send to Staff API
        try:
            staff_response = requests.post("http://10.14.147.179:8004/staff", json=staff_payload)
            if staff_response.status_code in [200, 201]:
                st.success("✅ Staff added successfully!")
            else:
                st.error(f"❌ Staff API error: {staff_response.text}")
        except Exception as e:
            st.error(f"🚨 Error connecting to Staff API: {e}")

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

        # Friendly error messages
        friendly_errors = {
            "connection": "Couldn't connect to the server. Please check your internet or try again later.",
            "timeout": "The request took too long. Please try again after some time.",
            "invalid_data": "Something was wrong with the information entered. Please check the fields and try again.",
            "unknown": "An unexpected error occurred. Please contact support if this continues.",
        }

        emp_success = False
        staff_success = False

        # Send to Employee API
        try:
            emp_response = requests.post("https://ccproject.navisto.cloud/v1/employee/api/employees", json=emp_payload, timeout=10)
            if emp_response.status_code in [200, 201]:
                emp_success = True
            else:
                st.error("❌ Couldn't add the employee. Please make sure all fields are correctly filled.")
        except requests.exceptions.ConnectionError:
            st.error(f"🚨 {friendly_errors['connection']}")
        except requests.exceptions.Timeout:
            st.error(f"⏳ {friendly_errors['timeout']}")
        except requests.exceptions.RequestException:
            st.error(f"⚠️ {friendly_errors['invalid_data']}")
        except Exception:
            st.error(f"😕 {friendly_errors['unknown']}")

        # Send to Staff API
        try:
            staff_response = requests.post("http://10.20.203.157:8004/staff", json=staff_payload, timeout=10)
            if staff_response.status_code in [200, 201]:
                staff_success = True
            else:
                st.error("❌ Couldn't add the staff member. Please check the inputs and try again.")
        except requests.exceptions.ConnectionError:
            st.error(f"🚨 {friendly_errors['connection']}")
        except requests.exceptions.Timeout:
            st.error(f"⏳ {friendly_errors['timeout']}")
        except requests.exceptions.RequestException:
            st.error(f"⚠️ {friendly_errors['invalid_data']}")
        except Exception:
            st.error(f"😕 {friendly_errors['unknown']}")

        # Show single success message if both succeeded
        if emp_success and staff_success:
            st.success("✅ Success!")
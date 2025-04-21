import streamlit as st
import requests
from datetime import date, datetime

# API endpoints
PURCHASE_ORDER_API = "http://10.14.147.239:3004/api/purchase-orders"
EQUIPMENT_API = "http://10.14.147.179:8001/equipment"

# Helper to fetch equipment names from friend's API
@st.cache_data
def fetch_equipment_names():
    try:
        res = requests.get(EQUIPMENT_API)
        if res.status_code == 200:
            return list({item["name"] for item in res.json()})
        else:
            return []
    except:
        return []

st.title("📝 Create a New Purchase Order")

equipment_name_list = fetch_equipment_names()

# --- Purchase Order Details ---
st.header("🧾 Purchase Order Details")
po_number = st.text_input("PO Number (unique)", "PO123456")
vendor_id = st.text_input("Vendor ID (UUID)")
department_id = st.text_input("Department ID (UUID)")
order_date = st.date_input("Order Date", value=date.today())
delivery_date = st.date_input("Delivery Date", value=date.today())
total_amount = st.number_input("Total Amount", min_value=0.0)
tax_amount = st.number_input("Tax Amount", min_value=0.0, value=0.0)
shipping_amount = st.number_input("Shipping Amount", min_value=0.0, value=0.0)
grand_total = total_amount + tax_amount + shipping_amount
status = st.selectbox("Status", ["pending", "approved", "rejected", "completed"])
approved_by = st.text_input("Approved By (UUID)", "")
approved_at = st.text_input("Approved At (ISO timestamp)", value=datetime.utcnow().isoformat())
notes = st.text_area("Notes", "Purchase for sports equipment.")

# --- Items Section ---
st.header("📦 Items in this Order")
items = []
equipment_items = []

num_items = st.number_input("How many items?", min_value=1, step=1)

for i in range(num_items):
    st.subheader(f"Item #{i+1}")
    item_name = st.text_input(f"Equipment Name #{i+1}", key=f"name_{i}")
    equipment_type = st.selectbox(
        f"Equipment Type #{i+1}",
        options=["basketball", "badminton", "volleyball", "general"],
        key=f"type_{i}"
    )
    condition = st.selectbox(f"Condition #{i+1}", ["new", "good", "fair", "poor"], key=f"cond_{i}")
    quantity = st.number_input(f"Quantity #{i+1}", min_value=1, key=f"qty_{i}")
    unit_price = st.number_input(f"Unit Price (Cost) #{i+1}", min_value=0.0, key=f"price_{i}")
    total_price = quantity * unit_price
    purchase_date = st.date_input(f"Purchase Date #{i+1}", value=date.today(), key=f"pdate_{i}")
    last_maintenance = st.date_input(f"Last Maintenance #{i+1}", value=date.today(), key=f"mdate_{i}")
    is_available = st.checkbox(f"Is Available #{i+1}", value=True, key=f"avail_{i}")

    st.text(f"Total Price: ₹ {total_price:.2f}")

    # Purchase Order Item
    items.append({
        "item_description": item_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price
    })

    # Equipment Item Payload
    equipment_items.append({
        "name": item_name,
        "equipment_type": equipment_type,
        "quantity": quantity,
        "condition": condition,
        "purchase_date": datetime.combine(purchase_date, datetime.min.time()).isoformat(),
        "last_maintenance": datetime.combine(last_maintenance, datetime.min.time()).isoformat(),
        "cost": unit_price,
        "is_available": is_available
    })

# --- Submit Button ---
if st.button("✅ Submit Purchase Order"):
    po_payload = {
        "po_number": po_number,
        "vendor_id": vendor_id,
        "department_id": department_id,
        "order_date": str(order_date),
        "delivery_date": str(delivery_date),
        "total_amount": total_amount,
        "tax_amount": tax_amount,
        "shipping_amount": shipping_amount,
        "grand_total": grand_total,
        "status": status,
        "approved_by": approved_by if approved_by else None,
        "approved_at": approved_at if approved_at else None,
        "notes": notes,
        "items": items
    }

    try:
        # Submit Purchase Order
        response_po = requests.post(PURCHASE_ORDER_API, json=po_payload)
        if response_po.status_code in [200, 201]:
            st.success("✅ Purchase order submitted successfully!")

            # Submit Equipment Items
            equipment_success = []
            for eq in equipment_items:
                try:
                    res = requests.post(EQUIPMENT_API, json=eq)
                    if res.status_code in [200, 201]:
                        equipment_success.append(eq["name"])
                    else:
                        st.warning(f"⚠️ Failed to post {eq['name']} to /equipment (Status {res.status_code})")
                except Exception as ex:
                    st.error(f"❌ Error posting to /equipment: {eq['name']} - {ex}")

            if equipment_success:
                st.success("📦 Equipment items added: " + ", ".join(equipment_success))
        else:
            st.error(f"❌ Failed to submit PO: {response_po.status_code} - {response_po.text}")
    except Exception as e:
        st.error(f"🔥 Error occurred: {str(e)}")

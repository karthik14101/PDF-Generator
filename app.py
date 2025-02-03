import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_meal_plan(dietary_preference, goal, meal_plan, shopping_list):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 100, f"Personalized Meal Plan ({goal})")
    
    c.setFont("Helvetica", 14)
    c.drawString(100, height - 150, f"Dietary Preference: {dietary_preference}")
    c.drawString(100, height - 170, f"Goal: {goal}")
    
    y_position = height - 200
    for meal, items in meal_plan.items():
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, y_position, f"{meal}:")
        y_position -= 20
        c.setFont("Helvetica", 12)
        for item in items:
            c.drawString(120, y_position, f"- {item}")
            y_position -= 15
    
    y_position -= 30
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y_position, "Shopping List:")
    
    y_position -= 20
    c.setFont("Helvetica", 12)
    for item in shopping_list:
        c.drawString(120, y_position, f"- {item}")
        y_position -= 15
    
    c.save()
    buffer.seek(0)
    return buffer

def main():
    st.title("Personalized Meal Planner")
    
    dietary_preference = st.selectbox("Select Dietary Preference", ["Vegetarian", "Vegan", "Gluten-Free", "Non-Vegetarian"])
    goal = st.selectbox("Select Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    
    # Example meal plan and shopping list (to be dynamically generated based on input)
    meal_plan = {
        "Breakfast": ["Oats with fruits", "Almonds", "Green tea"],
        "Lunch": ["Grilled chicken with quinoa", "Vegetables", "Apple"],
        "Dinner": ["Salmon with steamed broccoli", "Sweet potato"],
        "Snack": ["Greek yogurt", "Mixed nuts"]
    }
    shopping_list = ["Oats", "Chicken", "Quinoa", "Broccoli", "Sweet potato", "Greek yogurt", "Almonds"]
    
    if st.button("Generate Meal Plan"):
        pdf_buffer = generate_meal_plan(dietary_preference, goal, meal_plan, shopping_list)
        st.download_button(
            label="Download Meal Plan PDF",
            data=pdf_buffer,
            file_name="meal_plan.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()

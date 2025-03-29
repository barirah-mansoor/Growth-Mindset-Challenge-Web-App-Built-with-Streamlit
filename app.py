import streamlit as st
import random
import uvicorn

growth_mindset_messages = [
    "Mistakes help you learn!",
    "Challenges help you grow!",
    "You can improve with practice!",
    "Keep trying, you can do it!",
    "Failure is just a lesson to learn from!"
]

def show_growth_mindset_message():
    message = random.choice(growth_mindset_messages)
    st.write(f"### Growth Mindset Reminder: {message}")


def get_user_goal():
    goal = st.text_input("What is something you want to achieve? Write your goal:")
    return goal

def get_user_reflection():
    reflection = st.text_area("Reflect on a challenge you faced today. How did you handle it? What did you learn?")
    return reflection


def growth_mindset_challenge():
    st.title("Growth Mindset Challenge")
    

    show_growth_mindset_message()

    
    goal = get_user_goal()
    if goal:
        st.write(f"### Your Goal: {goal}")


    reflection = get_user_reflection()
    if reflection:
        st.write(f"### Your Reflection: {reflection}")

   
    if goal and reflection:
        st.write("\nGreat job! Keep working on your goals and reflecting on your progress!")
    else:
        st.write("\nKeep going! Set your goal and reflect when you're ready.")

if __name__ == "__main__":
    growth_mindset_challenge()


   

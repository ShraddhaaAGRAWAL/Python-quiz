import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Python-Quiz", page_icon="🧧")
st.header("🐍2 minute python quiz🐍")

questions = [" Which type of Programming does Python support?",
             "Is Python case sensitive when dealing with identifiers?",
             "Is Python code compiled or interpreted?",
             "Which of the following is used to define a block of code in Python language?",
             "Python supports the creation of anonymous functions at runtime, using a construct called __________",
             "Which of the following character is used to give single-line comments in Python?",
             "Which of the following is not a core data type in Python programming?",
             "Which of these is the definition for packages in Python?",
             "Which one of the following is the use of function in python?",
             " What is output of print(math.pow(3, 2))?"
             ]
options = [
    ["object oriented programming","structured programming","functional programming","all of the mentioned"],
    ["no","yes","machine dependent","none of the mentioned"],
    ["Python code is both compiled and interpreted","Python code is neither compiled nor interpreted","Python code is only compiled","Python code is only interpreted"],
    ["Indentation","Key","Brackets","All of the mentioned"],
    ["pi", "anonymous","lambda","none of the mentioned"],
    ["//","#", "!","/*"],
    ["tuple", "class", "list","dictionary"],
    ["A set of main modules","A folder of python modules","A number of files containing Python definitions and statements","A set of programs making use of Python modules"],
    ["Functions don’t provide better modularity for your application","you can’t create your own functions","Functions are reusable pieces of programs","All of the mentioned"],
    ["9.0","None","9","None of the mentioned"]
    ]
answers = ["all of the mentioned", "yes", "Python code is both compiled and interpreted", "Indentation", "lambda","#", "class","A folder of python modules","Functions are reusable pieces of programs","9.0"]

with st.form("quiz"):
    selected_answers = []
    for i in range(len(questions)):
        answer = st.radio(questions[i], options[i])
        selected_answers.append(answer)
        st.write("---")

    correct_answers = 0
    for i in range(len(questions)):
        if selected_answers[i] == answers[i]:
            correct_answers += 1

    submitted = st.form_submit_button("submit")
    if submitted:
        if correct_answers == len(questions):
            st.success("your answers are correct", icon="🏆")
            rain(
                emoji="👍",
                font_size=50,
                falling_speed=3,
                animation_length=5)
        else:
            st.error(f"You were able to answer {correct_answers} out of {len(questions)} answers correctly. Better luck next time", icon="🙂")


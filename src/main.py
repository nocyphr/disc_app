import streamlit as st
import json
import pandas as pd
import plost

def load_questions():
    with open('src/questionaire.json', 'r') as file:
        data = json.load(file)
    return data["questionaire"]

# Use session state to load data if it hasn't been loaded yet
if 'data' not in st.session_state:
    st.session_state.data = load_questions()

# Initialize a counter for each color
if 'color_counts' not in st.session_state:
    st.session_state.color_counts = {"r": 0, "g": 0, "b": 0, "y": 0}

def main():
    data = st.session_state.data  # Retrieve data from session state

    # If current_question_idx is not in the session state, initialize it
    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0

    if st.session_state.current_question_idx < len(data):
        question = data[st.session_state.current_question_idx]
        question_text = list(question.keys())[0]
        options = list(question[question_text].keys())

        st.markdown(f'## {question_text}')
        answer = st.radio('', options, index=None, key=f'q_{st.session_state.current_question_idx}')

        # Check if an answer has been selected
        if answer:
            # Increment the color count
            

            # If answer is selected, show the next button
            if st.button("Next"):
                selected_color = question[question_text][answer]
                st.session_state.color_counts[selected_color] += 1
                st.session_state.current_question_idx += 1
                st.experimental_rerun()

    if st.session_state.current_question_idx >= len(data):
        # If there are no more questions, display the bar chart
        colors = list(st.session_state.color_counts.keys())
        counts = list(st.session_state.color_counts.values())
        df = pd.DataFrame({"Color": colors, "Count": counts})
        st.dataframe(df)
        plost.donut_chart(
            data=df,
            theta='Count',
            color='Color')

if __name__ == "__main__":
    main()

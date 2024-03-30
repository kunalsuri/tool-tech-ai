# Tutorial_Streamlit.py : Tutorial to use Streamlit elements
import streamlit as st

def section_1():
    st.header("Section 1")
    st.write("This is the content of section 1.")
    # Add more content for section 1 as needed

def section_2():
    st.header("Section 2")
    st.write("This is the content of section 2.")
    # Add more content for section 2 as needed

def section_3():
    st.header("Section 3")
    st.write("This is the content of section 3.")
    # Add more content for section 3 as needed

def main():
    st.title("Multi-Section Streamlit App")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Section 1", "Section 2", "Section 3"])

    # Display selected section
    if selection == "Section 1":
        section_1()
    elif selection == "Section 2":
        section_2()
    elif selection == "Section 3":
        section_3()

if __name__ == "__main__":
    main()

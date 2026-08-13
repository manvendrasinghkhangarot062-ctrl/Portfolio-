import streamlit as st
st.set_page_config(page_title ="MANVENDRA's Portfolio")
st.title("MANDATA MANVENDRA SINGH")
st.subheader("QA Engineer/Developer")
st.write(""""welcome to my portfolio
I am corrently working at Genpact and learning
-"python",
-"streamlit",
-"git and github",
-"QA (software Testing)"
-"web developing""")

st.header("SKILLS")

skills=["python""streamlit""git""git hub""QA Testing""web developing""jira""autometion"]
for skill in skills:
    st.write("tick",skill)# we need to add tick logo from pc 
    st.header("current projects")# need to add logo of book from pc 
    st.write("1.python calculator")#this is so basic we might need to remove it 
    st.write("2.Stock Market Visulization App")
    st.write("3.QA Learning Journey")
    
    st.header("contact")#call logo add
    email=("manvendrasinghkhangarot666@gmail.com")
    linkedin=("manvendrasingh")
    
    
    st.success("thank you for visiting my portfolio")
    

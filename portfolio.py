import streamlit as st

st.set_page_config(
    page_title="Manvendra's Portfolio",
    page_icon="💻",
    layout="wide"
)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpg", width=220)

with col2:
    st.title("Manvendra Singh")
    st.subheader("Aspiring QA Automation Engineer | Python Developer")

    st.write("📍 Jaipur, Rajasthan")
    st.write("🏢 Currently working at Genpact")
    st.write("🎓 BCA Student (IGNOU)")
    # Your profile section


st.write("🚀 Passionate about QA Automation and Software Development")
st.write("📚 Learning Python, Streamlit, Git & GitHub")

st.markdown("---")
# Skills section

st.markdown("## Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("🧪 QA Testing")

with col3:
    st.info("⚡ Streamlit")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🔧 Git & GitHub")

with col2:
    st.info("🌐 Web Development")

with col3:
    st.info("📊 Excel")

st.markdown("---")

st.markdown("## 🏆 Certifications")

st.success("📜 Python Programming")
st.success("📜 QA Testing Fundamentals")
st.success("📜 Microsoft Excel")

# PASTE PROJECTS HERE
st.markdown("## 🚀 Projects")

st.info("🧮 Python Calculator")
st.write("A calculator built using Python functions and user input.")

st.info("🌐 Portfolio Website")
st.write("Personal portfolio created using Streamlit and Python.")

st.info("📊 Excel Dashboard")
st.write("Data analysis and reporting using Microsoft Excel.")

st.link_button(
    "🧮 Python Calculator",
    "YOUR_GITHUB_PROJECT_LINK"
)
st.link_button(
    "🌐 Portfolio Website",
    "YOUR_GITHUB_PROJECT_LINK")

st.write("## ☎ Contact Me")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/mandata-manvendra-singh-khangarot-737691429")

with col2:
    st.link_button("💻 GitHub", "https://github.com/manvendrasinghkhangarot062-ctrl")

with col3:
    st.link_button("📧 Email", "mailto:manvendrasinghkhangarot666@gmail.com")

with col4:
    with open("Manvendra CV.pdf", "rb") as pdf_file:
        st.download_button(
            "📄 Resume",
            pdf_file,
            file_name="Manvendra_Singh_Resume.pdf",
            mime="application/pdf"
        )



("""Thank you for visiting my portfolio!""")
    



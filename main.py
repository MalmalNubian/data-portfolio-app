import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Portfolio Site",
    page_icon=":mortar_board:",
    layout="wide",
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with open("styles.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


lottie_coder = load_lottieurl("https://lottie.host/a6f74205-1506-4c02-b1d9-76d90d99a086/D2TfP5ttRw.json")
lottie_aviation = load_lottieurl("https://lottie.host/26e9a562-5943-4767-9482-88546515cc8e/VcDT8TOk8f.json")
lottie_education = load_lottieurl("https://lottie.host/d50e0cec-1bdd-4233-91d5-d0f3e7232fc7/2YeGZsA4oH.json")
lottie_skills = load_lottieurl("https://lottie.host/42cb0da6-0b08-46bd-8851-49174f18254a/mlRIgfCRO3.json")
lottie_contact= load_lottieurl("https://lottie.host/667787ff-95f3-4eed-aae0-0481c3f46ef8/nOPzrgZbmB.json")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal',
        styles={
        "container": {"padding": "0!important", "background-color": "#f0f4f8"},
        "icon": {"color": "#003366", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#53A9AF"},
        }
        )

    st.markdown("<br>", unsafe_allow_html=True)


if selected == 'About':
  gap_size = "large"
  with st.container():
    col1, col2 = st.columns([1, 1], gap=gap_size)


    with col1:
      st.write("Who am I?")
      st.title("Hi :wave: I am Yasmin")
      st.subheader("""
      I am data scientist passionate about leveraging data to solve business problems and make informed decisions.
      """)
      st_lottie(lottie_coder, height=300)
      
    with col2:
      st.write("Journey to Data Science")
      st.title("From Aviation to Data")
      st.subheader("""
      Transitioned from aviation underwriting, where I specialized in risk analysis and risk mitigation, to data science.
      """)
      st_lottie(lottie_aviation, height=300) 

  st.markdown("<br><br>", unsafe_allow_html=True)



  with st.container():
    col1, col2 = st.columns([1, 1], gap=gap_size)
    
    with col1:
      st.write("Educational Background")
      st.title("Path of Learning")
      st.subheader("""
      Holding an Economics degree and an MBA, I've enhanced my education with a software engineering bootcamp and a data science course through continuous self-learning.
      """)
      st_lottie(lottie_education, height=350)
    
    with col2:
      st.write("Skills and Tools")
      st.title("Toolkit of a Data Scientist")
      st.subheader("""
      In my data science journey, I've become proficient in analysis, visualization, and machine learning, acquiring the following key skills:
      - Languages, tools and Frameworks: Python, CSS, JavaScript, Node.js, Streamlit
      - Data Analysis: Pandas, NumPy
      - Visualization: Matplotlib, Plotly, Seaborn,
      - Machine Learning: Scikit-learn
      - Version Control: GitHub
      """)
      st_lottie(lottie_skills, height=250)



if selected == "Projects":
    with st.container():
      st.title("Predicting Emotions")
      st.write("""
               Welcome to the 'Emotions' dataset – a collection of English Twitter messages meticulously annotated with six fundamental emotions: 
                **anger, fear, joy, love, sadness,** and **surprise**. 
                Can we accurately predict the emotion of a tweet based on its content? 
                *Give it a try!*
                """)
    st.markdown("[Visit Streamlit page](https://emotion-analysis6.streamlit.app/) | [Visit Github repo](https://github.com/MalmalNubian/emotion-analysis)", unsafe_allow_html=True)


if selected == "Contact":
    st.header("Get in touch!")
    st.markdown("<br>", unsafe_allow_html=True)

    contact_form = """
    <form action="https://formsubmit.co/y.adan@hotmail.co.uk" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="URL_to_redirect_after_submission">
      <input type="hidden" name="_template" value="plain">
      <input type="text" name="name" placeholder="Your name" required>
      <input type="email" name="email" placeholder="Your email" required>
      <textarea name="message" placeholder="Your message" required></textarea>
      <button type="submit">Send</button>
    </form>
    """


    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact, height=300)

    if st.session_state.get('form_submitted', False):
        st.success("Your message has been sent successfully!")

    footer = """
      <div class="footer">
      <p>Connect with me on:</p>
      <a href='https://www.linkedin.com/in/yasmin-adan-22a5a734/' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'></a>
      &nbsp;
      <a href='https://github.com/MalmalNubian' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' width='25' height='25'></a>
      &nbsp;
      <br>
      <br>
      <p>© 2024 by Yasmin. All rights reserved.</p>
      </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
    


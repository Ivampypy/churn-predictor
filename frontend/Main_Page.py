import streamlit as st
import requests

st.set_page_config("AI Churn Predictor", page_icon="frontend/image.png", layout="wide")


custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    @keyframes slideUpFade {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    

    div[data-testid="stMetric"] {
        animation: slideUpFade 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    

    div[data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.6s; }
    div[data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.9s; }
    div[data-testid="stMetric"]:nth-of-type(3) { animation-delay: 1.2s; }


    div[data-testid="stAlert"] {
        animation: slideUpFade 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        animation-delay: 1.8s; /* Появляются почти через 2 секунды */
    }
    

    .hero-section {
        animation: slideUpFade 1.2s ease-out forwards;
        animation-delay: 0.2s;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)


st.markdown(
    """
<div class="hero-section" style="background-color: #1E1E2E; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
    <h1 style="color: white; margin: 0;"> AI Retention System</h1>
    <p style="color: #a0a0a0; font-size: 18px; margin-top: 10px;">
        Predicting customer churn using PyTorch and generating retention offers with LLM
    </p>
</div>
""",
    unsafe_allow_html=True,
)


ACCENTS = {
    "Teal": "#0F8B8D",
    "Indigo": "#5B6CFF",
    "Amber": "#D99A1E",
    "Rose": "#D6456B",
}


def api_is_up(url):
    try:
        return requests.get(url.rstrip("/") + "/docs", timeout=2).status_code < 500
    except requests.exceptions.RequestException:
        return False


with st.sidebar:
    st.header("Settings")

    accent_name = st.selectbox("Accent color", list(ACCENTS))
    animations = st.toggle("Animations", value=True)

    st.subheader("Sections")
    show_flow = st.checkbox("Prediction pipeline", value=True)
    show_metrics = st.checkbox("Model performance", value=True)
    show_pages = st.checkbox("Where to start", value=True)

    st.subheader("Backend")
    api_url = st.text_input("API address", "http://127.0.0.1:8000")
    if st.button("Check connection"):
        st.session_state["api_up"] = api_is_up(api_url)

    api_state = st.session_state.get("api_up")
    if api_state is True:
        st.success("API is reachable")
    elif api_state is False:
        st.error("API is not reachable")

accent = ACCENTS[accent_name]

page_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp {{
    font-family: 'Public Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
}}

.hero-section {{
    box-shadow: inset 0 -4px 0 {accent};
}}

.section-title {{
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    margin: 2.2rem 0 0.3rem 0;
}}
.section-note {{
    opacity: 0.68;
    margin: 0 0 1.1rem 0;
    max-width: 62ch;
}}

.flow {{
    display: flex;
    gap: 0;
    align-items: stretch;
    flex-wrap: wrap;
}}
.flow .node {{
    position: relative;
    flex: 1 1 190px;
    min-width: 190px;
    padding: 1.1rem 1.3rem 1.2rem 1.3rem;
    background: rgba(128, 128, 128, 0.08);
    border-top: 4px solid {accent};
    margin-right: 26px;
}}
.flow .node:last-child {{
    margin-right: 0;
}}
.flow .node:not(:last-child)::after {{
    content: "";
    position: absolute;
    right: -26px;
    top: 50%;
    width: 26px;
    height: 2px;
    background: {accent};
}}
.flow .node:not(:last-child)::before {{
    content: "";
    position: absolute;
    right: -26px;
    top: calc(50% - 4px);
    border-left: 8px solid {accent};
    border-top: 5px solid transparent;
    border-bottom: 5px solid transparent;
}}
.flow .tech {{
    font-size: 0.85rem;
    font-weight: 600;
    color: {accent};
}}
.flow .name {{
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0.15rem 0 0.35rem 0;
}}
.flow .what {{
    font-size: 0.93rem;
    opacity: 0.75;
    line-height: 1.45;
}}

div[data-testid="stMetric"] {{
    background: rgba(128, 128, 128, 0.08);
    border-left: 4px solid {accent};
    padding: 1rem 1.3rem;
    border-radius: 4px;
}}
div[data-testid="stMetricValue"] {{
    font-weight: 700;
}}

.start {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.2rem;
}}
.start .card {{
    padding: 1.2rem 1.4rem;
    border: 1px solid rgba(128, 128, 128, 0.28);
    border-radius: 6px;
}}
.start .card b {{
    display: block;
    font-size: 1.05rem;
    margin-bottom: 0.3rem;
}}
.start .card span {{
    opacity: 0.75;
    line-height: 1.5;
}}
</style>
"""
st.markdown(page_css, unsafe_allow_html=True)

if not animations:
    st.markdown(
        "<style>*, *::before, *::after {animation: none !important; transition: none !important;}</style>",
        unsafe_allow_html=True,
    )

if show_flow:
    st.markdown(
        """
<div class="section-title">How a prediction is made</div>
<p class="section-note">A customer record travels through four stages, from the form to a written retention plan.</p>
<div class="flow">
    <div class="node">
        <div class="tech">Streamlit</div>
        <div class="name">Customer form</div>
        <div class="what">You enter the account details and services of one customer.</div>
    </div>
    <div class="node">
        <div class="tech">FastAPI</div>
        <div class="name">Scoring service</div>
        <div class="what">Receives the record and prepares it for the model.</div>
    </div>
    <div class="node">
        <div class="tech">PyTorch MLP</div>
        <div class="name">Churn model</div>
        <div class="what">Returns the probability that the customer leaves.</div>
    </div>
    <div class="node">
        <div class="tech">LLM via OpenRouter</div>
        <div class="name">Strategy agent</div>
        <div class="what">Turns the profile and score into a retention plan.</div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

if show_metrics:
    st.markdown(
        """
<div class="section-title">Model performance</div>
<p class="section-note">Recall is the share of customers who really left that the model caught.</p>
""",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Accuracy", value="76.5%")
    col2.metric("Recall", "61.5%")
    col3.metric("F1", "0.58")

if show_pages:
    st.markdown(
        """
<div class="section-title">Where to start</div>
<p class="section-note">Use the page list at the top of the sidebar to move between the steps.</p>
<div class="start">
    <div class="card">
        <b>Prediction</b>
        <span>Fill in a customer profile and get the churn probability.</span>
    </div>
    <div class="card">
        <b>Agent</b>
        <span>After a prediction, ask the LLM for a retention strategy for that customer.</span>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
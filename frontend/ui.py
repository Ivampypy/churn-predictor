import streamlit as st
 
HIGH_RISK = "#B3261E"
LOW_RISK = "#1F7A6B"
 
_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&display=swap');
 
html, body, [class*="css"], .stApp {
    font-family: 'Public Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
}
#MainMenu, footer {visibility: hidden;}
 
.page-title { margin: 0 0 0.25rem 0; font-size: 2.1rem; font-weight: 700; letter-spacing: -0.02em; }
.page-sub   { margin: 0 0 1.5rem 0; font-size: 1.05rem; opacity: 0.72; max-width: 60ch; }
 
@media (prefers-reduced-motion: no-preference) {
    .page-title.enter { animation: rise 0.9s cubic-bezier(0.16, 1, 0.3, 1) both; }
    @keyframes rise { from {opacity: 0; transform: translateY(24px);} to {opacity: 1; transform: none;} }
}
 
.risk {
    border-left: 6px solid var(--accent);
    background: #FFFFFF;
    padding: 1.1rem 1.4rem;
    border-radius: 4px;
    margin: 1rem 0 0.5rem 0;
}
.risk .value  { font-size: 3rem; font-weight: 700; line-height: 1; color: var(--accent); }
.risk .verdict { font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem; }
.risk .detail  { opacity: 0.7; margin-top: 0.15rem; }
.risk .bar     { height: 8px; background: #E3E8EA; border-radius: 4px; margin-top: 0.9rem; overflow: hidden; }
.risk .bar > div { height: 100%; background: var(--accent); }
 
.step { border-top: 3px solid #0F6E6E; padding-top: 0.6rem; }
.step b { display: block; margin-bottom: 0.2rem; }
.step span { opacity: 0.72; font-size: 0.95rem; }
</style>
"""
 
 
def inject_theme() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)
 
 
def setup_page(title: str, subtitle: str, animate: bool = False) -> None:
    inject_theme()
    cls = "page-title enter" if animate else "page-title"
    st.markdown(
        f'<h1 class="{cls}">{title}</h1><p class="page-sub">{subtitle}</p>',
        unsafe_allow_html=True,
    )
 
 
def risk_card(probability: float, will_churn: bool) -> None:
    accent = HIGH_RISK if will_churn else LOW_RISK
    verdict = "High risk of leaving" if will_churn else "Likely to stay"
    detail = (
        "Plan a retention offer for this customer."
        if will_churn
        else "No urgent action needed. Keep the relationship healthy."
    )
    pct = max(0.0, min(probability * 100, 100.0))
    st.markdown(
        f"""
        <div class="risk" style="--accent: {accent};">
            <div class="value">{pct:.1f}%</div>
            <div class="verdict">{verdict}</div>
            <div class="detail">{detail}</div>
            <div class="bar"><div style="width: {pct:.1f}%;"></div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
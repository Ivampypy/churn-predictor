import streamlit as st


st.set_page_config('AI Churn Predictor', page_icon='frontend/image.png',layout='wide')

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #1E1E2E; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
    <h1 style="color: white; margin: 0;"> AI Retention System</h1>
    <p style="color: #a0a0a0; font-size: 18px; margin-top: 10px;">
        Predicting customer churn using PyTorch and generating retention offers with LLM
    </p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3=st.columns(3)

c2.subheader("📊 Metrics of model")

col1,col2,col3=st.columns(3)

col1.metric(label='Accuracy',value='76.5%')
col2.metric(
    'Recall','61.5%'
)
col3.metric('F1','0.58')

st.divider()

a,b,c,d=st.columns(4)

with a:
    st.info('Frontend\n\nStreamlit')

with b:
    st.success('Backend\n\nFastAPI')

with c:
    st.warning('MLP Model\n\nPyTorch')

with d:
    st.error('LLM agent\n\nLLM(GPT)')
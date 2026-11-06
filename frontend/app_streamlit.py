import streamlit as st


st.set_page_config('AI Churn Predictor', page_icon='frontend/image.png', layout='wide')


custom_css = """
    <style>
    /* Скрываем лишнее */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Ключевые кадры для эффекта выезда снизу */
    @keyframes slideUpFade {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Анимация для карточек с метриками - теперь длится 1.5 секунды */
    div[data-testid="stMetric"] {
        animation: slideUpFade 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    /* Увеличенные каскадные задержки (выезжают с большим интервалом) */
    div[data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.6s; }
    div[data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.9s; }
    div[data-testid="stMetric"]:nth-of-type(3) { animation-delay: 1.2s; }

    /* Анимация для цветных блоков архитектуры - выезжают в самом конце */
    div[data-testid="stAlert"] {
        animation: slideUpFade 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        animation-delay: 1.8s; /* Появляются почти через 2 секунды */
    }
    
    /* Плавное появление шапки */
    .hero-section {
        animation: slideUpFade 1.2s ease-out forwards;
        animation-delay: 0.2s;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)


st.markdown("""
<div class="hero-section" style="background-color: #1E1E2E; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
    <h1 style="color: white; margin: 0;"> AI Retention System</h1>
    <p style="color: #a0a0a0; font-size: 18px; margin-top: 10px;">
        Predicting customer churn using PyTorch and generating retention offers with LLM
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c2.subheader(" Metrics of model")

# 5. Сами метрики
col1, col2, col3 = st.columns(3)
col1.metric(label='Accuracy', value='76.5%')
col2.metric('Recall', '61.5%')
col3.metric('F1', '0.58')

st.divider()


a, b, c, d = st.columns(4)

with a:
    st.info('Frontend\n\nStreamlit')

with b:
    st.success('Backend\n\nFastAPI')

with c:
    st.warning('MLP Model\n\nPyTorch')

with d:
    st.error('LLM agent\n\nLLM(GPT)')
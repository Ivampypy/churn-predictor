from openai import OpenAI
import streamlit as st

st.subheader('AI Strategy Adviser Powered by LLM')

client_data=st.session_state.get('client_data')
probs=st.session_state.get('probability')




api_key=st.secrets['OPENROUTER_API_KEY']

client=OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

if probs is None or client_data is None:
    st.warning('Firstly do predictions on predictions page!')
    st.stop()


st.write(f"Probability of leaving: {probs*100:.2f}%")

with st.expander("Get client's data"):
    st.json(client_data)

generate_bttn=st.button('Click to generate the strategy')
if generate_bttn:
    formed_client_data='\n'.join([f'-{k}: {v}' for k,v in client_data.items()])


    prompt=f'Imagine that you are marketing specialist with a huge amount of experience in these sphere.\
        Customer of our company passed the questionarre which i am representing to you in a list of strings.\
            Here it is: {formed_client_data}. I calculated\
            the probability of leaving this customer from our products. Here it is: {probs*100:.1f}%.\
            So, if the prob is quite close to 35 (about 1-2%), come up to me with the idea how to decrease this number,\
            and if it is higher than 35, tell me what to do to save the customer. Your response should be not so big,\
            but informative and clear.'

    with st.spinner('Agent is analyzing the request...'):
        try:
            response=client.chat.completions.create(
                model='nvidia/nemotron-3.5-super-vl:free',
                messages=[
                    {'role':'user','content': prompt}
                    ]
            )

            st.divider()
            st.info(response.choices[0].message.content)
        except Exception as e:
            st.error(f'Error occured: {e}')


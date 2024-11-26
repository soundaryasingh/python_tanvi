import streamlit as st
import pickle

# load model
model = pickle.load(open('sentiment3.pkl', 'rb'))

# create title
st.title('Flipkart Review ⭐⭐⭐⭐⭐')

review = st.text_input('Enter your review:')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive Review🥰')
    elif prediction[0] == 'negative':
        st.success('negative Review😨')
    else:
        st.success('Review not eligble')

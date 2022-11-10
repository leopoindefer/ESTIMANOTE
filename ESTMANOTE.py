import streamlit as st
import pickle as pkle  
import math

st.set_page_config(
    page_title="ESTIMANOTE",
    page_icon="💯",
)

st.title("Estimez vos notes")

hide_st_style = """
            <style>
            #MainMenu {Visibility: hidden;}
            footer {visibility: hidden;}
            .bouton {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True) 

st.header("Matière dont la note est connu")

col1, col2, col3 = st.columns(3)

with col1:
    matiere1 = st.text_input('1ere matière connu')
    matiere2 = st.text_input('2eme matière connu')
                    
with col2:
    coef1 = st.number_input('1er coefficient', 1, 20)
    coef2 = st.number_input('2eme coefficient', 1, 20)
                    
with col3:
    note1 = st.slider('1ere note', 0, 20, 10)
    note2 = st.slider('2eme note', 0, 20, 10)

if st.button('Ajouter une matière'):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        matiere3 = st.text_input('1ere matière connu')
                            
    with col2:
        coef3 = st.number_input('1er coefficient', 1, 20)
                            
    with col3:
        note3 = st.slider('1ere note', 0, 20, 10)

else:
    st.write("hey")

st.header("Matière dont la note est à estimer")

col1, col2 = st.columns(2)

with col1:
    matierex = st.text_input('1er matière dont la note à estimer')
                    
with col2:
    coefx = st.number_input('Coefficient de la note à estimer', 1, 20)

resultat = (((10 * (coef1 + coefx)) - (note1 * coef1)) / coefx)
resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

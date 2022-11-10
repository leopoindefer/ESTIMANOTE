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

st.header("Combien de matière dont les notes sont connus avez-vous ?")
matiereavecnote = st.number_input('Nombre de matière dont les notes sont connus', 1, 10)

st.header("Combien de matière dont les notes sont à estimer avez-vous ?")
matieresansnote = st.number_input('Nombre de matière dont la/les note/s sont à estimer', 1, 5)

if matiereavecnote == 2:

    st.header("Matière dont la note est connu")

    col1, col2, col3 = st.columns(3)

    with col1:
        matiere1 = st.text_input('Nom de la matière connu')
                    
    with col2:
        coef1 = st.number_input('Son coefficient', 1, 20)
                    
    with col3:
        note1 = st.slider('Votre note', 0, 20, 10)

    st.header("Matière dont la note est à estimer")

    col1, col2 = st.columns(2)

    with col1:
        matierex = st.text_input('1er matière dont la note à estimer')
                    
    with col2:
        coefx = st.number_input('Coefficient de la note à estimer', 1, 20)

    resultat = (((10 * (coef1 + coefx)) - (note1 * coef1)) / coefx)
    resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
    st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 3:
    if matieresansnote == 1:
        
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
                    
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient2', 1, 20)
                    
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                    
        with col2:
            coefx = st.number_input('Son coefficient', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coefx)) - (note1 * coef1) - (note2 * coef2)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2 :
        st.header("Matière dont la note est connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('Votre matière')
                    
        with col2:
            coef1 = st.number_input('Son coefficient', 1, 20)
                    
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)

        st.header("Matière dont les notes est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                    
        with col2:
            coefx = st.number_input('1er coefficient', 1, 20)
            coefy = st.number_input('2eme coefficient', 1, 20)

        resultat = ((((10 * (coef1 + coefx + coefy)) - (note1 * coef1)) / coefx + coefy)/2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    else:
        st.write("2 notes à estimer maximum")    

elif matiereavecnote == 4:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matiere')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('Son coefficient', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coefx + coefy + coefz)) - (note1 * coef1)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex},en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 5:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coefx + coefy + coefz + coefw)) - (note1 * coef1)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 6:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coefx + coefy + coefz + coefw)) - (note1 * coef1) - (note2 * coef2)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 7:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coefx + coefy + coefz + coefw)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 8:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)
            
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7+ coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coefx + coefy + coefz + coefw)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 9:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
            matiere8 = st.text_input('8eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
            coef8 = st.number_input('8eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)
            note8 = st.slider('8eme note', 0, 20, 10)
            
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7 + coef8 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7) - (note8 * coef8)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coefx + coefy + coefz + coefw)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

elif matiereavecnote == 10:
    if matieresansnote == 1:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
            matiere8 = st.text_input('8eme matière')
            matiere9 = st.text_input('9eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
            coef8 = st.number_input('8eme coefficient', 1, 20)
            coef9 = st.number_input('9eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)
            note8 = st.slider('8eme note', 0, 20, 10)
            note9 = st.slider('9eme note', 0, 20, 10)
            
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)

        resultat = (((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7 + coef8 + coef9 + coefx)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7) - (note8 * coef8) - (note9 * coef9)) / coefx)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} doit être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 2:
    
        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
            matiere8 = st.text_input('8eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
            coef8 = st.number_input('8eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)
            note8 = st.slider('8eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7 + coef8 + coefx + coefy)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7) - (note8 * coef8)) / coefx + coefy) / 2)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex} et en {matierey} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 3:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
            matiere7 = st.text_input('7eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
            coef7 = st.number_input('7eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)
            note7 = st.slider('7eme note', 0, 20, 10)
 
        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coef7 + coefx + coefy + coefz)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6) - (note7 * coef7)) / coefx + coefy + coefz) / 3)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey} et en {matierez} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

    elif matieresansnote == 4:

        st.header("Matière dont les notes sont connus")

        col1, col2, col3 = st.columns(3)

        with col1:
            matiere1 = st.text_input('1ere matière')
            matiere2 = st.text_input('2eme matière')
            matiere3 = st.text_input('3eme matière')
            matiere4 = st.text_input('4eme matière')
            matiere5 = st.text_input('5eme matière')
            matiere6 = st.text_input('6eme matière')
                        
        with col2:
            coef1 = st.number_input('1er coefficient', 1, 20)
            coef2 = st.number_input('2eme coefficient', 1, 20)
            coef3 = st.number_input('3eme coefficient', 1, 20)
            coef4 = st.number_input('4eme coefficient', 1, 20)
            coef5 = st.number_input('5eme coefficient', 1, 20)
            coef6 = st.number_input('6eme coefficient', 1, 20)
                            
        with col3:
            note1 = st.slider('1ere note', 0, 20, 10)
            note2 = st.slider('2eme note', 0, 20, 10)
            note3 = st.slider('3eme note', 0, 20, 10)
            note4 = st.slider('4eme note', 0, 20, 10)
            note5 = st.slider('5eme note', 0, 20, 10)
            note6 = st.slider('6eme note', 0, 20, 10)

        st.header("Matière dont la note est à estimer")

        col1, col2 = st.columns(2)

        with col1:
            matierex = st.text_input('1ere matière dont la note est à estimer')
            matierey = st.text_input('2eme matière dont la note est à estimer')
            matierez = st.text_input('3eme matière dont la note est à estimer')
            matierew = st.text_input('4eme matière dont la note est à estimer')
                            
        with col2:
            coefx = st.number_input('1er coefficient dont la note est à estimer', 1, 20)
            coefy = st.number_input('2eme coefficient dont la note est à estimer', 1, 20)
            coefz = st.number_input('3eme coefficient dont la note est à estimer', 1, 20)
            coefw = st.number_input('4eme coefficient dont la note est à estimer', 1, 20)

        resultat = ((((10 * (coef1 + coef2 + coef3 + coef4 + coef5 + coef6 + coefx + coefy + coefz + coefw)) - (note1 * coef1) - (note2 * coef2) - (note3 * coef3) - (note4 * coef4) - (note5 * coef5) - (note6 * coef6)) / coefx + coefy + coefz + coefw) / 4)
        resultat = f'<span style="color: #7DCEA0;">{math.ceil(resultat)}</span>'
        st.write(f'### Ta note en {matierex}, en {matierey},en {matierez} et en {matierew} doivent être de {resultat} pour avoir une moyenne générale de 10/20', unsafe_allow_html=True)

else:
    st.write("Veuillez indiquer le nombre de matière")

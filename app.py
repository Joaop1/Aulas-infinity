import datetime

import streamlit as st
import _datetime
st.title("Média de notas")
choice_quant = int(st.number_input("Informe o número de alunos: "))


x = datetime.datetime.now()
st.write(x)


# cont = 1
#
#
# while cont < 5:
#     choice2 = st.text_input("Informe o nome do aluno: ")
#     choice_n1 = st.number_input("Informe a primeira nota: ")
#     choice_n2 = st.number_input("Informe a segunda nota: ")
#     choice_n3 = st.number_input("Informe a terceira nota: ")
#     media = (choice_n1 + choice_n2 + choice_n3)/3
#     st.write(f"{choice} | {choice_n1} | {choice_n2} | {choice_n3} | {media}")
#     cont+=1




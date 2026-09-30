import streamlit as st
from service import Service
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            Service.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
<<<<<<< HEAD:project/templates/abrircontaui.py
            st.rerun
=======
            st.rerun()
>>>>>>> 31c8cc3b7314c0a3b2278132d4836a676cd99c5b:projeto/template/abrircontaui.py

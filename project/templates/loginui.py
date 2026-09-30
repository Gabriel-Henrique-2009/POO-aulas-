import streamlit as st
from service import Service

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = Service.cliente_autenticar(email, senha)
<<<<<<< HEAD:project/templates/loginui.py
            if c != None:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = "cliente"
                st.rerun()
 
            p = Service.profissional_autenticar(email, senha)
            if p != None:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["usuario_tipo"] = "profissional"
                st.rerun()
 
            if c == None and p == None: st.write("E-mail ou senha inválidos")
=======
            if c == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.rerun()
                
>>>>>>> 31c8cc3b7314c0a3b2278132d4836a676cd99c5b:projeto/template/loginui.py

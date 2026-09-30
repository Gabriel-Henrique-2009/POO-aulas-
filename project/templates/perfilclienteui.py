import streamlit as st
from service import Service
import time
<<<<<<< HEAD:project/templates/perfilclienteui.py
=======

>>>>>>> 31c8cc3b7314c0a3b2278132d4836a676cd99c5b:projeto/template/perfilclienteui.py
class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
<<<<<<< HEAD:project/templates/perfilclienteui.py
        nome = st.text_input("informe o novo nome", op.get_nome())
        email = st.text_input("informe o novo email", op.get_email())
        fone = st.text_input("informe o novo fone", op.get_fone())
        senha = st.text_input("informe a nova senha", op.get_senha(), type="password")
=======
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
>>>>>>> 31c8cc3b7314c0a3b2278132d4836a676cd99c5b:projeto/template/perfilclienteui.py
        if st.button("Atualizar"):
            id = op.get_id()
            Service.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()
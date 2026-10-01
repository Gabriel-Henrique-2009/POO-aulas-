import streamlit as st
import time
from service import Service

class AlterarSenhaUI:
    @staticmethod
    def main():
        st.header("Alterar Senha")
        
        nova_senha = st.text_input("Informe a nova senha", type="password")
        confirmar_senha = st.text_input("Confirme a nova senha", type="password")

        if st.button("Alterar Senha"):
            if nova_senha != confirmar_senha:
                st.error("As senhas não coincidem!")
            elif not nova_senha.strip():
                st.error("A senha não pode estar em branco!")
            else:
                id_admin = st.session_state["usuario_id"]
                Service.admin_alterar_senha(id_admin, nova_senha)
                st.success("Senha alterada com sucesso!")
                time.sleep(1.5)
                st.rerun()
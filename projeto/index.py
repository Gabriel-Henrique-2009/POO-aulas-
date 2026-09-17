from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
from template.manteratendimentoui import ManterAtendimentoUI
from template.abrircontaui import AbrirContaUI
from template.loginui import LoginUI
from template.perfilclienteui import PerfilClienteUI

from service import Service
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Atendimentos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()
from aulas_e_exercicios.projeto_2.templates.manterclienteui import ManterClienteUI
from aulas_e_exercicios.projeto_2.templates.manterservicoui import ManterServicoUI
from aulas_e_exercicios.projeto_2.templates.manterhorarioui import ManterHorarioUI
from aulas_e_exercicios.projeto_2.templates.manterprofissionalui import ManterProfissionalUI
from aulas_e_exercicios.projeto_2.templates.manteratendimentoui import ManterAtendimentoUI
from aulas_e_exercicios.projeto_2.templates.abrircontaui import AbrirContaUI
from aulas_e_exercicios.projeto_2.templates.loginui import LoginUI
from aulas_e_exercicios.projeto_2.templates.perfilclienteui import PerfilClienteUI
from aulas_e_exercicios.projeto_2.templates.perfilprofissionalui import PerfilProfissionalUI
from aulas_e_exercicios.projeto_2.templates.agendarservicoui import AgendarServicoUI
from aulas_e_exercicios.projeto_2.templates.abrirminhaagendaui import AbrirMinhaAgendaUI
from aulas_e_exercicios.projeto_2.templates.visualizarmeusservicosui import VisualizarMeusServicosUI
from aulas_e_exercicios.projeto_2.templates.visualizarminhaagendaui import VisualizarMinhaAgendaUI
from aulas_e_exercicios.projeto_2.templates.confirmarservicoui import ConfirmarServicoUI

from aulas_e_exercicios.projeto_2.service import Service
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": VisualizarMeusServicosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirMinhaAgendaUI.main()
        if op == "Minha Agenda": VisualizarMinhaAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
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
            else: 
                if st.session_state["usuario_tipo"] == "cliente": IndexUI.menu_cliente()
                else: IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()
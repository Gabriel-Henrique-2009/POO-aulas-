import streamlit as st
from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
from templates.agendarservicoui import AgendarServicoUI
from templates.abrirminhaagendaui import AbrirMinhaAgendaUI
from templates.visualizarminhaagendaui import VisualizarMinhaAgendaUI
from templates.visualizarmeusservicosui import VisualizarMeusServicosUI
from templates.confirmarservicoui import ConfirmarServicoUI
from templates.alterarsenhaui import AlterarSenhaUI
from service import Service

class IndexUI:

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        elif op == "Abrir Conta":
            AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Visualizar Meus Serviços"])
        if op == "Meus Dados":
            PerfilClienteUI.main()
        elif op == "Agendar Serviço":
            AgendarServicoUI.main()
        elif op == "Visualizar Meus Serviços":
            VisualizarMeusServicosUI.main()

    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Visualizar Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados":
            PerfilProfissionalUI.main()
        elif op == "Abrir Minha Agenda":
            AbrirMinhaAgendaUI.main()
        elif op == "Visualizar Minha Agenda":
            VisualizarMinhaAgendaUI.main()
        elif op == "Confirmar Serviço":
            ConfirmarServicoUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Alterar Senha"])
        if op == "Clientes":
            ManterClienteUI.main()
        elif op == "Serviços":
            ManterServicoUI.main()
        elif op == "Horários":
            ManterHorarioUI.main()
        elif op == "Profissionais":
            ManterProfissionalUI.main()
        elif op == "Atendimentos":
            ManterAtendimentoUI.main()
        elif op == "Alterar Senha":
            AlterarSenhaUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            st.session_state.clear()
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write(f"Bem-vindo(a), {st.session_state.get('usuario_nome', '')}")
            if st.session_state.get("usuario_nome") == "admin":
                IndexUI.menu_admin()
            else:
                if st.session_state.get("usuario_tipo") == "cliente":
                    IndexUI.menu_cliente()
                else:
                    IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()
        

if __name__ == "__main__":
    IndexUI.main()
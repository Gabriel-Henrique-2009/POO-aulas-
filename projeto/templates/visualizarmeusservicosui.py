import streamlit as st
import pandas as pd
from service import Service

class VisualizarMeusServicosUI:
    def main():
        st.header("Meus Serviços")
        id_cliente = st.session_state["usuario_id"]
        servicos = Service.horario_listar_servicos_cliente(id_cliente)
        
        if len(servicos) == 0:
            st.write("Nenhum serviço agendado ou realizado.")
        else:
            df = pd.DataFrame(servicos)
            st.dataframe(df)
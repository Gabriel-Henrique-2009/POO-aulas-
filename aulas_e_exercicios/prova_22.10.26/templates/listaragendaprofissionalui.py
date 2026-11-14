import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaProfissionalUI:
    @staticmethod
    def main():
        st.header("Agenda do Profissional")        
        profissionais = Service.profissional_listar()        
        if len(profissionais) == 0:
            st.warning("Nenhum profissional cadastrado no sistema.")
            return

        dic_profissional = {f"{p.get_id()} - {p.get_nome()}": p.get_id() for p in profissionais}
        selecionado = st.selectbox("Selecione o Profissional", list(dic_profissional.keys()))
        
        if selecionado:
            id_prof = dic_profissional[selecionado]
            agenda = Service.horario_listar_agenda_profissional_admin(id_prof)
            
            if len(agenda) == 0:
                st.info("Nenhum horário cadastrado na agenda deste profissional.")
            else:
                df = pd.DataFrame(agenda)
                st.dataframe(df)
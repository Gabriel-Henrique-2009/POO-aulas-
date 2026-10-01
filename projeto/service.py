from datetime import datetime, timedelta
from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

class Service:
    # --- TAREFA 1: ABRIR MINHA AGENDA ---
    @staticmethod
    def horario_abrir_minha_agenda(data, horario_inicio, horario_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(data + " " + horario_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(data + " " + horario_fim, "%d/%m/%Y %H:%M")
        delta = timedelta(minutes=int(intervalo))
        
        x = data_inicio
        while x <= data_fim:
            Service.horario_inserir(x, False, None, None, id_profissional)
            x += delta

    # --- TAREFA 2: VISUALIZAR MINHA AGENDA (PROFISSIONAL) ---
    @staticmethod
    def horario_listar_agenda_profissional(id_profissional):
        agenda = []
        todos_horarios = Service.horario_listar()
        
        for h in todos_horarios:
            if h.get_id_profissional() == id_profissional:
                cliente = Service.cliente_listar_id(h.get_id_cliente()) if h.get_id_cliente() else None
                servico = Service.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
                
                agenda.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%Y-%m-%d %H:%M:%S") if isinstance(h.get_data(), datetime) else str(h.get_data()),
                    "confirmado": h.get_confirmado(),
                    "cliente": cliente.get_nome() if cliente else "Nenhum",
                    "servico": servico.get_descricao() if servico else "Nenhum"
                })
        return agenda

    # --- TAREFA 3: VISUALIZAR MEUS SERVIÇOS (CLIENTE) ---
    @staticmethod
    def horario_listar_servicos_cliente(id_cliente):
        servicos = []
        todos_horarios = Service.horario_listar()
        
        for h in todos_horarios:
            if h.get_id_cliente() == id_cliente:
                profissional = Service.profissional_listar_id(h.get_id_profissional()) if h.get_id_profissional() else None
                servico = Service.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
                
                servicos.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%Y-%m-%d %H:%M:%S") if isinstance(h.get_data(), datetime) else str(h.get_data()),
                    "confirmado": h.get_confirmado(),
                    "servico": servico.get_descricao() if servico else "Não definido",
                    "profissional": profissional.get_nome() if profissional else "Não definido"
                })
        return servicos

    # --- TAREFA 4: CONFIRMAR SERVIÇO (PROFISSIONAL) ---
    @staticmethod
    def horario_listar_pendentes_profissional(id_profissional):
        horarios = Service.horario_listar()
        return [
            h for h in horarios 
            if h.get_id_profissional() == id_profissional 
            and h.get_id_cliente() is not None 
            and not h.get_confirmado()
        ]

    @staticmethod
    def horario_confirmar(id_horario):
        h = Service.horario_listar_id(id_horario)
        if h:
            h.set_confirmado(True)
            HorarioDAO().atualizar(h)

    # --- TAREFA 5: ALTERAR SENHA (ADMIN) ---
    @staticmethod
    def admin_alterar_senha(id_admin, nova_senha):
        admin = Service.cliente_listar_id(id_admin)
        if admin and admin.get_email() == "admin":
            admin.set_senha(nova_senha)
            ClienteDAO().atualizar(admin)
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
    # --- MÉTODOS DE CLIENTE ---
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(c)

    @staticmethod
    def cliente_criar_admin():
        clientes = Service.cliente_listar()
        for c in clientes:
            if c.get_email() == "admin":
                return
        Service.cliente_inserir("admin", "admin", "00000000", "1234")

    # --- MÉTODOS DE PROFISSIONAL ---
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    # --- MÉTODOS DE SERVIÇO ---
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)

    # --- MÉTODOS DE HORÁRIO ---
    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(0, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO().inserir(h)

    # --- TAREFA 1: ABRIR MINHA AGENDA ---
    @staticmethod
    def horario_abrir_minha_agenda(data, horario_inicio, horario_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(f"{data} {horario_inicio}", "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(f"{data} {horario_fim}", "%d/%m/%Y %H:%M")
        delta = timedelta(minutes=int(intervalo))
        
        x = data_inicio
        while x <= data_fim:
            Service.horario_inserir(x, False, None, None, id_profissional)
            x += delta

    # --- TAREFA 2: VISUALIZAR MINHA AGENDA (PROFISSIONAL) ---
    @staticmethod
    def horario_listar_agenda_profissional(id_profissional):
        agenda = []
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                cli = Service.cliente_listar_id(h.get_id_cliente()) if h.get_id_cliente() else None
                srv = Service.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
                
                agenda.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%Y-%m-%d %H:%M:%S") if isinstance(h.get_data(), datetime) else str(h.get_data()),
                    "confirmado": h.get_confirmado(),
                    "cliente": cli.get_nome() if cli else "Nenhum",
                    "servico": srv.get_descricao() if srv else "Nenhum"
                })
        return agenda

    # --- TAREFA 3: VISUALIZAR MEUS SERVIÇOS (CLIENTE) ---
    @staticmethod
    def horario_listar_servicos_cliente(id_cliente):
        servicos = []
        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                prof = Service.profissional_listar_id(h.get_id_profissional()) if h.get_id_profissional() else None
                srv = Service.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None
                
                servicos.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%Y-%m-%d %H:%M:%S") if isinstance(h.get_data(), datetime) else str(h.get_data()),
                    "confirmado": h.get_confirmado(),
                    "servico": srv.get_descricao() if srv else "Não definido",
                    "profissional": prof.get_nome() if prof else "Não definido"
                })
        return servicos

    # --- TAREFA 4: CONFIRMAR SERVIÇO ---
    @staticmethod
    def horario_listar_pendentes_profissional(id_profissional):
        return [
            h for h in Service.horario_listar() 
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
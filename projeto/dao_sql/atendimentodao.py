from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    @classmethod
    def _para_texto(cls, data):
        if isinstance(data, datetime):
            return data.strftime("%d/%m/%Y %H:%M")
        return data

    @classmethod
    def _para_data(cls, data):
        if isinstance(data, str):
            try:
                return datetime.strptime(data, "%d/%m/%Y %H:%M")
            except ValueError:
                return datetime.fromisoformat(data)
        return data

    @classmethod
    def _para_objeto(cls, row):
        id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario = row
        obj = Atendimento(id, cls._para_data(data))
        obj.set_queixa_principal(queixa_principal)
        obj.set_historico_saude(historico_saude)
        obj.set_avaliacao(avaliacao)
        obj.set_prescricao(prescricao)
        obj.set_id_horario(id_horario)
        return obj

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cls.execute(sql, (cls._para_texto(obj.get_data()), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM atendimento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [cls._para_objeto(row) for row in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM atendimento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = cls._para_objeto(row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE atendimento SET data=?, queixa_principal=?, historico_saude=?, avaliacao=?, prescricao=?, id_horario=?
            WHERE id=?
        """
        cls.execute(sql, (cls._para_texto(obj.get_data()), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM atendimento WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()
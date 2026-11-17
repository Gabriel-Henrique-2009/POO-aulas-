from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    @classmethod
    def _para_texto(cls, data):
        if isinstance(data, datetime):
            return data.strftime("%d/%m/%Y %H:%M")
        return data

    @classmethod
    def _para_objeto(cls, row):
        id, data, confirmado, id_cliente, id_servico, id_profissional = row
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y %H:%M")
            except ValueError:
                data = datetime.fromisoformat(data)
        return Horario(id, data, bool(confirmado), id_cliente, id_servico, id_profissional)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (cls._para_texto(obj.get_data()), int(obj.get_confirmado()), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM horario"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [cls._para_objeto(row) for row in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = cls._para_objeto(row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        cls.execute(sql, (cls._para_texto(obj.get_data()), int(obj.get_confirmado()), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()
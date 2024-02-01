from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class VendedoresEnum(str, Enum):
    Luis = "Luis"
    Gustavo = "Gustavo"
    Luciano = "Luciano"

class Vendas(BaseModel):
    """
    Modelo de dados para Vendas

    Args:
        email (str): Email do comprador
        data (datetime): Data da Compra
        id_compra (int): Identificador da Compra
        valor_compra (float): Valor da Compra
        vendedor (str): Vendedor que realizou a compra

    """
    email: EmailStr
    data: datetime
    id_compra: PositiveInt
    valor_compra: PositiveFloat
    vendedor: VendedoresEnum

    @field_validator('vendedor')
    def vendedor_deve_estar_enum(cls, error):
        return error

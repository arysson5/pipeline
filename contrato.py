from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator
from enum import Enum

# Enum para produtos
class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "ChatGPT"
    produto3 = "Lhama"

# Modelo para as vendas
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: float
    qtde: int
    produto: ProdutoEnum

    # Validador para o campo 'produto' (não é necessário para o enum, mas mantido como exemplo)
    @validator('produto')
    def categoria_enum(cls, v):
        if v not in ProdutoEnum:
            raise ValueError("Produto inválido.")
        return v

# Exemplo de uso
# venda = Vendas(
#     email="exemplo@empresa.com",
#     data=datetime.now(),
#     valor=100.0,
#     qtde=2,
#     produto="Gemini"  # Usando o enum ProdutoEnum.produto1 ou diretamente "Gemini"
# )

# print(venda)

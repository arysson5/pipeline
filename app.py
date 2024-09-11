import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title("Sistemas de CRM e vendas da zapflow")

    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9, 0))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    qtde = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Escolher produto", options=["Gemini", "ChatGPT", "Lhama"])

    if st.button("Enviar venda"):
        data_hora = datetime.combine(data, hora)
        try:
            vendas = Vendas(

            email = email,
            data = data_hora,
            valor = valor,
            qtde = qtde,
            produto = produto
            )
            salvar_no_postgres(vendas)
        except ValidationError as e:
            st.error("Erro ao enviar venda: " + str(e))
        
        

        

if __name__ == "__main__":
    main()

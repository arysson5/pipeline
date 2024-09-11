import streamlit as st
import contrato
from datetime import datetime, time

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
        st.write("**Venda enviada com sucesso!**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e hora da compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor}")
        st.write(f"Quantidade de Produtos: {qtde}")
        st.write(f"Produto: {produto}")

if __name__ == "__main__":
    main()

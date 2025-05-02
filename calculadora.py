import streamlit as st

def calcular_preco_final(preco_base):
    if preco_base <= 1000:
        preco_ajustado = preco_base * 1.30
    else:
        preco_ajustado = preco_base * 1.20

    preco_com_acrescimo = preco_ajustado + 65
    preco_final = preco_com_acrescimo * 1.14

    return round(preco_final, 2)

st.title("Calculadora de Preço ZAP")
preco_input = st.number_input("Informe o preço base (R$):", min_value=0.0, step=0.01)

if st.button("Calcular"):
    resultado = calcular_preco_final(preco_input)
    st.success(f"💰 Preço final: R${resultado}")

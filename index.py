import json
from datetime import date, datetime 
import streamlit as st

json_files = st.file_uploader(
  "Selecione o arquivo JSON:", accept_multiple_files=True, type="json"
)

if json_files is not None:
  st.write("Filtre os dados:")
  data_inicial = st.date_input("Data Inicial", date.today())
  data_final = st.date_input("Data Final", date.today())

# for json_file in json_files:
#   df = json.load(json_file)
#   actions = df["actions"]
#   activeActions = [
#         x for x in actions
#         if x.get("data", {}).get("card", {}).get("closed") == True
#     ]

  # activities:
  #   Data em que atividade foi finalizada:
  #   Atividade realizada: Título
  #   Descrição da atividade: ["cards"]["desc"] DESCRICAO
  #   Setor: está no título
  #   Status: CONCLUÍDO ou valor da etiqueta
  #   Observação: ["cards"]["desc"] DESCRICAO || Concluído no dia {Data em que atividade foi finalizada}
  # activities = []
  
  # for activeAction in activeActions:
  #   activity = {
  #     data: activeAction.
  #   }
  
  # st.write("JSON DATA:")
  # st.json(activeActions)
import requests
import json

config = {
  "apiKey": "AIzaSyDTVp9KGSRA08_XhSZth8dQdXbwF8b7a5I",
  "authDomain": "fir-tutorial-16ff6.firebaseapp.com",
  "projectId": "fir-tutorial-16ff6",
  "storageBucket": "fir-tutorial-16ff6.appspot.com",
  "messagingSenderId": "910709372601",
  "appId": "1:910709372601:web:0b959e237cfbc9930dcd68"
}

link = "https://fir-tutorial-16ff6-default-rtdb.firebaseio.com/"

# Criar uma nova venda
def create_sale(data):
  r = requests.post(f"{link}/Vendas/.json", data=json.dumps(data))
  print(r)
  print(r.text)


# Editar uma venda
def update_sale(id, data):
  r = requests.patch(f"{link}/Vendas/{id}/.json", data=json.dumps(data))
  print(r)
  print(r.text)

# Criar um novo produto
def create_procuct(data):
  r = requests.post(f"{link}/Produtos/.json", data=json.dumps(data))
  print(r)
  print(r.text)



"""id="-NB8o0PwOjCoy9uReeS-"
data = {'cliente': 'Orochi'}
update_sale(id, data)"""

#create_sale(data={'cliente':'Naruto', 'preco':150, 'produto':'teclado'})

#create_procuct(data={'nome':'mouse', 'preco':45, 'quantidade':60})

r = requests.get(f"{link}/.json")
print(r)
dic_r = r.json()
print(dic_r)
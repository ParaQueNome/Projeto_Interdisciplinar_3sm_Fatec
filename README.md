# Projeto_Interdisciplinar_3sm_Fatec

## Projeto destinado às atualizações do Projeto Interdisciplinar.

<p>Membros: </p> <br>

<ul>
  <li>
    Fabiano Marques Soares Junior
  </li>
  <li>
    Fernando
  </li>
  <li>
    Igor
  </li>
  <li>
    Giovani Ruzzon de Jesus Ortega
  </li>
  <li>
    Guilherme
  </li>
</ul>

## Tema: Gestão inteligente de alimentos e Fome Zero

<h1>Requisitos para rodar o Projeto:</h1>

Configuração do Ambiente (Windows)

```bash
git clone https://github.com/ParaQueNome/Projeto_Interdisciplinar_3sm_Fatec.git
cd PI3
python -m venv venv
venv\Scripts\activate.bat
cd..
cd..
cd PI3
pip install -r requeriments.txt
# Inicie o MongoDB (certifique-se de ter o MongoDB instalado)
# Você deve usar o MongoDB Compass para conectar-se ao localhost.
# Utilize o nome 'FoodShare' na criação do banco de dados e na coleção
# Aplicando migrações, executando testes e iniciando o servidor
python manage.py migrate
python manage.py test
python manage.py runserver
```
Configuração do Ambiente (Linux)
```bash
git clone https://github.com/ParaQueNome/Projeto_Interdisciplinar_3sm_Fatec.git
cd PI3
python -m venv venv
source venv/bin/activate
cd ..
cd ..
cd PI3
pip install -r requeriments.txt
# Inicie o MongoDB (certifique-se de ter o MongoDB instalado)
# Você deve usar o MongoDB Compass para conectar-se ao localhost.
# Utilize o nome 'FoodShare' na criação do banco de dados e na coleção
# Aplicando migrações, executando testes e iniciando o servidor
python manage.py migrate
python manage.py test
python manage.py runserver
```


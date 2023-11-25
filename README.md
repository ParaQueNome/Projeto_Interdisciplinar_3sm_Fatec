# Projeto_Interdisciplinar_3sm_Fatec

## Projeto destinado às atualizações do Projeto Interdisciplinar.

<p>Membros: </p> <br>

<ul>
  <li>
    Fabiano
  </li>
  <li>
    Fernando
  </li>
  <li>
    Igor
  </li>
  <li>
    Giovani
  </li>
  <li>
    Guilherme
  </li>
</ul>

## Tema: Gestão inteligente de alimentos e Fome Zero

<h1>Requisitos para rodar o Projeto:</h1> <br>

## Configuração do Ambiente

git clone https://github.com/ParaQueNome/Projeto_Interdisciplinar_3sm_Fatec.git && \
cd PI3 && \
python -m virtualenv venv && \
cd venv/Scripts && \
activate.bat || source activate && \
cd ../../PI3 && \
pip install -r requirements.txt && \
sudo systemctl start mongod && \
sudo systemctl stop mongod

# Abra o MongoDB Compass e conecte-se ao localhost.

## Executando o Projeto

cd PI3 && \
python manage.py migrate && \
python manage.py test && \
python manage.py runserver


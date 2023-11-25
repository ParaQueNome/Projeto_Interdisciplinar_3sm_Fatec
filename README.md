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

### Clonando o Repositório e Configurando Ambiente Virtual

git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1
python -m virtualenv venv
cd venv
cd Scripts
activate.bat  # Para usuários Windows || source activate  # Para usuários Linux ou MacOS
cd ../..

### Instalando Dependências e Configurando o MongoDB

pip install -r requirements.txt

# Se estiver usando Linux
sudo systemctl start mongod  # Inicializa o servidor
sudo systemctl stop mongod  # Para o servidor

# Abra o MongoDB Compass e conecte-se ao localhost.

## Executando o Projeto

### Aplicando Migrações, Executando Testes e Iniciando o Servidor

cd Pratica_TDD_1
python manage.py migrate
python manage.py test
python manage.py runserver


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

## Configuração do Ambiente (Windows)

### Clonando o Repositório e Configurando Ambiente Virtual

```bash
git clone https://github.com/ParaQueNome/Projeto_Interdisciplinar_3sm_Fatec.git
cd PI3
python -m venv venv
venv\Scripts\activate.bat

pip install -r requeriments.txt

# Inicie o MongoDB (certifique-se de ter o MongoDB instalado)
# Você pode usar o MongoDB Compass para conectar-se ao localhost.
### Aplicando migrações, executando testes e iniciando o servidor
python manage.py migrate
python manage.py test
python manage.py runserver


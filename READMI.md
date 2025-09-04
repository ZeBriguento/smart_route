# Roteirizador Inteligente e Sustentável

Sistema que gera roteiros personalizados e sustentáveis com base em orçamento, tempo, preferências e tipo de transporte. O projeto calcula impacto ambiental e sugere práticas sustentáveis.

---

## 🔹 Fluxo de Funcionamento

1. **Input do Utilizador**
   - Orçamento total
   - Tempo (dias pretendidos)
   - Preferências (ex.: lazer, gastronomia, cultura)
   - Tipo de transporte

2. **Cálculo Inicial**
   - `custo_medio_diario = orcamento / tempo`
   - Filtrar pontos turísticos cujo custo médio diário ≤ `custo_medio_diario`
   - Filtrar por preferências selecionadas

3. **Seleção das Províncias**
   - Selecionar 1 ou mais províncias que melhor se ajustam às condições
   - Associar pontos turísticos e atividades disponíveis

4. **Cálculo de Impacto Ambiental**
   - `impacto_CO2 = emissoes_CO2(transporte) * dias`
   - Selecionar o roteiro mais sustentável

5. **Sugestões de Sustentabilidade**
   - Trocar transporte por outro com menor emissão de CO2
   - Usar menos plástico
   - Reduzir consumo de água
   - Escolher alimentação local

---

## 🔹 Tecnologias

- **Backend / Lógica**: Python 3.12.3, Django 5.2.6, Django REST Framework 3.16.1
- **Banco de Dados**: SQLite
- **Frontend**: React / Next.js (opcional)
- **Dependências** adicionais:  
  `asgiref==3.9.1`, `django-cors-headers==4.7.0`, `sqlparse==0.5.3`

---

## 🔹 Pré-requisitos

- Python 3.12+
- Pip
- Node.js (para frontend)
- SQLite (já incluso no Python)

---

## 🔹 Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git

#Acesse a pasta do projecto
cd seu-projeto

#Crie o ambiente virtual
python -m venv venv
# Linux/macOS

#Active o ambiente
source venv/bin/activate

# Windows
venv\Scripts\activate

#Instale as dependências:
pip install -r requirements.txt

#Rode migrações:
python manage.py migrate

#Popule o banco de dados com dados iniciais usando o seed:
python seed_full.py

#execute o projecto 
python manage.py runserver

#O backend estará disponível em
http://127.0.0.1:8000/

#Acesse a pasta do frontend:
cd smart-route-web
#Instale as dependencias
npm install
#Execute o front-end
npm run dev
#Acesse a rota 
http://localhost:3000/

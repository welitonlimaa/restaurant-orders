# Restaurant Orders
Este é um projeto que consiste em uma ferramenta para construção de cardápios para um restaurante. A ferramenta permite gerar cardápios personalizados levando em consideração restrições alimentares dos clientes e a disponibilidade dos ingredientes em estoque.

## Funcionalidades

* Geração de cardápios com base em restrições alimentares e estoque de ingredientes
* Gestão de receitas e ingredientes
* Controle de estoque de ingredientes
* Consumo de ingredientes ao preparar uma receita
  
## Requisitos do Sistema
Python 3.7 ou superior

## Instalação
1. Clone o repositório do projeto: git clone https://github.com/seu-usuario/restaurant-orders.git
2. Navegue até o diretório do projeto: cd restaurant-orders
3. Crie e ative um ambiente virtual (opcional, mas recomendado): python -m venv venv source venv/bin/activate
4. Instale as dependências do projeto: pip install -r requirements.txt

## Uso
Execute o script principal para gerar um cardápio:
python3 -m uvicorn app:app

## Testes
Para executar os testes automatizados, execute o seguinte comando: python3 -m pytest 

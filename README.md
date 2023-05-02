<p align="center">
  <img src="./src/img/logo-lbfb.png" alt="Logo da Liga Brasileira de Futebol de Botão">
</p>

# LBFB - Liga Brasileira de Futebol de Botão ⚽

O LBFB é um site com o proposito de divulgar a arte de jogar futebol de botão, temos uma área de cadastro para clubes em nossa primeira versão, temos um roadmap planejado para criar uma área de login e em seguida criarmos um microserviço de tabelas e campeonatos.

O back-end da aplicação pode ser encontrado no seguinte repositório: [https://github.com/AlanAmaralCosta/lbfb-backend](https://github.com/AlanAmaralCosta/lbfb-backend)

## Funcionalidades 🤖

-   Visualizar uma lista de clubes cadastrados.
-   Cadastrar seu clube incluindo seu logo.
-   Alterar as informações do seu Clube.
-   Excluir seu Clube.

## Instalação 📦

Requer o [Python 3](https://www.python.org/downloads/) instalado para rodar.

Para usar o LBFB, siga estes passos:

1. Clone o repositório para a sua máquina.
2. Crie um ambiente virtual executando `python3 -m venv .lbfb_frontend` no terminal.
3. Ative o ambiente virtual executando `source .lbfb_frontend/bin/activate`.
4. Instale as dependências necessárias executando `pip install -r requirements.txt`.
5. Inicie o servidor front-end executando `python app.py` no terminal. Isso iniciará o servidor Flask em `http://localhost:5001`.

## Uso

Ambos os códigos devem estar rodando, tanto o back-end quanto o front-end do aplicativo devem estar em execução. Aqui estão os passos para usar o aplicativo:

1. Inicie o servidor back-end executando `python app.py` no terminal. Isso iniciará o servidor Flask em um localhost. Um exemplo da aplicação inicada na porta 5000 pode ser acessado em: `http://localhost:5000`.
2. Inicie o servidor frontend e acesse o sistema local em `http://localhost:5001`.
3. O Sistema front end tem um menu de navegação simples home - página inicial, Cadastro de Clubes - Lista, permite criar, alterar e deletar, Sobre - Um breve resumo de nossa história.
4. Todas as principais funcionalidades do CRUD estão no menu Cadastro de Clubes.

## Contribuindo

Se você gostaria de contribuir com o LBFB, abra um pull request ou uma issue no repositório do GitHub.

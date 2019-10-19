# Sistema para gerenciamento de vagas em imóveis

Aqui estão contidas informações sobre o desenvolvimento do sistema LocaFácil, que visa a divulgação e gerenciamento de vagas de imóveis. (README em construção...)

## Das regras

- Os commits podem ser feitos em português ou inglês 

## Requerimentos

- Python >= 3.6
- Pyqt na versão 5
- Qt Design 

## Funcionalidades 

- Alteramos a página inicial com os links para login/cadastro, a tela de sobre e realizamos algumas modificações em outras funcionalidades
- As funcionalidades não implementadas dependem do banco de dados, tais como: busca e listagem de imóveis e algumas funcionalidades relacionadas a salvar dados no banco


## Do uso

- Clone o projeto github (https://github.com/spbdlelis/Projeto-Loca-Facil.git) 
- Deve ser executado o arquivo Server.py e em seguida o Root.py 
- A cada vez que tem se uma instância nova do programa, o servidor mostra uma mensagem sinalizando uma "Nova Conexão"
- Existem Threads para: receber uma mensagem e processar o dado recebido, está última não faz o processamento ainda, pois depende do banco de dados

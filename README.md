Magia do Studio Ghibli ✨

Um projeto que traz a magia dos filmes do Studio Ghibli para a tela do seu navegador. Cada filme é apresentado em um card elegante, com animações suaves, efeitos 3D interativos e uma “aura” única que muda a cor do fundo quando você passa o mouse sobre ele.

Este projeto combina Frontend em HTML/CSS/JS com Backend em Python/Flask, consumindo uma API de filmes do Studio Ghibli.
<img width="1329" height="614" alt="image" src="https://github.com/user-attachments/assets/dca422ab-5fb4-4fc6-8c04-ad045bfb33c3" />


🎨 Funcionalidades do Frontend

Cards interativos para cada filme
Cada card mostra:

Poster do filme

Título e título original

Diretor

Ano de lançamento

Descrição resumida

Efeito 3D Parallax
Ao mover o mouse sobre o card, ele se inclina suavemente, criando um efeito de profundidade.

Aura mágica

Cada card tem uma cor temática baseada no filme (definida no JS).

Ao passar o mouse sobre o card:

A tag muda de cor para combinar com o filme.

O fundo do site recebe um tom suave da cor do filme, criando um efeito de “aura” que envolve todo o layout.

Ao retirar o mouse, o fundo e a tag voltam ao estado original.

Transições e animações suaves

Zoom e brilho nas imagens dos filmes.

Mudança de cor do fundo com transição suave.

Cards flutuando e sombras realçadas para sensação de leveza.

Responsivo
Funciona bem em desktops e dispositivos móveis.

⚡ Funcionalidades do Backend

O backend em Python + Flask serve duas funções principais:

Servir o Frontend

O arquivo Front.html é servido diretamente pelo Flask quando acessamos http://127.0.0.1:5000.

API para fornecer os filmes

Rota: /api/filmes

Faz uma requisição para a API externa de filmes do Studio Ghibli (https://ghibliapi.vercel.app/films) e retorna o JSON para o frontend.

Isso permite que o frontend permaneça leve, apenas consumindo dados do backend.

CORS habilitado para permitir que o frontend, mesmo em outro domínio ou porta, faça requisições ao backend sem problemas.

🖥 Como rodar o projeto

Instale as dependências do Python

pip install flask flask-cors requests

Rode o backend

python Back.py

Isso vai iniciar o servidor em http://127.0.0.1:5000.

Acesse no navegador
Abra http://127.0.0.1:5000 para ver os cards mágicos carregando os filmes.

💡 Como a “Aura” funciona

Cada filme tem uma cor associada no JS (movieColors).

Quando o mouse entra no card:

O card aplica a cor na tag e cria um radial gradient no card.

O fundo do body recebe uma cor suave baseada nessa mesma cor (ex: adicionando opacidade com 66 no hex) para que todo o site ganhe uma aura luminosa.
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d66ef60a-3a64-40a1-9181-72b68ce7b7fd" />



Quando o mouse sai:

O card e o fundo voltam à cor original definida nas variáveis CSS (--bg-color e --secondary-color).

Esse efeito cria a sensação de que cada filme emite sua própria energia mágica, deixando a experiência mais imersiva e divertida. ✨
<img width="1323" height="616" alt="image" src="https://github.com/user-attachments/assets/67c843d1-1c99-4eb1-9ec7-f8cf33113ae6" />


📂 Estrutura do projeto
MagiaGhibli/
│
├─ Back.py           # Backend em Flask
├─ Front.html        # Frontend com HTML, CSS e JS
└─ README.md
🚀 Tecnologias usadas

Frontend: HTML5, CSS3, JavaScript

Backend: Python 3, Flask, Flask-CORS, Requests

API de filmes: Studio Ghibli API Vercel

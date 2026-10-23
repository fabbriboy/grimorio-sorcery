Grimório Sorcery v2

Conteúdo
  index.html, sw.js, manifest.json, ícones  -> o app
  data/cards.json                            -> as 1.100 cartas com texto em português
  data/decks.json                            -> listas dos 8 decks prontos (Beta e Gothic)
  img/                                       -> já vem com as 132 imagens dos decks Beta
  tools/preparar_imagens.py                  -> gera as imagens de todas as cartas

1. Gerar as imagens (no seu computador)
   sudo pacman -S python-pillow
   cd grimorio-sorcery
   python tools/preparar_imagens.py "/home/Fabbri/Downloads/Card Images (API)"

2. Enviar para o GitHub
   São mais de 1.100 arquivos, e o upload pelo site aceita só 100 por vez.
   Por isso use o git (com o GitHub CLI logado: sudo pacman -S github-cli && gh auth login):

   cd ~
   git clone https://github.com/fabbriboy/grimorio-sorcery.git repo-grimorio
   cp -r grimorio-sorcery/* repo-grimorio/
   cd repo-grimorio
   git add -A
   git commit -m "Grimório v2: todas as coleções, decks do Gothic e mesa"
   git push

   O site atualiza em um ou dois minutos em https://fabbriboy.github.io/grimorio-sorcery/

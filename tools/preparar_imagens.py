#!/usr/bin/env python3
"""Prepara as imagens das cartas para o Grimório Sorcery.

Uso:
    python tools/preparar_imagens.py "/home/Fabbri/Downloads/Card Images (API)"

Lê a pasta oficial de imagens, escolhe uma impressão normal (não foil) de cada
carta, reduz para 560 px, gira os terrenos para a horizontal e salva em img/<carta>.webp.
Precisa do Pillow:  sudo pacman -S python-pillow
"""
import json, os, sys
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    origem = sys.argv[1]
    destino = os.path.join(RAIZ, "img")
    os.makedirs(destino, exist_ok=True)
    mapa = json.load(open(os.path.join(AQUI, "mapa_imagens.json")))

    arquivos = {}
    for pasta, _, nomes in os.walk(origem):
        for n in nomes:
            base, ext = os.path.splitext(n)
            if ext.lower() in (".png", ".jpg", ".jpeg", ".webp"):
                arquivos.setdefault(base.lower(), os.path.join(pasta, n))

    feitas, faltando = 0, []
    for slug, info in mapa.items():
        caminho = next((arquivos[p.lower()] for p in info["p"] if p.lower() in arquivos), None)
        if not caminho:
            faltando.append(slug); continue
        im = Image.open(caminho).convert("RGB")
        if info["site"] and im.height > im.width:
            im = im.rotate(-90, expand=True)
        escala = 560 / max(im.size)
        if escala < 1:
            im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
        im.save(os.path.join(destino, slug + ".webp"), "WEBP", quality=80)
        feitas += 1
        if feitas % 100 == 0:
            print(f"{feitas} imagens prontas...")

    print(f"Pronto: {feitas} de {len(mapa)} cartas com imagem em {destino}")
    if faltando:
        print(f"Sem imagem encontrada para {len(faltando)} cartas: " + ", ".join(faltando[:15]) + (" ..." if len(faltando) > 15 else ""))

if __name__ == "__main__":
    main()

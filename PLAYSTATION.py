from playwright.sync_api import sync_playwright
from time import sleep
import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def notificar(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": mensagem})


lista_jogos_play = [
    "Assassin’s Creed Shadows", "Assassin's Creed Black Flag Resynced", "Resident Evil Requiem", "Black Myth: Wukong",
    "DEATH STRANDING 2: ON THE BEACH", "Ghost of Yōtei™ Edição Completa",
    "Sekiro™: Shadows Die Twice - Edição Jogo do Ano"
]

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page()
    pagina.goto("https://store.playstation.com/pt-br/pages/latest")
    for games in lista_jogos_play:
        try:
            pagina.get_by_role("button", name="Pesquisar").click()
            campo_busca = pagina.get_by_role("searchbox", name="Pesquise na PlayStation Store")
            campo_busca.fill(games)
            campo_busca.press('Enter')
            sleep(2)
            pagina.get_by_role("link", name=games, exact=True).click()
            sleep(2)
            preco = pagina.get_by_text("R$").first
            novo_preco = float(preco.inner_text().replace('R$', '').replace(',', '.').strip())
            if novo_preco < 200:
                mensagem = f'O preço de {games} esta {novo_preco} na Playstation store, vai comprar?'
                notificar(mensagem)
            else:
                continue
        except:
            mensagem_erro = f'Aconteceu alguma coisa com o {games}, da uma olhada'
            notificar(mensagem_erro)
            

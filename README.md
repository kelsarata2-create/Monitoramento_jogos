# Monitor de Preços - PlayStation Store

Script em Python que monitora automaticamente os preços de uma lista de jogos na PlayStation Store e envia uma notificação via Telegram quando o preço de algum jogo cai abaixo de um valor definido.

## Como funciona

O script utiliza o [Playwright](https://playwright.dev/python/) para automatizar a navegação na PlayStation Store:

1. Abre a página de lançamentos da PlayStation Store (`store.playstation.com/pt-br/pages/latest`).
2. Para cada jogo da lista `lista_jogos_play`, faz uma busca pelo nome exato.
3. Acessa a página do jogo e extrai o preço exibido.
4. Se o preço for **menor que R$ 200**, envia uma notificação via Telegram avisando que o jogo está com um preço interessante.
5. Se ocorrer qualquer erro durante o processo (jogo não encontrado, elemento não localizado, etc.), envia uma notificação de erro informando qual jogo apresentou problema.

## Pré-requisitos

- Python 3.8+
- Um bot do Telegram criado (via [@BotFather](https://t.me/BotFather)) e o ID do chat para onde as mensagens serão enviadas

## Instalação

```bash
pip install playwright requests
playwright install chromium
```

## Configuração

O script lê o token do bot e o ID do chat a partir de variáveis de ambiente:

```bash
export TELEGRAM_TOKEN="seu_token_aqui"
export TELEGRAM_CHAT_ID="seu_chat_id_aqui"
```

> No Windows (PowerShell), use `$env:TELEGRAM_TOKEN="seu_token_aqui"`.

## Uso

Edite a lista `lista_jogos_play` no script com os jogos que deseja monitorar (os nomes devem corresponder exatamente ao título exibido na PlayStation Store) e execute:

```bash
python monitor_precos.py
```

## Personalização

- **Valor limite de notificação**: altere a condição `if novo_preco < 200:` para o valor desejado.
- **Lista de jogos**: adicione ou remova itens de `lista_jogos_play`.
- **Frequência de execução**: o script roda uma única vez; para monitoramento contínuo, agende-o via `cron` (Linux/Mac) ou Agendador de Tarefas (Windows), ou adicione um laço com `sleep`.

## Observações

- O script depende da estrutura atual do site da PlayStation Store; mudanças no layout podem exigir ajustes nos seletores.
- O bloco `try/except` genérico captura qualquer falha, mas não diferencia os tipos de erro — pode ser útil especificar as exceções para facilitar a depuração.
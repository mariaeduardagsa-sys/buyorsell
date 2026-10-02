# Buy or Sell

Projeto de acompanhamento e análise de ativos, desenvolvido progressivamente
para aprofundar conhecimentos de Python. O MVP não executará operações financeiras.

## Branding e UI

Nome do produto: **Buy or Sell**.
Tagline: **Monitor. Analyze. Act.**

A identidade visual inicial apresentada pelo usuário é a referência para a futura
aplicação mobile. Qualquer redesign da marca exige consultar o usuário antes.

- Fundo azul-marinho escuro.
- Verde para BUY e movimentos positivos.
- Vermelho para SELL e movimentos negativos.
- Cores neutras ou claras para HOLD e informações gerais.
- Candlesticks e símbolos de movimentos ascendentes e descendentes.

A interface deve comunicar estados com texto e ícones, além da cor: por exemplo,
`BUY` com um ícone de compra, `HOLD` com um ícone de pausa e `SELL` com um ícone
de venda. Ícones devem ter significado consistente e rótulos acessíveis;
leitores de tela devem conseguir identificar o estado sem depender da aparência.
Texto e elementos relevantes devem manter contraste adequado com o fundo.

Movimento de preço e sinal da estratégia são informações distintas: uma variação
positiva não significa automaticamente BUY. A UI deve rotular cada informação
explicitamente e distinguir sinais de decisões e ordens.

Os valores exatos de cores ainda não foram definidos como tokens de UI.
A referência visual não autoriza inventar uma nova paleta ou redesenhar o logo.
Esta definição orienta etapas futuras; a fase atual continua sendo Python puro.

## Método

Cada etapa segue: objetivo, conceito, comparação com Java/Go quando útil, exemplo
pequeno e tarefa do aluno. A próxima etapa só começa depois da implementação,
revisão e correções. O código dos exercícios não será implementado automaticamente.

## Previsão, sinal e decisão

- **Previsão:** estimativa sobre um resultado futuro, com horizonte definido.
  Probabilidades precisam de uma metodologia de avaliação; não representam certeza.
- **Sinal:** resultado das regras de uma estratégia: BUY, HOLD ou SELL, acompanhado
  de motivos, dados utilizados, horário e versão da estratégia. Pode existir sem
  previsão, por exemplo usando regras determinísticas sobre indicadores.
- **Decisão:** escolha de agir ou não sobre o sinal, considerando posição atual,
  capital disponível, limites de risco, qualidade dos dados e custos.
- **Ordem:** instrução concreta resultante de uma decisão aprovada, com ativo,
  lado, quantidade e parâmetros de execução. Enviar uma ordem não garante execução.

Assim, uma previsão não produz automaticamente BUY; BUY não produz automaticamente
uma compra. No MVP, o fluxo termina na análise e nos sinais. Decisão simulada e
ordens simuladas ficam para etapas futuras; execução real não faz parte do MVP.

## Fase atual: Python puro

Estrutura mínima a ser criada durante os exercícios:

```text
buyorsell/
    pyproject.toml
    .python-version
    app/
        __init__.py
        domain/
            __init__.py
            asset.py
    tests/
        test_asset.py
```

Começamos pelo domínio, sem diretórios vazios para serviços, repositórios ou APIs.
`__init__.py` identifica os pacotes regulares; `asset.py` é um módulo.

O `pyproject.toml` centraliza metadados, dependências e configuração das ferramentas.
`dependencies` contém dependências da aplicação; o grupo `dev` contém pytest,
Ruff e mypy. Usamos o projeto sem empacotamento nesta fase (`package = false`).

O uv gerencia versões de Python, ambientes virtuais e dependências. O ambiente
`.venv` isola as dependências deste projeto. O arquivo `uv.lock`, quando gerado,
deve ser versionado para registrar a resolução das dependências.

Depois de disponibilizar uv no terminal:

```powershell
uv sync
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy app
```

Os comandos de teste e typing passam a fazer sentido depois de criar o exercício.

## Primeiro exercício: Asset

Crie `app/__init__.py`, `app/domain/__init__.py` e `app/domain/asset.py`.
Os dois arquivos `__init__.py` podem começar vazios.

Em `asset.py`, implemente:

1. Um `AssetType` usando `Enum`, com STOCK, ETF e CRYPTO e valores textuais.
2. Uma classe `Asset` usando `@dataclass`, com os campos `symbol: str`,
   `name: str` e `asset_type: AssetType`, todos obrigatórios.
3. Por enquanto, sem validação, persistência, preço, previsão ou sinal no Asset.

Uma dataclass gera métodos como inicialização, representação e igualdade,
reduzindo código repetitivo. Type hints descrevem o contrato para ferramentas;
não validam os valores automaticamente em runtime.

Envie sua implementação para revisão antes de avançarmos.

## Estado atual

- Ambiente configurado com Python 3.14 e uv.
- AssetType implementado com STOCK, ETF e CRYPTO.
- Asset implementado como dataclass com símbolo, nome e tipo.
- Teste de armazenamento dos campos passando.
- Código verificado com Ruff e mypy.

## Desenvolvimento local

Pré-requisito: uv instalado.

Instale as dependências:

```powershell
uv sync

```

Execute as verificações:

```powershell
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy app
```

## Propósito do produto

O Buy or Sell acompanha ativos, analisa dados de mercado e
apresenta avisos de possíveis oportunidades com seus motivos.
O usuário decide se deseja agir. O MVP não envia ordens nem
executa compras ou vendas.

BUY, HOLD e SELL representam estados das estratégias.
Uma alta de preço não significa automaticamente uma
oportunidade de compra.

O acompanhamento de posições e a estimativa de ganho ou perda
ficam para uma etapa futura.

## Demonstração no terminal

Execute:

```powershell
uv run python -m app.main
```

A demonstração usa um ativo fictício e preços de exemplo.
Compara o último fechamento com a média dos últimos três
candles e apresenta o estado da estratégia com seu motivo.

Essa regra é didática e ainda não foi avaliada em dados históricos.
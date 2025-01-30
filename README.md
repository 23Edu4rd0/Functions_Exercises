# Exercícios em Python

Este repositório contém soluções para exercícios práticos em Python, focados no desenvolvimento de funções e manipulação de dados. Cada arquivo representa um desafio resolvido, ajudando a reforçar conceitos fundamentais da linguagem.

## Estrutura do Repositório

```plaintext
/exercicios_python
│-- format_name.py      # Função para formatar nomes
│-- is_leap_year.py     # Função para verificar se um ano é bissexto
│-- README.md           # Documentação do repositório
```

## Exercícios

### 1. Formatador de Nomes (`format_name.py`)

Esta função solicita ao usuário um primeiro e um último nome, garantindo que a entrada seja válida e retornando os nomes formatados corretamente com a primeira letra em maiúsculo.

**Exemplo de Uso:**

```python
print(format_name())
```

### 2. Verificador de Ano Bissexto (`is_leap_year.py`)

Esta função verifica se um determinado ano é bissexto com base nas regras:
- O ano deve ser divisível por 4.
- Se for divisível por 100, só é bissexto se também for divisível por 400.

**Exemplo de Uso:**

```python
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```

## Como Usar

Clone este repositório e execute os scripts diretamente no Python:

```sh
git clone https://github.com/seu-usuario/exercicios_python.git
cd exercicios_python
python format_name.py
python is_leap_year.py
```

## Contribuição

Sinta-se à vontade para sugerir melhorias ou adicionar novos exercícios via pull request!

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

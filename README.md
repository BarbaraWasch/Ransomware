# Ransomware (Criptografador e Descriptografador)

Este repositório contém um exemplo simples de **ransomware** implementado em Python. O código criptografa e descriptografa arquivos utilizando a biblioteca `pyaes` para realizar a criptografia AES no modo CTR.

## Estrutura do Projeto

O projeto é dividido em dois scripts:

- **`encrypter.py`**: Script para criptografar arquivos.
- **`decrypter.py`**: Script para descriptografar arquivos.

### Funcionalidade

- **Criptografia**: O script `encrypter.py` pega um arquivo, criptografa seu conteúdo com uma chave AES fixa e gera um arquivo criptografado com a extensão `.ransomwaretroll`.
  
- **Descriptografia**: O script `decrypter.py` pega o arquivo criptografado, descriptografa o conteúdo e restaura o arquivo original.

### Dependências

Para rodar o projeto, você precisará instalar a biblioteca `pyaes`. Você pode instalá-la utilizando o pip:

```bash
pip install pyaes
Como Usar
Criptografar Arquivo:

Edite o arquivo encrypter.py e defina o nome do arquivo que deseja criptografar (exemplo: teste.txt).
Execute o script:
bash
Copiar código
python encrypter.py
Descriptografar Arquivo:

Edite o arquivo decrypter.py e defina o nome do arquivo criptografado (exemplo: teste.txt.ransomwaretroll).
Execute o script:
bash
Copiar código
python decrypter.py
Como Funciona
Criptografia: O arquivo original é lido em modo binário e criptografado com uma chave fixa de 16 bytes (testeransomwares). O arquivo original é excluído e um novo arquivo com a extensão .ransomwaretroll é criado.

Descriptografia: O arquivo criptografado é lido em modo binário e descriptografado com a mesma chave usada para criptografia. O arquivo criptografado é excluído e um novo arquivo sem a extensão .ransomwaretroll é criado.

Exemplo
Criptografia:
Arquivo original: teste.txt
Arquivo criptografado: teste.txt.ransomwaretroll
Descriptografia:
Arquivo criptografado: teste.txt.ransomwaretroll
Arquivo restaurado: teste.txt
Log de Atividades
O sistema gera um arquivo de log ransomware_log.txt onde todos os eventos de criptografia e descriptografia são registrados, incluindo erros, caso ocorram.

Considerações de Segurança
Este projeto é apenas para fins educacionais. A utilização de ransomware real, em qualquer contexto, é ilegal e antiética. Não utilize este código de forma maliciosa.

# TABD
 
 #### Trabalho desenvolvido para disciplina de Tópicos Avançados de Banco de Dados.
 
 
 ## Direito de exclusão de dados com a LGPD (Lei Geral de Proteção de Dados)
 - A LGPD, em seu artigo 48, §3º, estabelece que “no juízo de gravidade do incidente, será avaliada eventual comprovação de que foram adotadas medidas técnicas adequadas que tornem os dados pessoais afetados ininteligíveis, no âmbito e nos limites técnicos de seus serviços, para terceiros não autorizados a acessá-los”. 
 - Na dimensão digital, a criptografia é uma técnica que emprega fórmulas e algoritmos matemáticos para transformar um texto em um código cifrado. Essa técnica é utilizada muito eficientemente para a proteção de dados, uma vez que somente o emissor e o receptor podem entendê-la. Existem dois tipos de criptografia: a simétrica, que utiliza mesma chave de codificação para a decodificação; e a assimétrica, que utiliza uma chave para codificação e outra para a decodificação.
 - Logo, mesmo que a criptografia não seja obrigatória por lei, ela é uma das medidas mais seguras atualmente e utilizá-la é uma boa prática quando se fala em proteção de dados pessoais, e, além disso, acaba por se tornar um diferencial competitivo, pois empresas que preservam a privacidade preferem negociar com organizações que se mostram atualizadas e preocupadas com a proteção de suas informações.
 
## Atividade desenvolvida:
- Foi desenvolida um aplicação simples que gerar uma chave para criptografar um arquivo que apresenta todos os registros cadastrados de clientes.

## Para execução:
1. Instalação de bibliotecas

pip install flask
pip install flask_mysqldb
pip install cryptography

Ao utilizar a cryptography para implemntação, utilizou o método de Fernet que utiliza a criptografia autenticada simétrica, também conhecida como “chave secreta”. Criptografia simétrica é quando uma chave é usada para criptografar e descriptografar uma mensagem ou arquivo.

## Execução

1. Executar o arquivo cripto.py para gerar uma chave para criptografia.
2. Executar o arquivo excel.py que trará via aplicação web e permiirá o download do arquivo criptografado.

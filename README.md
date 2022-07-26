# TABD
 
 #### Trabalho desenvolvido para disciplina de Tópicos Avançados de Banco de Dados.
 
 
 ## Direito de exclusão de dados com a LGPD (Lei Geral de Proteção de Dados)
 - A LGPD em seu artigo 18, menciona que o titular poderá a qualquer momento e mediante requisição, a eliminação dos dados pessoais tratados com o consentimento do titular, exceto nas hipóteses previstas no art. 16 desta lei.
 - Caso a base de contatos seja formada pela base de clientes da empresa, não será necessário apagar. Contudo, o tratamento dos dados deve ser para a finalidade específica que justifique o seu uso de acordo com a base legal da respectiva finalidade.
 - As bases de dados deverão ser tratadas de acordo com finalidades específicas, necessárias e adequadas para as atividades da empresa naquele momento, sendo justificadas pelas bases legais previstas na LGPD.

## Atividade desenvolvida:
- Foi desenvolida uma api para apagar cadastro de clientes sem perder rastreabilidade interna das vendas atribuidas ao clientes.
- A api persiste um trigger para quando executar a ação de delete do cliente, esse trigger  auxilia na substituição de qualquer dado relacionado ao clientes nas vendas, e as relacionando como cliente padrão, definido como inválido.


## Para execução:
1. Instalação de bibliotecas

pip install flask
pip install flask_mysqldb
pip install PyMySQL

## Execução

1. Executar o arquivo app.py para iniciar a aplicação
2. Usar rota /customer (método GET) - para visulização de clientes
3. Usar rota /customer/config (método GET) - para atribuição do trigger de deletar e substituição do dado.
4. Usar rota /customer/<idCustomer> (método DELETE) - para remover um respetivo cliente
5. Usar rota /oldcustomers (método DELETE) - para remover clientes antigos (conforme estipulado um certo período)
 
 
 ## Registro no banco
 ![alt text](https://github.com/ferpsalles/TABD/blob/main/Capturar.JPG)
 
 O registro do cliente eliminado na tabela de vendas fica atribuido como inválido, sem perder a rastreabilidade. Apenas modificada o cliente atribuido a ela.
 
 
 
 

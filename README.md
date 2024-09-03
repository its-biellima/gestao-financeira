*Manual do Software de Gestão Financeira*

Este software é projetado para gerenciar receitas e despesas, 
permitindo a adição, visualização, exclusão e cálculo de saldos. 
Ele utiliza o banco de dados PostgreSQL para armazenar os lançamentos 
financeiros e a interface gráfica foi criada com a biblioteca Tkinter.

Uso do Software
1. Adicionar Receita ou Despesa
Preencha os campos necessários:

Data: Formato DD-MM-AAAA.
Descrição: Breve descrição do lançamento.
Valor: Valor da receita ou despesa.
Categoria: Categoria do lançamento.
Clique em um dos botões:

Adicionar Receita para registrar uma receita.
Adicionar Despesa para registrar uma despesa.
O sistema validará a data e, se tudo estiver correto, 
a receita ou despesa será adicionada ao banco de dados.

2. Exibir Lançamentos
Selecione o intervalo de datas:

Data Início: Data de início para o filtro (opcional).
Data Fim: Data de fim para o filtro (opcional).
Clique em um dos botões:

Exibir Todas para visualizar todos os lançamentos.
Exibir Receitas para visualizar apenas receitas.
Exibir Despesas para visualizar apenas despesas.
A tabela será atualizada com os lançamentos que correspondem aos filtros aplicados.

3. Exibir Saldo
Selecione o intervalo de datas (opcional).

Clique no botão:

Exibir Saldo
O sistema calculará o saldo total, mostrando a soma das receitas 
e despesas no intervalo de datas selecionado.

4. Excluir Lançamento
Selecione o lançamento na tabela que deseja excluir.

Clique no botão:

Excluir Selecionado
O lançamento selecionado será removido do banco de dados e da tabela exibida.

Interface Gráfica
Campos de Entrada:

Data: Campo para inserir a data do lançamento.
Descrição: Campo para inserir a descrição do lançamento.
Valor: Campo para inserir o valor do lançamento.
Categoria: Campo para inserir a categoria do lançamento.
Data Início: Campo para inserir a data de início do filtro.
Data Fim: Campo para inserir a data de fim do filtro.
Botões:

Adicionar Receita: Adiciona uma receita.
Adicionar Despesa: Adiciona uma despesa.
Exibir Todas: Mostra todos os lançamentos.
Exibir Receitas: Mostra apenas as receitas.
Exibir Despesas: Mostra apenas as despesas.
Excluir Selecionado: Remove o lançamento selecionado.
Exibir Saldo: Calcula e exibe o saldo entre receitas e despesas.
Tabela de Lançamentos:

Exibe os lançamentos com as colunas: ID, Data, Descrição, Valor, Categoria e Tipo.

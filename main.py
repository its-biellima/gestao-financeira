
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pg8000
from datetime import datetime

# Conexão com o banco de dados PostgreSQL usando pg8000
def connect_db():
    conn = pg8000.connect(
        database="kaka",
        user="postgres",
        password="31415",
        host="127.0.0.1"
    )
    return conn

# Função para adicionar uma receita ou despesa
def add_lancamento(tipo):
    conn = connect_db()
    cur = conn.cursor()
    
    # Conversão da data para o formato YYYY-MM-DD antes de inserir no banco
    data_input = entry_data.get()
    try:
        data = datetime.strptime(data_input, "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido! Use DD-MM-AAAA.")
        return
    
    descricao = entry_descricao.get()
    valor = float(entry_valor.get())
    categoria = entry_categoria.get()
    
    cur.execute(
        "INSERT INTO lancamentos (data, descricao, valor, categoria, tipo) VALUES (%s, %s, %s, %s, %s)",
        (data, descricao, valor, categoria, tipo)
    )
    conn.commit()
    cur.close()
    conn.close()
    messagebox.showinfo("Sucesso", f"{tipo.capitalize()} adicionada com sucesso!")
    limpar_campos()

# Função para limpar os campos de entrada
def limpar_campos():
    entry_data.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)

# Função para exibir lançamentos (receitas ou despesas) filtrados por data
def exibir_lancamentos(tipo=None):
    conn = connect_db()
    cur = conn.cursor()

    data_inicio_input = entry_data_inicio.get()
    data_fim_input = entry_data_fim.get()

    query = "SELECT * FROM lancamentos"
    params = []

    if tipo:
        query += " WHERE tipo = %s"
        params.append(tipo)
    
    if data_inicio_input and data_fim_input:
        try:
            data_inicio = datetime.strptime(data_inicio_input, "%d-%m-%Y").strftime("%Y-%m-%d")
            data_fim = datetime.strptime(data_fim_input, "%d-%m-%Y").strftime("%Y-%m-%d")
            if tipo:
                query += " AND data BETWEEN %s AND %s"
            else:
                query += " WHERE data BETWEEN %s AND %s"
            params.extend([data_inicio, data_fim])
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use DD-MM-AAAA.")
            return

    query += " ORDER BY data ASC"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    tree.delete(*tree.get_children())  # Limpa a tabela antes de inserir novas linhas
    for row in rows:
        data_formatada = row[1].strftime("%d-%m-%Y")
        tree.insert("", tk.END, values=(row[0], data_formatada, row[2], row[3], row[4], row[5]))
    
    cur.close()
    conn.close()

# Função para calcular e exibir o saldo entre receitas e despesas
def exibir_saldo():
    conn = connect_db()
    cur = conn.cursor()

    query_receitas = "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'receita'"
    query_despesas = "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'despesa'"
    
    data_inicio_input = entry_data_inicio.get()
    data_fim_input = entry_data_fim.get()

    params = []

    if data_inicio_input and data_fim_input:
        try:
            data_inicio = datetime.strptime(data_inicio_input, "%d-%m-%Y").strftime("%Y-%m-%d")
            data_fim = datetime.strptime(data_fim_input, "%d-%m-%Y").strftime("%Y-%m-%d")
            query_receitas += " AND data BETWEEN %s AND %s"
            query_despesas += " AND data BETWEEN %s AND %s"
            params.extend([data_inicio, data_fim])
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use DD-MM-AAAA.")
            return

    cur.execute(query_receitas, params)
    total_receitas = cur.fetchone()[0] or 0.0

    cur.execute(query_despesas, params)
    total_despesas = cur.fetchone()[0] or 0.0

    saldo = total_receitas - total_despesas

    messagebox.showinfo("Saldo", f"Saldo total: R${saldo:.2f}\nReceitas: R${total_receitas:.2f}\nDespesas: R${total_despesas:.2f}")

    cur.close()
    conn.close()

# Função para excluir um lançamento
def excluir_lancamento():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        lancamento_id = item['values'][0]

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM lancamentos WHERE id = %s", (lancamento_id,))
        conn.commit()
        cur.close()
        conn.close()

        tree.delete(selected_item)
        messagebox.showinfo("Sucesso", "Lançamento excluído com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Nenhum lançamento selecionado!")

# Interface gráfica
root = tk.Tk()
root.title("Gestão Financeira")
root.geometry("700x600")

# Labels e Entradas
tk.Label(root, text="Data (DD-MM-AAAA)").grid(row=0, column=0)
entry_data = tk.Entry(root)
entry_data.grid(row=0, column=1)

tk.Label(root, text="Descrição").grid(row=1, column=0)
entry_descricao = tk.Entry(root)
entry_descricao.grid(row=1, column=1)

tk.Label(root, text="Valor").grid(row=2, column=0)
entry_valor = tk.Entry(root)
entry_valor.grid(row=2, column=1)

tk.Label(root, text="Categoria").grid(row=3, column=0)
entry_categoria = tk.Entry(root)
entry_categoria.grid(row=3, column=1)

tk.Label(root, text="Data Início (DD-MM-AAAA)").grid(row=4, column=0)
entry_data_inicio = tk.Entry(root)
entry_data_inicio.grid(row=4, column=1)

tk.Label(root, text="Data Fim (DD-MM-AAAA)").grid(row=4, column=2)
entry_data_fim = tk.Entry(root)
entry_data_fim.grid(row=4, column=3)

# Botões
tk.Button(root, text="Adicionar Receita", command=lambda: add_lancamento("receita")).grid(row=5, column=0, pady=10)
tk.Button(root, text="Adicionar Despesa", command=lambda: add_lancamento("despesa")).grid(row=5, column=1, pady=10)
tk.Button(root, text="Exibir Todas", command=lambda: exibir_lancamentos()).grid(row=6, column=0, pady=10)
tk.Button(root, text="Exibir Receitas", command=lambda: exibir_lancamentos("receita")).grid(row=6, column=1, pady=10)
tk.Button(root, text="Exibir Despesas", command=lambda: exibir_lancamentos("despesa")).grid(row=6, column=2, pady=10)
tk.Button(root, text="Excluir Selecionado", command=excluir_lancamento).grid(row=7, column=0, columnspan=3, pady=10)
tk.Button(root, text="Exibir Saldo", command=exibir_saldo).grid(row=7, column=2, pady=10)

# Tabela de Lançamentos
columns = ("ID", "Data", "Descrição", "Valor", "Categoria", "Tipo")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

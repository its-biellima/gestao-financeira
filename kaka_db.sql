-- Criação da tabela 'lancamentos' para armazenar receitas e despesas
CREATE TABLE lancamentos (
    id SERIAL PRIMARY KEY,             -- ID único e autoincrementado para cada lançamento
    data DATE NOT NULL,                -- Data do lançamento
    descricao TEXT NOT NULL,           -- Descrição do lançamento
    valor NUMERIC(10, 2) NOT NULL,     -- Valor do lançamento
    categoria TEXT NOT NULL,           -- Categoria do lançamento
    tipo TEXT NOT NULL CHECK (tipo IN ('receita', 'despesa'))  -- Tipo de lançamento (receita ou despesa)
);

-- Criação de índices para melhorar a performance de consultas
CREATE INDEX idx_lancamentos_data ON lancamentos(data);  -- Índice para consultas por data
CREATE INDEX idx_lancamentos_tipo ON lancamentos(tipo);  -- Índice para consultas por tipo (receita ou despesa)

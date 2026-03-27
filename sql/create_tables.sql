-- ============================================================
--  InovaNiver — Script de criação do banco de dados
--  PostgreSQL 14+
-- ============================================================

-- Cria o banco (execute fora de uma transação, se necessário)
-- CREATE DATABASE inovaniver;

-- Conecte-se ao banco antes de executar o restante:
-- \c inovaniver

-- ------------------------------------------------------------
--  TABELA: aniversarios
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS aniversarios (
    id                SERIAL          PRIMARY KEY,
    nome              VARCHAR(200)    NOT NULL,
    data_aniversario  DATE            NOT NULL,
    vinculo           VARCHAR(100)    NOT NULL,
    telefone          VARCHAR(20)     NULL,
    mensagem_enviada  BOOLEAN         NOT NULL DEFAULT FALSE,
    created_at        TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at        TIMESTAMPTZ     NULL
);

-- Índices para consultas por mês (filtro principal da aplicação)
CREATE INDEX IF NOT EXISTS idx_aniversarios_mes
    ON aniversarios (EXTRACT(MONTH FROM data_aniversario));

CREATE INDEX IF NOT EXISTS idx_aniversarios_data
    ON aniversarios (data_aniversario);

-- ------------------------------------------------------------
--  Comentários de documentação
-- ------------------------------------------------------------
COMMENT ON TABLE  aniversarios                    IS 'Registro de aniversários para notificação';
COMMENT ON COLUMN aniversarios.nome               IS 'Nome completo da pessoa';
COMMENT ON COLUMN aniversarios.data_aniversario   IS 'Data de nascimento ou data de aniversário a comemorar';
COMMENT ON COLUMN aniversarios.vinculo            IS 'Parentesco ou vínculo com a pessoa (ex: Amigo, Cliente, Filho)';
COMMENT ON COLUMN aniversarios.telefone           IS 'Número WhatsApp com código do país, sem espaços (ex: 5511999999999)';
COMMENT ON COLUMN aniversarios.mensagem_enviada   IS 'Indica se a mensagem de parabéns já foi enviada no ano corrente';
COMMENT ON COLUMN aniversarios.created_at         IS 'Data e hora de criação do registro';
COMMENT ON COLUMN aniversarios.updated_at         IS 'Data e hora da última atualização';

-- ------------------------------------------------------------
--  Dados de exemplo (opcional — remova em produção)
-- ------------------------------------------------------------
INSERT INTO aniversarios (nome, data_aniversario, vinculo, telefone, mensagem_enviada) VALUES
    ('Maria Silva',    TO_DATE('1990-' || LPAD(EXTRACT(MONTH FROM NOW())::TEXT, 2, '0') || '-05', 'YYYY-MM-DD'), 'Cliente',          '5511987654321', FALSE),
    ('João Souza',     TO_DATE('1985-' || LPAD(EXTRACT(MONTH FROM NOW())::TEXT, 2, '0') || '-15', 'YYYY-MM-DD'), 'Colega de trabalho', NULL,           FALSE),
    ('Ana Pereira',    TO_DATE('1995-' || LPAD(EXTRACT(MONTH FROM NOW())::TEXT, 2, '0') || '-' || LPAD(EXTRACT(DAY FROM NOW())::TEXT, 2, '0'), 'YYYY-MM-DD'), 'Amigo(a)', '5521999888777', FALSE);

-- Os dados de exemplo inserem registros no mês atual, sendo o terceiro
-- no dia de hoje, para demonstrar o destaque visual de aniversariante do dia.

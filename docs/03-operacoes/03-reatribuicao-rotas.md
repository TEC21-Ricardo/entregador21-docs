# Reatribuição de Rotas

## O que é Reatribuição de Rotas?

Reatribuição de Rotas é uma **função automática** que reprocessa e redistribui intimações para as rotas corretas baseado nas **rotas condicionais pré-configuradas**.

---

## Quando Usar Reatribuição de Rotas

### ✅ Ao Enviar Intimações Novas
- Quando envia um novo lote de intimações do cartório
- O sistema automaticamente distribui para as rotas corretas

### ✅ Ao Corrigir Rotas Indefinidas
- Após adicionar novos termos/bairros às rotas
- Reprocessa intimações que ficaram com rota indefinida

### ✅ Ao Alterar Configurações de Rotas
- Se as regras de rotas foram modificadas
- Redistribui as intimações conforme novas regras

---

## Como Acessar Reatribuição de Rotas

### Na Tabela de Intimações

1. **Acesse a página de Intimações** no painel administrativo
2. **Veja a tabela** com a listagem de intimações/ordens de serviço
3. **Localize as intimações** que deseja redistribuir
4. **Passe o mouse sobre os "..."** (três pontos) na linha da intimação
5. **Clique em "Reatribuir Rotas"** no menu que aparece

---

## Passo a Passo Detalhado

### Passo 1: Abrir Intimações

Navegue até a seção **Intimações** no menu lateral.

**Campos disponíveis para filtro:**
- Data Inicial / Data Final
- Cliente/Filial
- Status
- Origem
- Código de Intimação

---

### Passo 2: Selecionar Intimações

**Opções:**

**A) Redistribuir Uma por Uma**
- Localize a intimação específica na tabela
- Passe o mouse sobre os "..." da linha
- Clique em "Reatribuir Rotas"

**B) Redistribuir Múltiplas (se disponível)**
- Selecione as intimações desejadas (checkboxes)
- Clique no botão "Colocar destinos selecionados em Rota"
- Sistema redistribui todas selecionadas

---

### Passo 3: Confirmação

Após clicar em "Reatribuir Rotas":

✅ **Sistema valida** as rotas condicionais  
✅ **Processa** cada intimação baseado nos critérios  
✅ **Atribui automaticamente** à rota correta  
✅ **Salva** a nova atribuição

---

## Resultado: Rotas Definidas ✅

Após reatribuição bem-sucedida:

```
Status ANTES:          Status DEPOIS:
Rota Indefinida   →    Rota 1
Rota Indefinida   →    Rota 2
Rota Indefinida   →    Rota 3
```

---

## E se Ficar Rota Indefinida?

Às vezes, mesmo após reatribuição, algumas intimações podem permanecer com **"Rota Indefinida"**.

**Motivo usual:** Bairro/termo que não está mapeado nas rotas condicionais

**Exemplo:**
```
Intimação chega com: "V. Mariana"
Rotas cadastradas têm: "Vila Mariana"
Resultado: Rota Indefinida ❌
```

**Solução:** Ver [Atribuir Rotas aos Selecionados](./04-atribuir-rotas-selecionados.md)

---

## Fluxo Completo de Rotas

```
1. Envio de Intimações
        ↓
2. Reatribuição de Rotas (automática)
        ↓
3. Validar Resultado
        ├─ Todas com rota definida? → ✅ Pronto!
        └─ Tem indefinidas? → Ir para Atribuir Rotas Selecionados
        ↓
4. Zero Entregas Indefinidas
        ↓
5. Enviar para Motoboy
```

---

## Dicas Importantes

### 💡 Faça Frequentemente
Após cada lote de intimações, execute reatribuição de rotas para garantir distribuição correta.

### 💡 Monitore Resultado
Sempre verifique se restaram rotas indefinidas após reatribuição.

### 💡 Manutenção de Rotas
Periodicamente revise o mapeamento de rotas para adicionar novos bairros/termos encontrados.

---

## Checklist: Reatribuição de Rotas

- [ ] Intimações carregadas na plataforma
- [ ] Acessada página de Intimações
- [ ] Selecionadas as intimações para redistribuir
- [ ] Clicado em "Reatribuir Rotas"
- [ ] Verificado resultado (rotas definidas)
- [ ] Tratadas rotas indefinidas (se necessário)
- [ ] Pronto para enviar aos motoboys

---

## Próximo Passo

Se houve rotas indefinidas, acesse [Atribuir Rotas aos Selecionados](./04-atribuir-rotas-selecionados.md)  
Caso contrário, prossiga com distribuição aos motoboys.

# Envio de Rota para Entregador

## O que é Envio de Rota?

Envio de Rota é o processo de **enviar os destinos/entregas agrupadas para o aplicativo do entregador (motoboy)**, após já terem sido filtradas e agrupadas por rota.

**Objetivo:** Disponibilizar as entregas organizadas no app mobile para que o motoboy possa executar as entregas.

---

## Visualização: Envio de Rota para Entregador

![Envio de Rota - Demonstração](./gifs/envio-rota-entregador.gif)

> 💡 **Dica:** Use Ctrl + para aumentar o zoom se a imagem ficar pequena

---

## Opções de Envio de Entregas

Existem **duas formas** de enviar as entregas após agrupá-las:

### 🚚 **Opção 1: Enviar para "Em Rota"**
Envia imediatamente para o aplicativo do motoboy para execução imediata.

**Status:** 
- Antes: `Registrado` → Depois: `Em Rota` ✅
- As entregas aparecem no app do motoboy para entrega

**Quando usar:**
- Quando deseja enviar as entregas para execução no mesmo dia
- Quando as entregas estão prontas para o entregador

---

### 📦 **Opção 2: Colocar em "Em Separação"**
Coloca as entregas em status de separação, aguardando o próximo ciclo.

**Status:**
- Antes: `Registrado` → Depois: `Em Separação`
- As entregas ficam em processamento

**Fluxo Típico:**
1. **Dia 1:** Entregas colocadas em `Em Separação`
2. **Dia 2:** Sistema as **filtra automaticamente**
3. **Dia 2:** Rotas são **criadas/redistribuídas**
4. **Dia 2:** Entregas movem para `Em Rota` (prontas para entrega)

**Quando usar:**
- Quando as entregas chegam no final do dia
- Quando você deseja processar tudo no dia seguinte
- Para melhor organização do fluxo operacional

---

## Quando Fazer Envio de Rota

### ✅ Após Agrupamento de Entregas
- Depois de agrupar os destinos
- Antes de enviar ao motoboy

### ✅ Com Entregas Já Filtradas
- As entregas já devem estar filtradas por rota
- E agrupadas para melhor organização

### ✅ Pronto para Execução
- Quando as entregas estão prontas para o entregador (Em Rota)
- Ou quando deseja colocar em separação (Em Separação)

---

## Como Funciona o Envio

### **Passo 1: Selecionar Entregas**

1. Na página de **Intimações**
2. Filtre as entregas por rota
3. Agrupe os destinos (se não feito ainda)
4. **Selecione as entregas** que deseja enviar

### **Passo 2: Escolher Ação**

Com as entregas selecionadas, escolha uma das opções:

#### **Opção A: Enviar para "Em Rota"**
1. Procure pela opção **"Enviar para o Entregador"** ou **"Enviar Rota"**
2. As entregas mudam de status: `Registrado` → `Em Rota` ✅
3. Aparecem imediatamente no app do motoboy

#### **Opção B: Colocar em "Em Separação"**
1. Procure pela opção **"Colocar em Separação"** ou **"Separação"**
2. As entregas mudam de status: `Registrado` → `Em Separação`
3. Serão processadas e filtradas automaticamente no próximo ciclo

### **Passo 3: Confirmação**

1. O sistema processa a ação
2. **Status atualizado** com sucesso
3. Entregas prontas para:
   - **Em Rota:** Execução imediata no app do motoboy
   - **Em Separação:** Processamento automático no dia seguinte

---

## Resultado: Status das Entregas

### **Se você escolheu "Em Rota":**
- ✅ Entregas aparecem no app do motoboy
- ✅ Organizadas por rota
- ✅ Em ordem (agrupadas)
- ✅ Prontas para execução imediata
- 📊 Status: `Em Rota`

### **Se você escolheu "Em Separação":**
- ✅ Entregas colocadas em processamento
- ✅ Status: `Em Separação`
- ⏳ Aguardam próximo ciclo de processamento
- 📊 Serão filtradas e enviadas para `Em Rota` automaticamente no dia seguinte

---

## Fluxo Completo de Distribuição

### **Ciclo Completo (Em Rota):**
```
1. Envio de Intimações (Registrado)
        ↓
2. Reatribuição de Rotas (automática)
        ↓
3. Filtrar Rotas
        ↓
4. Agrupamento de Entregas
        ↓
5. Envio de Rota para Entregador ← Você está aqui
        ↓
6. Status: Registrado → EM ROTA ✅
        ↓
7. Motoboy Recebe no App
        ↓
8. Execução das Entregas
```

### **Ciclo com Separação (Em Separação):**
```
1. Envio de Intimações (Registrado)
        ↓
2. Reatribuição de Rotas (automática)
        ↓
3. Filtrar Rotas
        ↓
4. Agrupamento de Entregas
        ↓
5. Colocar em Separação ← Você está aqui
        ↓
6. Status: Registrado → EM SEPARAÇÃO
        ↓
7. [Próximo Dia] Sistema filtra automaticamente
        ↓
8. Status: Em Separação → EM ROTA ✅
        ↓
9. Motoboy Recebe no App
        ↓
10. Execução das Entregas
```

---

## Boas Práticas

### 💡 Verificar Antes de Enviar
- Valide que as entregas estão corretas
- Confirme as rotas e agrupamento
- Verifique se não há erros

### 💡 Acompanhar Envio
- Verifique se as entregas chegaram ao app
- Confirme com o motoboy o recebimento
- Esteja disponível para suporte

### 💡 Registrar Envios
- Documente quais rotas foram enviadas
- Registre a data e hora
- Mantenha histórico para auditoria

---

## Checklist: Envio de Rota

### **Antes do Envio:**
- [ ] Entregas filtradas por rota
- [ ] Entregas agrupadas
- [ ] Verificação realizada

### **Escolher Ação:**
- [ ] Opção selecionada (Em Rota OU Em Separação)
- [ ] Entregas selecionadas corretamente
- [ ] Ação executada

### **Após o Envio:**
- [ ] Status atualizado (Em Rota OU Em Separação)
- [ ] Confirmação visual no sistema
- [ ] Histórico registrado

### **Se Em Rota:**
- [ ] Confirmação do recebimento no app do motoboy
- [ ] Motoboy tem as entregas disponíveis

### **Se Em Separação:**
- [ ] Aguardar próximo ciclo de processamento
- [ ] Verificar filtro automático no dia seguinte
- [ ] Confirmar transição para Em Rota

---

## Próximo Passo

Após enviar para o entregador, o motoboy executa as entregas conforme a rota recebida.

**Acompanhamento:** Verifique o status das entregas no app do motoboy ou no dashboard de operações.

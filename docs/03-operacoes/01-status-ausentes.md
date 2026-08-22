# Status Ausentes

## O que é Status Ausente?

O status "Ausente" é registrado quando um motoboy tenta fazer uma entrega e a pessoa não está no local. A plataforma permite configurar quantas tentativas de ausência são necessárias antes de marcar definitivamente como entrega não realizada.

---

## Configuração de Ausentes

Antes de iniciar as operações, é essencial validar com o cartório as regras de ausentes que serão aplicadas:

### Definir Número de Ausentes

**Pergunta para o Cartório:**
- Quantas tentativas de ausência são permitidas? (1x, 2x ou 3x)

**Exemplos:**
- **1x Ausente**: Após 1 tentativa malsucedida, marca como não entregue
- **2x Ausente**: Permite 2 tentativas antes de marcar como não entregue  
- **3x Ausente**: Permite 3 tentativas antes de marcar como não entregue

---

## Agendamento de Ausentes

**Pergunta para o Cartório:**
- As tentativas de ausência serão em **dias diferentes** ou no **mesmo dia**?

### Mesmo Dia
- As múltiplas tentativas ocorrem no mesmo dia
- Exemplo: 3 tentativas em um único dia

### Dias Diferentes
- Cada tentativa ocorre em dia diferente
- Exemplo: 1ª tentativa dia 01, 2ª tentativa dia 02, 3ª tentativa dia 03

---

## Envio de Intimações com Ausentes

**Pergunta para o Cartório:**
- O envio para o motoboy será **automático** ou **manual**?

### Envio Automático
- O sistema envia automaticamente as intimações para o motoboy conforme a agenda de ausentes
- Sem necessidade de intervenção manual

### Envio Manual (Controle do Entregador)
- O motoboy/operador controla manualmente quando enviar as próximas tentativas
- Usa os campos **Distribuído** e **Expresso** no app para gerenciar o envio
- Estratégia: 
  - Dia 1: Envia do campo "Distribuído" para "Expresso"
  - Dia 2: Move de "Expresso" de volta para "Distribuído" para nova tentativa
  - Continua até atingir o limite de ausentes

---

## Ajuste de Prazos

Quando configurar ausentes múltiplos, pode ser necessário **ajustar o prazo das intimações** no sistema do cartório.

**Por exemplo:**
- Se a intimação original vence em 5 dias e há 3 tentativas em dias diferentes
- O prazo pode precisar ser estendido para 7-8 dias para acomodar as 3 tentativas

**Validar com o cartório:**
- Qual será o novo prazo considerando o número e espaçamento de ausentes?

---

## Checklist: Status Ausentes

- [ ] Validado número de tentativas (1x, 2x ou 3x)
- [ ] Definido espaçamento (mesmo dia ou dias diferentes)
- [ ] Configurado tipo de envio (automático ou manual)
- [ ] Ajustado prazo das intimações (se necessário)
- [ ] Documentado em planilha para referência

---

## Próximo Passo

Após definir a política de ausentes, prossiga para [Criação de Rotas Condicionais](./02-criacao-rotas.md)

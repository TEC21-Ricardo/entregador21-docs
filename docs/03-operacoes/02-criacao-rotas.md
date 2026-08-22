# Criação de Rotas Condicionais

## O que são Rotas Condicionais?

Rotas condicionais são **regras automáticas** que distribuem automaticamente as intimações para rotas específicas baseado em critérios definidos (como bairro, CEP, ou outros atributos da intimação).

**Exemplo:**
```
SE bairro = "Centro" → Vai para ROTA 1
SE bairro = "Zona Sul" → Vai para ROTA 2  
SE bairro = "Zona Norte" → Vai para ROTA 3
```

Isso torna a distribuição de entregas muito mais ágil e organizada.

---

## Como Funciona o Processo

### 1️⃣ Cartório Cria a Documentação

O cartório prepara um documento (planilha Excel ou Word) contendo as **regras de rotas condicionais** que deseja aplicar.

**Exemplo de planilha:**

```
BAIRRO              | ROTA
--------------------|-------
Centro              | Rota 1
Zona Sul            | Rota 2
Zona Norte          | Rota 3
Zona Leste          | Rota 4
Zona Oeste          | Rota 5
```

### 2️⃣ Envio para Desenvolvedor

O cartório envia o documento para os **desenvolvedores do Entregador21** com as rotas a cadastrar.

**Quem recebe:** Desenvolvedores da equipe TEC21/Entregador21

### 3️⃣ Cadastro no Sistema

Os desenvolvedores cadastram as rotas condicionais na plataforma, configurando as regras.

**Resultado:** As rotas estão prontas para serem usadas

---

## Tipos de Critérios para Rotas

As rotas podem ser criadas baseadas em diferentes critérios:

### Por Bairro
```
Bairro = "Centro" → Rota 1
Bairro = "Vila Mariana" → Rota 2
```

### Por CEP
```
CEP começa com "01" → Rota 1
CEP começa com "02" → Rota 2
```

### Por Código do Bairro
```
Código Bio-X → Rota 1
Código Bio-Y → Rota 2
```

### Por Outros Atributos
- Zona geográfica
- Cidade
- Região
- Combinação de vários critérios

---

## Validação com o Cartório

Antes de enviar para cadastro, **validar com o cartório:**

✅ Quais são os critérios principais? (bairro, CEP, código?)
✅ Quantas rotas serão necessárias?
✅ Qual é o mapeamento exato de cada critério?
✅ Há bairros/locais específicos que precisam rotas especiais?

---

## Após Criação das Rotas

Depois que os desenvolvedores cadastram as rotas, você pode:

1. **Enviar intimações** → Sistema redistribui automaticamente
2. **Usar a função "Reatribuir Rotas"** → Para reprocessar intimações já enviadas
3. **Tratar rotas indefinidas** → Ver [Atribuição de Rotas Selecionadas](./04-atribuir-rotas-selecionados.md)

---

## Bairros Abreviados

⚠️ **Atenção:** Às vezes o bairro vem abreviado no sistema do cartório, mas a abreviação **não constava no documento original** de mapeamento de rotas.

**Exemplo:**
- Documento original tinha: "Vila Mariana"
- Sistema envia: "V. Mariana" (abreviado)
- Resultado: Rota indefinida ❌

**Solução:** Ver [Atribuir Rotas aos Selecionados](./04-atribuir-rotas-selecionados.md) para corrigir e adicionar novos termos

---

## Checklist: Criação de Rotas

- [ ] Validado com cartório critérios de rotas
- [ ] Planilha/documento de mapeamento preparado
- [ ] Enviado para desenvolvedores
- [ ] Rotas cadastradas no sistema
- [ ] Testada distribuição com dados de teste

---

## Próximo Passo

Após criar as rotas, prossiga para [Reatribuição de Rotas](./03-reatribuicao-rotas.md)

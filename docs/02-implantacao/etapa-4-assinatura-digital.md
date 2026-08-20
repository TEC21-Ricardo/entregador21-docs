# Etapa 4: Assinatura Digital (AR Digital)

## Objetivo

Configurar assinatura digital dos motoboys para comprovação de entrega com AR Digital (Aviso de Recebimento Eletrônico).

## O que é AR Digital?

**AR Digital** (Aviso de Recebimento Digital) é um comprovante eletrônico que substitui o papel tradicional de AR (Aviso de Recebimento).

### Benefícios

- 📱 Mais prático que papel
- 🔐 Segurança com assinatura digital
- 📊 Rastreamento eletrônico
- 🌍 Compatível com legislação
- ⚡ Agilidade no processo

## Pré-Requisitos

Antes de começar, valide com o cartório:

```
☐ Cartório trabalha com AR Digital?
☐ Sistema cartório suporta AR Digital?
☐ Há suporte de leis estaduais?
☐ Certificado digital disponível? (conforme estado)
```

## Passo 1: Decisão do Cartório

### Pergunta Chave

Validar com o cartório se trabalharão com **ARDIGITAL**.

**Caso Positivo (SIM):**
- ✅ Prossiga com coleta de assinatura
- ✅ Configure no Entregador21
- ✅ Integre com sistema cartório

**Caso Negativo (NÃO):**
- ⏭️ Pule para Etapa 5
- ⏭️ Use apenas sistema de acompanhamento físico
- ⏭️ Documentar que não utiliza AR Digital

## Passo 2: Coleta de Assinatura dos Motoboys

### O Que É Necessário

Assinatura de cada motoboy que fará entregas com AR Digital.

### Material Necessário

- 📄 Papel branco (sem linhas)
- 🖊️ Caneta preta (escrita legível)
- 📱 Smartphone/Scanner para digitalizar

### Instruções para Coleta

Solicite ao cartório que oriente aos motoboys:

#### 📋 Comunicado aos Motoboys

```
Pessoal, para implementarmos o sistema AR Digital com assinatura eletrônica,
solicitamos que façam o seguinte:

1️⃣ ASSINATURA EM PAPEL
   - Assinem em papel em branco
   - Use caneta preta
   - Escrita legível (não usar maiúsculas contínuas)
   - Assine por extenso (não abreviar)

2️⃣ EXEMPLO VISUAL
   [Mostrar exemplo de assinatura legível]

3️⃣ ESCANEAR/FOTOGRAFAR
   - Use o app do celular
   - Tire foto em boa iluminação
   - Certifique que a assinatura está toda visível
   - Salve como JPG ou PNG

4️⃣ ENVIAR ARQUIVO
   - Renomeie o arquivo como: NOME_COMPLETO.jpg
   - Exemplo: ricardononato.jpg (sem espaços, tudo minúsculo)
   - Envie via WhatsApp/Email
```

### Exemplo de Arquivo

```
Entrada:
├─ Assinatura_motoboy.jpg (INCORRETO - nome muito comprido)
└─ ricardononato.jpg (CORRETO)
```

### Armazenamento de Assinatura Coletada

Após receber as assinaturas escaneadas:

1. **Organize em Pasta**
   ```
   \\sp21\Temp\Avengers\Suporte\Entregador21\[Estado]\
   └── Assinaturas_Motoboys\
       ├── ricardononato.jpg
       ├── andersonsilva.jpg
       └── carlosmendes.jpg
   ```

2. **Valide Qualidade**
   - ✅ Assinatura legível
   - ✅ Arquivo em JPG/PNG
   - ✅ Resolução adequada (mín 150 DPI)
   - ✅ Tamanho razoável (100KB-2MB)

3. **Documente**
   - Data de coleta
   - Nome do motoboy
   - Status do arquivo

## Passo 3: Configuração no Entregador21

### Upload de Assinatura

#### Via SGC (Recomendado)

1. **Acesse SGC**
   - URL: https://sgc.entregador21.com
   - Autentique-se

2. **Navegue para Motoboys**
   - Menu → Motoboys → [Selecione motoboy]

3. **Seção de Assinatura**
   - Clique em "Adicionar Assinatura"
   - Envie o arquivo JPG/PNG
   - Confirme qualidade
   - Salve

4. **Validação**
   - Sistema valida o arquivo
   - Confirma legibilidade
   - Ativa para AR Digital

#### Estrutura no SGC

```
CADASTRO DO MOTOBOY
├─ Informações Básicas
│  ├─ Nome
│  ├─ Celular
│  └─ Email
├─ Assinatura Digital
│  ├─ Upload Arquivo
│  ├─ Data Coleta
│  └─ Status
└─ Permissões
   ├─ AR Digital: ✅ Ativado
   └─ Acesso App: ✅ Ativado
```

## Passo 4: Validação de Assinatura

### Testes

Após configurar assinaturas:

1. **Visualizar no Sistema**
   - ✅ Abra perfil do motoboy
   - ✅ Verifique assinatura aparece
   - ✅ Valide legibilidade

2. **Testar em Entrega**
   - ✅ Gere uma intimação de teste
   - ✅ Baixe pelo app
   - ✅ Complete entrega
   - ✅ Valide assinatura no PDF

3. **Geração de PDF**
   - ✅ AR Digital gerado corretamente
   - ✅ Assinatura aparece no documento
   - ✅ Data e hora registradas
   - ✅ QR Code presente (conforme legislação)

## Problemas Comuns

### ❓ Assinatura não legível

**Sinal:** Sistema rejeita arquivo ou legibilidade baixa

**Solução:**
1. Peça para o motoboy assinar novamente
2. Imprima exemplo com escrita legível
3. Use melhor iluminação ao fotografar
4. Escaneie em maior resolução

**Prevenção:**
- Forneça caneta adequada
- Oriente sobre escrita por extenso
- Teste antes de implantar

### ❓ Arquivo corrompido

**Sinal:** Erro ao fazer upload

**Solução:**
1. Recolha assinatura
2. Digitalize em melhor qualidade
3. Valide formato (JPG/PNG)
4. Comprove tamanho arquivo

### ❓ Assinatura desaparece após entrega

**Sinal:** AR Digital gerado sem assinatura

**Solução:**
1. Verifique se assinatura está ativa em perfil
2. Revise configuração no SGC
3. Teste novamente
4. Contate Daniel se persistir

## Checklist da Etapa 4

- [ ] Cartório confirmou uso de AR Digital
- [ ] Material coletado (papel, caneta preta)
- [ ] Motoboys instruídos
- [ ] Assinaturas coletadas e escaneadas
- [ ] Arquivos organizados e nomeados corretamente
- [ ] Qualidade de imagens validada
- [ ] Upload realizado no SGC
- [ ] Assinaturas visíveis nos perfis
- [ ] Testes de entrega realizados
- [ ] AR Digital gerado com assinatura
- [ ] Validação com cartório realizada

## Próximo Passo

Após configurar assinaturas digitais, prossiga para [Etapa 5 - Testes de Rotina](./etapa-5-testes.md)

---

**Duração estimada**: 3-7 dias  
**Responsáveis**: Cartório (coleta), Suporte (configuração), Daniel (integração)  
**Material**: Papel, caneta preta, scanner/smartphone

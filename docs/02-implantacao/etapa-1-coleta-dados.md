# Etapa 1: Coleta de Dados do Cartório

## Objetivo

Coletar informações essenciais do cartório necessárias para criar o ambiente de produção no Entregador21.

## Responsáveis

- 👤 **Suporte/Implantação**: Responsável pela comunicação
- 👤 **Cartório**: Fornecimento das informações

## Passos

### 1️⃣ Verificar Contato com Anderson

Antes de enviar o formulário, verifique com Anderson o contato direto do responsável pelo setor de protesto.

**Ações:**
- [ ] Solicitar a Anderson o contato principal
- [ ] Validar se há histórico de comunicação
- [ ] Confirmar disponibilidade do responsável

### 2️⃣ Criar Grupo de Comunicação

Estabeleça um canal de comunicação centralizado:

- 📱 **Recomendado**: Grupo WhatsApp
- **Responsável**: Anderson ou Suporte
- **Participantes**: 
  - Responsável cartório
  - Equipe suporte TEC21
  - DEVs do sistema cartório (conforme necessário)

### 3️⃣ Solicitar Informações ao Cartório

Entre em contato com o responsável pelo setor de protesto e solicite as seguintes informações:

#### Mensagem Padrão

```
Pessoal, vocês podem me passar:

📋 Nome do cartório
📄 CNPJ
📍 Endereço completo
🎨 Logomarca (se tiver, formato JPG/PNG)

Para gerarmos e montarmos o ambiente de vocês.
```

### 4️⃣ Dados Esperados

Os dados que você deve receber são:

| Campo | Exemplo | Formato |
|-------|---------|---------|
| Nome do Cartório | Cartório de Protesto de DF | Texto |
| CNPJ | 12.345.678/0001-00 | XX.XXX.XXX/XXXX-XX |
| Endereço | Rua X, nº 123, Brasília - DF | Texto completo |
| Logomarca | logo.png | Imagem JPG/PNG |

## Exemplo de Resposta do Cartório

```
Nome do cartório: Cartório de Protesto do Distrito Federal
CNPJ: 34.028.316/0001-78
Endereço: SBS Quadra 01, Bloco J, nº 60 - Brasília - DF - CEP: 70070-900
Logomarca: [Arquivo anexado]
```

## Armazenamento de Dados

⚠️ **IMPORTANTE**: Após coletar os dados:

1. Salve as informações em local seguro
2. Anote data de coleta
3. Confirme com o cartório os dados recebidos
4. Comunique ao Daniel para criação do ambiente

## Checklist da Etapa 1

- [ ] Contato com Anderson confirmado
- [ ] Grupo WhatsApp criado
- [ ] Mensagem de solicitação enviada
- [ ] Dados recebidos do cartório
- [ ] Logomarca obtida (se disponível)
- [ ] Dados validados com o cartório
- [ ] Informações documentadas

## Problemas Comuns

### ❓ Cartório não responde
**Solução**: Agende reunião com Anderson para reforçar a importância

### ❓ Dados incompletos
**Solução**: Envie mensagem de acompanhamento solicitando os campos faltantes

### ❓ Logomarca em formato incorreto
**Solução**: Solicite em PNG ou JPG, preferencialmente com resolução mínima de 300x300px

## Próximo Passo

Após coletar todos os dados, prossiga para [Etapa 2 - Ambiente de Produção](./etapa-2-ambiente-producao.md)

---

**Duração estimada**: 3-5 dias  
**Responsável**: Suporte/Implantação  
**Entrada necessária**: Coordenação com Anderson

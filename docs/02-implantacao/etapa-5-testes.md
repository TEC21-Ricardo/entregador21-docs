# Etapa 5: Testes de Rotina

## Objetivo

Realizar testes completos do fluxo de intimação com dados reais antes de liberar para operação plena.

## Responsáveis

- 👤 **DEVs Sistema Cartório**: Gerar lote de teste
- 👤 **Suporte/Implantação**: Coordenar testes
- 👤 **Cartório**: Validar resultados

## Escopo de Testes

### Fluxo Completo a Testar

```
1. Envio de intimações (API)
        ↓
2. Processamento no Entregador21
        ↓
3. Distribuição para motoboys
        ↓
4. Entrega (com diferentes cenários)
        ↓
5. Importação de baixas
        ↓
6. Recepção de imagens/AR Digital
        ↓
7. Relatórios gerados
```

## Passo 1: Preparar Lote de Teste

### Solicitar ao Cartório

Entre em contato com os desenvolvedores do sistema cartório:

#### 📋 Formulário de Solicitação

```
SOLICITAÇÃO DE LOTE DE TESTE - ENTREGADOR21

Cartório: [Nome]
Estado: [UF]
Data da Solicitação: [DD/MM/YYYY]

Solicitar:
- Lote de X intimações para teste
- Dados variados (cidades, bairros, CEPs diferentes)
- Mix de tipos de intimação
- Incluir dados de devedores distintos

Objetivo:
- Testar fluxo completo de envio/importação
- Validar processamento de baixas
- Testar captura de imagens
- Validar AR Digital (se aplicável)
```

### Características do Lote de Teste

**Quantidade:** Recomendado 10-20 intimações

**Variedade:**
- ✅ Diferentes cidades
- ✅ Diferentes bairros  
- ✅ CEPs variados
- ✅ Diferentes valores
- ✅ Mix de tipos de intimação

**Dados Realistas:**
- ✅ Nomes e endereços válidos (mas ficitícios)
- ✅ Valores coerentes com realidade
- ✅ Datas de vencimento variadas

## Passo 2: Enviar Intimações via API

### Validar Integração

Com o lote pronto, valide o envio:

1. **Verifique Credenciais**
   ```
   ✅ Token de API válido
   ✅ Código do cliente correto
   ✅ Código do serviço correto
   ✅ Base URL correta
   ```

2. **Envie Primeiro Lote**
   - Use ferramenta: Postman / cURL / Script
   - Endpoint: `/IntimacoesV1/AdicionarIntimacao`
   - Método: POST
   - Content-Type: application/json

3. **Validate Resposta**
   - Código HTTP: 200 (sucesso) ou apropriado
   - Verifique se intimações foram registradas
   - Documente IDs das intimações

### Exemplo de Requisição

```json
{
  "token": "3c5f87a12d9be044f71e2c8b5a96dfe2b018c35d",
  "codCliente": 2,
  "codEntregador": 1,
  "codIntegracaoEntregador": 0,
  "codServico": 128,
  "dataInicio": "01/01/2024",
  "horaInicio": "09:00:00",
  "dataLimite": "10/01/2024",
  "horaLimite": "18:00:00",
  "intimacoes": [
    {
      "empresaID": 221,
      "clienteID": 2,
      "cpfCnpjPagador": "12345678901",
      "protocolo": "P001",
      "protocoloDistribuidor": "D001",
      "nomePagador": "João Silva",
      "enderecoPagador": "Rua A, 123",
      "cidadePagador": "Brasília",
      "estadoPagador": "DF",
      "cepPagador": "70000000",
      "valorPrincipal": 1000.00,
      "valorTotal": 1150.00,
      "... outros campos obrigatórios ..."
    }
  ]
}
```

## Passo 3: Acompanhar Processamento

### Verificar Status no Dashboard

1. **Acesse Dashboard**
   - URL: https://app.entregador21.com
   - Autentique como admin

2. **Menu → Intimações**
   - Filtre por data de envio
   - Verifique status de cada intimação
   - Status esperado: "Recebida" ou "Processando"

3. **Acompanhe o Fluxo**
   ```
   Recebida → Distribuída → Em Entrega → Entregue/Ausente
   ```

### Métricas a Monitorar

- ✅ Taxa de recebimento
- ✅ Tempo de processamento
- ✅ Distribuição para motoboys
- ✅ Taxa de aceite pela plataforma

## Passo 4: Testar Diferentes Cenários de Entrega

### Cenário 1: Entrega Bem-Sucedida

**Processo:**
1. Motoboy recebe intimação no app
2. Navega até o local
3. Entrega ao destinatário
4. Coleta assinatura
5. Tira foto (se configurado)
6. Confirma entrega

**Validação:**
- ✅ Status muda para "Entregue"
- ✅ Data/hora registrada
- ✅ Assinatura presente
- ✅ Fotos anexadas

### Cenário 2: Entrega com Ausência

**Processo:**
1. Motoboy se dirige ao local
2. Ninguém encontrado
3. Marca como "Ausente"
4. Foto do local (se necessário)
5. Anotações

**Validação:**
- ✅ Status muda para "Ausente"
- ✅ Anotações salvas
- ✅ Próxima tentativa agendada
- ✅ Relatório gerado

### Cenário 3: Erro de Entrega

**Processo:**
1. Motoboy não consegue entregar (recusa, endereço errado, etc.)
2. Registra motivo do erro
3. Tira foto se aplicável

**Validação:**
- ✅ Status muda para "Erro"
- ✅ Motivo registrado
- ✅ Escalação criada (se necessário)
- ✅ Notificação gerada

**Obs: IMPORTANTE testar a importação das entregas com situação de ausente**

## Passo 5: Validar Importação de Baixas

### Fluxo de Retorno

1. **Motoboy Conclui Entrega**
   - App registra tudo
   - Sincroniza com servidor

2. **Sistema Cartório Importa**
   - Conecta-se à API de retorno
   - Puxa informações de entrega
   - Importa status
   - Atualiza sua base

3. **Validação**
   - ✅ Status importado corretamente
   - ✅ Data/hora sinc
   - ✅ Dados coerentes
   - ✅ Sem duplicatas

### Teste de Integração de Retorno

```
Entregador21 (Status) → API Retorno → Sistema Cartório
      ✅ Entregue              ✅                ✅
      ✅ Ausente               ✅                ✅
      ✅ Erro                  ✅                ✅
```

## Passo 6: Validar Recepção de Imagens e AR Digital

### Imagens de Entrega

**O que validar:**
- ✅ Fotos enviadas pelo motoboy
- ✅ Qualidade das imagens
- ✅ Vinculação correta à entrega
- ✅ Acesso no dashboard

### AR Digital (se aplicável)

**O que validar:**
- ✅ PDF gerado com assinatura
- ✅ Data e hora corretas
- ✅ QR Code presente
- ✅ Todos os dados incluídos
- ✅ Exportável/Imprimível

### Teste de Vinculação

```
Entrega → Assinatura → PDF → Relatório
  ✅          ✅        ✅       ✅
```

## Passo 7: Gerar e Validar Relatórios

### Relatórios a Testar

1. **Relatório de Entregas**
   - Filtre por período
   - Valide totalizações
   - Verifique status

2. **Relatório por Motoboy**
   - Entregas por entregador
   - Taxa de sucesso
   - Ausentes

3. **Relatório de Valores**
   - Totais enviados
   - Valores entregues
   - Diferenças

4. **Relatório de AR Digital**
   - Avisos gerados
   - Assinaturas coletadas
   - PDFs disponíveis

### Validação de Relatórios

- ✅ Dados corretos
- ✅ Totais conferem
- ✅ Período correto
- ✅ Formato legível
- ✅ Exportável em PDF/Excel

## Passo 8: Documentar Resultado dos Testes

### Relatório de Testes

Crie documento com:

```markdown
# RELATÓRIO DE TESTES - ENTREGADOR21

## Informações Gerais
- Cartório: [Nome]
- Estado: [UF]
- Data dos Testes: [DD/MM/YYYY]
- Responsáveis: [Nomes]

## Resumo de Testes

### Lote Enviado
- Total de intimações: 15
- Taxa de aceitação: 100% (15/15)
- Tempo processamento: 5 minutos

### Cenários Testados
- [x] Entrega bem-sucedida: ✅ PASSOU
- [x] Ausente: ✅ PASSOU  
- [x] Erro/Recusa: ✅ PASSOU

### Importação de Baixas
- [x] Status importado: ✅ OK
- [x] Datas sincronizadas: ✅ OK
- [x] Sem duplicatas: ✅ OK

### AR Digital
- [x] PDF gerado: ✅ OK
- [x] Assinatura presente: ✅ OK
- [x] QR Code: ✅ OK

### Relatórios
- [x] Relatório de entregas: ✅ OK
- [x] Relatório por motoboy: ✅ OK
- [x] Valores: ✅ OK

## Resultado Final
✅ APROVADO PARA PRODUÇÃO

## Observações
- Nenhuma falha crítica identificada
- Sistema pronto para operação
- Recomenda-se treinamento de usuários

## Aprovação
Assinado por: [Nome]
Data: [DD/MM/YYYY]
```

## Checklist da Etapa 5

- [ ] Lote de teste solicitado aos DEVs
- [ ] Lote recebido com dados variados
- [ ] Intimações enviadas via API
- [ ] Respostas validadas
- [ ] Intimações visíveis no dashboard
- [ ] Entrega bem-sucedida testada
- [ ] Ausência testada
- [ ] Erro/Recusa testada
- [ ] Importação de baixas validada
- [ ] Imagens anexadas e visíveis
- [ ] AR Digital gerado (se aplicável)
- [ ] Assinatura presente no PDF (se aplicável)
- [ ] Relatórios gerados e validados
- [ ] Documento de testes assinado
- [ ] Aprovação para produção obtida

## Após Testes

### Se APROVADO ✅
- Prossiga para operação plena
- Agende treinamento dos operadores
- Documente configurações finais
- Inicie suporte

### Se REPROVADO ❌
- Identifique problema
- Comunique ao Daniel
- Realize correções
- Repita testes

## Próximo Passo

Após aprovação nos testes, o cartório está pronto para operação. 
Consulte [Operações](../03-operacoes/) para guias de uso.

---

**Duração estimada**: 5-7 dias  
**Responsáveis**: Suporte (coordenação), Cartório (execução), DEVs (suporte)  
**Saída**: Aprovação para produção

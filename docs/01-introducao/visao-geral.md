# Visão Geral do Entregador21

## O que é Entregador21?

**Entregador21** é uma solução inovadora de software como serviço (SaaS) desenvolvida pela TEC21 para ajudar os cartórios de protesto a otimizarem o processo de intimação dos devedores.

## Problemas que Resolve

### ❌ Antes (Processo Manual)
- Impressão manual de notificações
- Entrega desorganizada
- Sem monitoramento em tempo real
- Custos elevados com entrega
- Dificuldade em rastrear o processo

### ✅ Depois (Com Entregador21)
- Automação da impressão
- Sistema organizado de entrega
- Monitoramento em tempo real
- Redução de custos
- Rastreamento completo do processo
- Suporte a AR Digital (Aviso de Recebimento eletrônico)

## Principais Funcionalidades

### 1. **Gerenciamento de Intimações**
Receba, processe e acompanhe intimações de forma centralizada através da API integrada.

### 2. **Monitoramento em Tempo Real**
Dashboard com status atualizado de todas as entregas, entregas bem-sucedidas, ausentes e com erros.

### 3. **Assinatura Digital (AR Digital)**
Integração com sistema de assinatura eletrônica para comprovação digital de entrega.

### 4. **Gestão de Motoboys**
Sistema completo de cadastro e monitoramento de entregadores com geolocalização.

### 5. **Relatórios Detalhados**
Relatórios customizáveis com informações de entregas, status, valores e análises.

### 6. **Integração de API**
API robusta para integração com sistemas cartorários existentes.

## Benefícios Principais

| Benefício | Descrição |
|-----------|-----------|
| **Redução de Custos** | Automação reduz gastos com operações manuais |
| **Aumento de Produtividade** | Processamento mais rápido de intimações |
| **Rastreabilidade** | Histórico completo de cada intimação |
| **Conformidade Legal** | Suporte a requisitos legais de cartórios |
| **Melhor Experiência** | Interface intuitiva para operadores |
| **Segurança** | Dados protegidos e backup automático |

## Componentes Principais

### 🖥️ **Plataforma Web**
Interface para gerenciamento, cadastros e monitoramento.

### 📱 **Aplicativo Mobile**
App para motoboys registrar entregas, fotografias e assinaturas.

### 🔌 **API REST**
Para integração com sistemas cartorários.

### 📊 **Dashboard**
Visualização de métricas e status em tempo real.

### 🔐 **Sistema de Autenticação**
Controle de acesso por perfil de usuário (Admin, Operador, Motoboy).

## Fluxo Geral

```
1. Cartório gera intimação
        ↓
2. Sistema cartório envia para Entregador21 (API)
        ↓
3. Entregador21 processa e distribui para motoboys
        ↓
4. Motoboy realiza entrega com app mobile
        ↓
5. Registro de assinatura/foto no app
        ↓
6. Retorno de status e imagens (AR Digital)
        ↓
7. Relatórios gerados no dashboard
```

## Estados Suportados

Atualmente o Entregador21 opera em:

- 🔷 **DF** - Distrito Federal
- 🔶 **AM** - Amazonas
- 🟢 **MT** - Mato Grosso
- 🟡 **MA** - Maranhão
- 🔴 **RJ** - Rio de Janeiro
- 🟣 **GO** - Goiás

Cada estado pode ter layout específico de intimação conforme legislação local.

## Próximos Passos

- **Implantadores**: Vá para [Fase de Implantação](../02-implantacao/fase-integracao.md)
- **Operadores**: Vá para [Operações](../03-operacoes/dashboard.md)
- **Desenvolvedores**: Vá para [Integração de API](../04-integracao-api/autenticacao.md)

---

**Versão**: 1.0  
**Última atualização**: 2024

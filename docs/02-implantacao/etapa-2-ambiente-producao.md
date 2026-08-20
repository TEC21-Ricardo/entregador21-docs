# Etapa 2: Criação do Ambiente de Produção

## Objetivo

Solicitar ao Daniel que crie o ambiente de produção do Entregador21 com os dados coletados na Etapa 1.

## Responsáveis

- 👤 **Daniel**: Criação do ambiente e credenciais
- 👤 **Suporte/Implantação**: Intermediação
- 👤 **Cartório**: Fornecimento final de dados (conforme necessário)

## Passos

### 1️⃣ Preparar Solicitação para Daniel

Com os dados coletados na Etapa 1, prepare uma solicitação contendo:

```
Solicitação de Criação de Ambiente - Entregador21

Cartório: [Nome]
CNPJ: [CNPJ]
Endereço: [Endereço Completo]
Estado: [UF]
Data da Solicitação: [DD/MM/YYYY]
Responsável Contato: [Nome - Telefone]

Logomarca: [Anexada/Não disponível]
```

### 2️⃣ Enviar para Daniel

Encaminhe a solicitação para Daniel através de:
- 📧 Email
- 💬 Canal de comunicação interno
- 📱 Conforme protocolo TEC21

**Informações de Contato Daniel:**
- Repositório: `\\sp21\Temp\Avengers\Suporte\Entregador21\`
- Status de credenciais criadas: `Credenciais de Intregração` (pasta)

### 3️⃣ Acompanhamento

Ao solicitar, defina:
- ⏰ Prazo esperado de criação (geralmente 1-2 dias)
- 📋 Forma de entrega das credenciais
- 📞 Contato para dúvidas

## Saídas da Etapa 2

Quando Daniel criar o ambiente, ele fornecerá:

### 📋 Credenciais de Acesso

As credenciais fornecidas devem incluir:

```
CREDENCIAIS DE ACESSO - ENTREGADOR21
====================================

Cartório: [Nome do Cartório]
Data de Criação: [DD/MM/YYYY]

URL DE ACESSO: https://app.entregador21.com/cartorio-[codigo]

USUÁRIO ADMINISTRADOR:
- Email/Usuário: [usuario-adm]
- Senha Temporária: [senha]

CREDENCIAIS PARA API:
- Token de Autenticação: [token-api]
- Código do Cliente: [cod-cliente]
- Código do Serviço: [cod-servico]
- ID da Empresa: [id-empresa]

BASE URL: https://api.entregadoronline.com/api/

INFORMAÇÕES ADICIONAIS:
- Documentação disponível em: https://docs.entregador21.com
- Suporte técnico: suporte@tec21.com.br
```

### 📁 Armazenamento de Credenciais

**IMPORTANTE - SEGURANÇA:**

As credenciais devem ser armazenadas em:

```
\\sp21\Temp\Avengers\Suporte\Entregador21\Credenciais de Intregração\
```

**Estrutura de Pasta:**
```
Credenciais de Intregração/
├── [Estado - Sigla]/
│   ├── [Cartório]/
│   │   ├── credenciais.txt
│   │   ├── token_api.txt
│   │   └── informacoes.md
```

**Exemplo:**
```
Credenciais de Intregração/
├── DF/
│   ├── Cartório de Protesto DF/
│   │   ├── credenciais.txt
│   │   ├── token_api.txt
│   │   └── informacoes.md
```

## 🔐 Protocolo de Segurança

### Ao Receber Credenciais

1. ✅ Validar integridade da mensagem
2. ✅ Verificar se é do Daniel (contato confirmado)
3. ✅ Armazenar em local seguro
4. ✅ Fazer backup criptografado
5. ✅ Compartilhar apenas com pessoas autorizadas

### Ao Compartilhar com Cartório

1. ✅ Nunca envie por email sem criptografia
2. ✅ Prefira compartilhamento direto/pessoal
3. ✅ Solicite confirmação de recebimento
4. ✅ Documente quem recebeu
5. ✅ Instrua sobre mudança de senha

## Checklist da Etapa 2

- [ ] Dados da Etapa 1 validados
- [ ] Solicitação preparada para Daniel
- [ ] Solicitação enviada
- [ ] Acompanhamento iniciado
- [ ] Credenciais recebidas de Daniel
- [ ] Credenciais validadas
- [ ] Credenciais armazenadas em local seguro
- [ ] Backup realizado
- [ ] Notificação enviada ao cartório (próxima etapa)

## Próximo Passo

Após receber as credenciais, prossiga para [Etapa 3 - Cadastro de Usuários](./etapa-3-cadastro-usuarios.md)

---

**Duração estimada**: 1-2 dias  
**Responsável**: Daniel (criação), Suporte (coordenação)  
**Status**: Bloqueado até resposta de Daniel

# Etapa 3: Cadastro de Usuários

## Objetivo

Cadastrar usuários administrativos e operadores no Entregador21 após a criação do ambiente de produção.

## Responsáveis

- 👤 **Daniel**: Criação de credenciais de acesso
- 👤 **Suporte/Implantação**: Cadastro via SGC
- 👤 **Cartório**: Fornecimento de dados dos usuários

## Estrutura de Usuários

O Entregador21 possui dois tipos principais de usuários:

### 1️⃣ Usuários Administrativos

**Função:** Gerenciar a plataforma, configurações e relatórios

**Permissões:**
- ✅ Acesso ao dashboard completo
- ✅ Gerenciamento de usuários
- ✅ Visualização de relatórios
- ✅ Configurações do cartório
- ✅ Monitoramento geral

**Quantidade:** Geralmente 2-3 por cartório

### 2️⃣ Usuários Intimadores (Motoboys)

**Função:** Realizar entregas e registrar informações

**Permissões:**
- ✅ Acesso ao app mobile
- ✅ Registro de entrega
- ✅ Coleta de assinatura
- ✅ Fotografias
- ✅ Visualização de suas entregas

**Quantidade:** Conforme número de entregadores

## Passo 1: Coleta de Dados de Usuários Administrativos

### Formulário de Coleta

Solicite ao cartório os seguintes dados:

#### 📋 Usuários Administrativos

```
Usuário Administrativo #1
├─ Nome Completo: [Nome completo do usuário]
└─ CPF: [CPF válido - XXX.XXX.XXX-XX]

Usuário Administrativo #2
├─ Nome Completo: [Nome completo do usuário]
└─ CPF: [CPF válido - XXX.XXX.XXX-XX]
```

### Mensagem Padrão

```
Pessoal, para configurar o acesso administrativo ao Entregador21, 
vocês podem me passar os dados dos usuários administrativos:

📋 Usuários Administrativos (2-3 pessoas):
- Nome completo
- CPF

Estes usuários terão acesso total ao dashboard e poderão gerenciar 
a plataforma.
```

### Validação de Dados

Ao receber, valide:
- ✅ CPF válido (use validação de dígito verificador)
- ✅ Nome completo (sem abreviações)
- ✅ Sem duplicatas
- ✅ Informações coerentes

## Passo 2: Cadastro no SGC (Sistema de Gestão Entregador21)

Com os dados dos usuários administrativos, realize o cadastro:

### Acesso ao SGC

```
URL: https://sgc.entregador21.com
Autenticação: Use credenciais fornecidas pelo Daniel
```

### Processo de Cadastro

1. **Acesse o SGC**
   - Faça login com suas credenciais

2. **Navegue para Gerenciamento de Usuários**
   - Menu → Usuários → Novo Usuário

3. **Preencha o Formulário**
   ```
   Nome Completo: [Nome do usuário]
   CPF: [CPF do usuário]
   Email: [email@cartorio.com.br]
   Perfil: Administrador
   Cartório: [Selecione o cartório criado]
   ```

4. **Ative o Usuário**
   - Marque a opção "Usuário Ativo"
   - Defina permissões (normalmente todas para admin)

5. **Salve**
   - Clique em "Criar Usuário"

### Saída do Cadastro SGC

Após o cadastro, o sistema deve retornar:
- ✅ Confirmação de criação
- ✅ ID do usuário
- ✅ Status do usuário

## Passo 3: Gerar Credenciais de Acesso

### Solicitar ao Daniel

Com os usuários cadastrados no SGC, solicite ao Daniel:

```
Solicitação de Credenciais de Acesso

Cartório: [Nome]
Usuários: [Listar nomes dos usuários administrativos]
Data da Solicitação: [DD/MM/YYYY]

Favor gerar as credenciais de acesso (usuário e senha) 
para os usuários administrativos listados acima.
```

### Dados que Daniel Fornecerá

Para cada usuário administrativo:

```
USUÁRIO ADMINISTRATIVO
Nome: [Nome do usuário]
Usuário (Email): usuario@cartorio.com.br
Senha Temporária: XXXXXX1234
URL de Acesso: https://app.entregador21.com/cartorio-[codigo]
```

## Passo 4: Comunicar Credenciais ao Cartório

### Envio de Credenciais

Após receber do Daniel, comunique ao cartório:

**Método:** Pessoal/Direto (mais seguro que email)

```
Pessoal, as credenciais de acesso foram geradas!

IMPORTANTE: Alterem a senha no primeiro acesso.

🔐 DADOS DE ACESSO
URL: https://app.entregador21.com/cartorio-[codigo]
Usuário: usuario@cartorio.com.br
Senha (Temporária): XXXXXX1234

⚠️ SEGURANÇA:
- Não compartilhem a senha
- Alterem no primeiro acesso
- Usem senhas fortes (maiúsculas, números, símbolos)

Qualquer dúvida, entrem em contato!
```

## Passo 5: Validar Acesso

Solicite ao cartório:

1. ✅ Acessar com as credenciais fornecidas
2. ✅ Alterar senha temporária
3. ✅ Navegar no dashboard
4. ✅ Confirmar acesso funcionando
5. ✅ Testar visualização de relatórios

### Teste de Acesso

Peça para o cartório confirmar:
```
☐ Consegui fazer login com as credenciais
☐ Alterei a senha temporária
☐ Consigo visualizar o dashboard
☐ Acesso está funcionando normalmente
```

## Passo 6: Cadastro de Usuários Intimadores (Motoboys)

### Coleta de Dados

Solicite ao cartório:

```
Usuários Motoboys/Intimadores

Motoboy #1
├─ Nome Completo: [Nome do motoboy]
└─ Número do Celular: [Tel com DDD - (XX) XXXXX-XXXX]

Motoboy #2
├─ Nome Completo: [Nome do motoboy]
└─ Número do Celular: [Tel com DDD]
```

### Cadastro na Plataforma

Os motoboys são cadastrados **dentro da própria plataforma** do Entregador21:

1. **Acesse com usuário administrativo**
   - URL: https://app.entregador21.com

2. **Navegue para Motoboys**
   - Menu → Motoboys → Novo Motoboy

3. **Preencha o Formulário**
   ```
   Nome Completo: [Nome do motoboy]
   Celular: [Telefone]
   Email: [Email do motoboy - opcional]
   Status: Ativo
   ```

4. **Salve**
   - Clique em "Criar"

5. **O Sistema Gerará**
   - ✅ Código único do motoboy
   - ✅ Link para baixar app
   - ✅ Instruções de acesso

## Checklist da Etapa 3

- [ ] Dados de usuários administrativos coletados
- [ ] Dados validados
- [ ] Cadastro realizado no SGC
- [ ] Solicitação de credenciais enviada ao Daniel
- [ ] Credenciais recebidas
- [ ] Credenciais comunicadas ao cartório
- [ ] Cartório validou acesso
- [ ] Senha alterada pelos usuários
- [ ] Dados de motoboys coletados
- [ ] Motoboys cadastrados na plataforma
- [ ] Link do app enviado aos motoboys

## Próximo Passo

Após cadastrar todos os usuários, prossiga para [Etapa 4 - Assinatura Digital](./etapa-4-assinatura-digital.md)

---

**Duração estimada**: 3-5 dias  
**Responsáveis**: Suporte (SGC), Daniel (credenciais), Cartório (dados)

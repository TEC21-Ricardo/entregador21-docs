# Guia de Importação no GitBook

## 📋 Resumo

Esta pasta contém a documentação completa do Entregador21 pronta para ser importada no GitBook.

## 📁 Estrutura do Projeto

```
entregador21-gitbook/
├── README.md                      # Página inicial
├── SUMMARY.md                     # Índice (necessário para GitBook)
├── GUIA_GITBOOK.md               # Este arquivo
├── .gitbook.yaml                 # Configuração do GitBook
└── docs/
    ├── 01-introducao/            # Seção: Introdução
    ├── 02-implantacao/           # Seção: Implantação (5 etapas)
    ├── 03-operacoes/             # Seção: Operações (em construção)
    ├── 04-integracao-api/        # Seção: Integração de API
    ├── 05-procedimentos/         # Seção: Procedimentos
    ├── 06-suporte/               # Seção: Suporte
    └── images/                   # Pasta para screenshots e imagens
```

## 🚀 Como Importar no GitBook

### Passo 1: Criar Conta no GitBook (se não tiver)

1. Acesse: https://www.gitbook.com
2. Clique em "Sign Up"
3. Crie uma conta com email
4. Confirme email

### Passo 2: Criar Novo Espaço/Projeto

1. Na dashboard, clique em "Create a new space"
2. Ou clique em "New" → "Create a new project"

### Passo 3: Nomear o Projeto

```
Nome: Entregador21 - Documentação Completa
Descrição: Guia de implantação, configuração e operações da plataforma Entregador21
Visibilidade: [Escolha entre Privado ou Público]
```

### Passo 4: Conectar com GitHub (Recomendado)

**Opção A: Sincronizar com GitHub**

1. Na criação do projeto, selecione "GitHub"
2. Autorize GitBook a acessar seus repositórios
3. Selecione o repositório com os arquivos
4. Selecione a branch (main/master)
5. Aponte para a pasta `docs/`

**Benefícios:**
- ✅ Sincronização automática
- ✅ Versionamento no Git
- ✅ Colaboração facilitada
- ✅ Backup automático

**Opção B: Upload Manual**

1. Se não usar GitHub, pode fazer upload direto
2. Clique em "Import" → "From Files"
3. Selecione a pasta `docs/`
4. Ou arraste e solte os arquivos

### Passo 5: Verificar Estrutura

Após importar:

1. ✅ Verifique se SUMMARY.md foi reconhecido
2. ✅ Valide se o menu aparece corretamente
3. ✅ Clique em alguns links para testar
4. ✅ Verifique formatação das imagens

## 📝 Customizando no GitBook

### Editar Configurações

1. Acesse o projeto no GitBook
2. Clique em "Settings" (engrenagem)

#### Geral

- **Project Name**: Entregador21 - Documentação
- **Project Desc**: Guia completo de implantação e operações
- **Project Icon**: [Upload logo da TEC21]

#### Idioma

- **Language**: Português (Brasil)
- **Theme**: Temas disponíveis (Choose "Light" for better readability)

#### Customização de Tema

1. Menu → Settings → Customization
2. Defina:
   - **Primary Color**: Azul TEC21 (#0066CC)
   - **Logo**: Logo TEC21
   - **Logo Text**: "Entregador21"
   - **Favicon**: Ícone TEC21

#### Compartilhamento

Se desejar compartilhar:
1. Settings → Share
2. Generate sharing link (permite leitura pública)
3. Ou convide usuários específicos

### Adicionar Colaboradores

1. Settings → Members
2. Clique "Invite members"
3. Adicione emails dos colaboradores
4. Selecione permissão (Editor/Commenter/Viewer)

## 🖼️ Adicionar Screenshots e Imagens

Para melhorar a documentação com prints da plataforma:

### 1. Preparar Imagens

```
Criar pasta: docs/images/

Sugestão de estrutura:
docs/images/
├── login/
│   ├── 01-tela-login.png
│   └── 02-primeira-senha.png
├── dashboard/
│   ├── 01-dashboard-inicial.png
│   └── 02-menu-principal.png
├── intimacoes/
│   └── 01-listar-intimacoes.png
└── relatorios/
    └── 01-relatorio-entregas.png
```

### 2. Inserir Imagens nos Documentos

Edite os arquivos Markdown e adicione:

```markdown
# Exemplo de Imagem

![Descrição da Imagem](../images/login/01-tela-login.png)

Ou com dimensão:

![Descrição da Imagem](../images/login/01-tela-login.png =800x600)
```

### 3. Tirar Screenshots da Plataforma

**Para Windows:**
- Use Snip & Sketch (Win + Shift + S)
- Salve como PNG
- Redimensione se necessário

**Para Mac:**
- Command + Shift + 4
- Salve como PNG

**Dicas:**
- ✅ Mantenha resolução mínima 1024x768
- ✅ Destaque áreas importantes com setas/círculos
- ✅ Oculte dados sensíveis (senhas, tokens, CPF)
- ✅ Use nomes descritivos para os arquivos

## 📚 Adicionando Novos Documentos

### Criar Nova Página

1. Na navegação do GitBook, clique no "+"
2. Selecione "Add a page"
3. Digite título da página
4. GitBook cria arquivo automaticamente

### Estrutura Recomendada para Novos Docs

```markdown
# [Título Principal]

## Objetivo

[Breve descrição do que será coberto]

## Seção 1

Conteúdo...

## Seção 2

Conteúdo...

## Checklist

- [ ] Item 1
- [ ] Item 2

---

**Versão**: 1.0  
**Última atualização**: [Data]  
**Responsável**: [Nome]
```

### Atualizar SUMMARY.md

Toda vez que criar nova página, atualize `SUMMARY.md`:

```markdown
- [Nova Página](docs/01-introducao/nova-pagina.md)
```

## 🔄 Fluxo de Sincronização (com GitHub)

### Se Usou Conectar com GitHub:

1. **Fazer mudanças localmente**
   ```bash
   git clone [seu-repo]
   cd entregador21-gitbook
   # Edite os arquivos .md
   git add .
   git commit -m "Adiciona nova documentação"
   git push
   ```

2. **GitBook sincroniza automaticamente**
   - Detecta mudanças no GitHub
   - Atualiza documentação em minutos
   - Histórico disponível

### Desfazer Mudança

1. No GitBook, acesse "History"
2. Localize versão anterior
3. Clique "Restore this version"
4. Confirme

## 🔐 Segurança e Privacidade

### Compartilhar Responsavelmente

⚠️ **Cuidado com:**
- Tokens de API (nunca incluir no doc público)
- Senhas e credenciais
- Emails privados
- Informações de cartórios específicos

### Ocultar Informações Sensíveis

Use placeholders:

```markdown
**Token:** [TOKEN_SUBSTITUIR_COM_VALOR_REAL]
**Email:** usuario@[cartorio].com.br
**Senha:** [USAR_SENHA_FORTE]
```

## 📱 Preview e Publicação

### Preview Local (Opcional)

Se quiser testar antes de publicar:

```bash
# Instale gitbook-cli
npm install -g gitbook-cli

# Vá até pasta do projeto
cd entregador21-gitbook

# Gere preview
gitbook serve

# Acesse http://localhost:4000
```

### Publicar no GitBook

1. Projeto criado/importado
2. Clique "Publish" (se tiver permissão)
3. Escolha domínio público
4. GitBook fornecerá URL de publicação

### URL Pública

Exemplo:
```
https://tec21-entregador21.gitbook.io/
```

## 🎯 Plano de Ação

### Curto Prazo (Próxima Semana)

- [ ] Importar documentação no GitBook
- [ ] Customizar aparência (logo, cores)
- [ ] Testar navegação
- [ ] Compartilhar link interno

### Médio Prazo (Próximas 2-3 Semanas)

- [ ] Adicionar screenshots das telas
- [ ] Completar seção de Operações
- [ ] Completar seção de API
- [ ] Completar seção de Procedimentos

### Longo Prazo (Próximo Mês)

- [ ] Adicionar vídeos tutoriais (links)
- [ ] Completar seção de Suporte/FAQ
- [ ] Publicar versão pública (site)
- [ ] Configurar comentários/feedback

## 📞 Suporte GitBook

Dúvidas sobre GitBook?

- 📖 Documentação: https://docs.gitbook.com
- 💬 Community: https://community.gitbook.com
- 📧 Support: support@gitbook.com

## ✅ Checklist Final

Antes de compartilhar:

- [ ] Todos os links funcionam
- [ ] Imagens aparecem corretamente
- [ ] Formatação está OK
- [ ] Nenhuma informação sensível exposta
- [ ] Índice (SUMMARY.md) está correto
- [ ] Página inicial README está clara
- [ ] Versão documentada
- [ ] Data de atualização preenchida

## 📞 Próximos Passos

1. ✅ Importar no GitBook
2. ✅ Customizar aparência
3. ✅ Adicionar screenshots
4. ✅ Testar todos os links
5. ✅ Compartilhar com equipe
6. ✅ Coletar feedback
7. ✅ Iterar e melhorar

---

**Versão**: 1.0  
**Criado em**: 2024  
**Autor**: Documentação TEC21  
**Status**: Pronto para Importação

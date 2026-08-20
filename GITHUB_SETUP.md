# Setup GitHub + GitBook para Entregador21

## 📋 Visão Geral

Este projeto está estruturado para:
- ✅ **Versionamento**: Código versionado no GitHub
- ✅ **Sincronização**: Automática entre GitHub → GitBook
- ✅ **Colaboração**: Múltiplos colaboradores podem contribuir
- ✅ **CI/CD Ready**: Pronto para automação futura

---

## 🚀 Passo 1: Preparar Repositório Local

### 1.1 Inicializar Git (PRIMEIRA VEZ)

```bash
cd "C:\Users\ricardo\Documents\entregador21-gitbook"

# Inicialize git
git init

# Configure usuário (use seus dados do GitHub)
git config user.name "Ricardo"
git config user.email "ricardo.p21sistemas@gmail.com"

# Verifique
git config --list
```

### 1.2 Adicionar Arquivos

```bash
# Adicione todos os arquivos
git add .

# Verifique status
git status

# Criar primeiro commit
git commit -m "docs: Documentação inicial Entregador21

- Seção 01: Introdução
- Seção 02: Implantação (5 etapas completas)
- Seção 03: Operações (parcial)
- Configuração GitBook
- README e estrutura base"
```

---

## 🌐 Passo 2: Criar Repositório no GitHub

### 2.1 Criar Repo

1. Acesse: https://github.com/new
2. Preencha:
   ```
   Repository name: entregador21-docs
   Description: Documentação completa - Implantação e Operações
   Visibilidade: Private (ou Public, conforme preferência)
   ☐ Initialize with README (NÃO marque - já temos)
   ☐ Add .gitignore (NÃO marque - já temos)
   ☐ Add license (Opcional - MIT recomendado)
   ```

3. Clique "Create repository"

### 2.2 Copiar URL

Após criar, você receberá uma URL:
```
https://github.com/seu-usuario/entregador21-docs.git
```

Guarde essa URL (vamos usar no próximo passo).

---

## 📤 Passo 3: Fazer Push para GitHub

### 3.1 Adicionar Remote

```bash
cd "C:\Users\ricardo\Documents\entregador21-gitbook"

# Adicione o remote (substitua sua URL)
git remote add origin https://github.com/seu-usuario/entregador21-docs.git

# Renomeie branch para main (padrão moderno)
git branch -M main

# Verifique
git remote -v
```

### 3.2 Fazer Push

```bash
# Envie para GitHub
git push -u origin main

# Próximas vezes, apenas:
# git push
```

**Resultado esperado:**
```
✓ Enviando para https://github.com/seu-usuario/entregador21-docs.git
✓ main -> main
```

### 3.3 Verificar no GitHub

1. Acesse seu repositório: `https://github.com/seu-usuario/entregador21-docs`
2. Verifique se todos os arquivos aparecem
3. Confirme que `.gitignore` e `README.md` estão lá

---

## 🔗 Passo 4: Conectar GitHub ao GitBook

### 4.1 Autorizando GitBook

1. Acesse: https://www.gitbook.com
2. Faça login
3. Vá para Settings → Developer → OAuth Applications
4. Ou acesse diretamente: https://app.gitbook.com/account/oauth/github/connect

### 4.2 Criar Novo Espaço com GitHub

**Opção 1: Novo Espaço**
1. Dashboard → "Create a new space"
2. Selecione "GitHub" como origem
3. Autorize GitBook a acessar seu GitHub
4. Selecione repositório: `seu-usuario/entregador21-docs`
5. Branch: `main`
6. Path: `docs/` (onde estão os markdown)

**Opção 2: Importar em Espaço Existente**
1. Espaço existente → Settings → Git Sync
2. Connect to GitHub
3. Selecione repositório
4. Branch: `main`
5. Folder: `docs/`

### 4.3 Configurar Sincronização

Em Settings → Git Sync:

```
GitHub Repository: seu-usuario/entregador21-docs
Branch: main
GitHub Path: docs/
Bidirectional Sync: ON (opcional)
```

**Isso significa:**
- ✅ Quando fazer push no GitHub → GitBook atualiza automaticamente
- ✅ Você edita no GitHub (local) → GitBook reflete em minutos
- ✅ Se ativar bidirecional → também edita no GitBook → atualiza GitHub

---

## 📝 Passo 5: Fluxo de Trabalho Diário

### Editar Documentação Localmente

```bash
# 1. Criar nova branch (recomendado)
git checkout -b feature/nova-secao

# 2. Editar arquivos .md
# (Abra com seu editor favorito)

# 3. Verificar mudanças
git status
git diff

# 4. Adicionar mudanças
git add .

# 5. Fazer commit (mensagem descritiva)
git commit -m "docs: Adiciona seção de API

- Adiciona autenticação
- Adiciona endpoints
- Adiciona exemplos"

# 6. Fazer push
git push origin feature/nova-secao
```

### Fazer Pull Request (Colaboração)

```bash
# 1. Depois do push, abra PR no GitHub
# 2. Title: "Adiciona seção de API"
# 3. Description: Descreva as mudanças
# 4. Aguarde review
# 5. Merge para main
# 6. GitBook atualiza automaticamente ✨
```

---

## 🔄 Passo 6: Manter Sincronizado

### Receber Atualizações do GitHub no Local

Se outra pessoa fez changes:

```bash
# Buscar mudanças
git fetch origin

# Atualizar local branch
git pull origin main
```

### Ver Histórico de Commits

```bash
# Ver todos os commits
git log

# Ver commits de um arquivo
git log docs/arquivo.md

# Ver diferenças do último commit
git diff HEAD~1
```

---

## 📚 Estrutura de Branches (Recomendado)

Use este padrão:

```
main (produção - sincronizado com GitBook)
├── feature/adiciona-api
├── feature/adiciona-screenshots
├── feature/melhora-operacoes
└── fix/corrige-links

docs (para sincronizar com docs site, se tiver)
└── ...
```

**Regra:**
- `main` = sempre pronto para produção
- Outras branches = em desenvolvimento
- Fazer PR antes de mergear na main

---

## 🔐 Segurança

### Proteger a Branch Main

No GitHub:
1. Settings → Branches
2. "Add rule"
3. Branch name pattern: `main`
4. ☑️ Require pull request reviews
5. ☑️ Require status checks to pass

Benefícios:
- ✅ Ninguém faz push direto em main
- ✅ Todas as mudanças passam por review
- ✅ Histórico limpo e rastreável

---

## 🛠️ Troubleshooting

### ❓ "fatal: remote origin already exists"

```bash
# Remove remote antigo
git remote remove origin

# Adicione novamente
git remote add origin https://github.com/seu-usuario/entregador21-docs.git
```

### ❓ "Permission denied (publickey)"

```bash
# Configure SSH (mais seguro que HTTPS)
# Gere chave SSH no GitHub Settings
# Depois use URL SSH:
# git@github.com:seu-usuario/entregador21-docs.git
```

### ❓ GitBook não está atualizando

1. Verifique se branch é `main`
2. Verifique se path é `docs/`
3. Aguarde 2-3 minutos (às vezes leva)
4. Clique "Sync" manualmente em Settings → Git Sync

### ❓ Fiz commit errado, como desfazer?

```bash
# Ver últimos commits
git log --oneline -5

# Desfazer último commit (mas manter mudanças)
git reset --soft HEAD~1

# Desfazer última commit (descartar mudanças)
git reset --hard HEAD~1

# Forçar push (CUIDADO!)
git push origin main --force
```

---

## 📋 Checklist Completo

Antes de considerar pronto:

- [ ] Git inicializado localmente
- [ ] Repositório criado no GitHub
- [ ] Primeiro push realizado com sucesso
- [ ] GitHub mostra todos os arquivos
- [ ] GitBook conectado ao GitHub
- [ ] GitBook sincroniza automaticamente
- [ ] Customização GitBook feita (logo, cores)
- [ ] Documento protegido (branch protection)
- [ ] Colaboradores adicionados (se houver)
- [ ] README no repositório está claro

---

## 🚀 Próximos Passos

1. ✅ Fazer setup GitHub (este doc)
2. ✅ Conectar ao GitBook
3. ⏳ Adicionar screenshots
4. ⏳ Completar seções faltantes
5. ⏳ Fazer 1º PR com melhorias
6. ⏳ Publicar no GitBook

---

## 📞 Referências Rápidas

**Comandos Git Principais:**
```bash
git init              # Iniciar repo
git add .             # Adicionar arquivos
git commit -m ""      # Fazer commit
git push              # Enviar para GitHub
git pull              # Receber de GitHub
git log               # Ver histórico
git branch -a         # Ver branches
git checkout -b       # Criar nova branch
```

**URLs Importantes:**
- GitHub Repo: `https://github.com/seu-usuario/entregador21-docs`
- GitBook Space: `https://app.gitbook.com/o/seu-workspace/s/entregador21`
- Documentação Pública: `https://seu-espaco.gitbook.io/entregador21`

---

**Status**: ✅ Pronto para setup  
**Versão**: 1.0  
**Data**: 2024  
**Próximo**: Executar Passo 1

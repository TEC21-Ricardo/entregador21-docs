# 🚀 Setup Completo: GitHub + GitBook + Entregador21

## 📋 Resumo do Processo

Este guia cobre todos os passos para:

1. ✅ Preparar repositório Git localmente
2. ✅ Criar repositório no GitHub
3. ✅ Fazer upload da documentação
4. ✅ Conectar GitHub ao GitBook
5. ✅ Configurar sincronização automática
6. ✅ Testar tudo funcionando

**Tempo estimado**: 20-30 minutos

---

## 📊 Diagrama do Fluxo

```
Seu Computador (Local)
    ↓
    ├─ Edita arquivos .md
    ├─ git add / git commit
    ↓
GitHub Repository
    ↓
GitBook (Sincronização Automática)
    ↓
Documentação Online (Pública/Privada)
    ↓
Leitores/Equipe
```

---

## 🔧 PASSO 1: Preparar Ambiente Local

### 1.1 Verificar Git Instalado

```bash
# Windows PowerShell (Execute como Administrador)
git --version

# Se não tiver, instale de: https://git-scm.com/download/win
```

**Resultado esperado:**
```
git version 2.x.x.windows.x
```

### 1.2 Configurar Git Globalmente (PRIMEIRA VEZ APENAS)

```bash
# Configure seu nome
git config --global user.name "Ricardo"

# Configure seu email (mesmo do GitHub)
git config --global user.email "ricardo.p21sistemas@gmail.com"

# Verifique
git config --global --list
```

### 1.3 Abrir Terminal na Pasta do Projeto

```bash
# Navegue até a pasta
cd "C:\Users\ricardo\Documents\entregador21-gitbook"

# Verifique que está no local certo
pwd
# Deve exibir: C:\Users\ricardo\Documents\entregador21-gitbook
```

---

## 🌍 PASSO 2: Criar Repositório no GitHub

### 2.1 Acessar GitHub

1. Abra: https://github.com
2. Se não tiver conta:
   - Clique "Sign up"
   - Crie com seu email (ricardo.p21sistemas@gmail.com)
   - Confirme email
   - Complete perfil

3. Se tiver conta:
   - Faça login

### 2.2 Criar Novo Repositório

1. Clique no **+** (canto superior direito)
2. Selecione **"New repository"**

### 2.3 Preencher Formulário

```
Repository name: entregador21-docs
Description: Documentação Entregador21 - Implantação e Operações
Visibilidade: ⚫ Private (privado, apenas você/equipe)
            ou
            ⚪ Public (público, qualquer um pode ver)

☐ Initialize this repository with:
   ☐ Add a README file (NÃO marque)
   ☐ Add .gitignore (NÃO marque)
   ☐ Choose a license (OPCIONAL)
```

### 2.4 Clique "Create Repository"

Após criar, você verá:

```
Quick setup — if you've done this kind of thing before

…or create a new repository on the command line
…or push an existing repository from the command line
```

**Copie a URL que aparece:**
```
https://github.com/seu-username/entregador21-docs.git
```

Vamos usar no próximo passo.

---

## 📤 PASSO 3: Inicializar Git e Fazer Push

### 3.1 Abrir PowerShell na Pasta

```bash
cd "C:\Users\ricardo\Documents\entregador21-gitbook"
```

### 3.2 Inicializar Repositório Git

```bash
# Se NUNCA fez git init nesta pasta
git init

# Verifique
git status
# Deve exibir "On branch master" ou "On branch main"
```

### 3.3 Adicionar Todos os Arquivos

```bash
# Adicione todos os arquivos
git add .

# Verifique o que será adicionado
git status
```

**Deve exibir algo como:**
```
Changes to be committed:
  new file:   README.md
  new file:   SUMMARY.md
  new file:   .gitbook.yaml
  ... (vários outros arquivos)
```

### 3.4 Fazer Primeiro Commit

```bash
git commit -m "docs: Documentação inicial Entregador21

- Seção 01: Introdução
- Seção 02: Implantação (5 etapas)
- Seção 03: Operações (autenticação)
- Configuração GitBook
- Estrutura base pronta"
```

**Resultado esperado:**
```
[main (root-commit) abc1234] docs: Documentação inicial Entregador21
 13 files changed, 5000+ insertions(+)
 create mode 100644 README.md
 ...
```

### 3.5 Adicionar URL Remota do GitHub

```bash
# Substitua EXATAMENTE a URL que copiou do GitHub
git remote add origin https://github.com/seu-username/entregador21-docs.git

# Verifique
git remote -v
# Deve exibir a URL que adicionou
```

### 3.6 Fazer Push para GitHub

```bash
# Envie tudo para o GitHub
git push -u origin main

# Na primeira vez, pode pedir credenciais GitHub
# Se pedir, use:
# - Usuário: seu_username_github
# - Senha: seu_personal_access_token (não senha normal)
```

> **Nota**: Se não tiver Personal Access Token:
> 1. GitHub Settings → Developer settings → Personal access tokens
> 2. Generate new token
> 3. Marque: `repo` e `workflow`
> 4. Use como "senha"

**Resultado esperado:**
```
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
...
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### 3.7 Verificar no GitHub

1. Acesse: https://github.com/seu-username/entregador21-docs
2. Verifique se todos os arquivos aparecem
3. Verifique se está na branch `main`

✅ **Parabéns! Seu código está no GitHub!**

---

## 🔗 PASSO 4: Conectar GitHub ao GitBook

### 4.1 Acessar GitBook

1. Acesse: https://www.gitbook.com
2. Faça login (ou crie conta)

### 4.2 Criar Novo Espaço

1. Na dashboard, clique **"Create a new space"**

2. Preencha:
   ```
   Name: Entregador21
   Description: Documentação de implantação e operações
   Privacy: Private (ou Internal)
   ```

3. Clique "Create"

### 4.3 Conectar com GitHub

#### Opção A: Durante Criação (Melhor)

Se pediu "How do you want to start?":
1. Selecione **"GitHub"**
2. Clique "Connect with GitHub"
3. GitHub pede autorização → Autorize
4. Selecione repositório: `seu-username/entregador21-docs`
5. Branch: `main`
6. Content folder: `docs/` ← **IMPORTANTE!**
7. Clique "Create"

#### Opção B: Depois (Se Já Criou)

1. Dentro do GitBook → Settings
2. Aba "Git Sync"
3. Clique "Connect"
4. GitHub → Autorize
5. Selecione `seu-username/entregador21-docs`
6. Branch: `main`
7. Folder: `docs/`
8. Salve

### 4.4 Aguardar Sincronização

GitBook fará:
1. ✓ Download do repositório
2. ✓ Leitura do `docs/` folder
3. ✓ Processamento de todos os `.md`
4. ✓ Geração da documentação

**Pode levar 2-5 minutos na primeira vez.**

Você verá:
- Status "Synced" em verde
- Ou "Syncing..." durante o processo

---

## ✅ PASSO 5: Testar Tudo

### 5.1 Verificar GitBook

1. Dentro do espaço GitBook
2. Clique no ícone de "eye" (Visualizar)
3. Ou acesse URL pública (se estiver pública)

**Deve exibir:**
- ✅ Menu lateral com todas as seções
- ✅ Página inicial (README)
- ✅ Todos os links funcionando
- ✅ Imagens visíveis (se houver)

### 5.2 Testar Sincronização

1. **Localmente**: Edite um arquivo `.md`
   ```bash
   # Exemplo: editar intro
   # Altere algo no docs/01-introducao/visao-geral.md
   ```

2. **Fazer commit e push**
   ```bash
   git add .
   git commit -m "test: Atualização teste de sincronização"
   git push
   ```

3. **Aguardar GitBook sincronizar**
   - Geralmente 1-2 minutos
   - Verifique Settings → Git Sync → Status

4. **Ver mudança no GitBook**
   - Recarregue a página GitBook
   - Sua mudança deve aparecer! ✨

### 5.3 Checklist Final

- [ ] Repositório GitHub criado e com arquivos
- [ ] Git funcionando localmente
- [ ] GitBook criado
- [ ] GitHub conectado ao GitBook
- [ ] Página inicial visível no GitBook
- [ ] Todos os links funcionam
- [ ] Sincronização testada (edit + push → GitBook atualiza)

---

## 🎯 PASSO 6: Configurar GitBook

### 6.1 Customizar Aparência

1. GitBook → Settings → Customization

2. Preencha:
   ```
   Logo: [Upload logo TEC21]
   Logo text: "Entregador21"
   Primary color: #0066CC (azul TEC21)
   Theme: Light (ou Dark)
   ```

### 6.2 Adicionar Favicon

1. Settings → Customization
2. "Favicon"
3. Upload ícone .ico ou .png

### 6.3 Configurar Domínio (Opcional)

Se quiser URL customizada (não padrão):

1. Settings → Sharing
2. "Custom domain"
3. Adicione: `entregador21-docs.tec21.com.br` (exemplo)
4. Configure DNS no seu provider de domínio

---

## 🔄 PASSO 7: Fluxo Diário de Trabalho

### Para Adicionar Novo Conteúdo

```bash
# 1. Atualizar repositório local
git pull origin main

# 2. Criar branch para sua mudança (recomendado)
git checkout -b feature/adiciona-api

# 3. Editar arquivos em docs/
# (Use seu editor favorito)

# 4. Ver mudanças
git status
git diff

# 5. Adicionar e fazer commit
git add .
git commit -m "docs: Adiciona seção de API

- Autenticação
- Endpoints
- Exemplos de código"

# 6. Fazer push
git push origin feature/adiciona-api

# 7. No GitHub, abra Pull Request
# 8. Revise e faça Merge

# 9. GitBook sincroniza automaticamente! ✨
```

### Para Correções Rápidas

```bash
# Direto na branch main (se tiver certeza)
git pull
# editar arquivo
git add .
git commit -m "docs: Corrige typo em página X"
git push
```

---

## 🚨 Troubleshooting

### ❌ "fatal: not a git repository"

```bash
# Solução:
cd "C:\Users\ricardo\Documents\entregador21-gitbook"
git status
```

### ❌ "Permission denied (publickey)"

```bash
# Use HTTPS em vez de SSH:
git remote set-url origin https://github.com/seu-user/entregador21-docs.git
git push
```

### ❌ GitBook não está sincronizando

1. Verifique Settings → Git Sync
2. Clique "Sync manually"
3. Verifique se branch é `main`
4. Verifique se folder é `docs/`
5. Aguarde 2-3 minutos

### ❌ "branch 'main' set to track remote, but receives no update"

```bash
# Não é erro, apenas aviso de que está sincronizado
# Ignore se tudo está funcionando
```

### ❌ Arquivo não aparece no GitBook

1. Verifique se arquivo está em `docs/`
2. Verifique se está em .md
3. Verifique se adicionou ao SUMMARY.md
4. Sincronize manualmente no GitBook

---

## 📚 Referência Rápida de Comandos

```bash
# Status
git status

# Ver histórico
git log --oneline

# Criar branch
git checkout -b nome-da-branch

# Mudar de branch
git checkout nome-da-branch

# Adicionar arquivos
git add .

# Fazer commit
git commit -m "mensagem"

# Enviar para GitHub
git push

# Receber de GitHub
git pull

# Ver remotes
git remote -v

# Desfazer último commit (mas manter mudanças)
git reset --soft HEAD~1
```

---

## ✅ Conclusão

Se chegou aqui e tudo funcionou:

✨ **Parabéns!** ✨

Você tem:
- ✅ Documentação versionada no GitHub
- ✅ Sincronização automática com GitBook
- ✅ Documentação online acessível
- ✅ Sistema pronto para colaboração

---

## 🎓 Próximas Etapas

1. Adicione screenshots (pasta `docs/images/`)
2. Complete seções faltantes (API, Procedimentos, Suporte)
3. Convide colaboradores
4. Configure branch protection (main)
5. Monitore e itere

---

## 📞 Suporte

**Dúvidas sobre Git/GitHub?**
- https://docs.github.com
- https://git-scm.com/doc

**Dúvidas sobre GitBook?**
- https://docs.gitbook.com

**Dúvidas sobre Entregador21?**
- suporte@tec21.com.br

---

**Versão**: 1.0  
**Status**: ✅ Pronto para execução  
**Criado**: 2024

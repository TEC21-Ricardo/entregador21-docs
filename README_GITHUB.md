# Documentação Entregador21

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![License](https://img.shields.io/badge/license-private-red.svg)

Documentação completa de implantação, operações e integração da plataforma **Entregador21** - Solução de gestão de intimações para cartórios de protesto.

## 📚 Documentação Online

🌐 **GitBook**: [Entregador21 Documentation](https://entregador21.gitbook.io)

> A documentação é sincronizada automaticamente desde este repositório

## 🎯 Sobre o Entregador21

**Entregador21** é uma solução SaaS desenvolvida pela TEC21 que ajuda cartórios de protesto a:

✨ Automatizar impressão e entrega de intimações  
📊 Monitorar entregas em tempo real  
🔐 Gerar AR Digital com assinatura eletrônica  
🚀 Integrar com sistemas cartorários via API  
💼 Gerenciar equipes de motoboys/entregadores  

## 📖 Conteúdo

### ✅ Disponível

- **Introdução** - Visão geral e conceitos
- **Implantação** - 5 etapas completas
  - Coleta de dados
  - Ambiente de produção
  - Cadastro de usuários
  - Assinatura digital
  - Testes de rotina
- **Operações** - Guias de uso
  - Autenticação e login
  - Dashboard (em progresso)
  - Gerenciamento de intimações (em progresso)

### ⏳ Em Progresso

- **Integração de API** - Documentação técnica
- **Procedimentos** - Fluxos operacionais
- **Suporte** - FAQ e troubleshooting

## 🚀 Quick Start

### Para Ler a Documentação

1. Acesse: https://entregador21.gitbook.io
2. Navegue pelos menus
3. Use busca para encontrar tópicos

### Para Contribuir

1. Clone o repositório:
```bash
git clone https://github.com/tec21/entregador21-docs.git
cd entregador21-docs
```

2. Crie uma branch para sua mudança:
```bash
git checkout -b feature/sua-mudanca
```

3. Edite os arquivos `.md` na pasta `docs/`

4. Faça commit das mudanças:
```bash
git add .
git commit -m "docs: Descrição clara da mudança"
```

5. Faça push:
```bash
git push origin feature/sua-mudanca
```

6. Abra um Pull Request no GitHub

## 📁 Estrutura

```
entregador21-docs/
├── README.md                    # Este arquivo (GitHub)
├── SUMMARY.md                   # Índice GitBook
├── .gitbook.yaml               # Configuração GitBook
├── GITHUB_SETUP.md             # Setup GitHub + GitBook
├── GUIA_GITBOOK.md             # Tutorial detalhado
├── QUICKSTART.md               # Início rápido
│
└── docs/
    ├── 01-introducao/
    │   └── visao-geral.md
    ├── 02-implantacao/
    │   ├── pre-requisitos.md
    │   ├── fase-integracao.md
    │   ├── etapa-1-coleta-dados.md
    │   ├── etapa-2-ambiente-producao.md
    │   ├── etapa-3-cadastro-usuarios.md
    │   ├── etapa-4-assinatura-digital.md
    │   └── etapa-5-testes.md
    ├── 03-operacoes/
    │   └── autenticacao.md
    ├── images/                  # Screenshots e imagens
    └── ...
```

## 👥 Colaboradores

- **Ricardo** - Documentação, Implantação
- **Anderson** - Product Owner
- **Daniel** - Desenvolvimento

## 🤝 Como Contribuir

Encontrou um erro ou quer sugerir melhoria?

1. **Issues**: Abra uma issue descrevendo o problema
2. **Pull Requests**: Faça suas mudanças e abra PR
3. **Discussions**: Sugestões gerais na aba Discussions

### Padrões de Commit

```bash
# Documentação
git commit -m "docs: Adiciona seção de API"

# Correção
git commit -m "fix: Corrige link quebrado em operacoes"

# Feature
git commit -m "feat: Adiciona screenshots do dashboard"

# Refatoração
git commit -m "refactor: Reorganiza estrutura de implantacao"
```

## 📝 Guias para Editores

- [GITHUB_SETUP.md](./GITHUB_SETUP.md) - Configurar Git + GitBook
- [GUIA_GITBOOK.md](./GUIA_GITBOOK.md) - Tutorial completo GitBook
- [QUICKSTART.md](./QUICKSTART.md) - Início rápido

## 🔗 Links Úteis

- **Plataforma**: https://app.entregador21.com
- **API Docs**: https://api.entregadoronline.com/docs
- **Suporte**: suporte@tec21.com.br
- **Website TEC21**: https://tec21.com.br

## 🔐 Segurança

⚠️ **IMPORTANTE**

- Nunca faça commit de senhas, tokens ou credenciais
- Oculte informações sensíveis (CPF, CNPJ, emails)
- Use placeholders: `[VALOR_REAL_AQUI]`
- Revise mudanças antes de fazer push

## 📋 Licença

Esta documentação é propriedade da TEC21 Soluções em TI.

Uso: Apenas para equipes TEC21 e clientes autorizados.

## 📞 Suporte

### Dúvidas sobre Documentação?

- 📧 Email: suporte@tec21.com.br
- 💬 WhatsApp: [Link Grupo]
- 👤 Ricardo: ricardo.p21sistemas@gmail.com

### Dúvidas sobre GitBook?

- 📖 [GitBook Docs](https://docs.gitbook.com)
- 💬 [GitBook Community](https://community.gitbook.com)

## 🙏 Agradecimentos

Documentação criada com ❤️ pela equipe TEC21.

---

**Versão**: 1.0  
**Atualizado**: 2024  
**Status**: ✅ Ativo  
**Sincronização**: ✅ GitHub → GitBook

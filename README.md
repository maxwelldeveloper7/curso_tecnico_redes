# Curso Técnico em Redes de Computadores

Repositório com o material didático para o Curso Técnico Pós-Médio em Redes, ministrado pelo Professor Maxwell de Oliveira Chaves.

## Visão geral

Este repositório reúne conteúdo em Markdown e páginas HTML para duas disciplinas principais:

- **Infraestrutura Física de Redes (IFR)** — conteúdo teórico e prático sobre cabeamento, patch panels, canaletas, eletrodutos e organização física de redes.
- **Oficina de Montagem e Conexão (OMC)** — montagem e manutenção de computadores, fontes, placa-mãe, e conexões elétricas.

## Estrutura do repositório

O conteúdo está organizado nas pastas principais abaixo (resumo):

```
curso_tecnico_redes/
├── index.html
├── LICENSE
├── README.md
├── infra_estrutura_fisica/
│   ├── atividades/
│   └── aulas/
├── Oficina_montagem_conexao/
│   ├── Atividades/
│   └── aulas/
└── web/
    ├── assets/   # css, imagens, js
    ├── ifr/      # páginas HTML da disciplina IFR (aulas, simulações)
    └── omc/      # páginas HTML da disciplina OMC
```

Observação: há diversas aulas e atividades em cada disciplina (ex.: `infra_estrutura_fisica/aulas/aula01.md` ... `aula09.md`, e páginas HTML correspondentes em `web/ifr/`).

## Como visualizar localmente

Você pode abrir `index.html` diretamente no navegador ou servir o diretório localmente (recomendado para navegar pelas páginas HTML corretamente):

Com Python 3 (porta 8000):

```bash
python3 -m http.server 8000
```

Depois abra `http://localhost:8000` no navegador.

## Conteúdo e navegação

- Páginas web compiladas estão em `web/` (ex.: `web/ifr/09.html` corresponde à Aula 09 de IFR).
- Material em Markdown está nas pastas `infra_estrutura_fisica/aulas/` e `Oficina_montagem_conexao/aulas/`.

## Contribuição

Contribuições são bem-vindas. Para adicionar/atualizar uma aula:

1. Edite ou adicione o Markdown em `infra_estrutura_fisica/aulas/` ou `Oficina_montagem_conexao/aulas/`.
2. Gere/atualize a versão HTML em `web/` (pode ser manualmente ou via script de geração, se existir).
3. Abra um pull request com uma descrição clara das mudanças.

## Autor

**Maxwell de Oliveira Chaves**

- [LinkedIn](https://www.linkedin.com/in/maxwell-oliveira-chaves/)

## 📄 Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).

---

*Última atualização: 2026-06-19*
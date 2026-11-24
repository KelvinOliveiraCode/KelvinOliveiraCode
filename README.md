# Kelvin Oliveira

[English](README.en.md)

Construo software com agentes. Eu escrevo a especificação, defino os limites de cada tarefa e reviso o resultado. Os agentes escrevem o código, rodam os testes e produzem a evidência. Eu opero o que sai desse loop.

O SelfEvoPI é o harness que nasceu desse processo. Hoje ele executa o próprio ciclo: detecta uma lacuna, escreve o artefato, verifica, aplica o gate e promove ou desfaz.

Portfólio: https://kelvinoliveiracode.github.io/portfolio/
Projetos: https://kelvinoliveiracode.github.io/portfolio/projetos/
LinkedIn: https://www.linkedin.com/in/kelvin-oliveira-code/

```text
KELVIN OLIVEIRA
+-- agentes     SelfEvoPI, orquestração, evals
+-- dados       deteccao de fraude, churn, KB-search
+-- cyber       pentest 11 CWE, SIEM 7 regras
+-- infra       VPC 3 camadas, Modbus do zero
+-- backend     Kodapay 6 GoF, Java 21, Spring Boot 3
+-- web         KODAROS 8 e-books, Garimpo 131 ofertas
+-- ti          service desk, backup com hash, onboarding
```

## Como trabalho

- Desenho o problema, as restrições e o critério de pronto antes de pedir código.
- Orquestro agentes com papéis, permissões e limites de contexto explícitos.
- Verifico com testes, evals determinísticos e checagem contra a fonte. Todo número vem de comando executado ou de fonte primária.
- Publico e mantenho. 14 páginas estão no ar e os repositórios seguem atualizados.

## Obras

**SelfEvoPI**

Harness de agente de código na versão 2.0.0, Windows nativo, zero dependências npm. A CLI é a única superfície e o motor é um processo externo falado por RPC.

- 1303 testes no `npm test`: 1296 passam e 7 são pulados. `npm run verify` fecha 33/33 URLs.
- O loop percorre detect, specify, generate, verify, gate e promote. Cada etapa é testável. Se o gate fica vermelho, o delta é desfeito.
- Contexto tratado como orçamento: +499 tokens sobre o teto de 1500. Cold start médio de ~82 ms em 7 execuções.
- Equipes persistentes com quadro e passo determinístico, barramento de eventos com cursor salvo e memória com redação de segredo.
- Auditoria de refutação com juiz externo na CLI, ledger de segurança para decisões block e warn, gate estático de 13 regras.
- 48 modelos com capacidades conferidas, nove papéis de modelo e cooldown para modelos que falham.

Site: https://kelvinoliveiracode.github.io/SelfEvoPI-site/
Código: https://github.com/KelvinOliveiraCode/SelfEvoPI

**Detecção de fraude em cartão**

Pipeline de machine learning sobre 284 mil transações, com 0,17% de fraude na base. O desbalanceamento foi tratado e três modelos foram comparados por critério declarado. O modelo final chegou a ROC AUC 0,94.

https://github.com/KelvinOliveiraCode/deteccao-de-fraudes

**KODAROS**

Plataforma de produtos digitais. A landing reúne oito e-books e seis páginas de serviço. O diagnóstico de três perguntas devolve um PDF. As ferramentas rodam 100% no navegador: 53 calculadoras e geradores, PWA offline-first e 19 asserts no smoke test com jsdom em CI. O mostruário tem 50 demos por nicho.

Site: https://kelvinoliveiracode.github.io/kodaros-landing/
Ferramentas: https://kelvinoliveiracode.github.io/kodaros-ferramentas/
Código: https://github.com/KelvinOliveiraCode/kodaros-landing

## Números

- 109 repositórios públicos
- 14 páginas no ar
- 5 bootcamps DIO em 2026, 219 horas de formação
- Cloud4All aprovado no CONNEPI 2026

Origem: https://github.com/KelvinOliveiraCode/portfolio/tree/main/data

## Onde atuo

- Dados e IA: pipelines em Python, machine learning com scikit-learn e XGBoost, dashboards e agentes com validação anti-alucinação.
- Backend: APIs REST com Spring Boot 3 e Java 21, padrões de projeto com propósito, testes e CI.
- Web e produto: sites estáticos em HTML, CSS e JavaScript puro, PWAs offline-first, publicação e manutenção.
- Cibersegurança: pentest com relatório por CWE, detecção com alertas MITRE ATT&CK, honeypot e conformidade LGPD.
- Redes e infraestrutura: topologia LAN, Modbus TCP do zero, survey de Wi-Fi, VPC em camadas e infraestrutura como código.
- TI e suporte: service desk com SLA, automação de estações, backup com verificação por hash e onboarding de câmeras.

## Laboratório

<details>
<summary>Índice de projetos por área</summary>

- Agentes e IA: SelfEvoPI, BIA, agente de suporte bancário RAG, gerador de currículos ATS
- Dados: detecção de fraude, análise de churn, previsão de demanda, KB-search, MLOps de drift
- Backend: Kodapay, KodaBudget, portal com OAuth2 e RBAC, JavaForge, marketplace de serviços
- Web: KODAROS, Garimpo, portfólio, Olaria, SlideStage, Cloud4All
- Cibersegurança: pentest lab, SIEM, honeypot, auditoria de headers, detector de deepfake
- Infraestrutura: VPC em três camadas, Modbus TCP, WiFi survey, FinOps, Terraform
- TI: service desk, inventário de ativos, backup GFS, onboarding de workstation

</details>

<details>
<summary>Formação e bootcamps</summary>

Ciência da Computação no IFPA e ADS na Uniasselvi. Formação de 219 horas na DIO em 2026: Santander, dados com Python e IA (50 h); Bradesco, GenAI, dados e cyber (52 h); Riachuelo, criação de produtos com IA (35 h); Santander, Excel com IA e Claude (29 h); CI&T, Java AI Copilot (53 h).

</details>

## Contato

LinkedIn: https://www.linkedin.com/in/kelvin-oliveira-code/
Email: kelvinrebelosw@gmail.com
WhatsApp: +55 91 98613-4599
Ananindeua, PA

# Kelvin Oliveira

[Português](README.md)

I build software with agents. I write the specification, set the limits for each task and review the result. The agents write the code, run the tests and produce the evidence. I operate what comes out of that loop.

SelfEvoPI is the harness that came out of that process. It now runs the cycle itself: it detects a gap, writes the artifact, verifies it, applies the gate and either promotes or reverts.

Portfolio: https://kelvinoliveiracode.github.io/portfolio/
Projects: https://kelvinoliveiracode.github.io/portfolio/projetos/
LinkedIn: https://www.linkedin.com/in/kelvin-oliveira-code/

```text
KELVIN OLIVEIRA
+-- agents      SelfEvoPI, orchestration, evals
+-- data        fraud detection, churn, KB-search
+-- cyber       pentest 11 CWE, SIEM 7 rules
+-- infra       VPC 3 tiers, Modbus from scratch
+-- backend     Kodapay 6 GoF, Java 21, Spring Boot 3
+-- web         KODAROS 8 e-books, Garimpo 131 offers
+-- it          service desk, hash-verified backup, onboarding
```

## How I work

- I define the problem, the constraints and the done criterion before asking for code.
- I orchestrate agents with explicit roles, permissions and context limits.
- I verify with tests, deterministic evals and checks against the source. Every number comes from a command I ran or a primary source.
- I publish and maintain. 14 pages are live and the repositories keep getting updates.

## Work

**SelfEvoPI**

A coding-agent harness at version 2.0.0, native on Windows, with zero npm dependencies. The CLI is the only surface and the engine is an external process spoken over RPC.

- 1303 tests in `npm test`: 1296 pass and 7 are skipped. `npm run verify` closes 33/33 URLs.
- The loop runs detect, specify, generate, verify, gate and promote. Every stage is testable. A red gate reverts the delta.
- Context is a budget: +499 tokens over a ceiling of 1500. Average cold start of ~82 ms across 7 runs.
- Persistent teams with a board and a deterministic step, an event bus with a saved cursor and memory with secret redaction.
- Refutation audit with an external judge in the CLI, a security ledger for block and warn decisions, a static gate with 13 rules.
- 48 models with checked capabilities, nine model roles and a cooldown for models that fail.

Site: https://kelvinoliveiracode.github.io/SelfEvoPI-site/
Code: https://github.com/KelvinOliveiraCode/SelfEvoPI

**Credit-card fraud detection**

A machine-learning pipeline over 284,000 transactions, with 0.17% fraud in the data. The imbalance was handled and three models were compared against a declared criterion. The final model reached ROC AUC 0.94.

https://github.com/KelvinOliveiraCode/deteccao-de-fraudes

**KODAROS**

A platform for digital products. The landing brings together eight e-books and six service pages. A three-question diagnosis returns a PDF. The tools run entirely in the browser: 53 calculators and generators, an offline-first PWA and 19 asserts in a jsdom smoke test on CI. The showcase has 50 demos, one per niche.

Site: https://kelvinoliveiracode.github.io/kodaros-landing/
Tools: https://kelvinoliveiracode.github.io/kodaros-ferramentas/
Code: https://github.com/KelvinOliveiraCode/kodaros-landing

## Numbers

- 109 public repositories
- 14 live pages
- 5 DIO bootcamps in 2026, 219 hours of training
- Cloud4All accepted at CONNEPI 2026

Source: https://github.com/KelvinOliveiraCode/portfolio/tree/main/data

## Where I work

- Data and AI: pipelines in Python, machine learning with scikit-learn and XGBoost, dashboards and agents with anti-hallucination validation.
- Backend: REST APIs with Spring Boot 3 and Java 21, design patterns with a stated purpose, tests and CI.
- Web and product: static sites in plain HTML, CSS and JavaScript, offline-first PWAs, publishing and maintenance.
- Cybersecurity: pentests with CWE reporting, detection with MITRE ATT&CK alerts, honeypots and LGPD compliance.
- Networks and infrastructure: LAN topology, Modbus TCP from scratch, WiFi surveys, tiered VPCs and infrastructure as code.
- IT and support: service desk with SLA, workstation automation, hash-verified backups and camera onboarding.

## Lab

<details>
<summary>Project index by area</summary>

- Agents and AI: SelfEvoPI, BIA, banking RAG agent, ATS resume builder
- Data: fraud detection, churn analysis, demand forecasting, KB-search, drift MLOps
- Backend: Kodapay, KodaBudget, OAuth2 and RBAC portal, JavaForge, services marketplace
- Web: KODAROS, Garimpo, portfolio, Olaria, SlideStage, Cloud4All
- Cybersecurity: pentest lab, SIEM, honeypot, header audit, deepfake detector
- Infrastructure: three-tier VPC, Modbus TCP, WiFi survey, FinOps, Terraform
- IT: service desk, asset inventory, GFS backup, workstation onboarding

</details>

<details>
<summary>Education and bootcamps</summary>

Computer Science at IFPA and a degree in Information Systems at Uniasselvi. 219 hours of training at DIO in 2026: Santander, data with Python and AI (50 h); Bradesco, GenAI, data and cyber (52 h); Riachuelo, building products with AI (35 h); Santander, Excel with AI and Claude (29 h); CI&T, Java AI Copilot (53 h).

</details>

## Contact

LinkedIn: https://www.linkedin.com/in/kelvin-oliveira-code/
Email: kelvinrebelosw@gmail.com
WhatsApp: +55 91 98613-4599
Ananindeua, PA, Brazil

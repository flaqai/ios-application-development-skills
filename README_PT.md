<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Um pacote de habilidades Codex para lançamento na App Store, ASO, SwiftUI e depuração no Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · <strong>Português</strong> · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Um plugin para todo o fluxo de entrega iOS

`ios-application-development-skills` é um plugin público do Codex Git Marketplace que combina operações seguras de lançamento na App Store, ASO somente para a Apple App Store e as nove habilidades OpenAI Build iOS Apps.

## Instalação rápida

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## O que você pode fazer

| Necessidade | Habilidade | Resultado |
| --- | --- | --- |
| Auditar página da App Store, palavras-chave e capturas | `$app-store-aso` | `aso-handoff.json` baseado em evidências e aprovado por campo |
| Criar, traduzir e validar um lançamento | `$ios-appstore-release-manager` | Vínculo de versão Flutter/Xcode e formulário schema 8 |
| Criar ou refatorar SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Layouts estáveis e views sustentáveis |
| Investigar crash, desempenho ou memória | `$ios-debugger-agent`, ETTrace, Memgraph | Diagnóstico com evidências do Simulator |

## As 11 habilidades

Além das duas habilidades de App Store, inclui `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` e `$swiftui-view-refactor`. Veja todos os detalhes no [README em inglês](README.md).

## Limites de lançamento seguro

Description, Promotional Text, Keywords e What’s New precisam de aprovação individual antes que `aso-handoff.json` seja marcado como `approved`. A habilidade de lançamento preserva aprovação por campo, confirmação de conflitos e leitura após salvar; ela para antes de “Add for Review”.

## Compatibilidade e licença

Os fluxos de Simulator exigem macOS, Xcode, Node.js/npm/npx e um iOS Simulator disponível. Leia a [nota de compatibilidade do XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Este repositório é licenciado sob a [MIT License](LICENSE).

## Ganhe comissão com o programa de afiliados da Flaq AI

Desenvolvedores, criadores de agentes, avaliadores, equipes criativas e educadores de IA podem [participar do programa de afiliados da Flaq AI](https://flaq.ai/affiliate-program/), criar um link de indicação e ganhar comissão sobre pedidos elegíveis feitos por usuários indicados. A estrutura pública atual informa 20% no primeiro pedido pago válido e 10% nos pedidos pagos válidos seguintes feitos dentro de 60 dias após o cadastro do usuário indicado.

Reembolsos, estornos, atribuição, análise de risco e regras de política podem afetar elegibilidade e pagamento. Divulgue claramente a relação de afiliado ao compartilhar um link de indicação e verifique os termos vigentes antes de promover. Leia o [guia do programa de afiliados em 15 idiomas](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

<p align="center"><img src="assets/ios-development-skills-hero-v5.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Ein Codex-Skillpaket für App-Store-Release, ASO, SwiftUI und Simulator-Debugging.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · <strong>Deutsch</strong> · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Ein Plugin für den gesamten iOS-Workflow

`ios-application-development-skills` ist ein öffentliches Codex-Git-Marketplace-Plugin. Es kombiniert sichere App-Store-Release-Abläufe, ASO nur für den Apple App Store und alle neun OpenAI Build iOS Apps Skills.

## Schnell installieren

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Was Sie damit tun können

| Ziel | Skill | Ergebnis |
| --- | --- | --- |
| App-Store-Seite, Keywords und Screenshots prüfen | `$app-store-aso` | Evidenzbasiertes, feldweise genehmigtes `aso-handoff.json` |
| Release erstellen, übersetzen und validieren | `$ios-appstore-release-manager` | Flutter/Xcode-Versionsbindung und Schema-8-Formular |
| SwiftUI bauen oder refaktorieren | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Stabile Layouts und wartbare Views |
| Abstürze, Performance oder Speicher analysieren | `$ios-debugger-agent`, ETTrace, Memgraph | Simulator-basierte Diagnose |

## Die 11 Skills

Zusätzlich zu den zwei App-Store-Skills enthält das Plugin `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` und `$swiftui-view-refactor`. Alle Details stehen im [englischen README](README.md).

## Sichere Release-Grenzen

Description, Promotional Text, Keywords und What’s New müssen einzeln freigegeben sein, bevor `aso-handoff.json` den Status `approved` erhält. Der Release-Skill behält feldweise Freigabe, Konfliktbestätigung und Rücklesen nach dem Speichern bei und stoppt vor „Add for Review“.

## Kompatibilität und Lizenz

Simulator-Workflows benötigen macOS, Xcode, Node.js/npm/npx und einen verfügbaren iOS Simulator. Lesen Sie den [XcodeBuildMCP-Kompatibilitätshinweis](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Dieses Repository steht unter der [MIT-Lizenz](LICENSE).

## Mit dem Flaq AI Affiliate Program Provision verdienen

Entwickler, Agent-Builder, Reviewer, Kreativteams und KI-Lehrende können dem [Flaq AI Affiliate Program](https://flaq.ai/affiliate-program/) beitreten, einen Empfehlungslink erstellen und Provisionen aus berechtigten Bestellungen geworbener Nutzer verdienen. Die aktuelle öffentliche Struktur nennt 20 % für die erste gültige bezahlte Bestellung und 10 % für weitere gültige bezahlte Bestellungen innerhalb von 60 Tagen nach der Registrierung des geworbenen Nutzers.

Erstattungen, Rückbuchungen, Zuordnung, Risikoprüfung und Richtlinien können Berechtigung und Auszahlung beeinflussen. Legen Sie die Affiliate-Beziehung beim Teilen eines Empfehlungslinks klar offen und prüfen Sie vor der Werbung die aktuellen Bedingungen. Lesen Sie den [Affiliate-Program-Guide in 15 Sprachen](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

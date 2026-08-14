<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Un ensemble de compétences Codex pour la publication App Store, l’ASO, SwiftUI et le débogage Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · <strong>Français</strong> · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Un plugin pour tout le parcours iOS

`ios-application-development-skills` est un plugin public Codex Git Marketplace qui associe des opérations de publication App Store sûres, l’ASO Apple App Store uniquement et les neuf compétences OpenAI Build iOS Apps.

## Installation rapide

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Ce que vous pouvez faire

| Besoin | Compétence | Résultat |
| --- | --- | --- |
| Auditer une fiche App Store, les mots-clés et les captures | `$app-store-aso` | `aso-handoff.json` approuvé champ par champ et fondé sur des preuves |
| Créer, traduire et valider une release | `$ios-appstore-release-manager` | Liaison Flutter/Xcode et formulaire schema 8 |
| Créer ou refactoriser SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Interfaces stables et vues maintenables |
| Diagnostiquer crash, performance ou mémoire | `$ios-debugger-agent`, ETTrace, Memgraph | Diagnostic fondé sur Simulator |

## Les 11 compétences

En plus des deux compétences App Store, le plugin inclut `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` et `$swiftui-view-refactor`. Consultez le [README anglais](README.md) pour le détail.

## Limites de sécurité des releases

Description, Promotional Text, Keywords et What’s New doivent être approuvés individuellement avant que `aso-handoff.json` puisse devenir `approved`. La compétence de publication conserve l’approbation par champ, la confirmation des conflits et la relecture après sauvegarde ; elle s’arrête avant « Add for Review ».

## Compatibilité et licence

Les flux Simulator demandent macOS, Xcode, Node.js/npm/npx et un iOS Simulator disponible. Lisez la [note de compatibilité XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Ce dépôt est sous [licence MIT](LICENSE).

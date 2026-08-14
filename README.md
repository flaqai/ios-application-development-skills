<p align="center">
  <img src="assets/ios-development-skills-hero-v5.png" alt="iOS Application Development Skills — App Store release, ASO, SwiftUI, and Simulator workflows" width="100%">
</p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">
  A Codex marketplace for shipping better iOS apps — from App Store metadata to SwiftUI and Simulator debugging.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-34C759.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/plugin-v0.1.0-007AFF.svg" alt="Plugin version 0.1.0">
  <img src="https://img.shields.io/badge/skills-11-5856D6.svg" alt="11 skills">
  <img src="https://img.shields.io/badge/platform-Codex-0A84FF.svg" alt="Codex marketplace">
</p>

<p align="center">
  <strong>English</strong> · <a href="README_ZH.md">简体中文</a> · <a href="README_ZH_TW.md">繁體中文</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a><br>
  <a href="README_ES.md">Español</a> · <a href="README_FR.md">Français</a> · <a href="README_DE.md">Deutsch</a> · <a href="README_PT.md">Português</a> · <a href="README_IT.md">Italiano</a><br>
  <a href="README_AR.md">العربية</a> · <a href="README_RU.md">Русский</a> · <a href="README_ID.md">Bahasa Indonesia</a> · <a href="README_TH.md">ไทย</a> · <a href="README_VI.md">Tiếng Việt</a>
</p>

## One plugin, the iOS delivery workflow

`ios-application-development-skills` is a public Codex Git Marketplace plugin that brings together safe App Store release operations, Apple-only ASO, and all nine OpenAI Build iOS Apps skills. It is designed as a practical path from product copy to a polished, debuggable iOS build.

| Start with this need | Use this skill | What you get |
| --- | --- | --- |
| Audit an App Store listing or improve keywords, screenshots, and positioning | [`$app-store-aso`](plugins/ios-application-development-skills/skills/app-store-aso/SKILL.md) | Evidence-backed audit and approval-gated `aso-handoff.json` |
| Prepare, translate, validate, or safely draft a release | [`$ios-appstore-release-manager`](plugins/ios-application-development-skills/skills/ios-appstore-release-manager/SKILL.md) | Flutter/Xcode version binding and a schema 8 release form |
| Build or refactor a SwiftUI screen | [`$swiftui-ui-patterns`](plugins/ios-application-development-skills/skills/swiftui-ui-patterns/SKILL.md) · [`$swiftui-view-refactor`](plugins/ios-application-development-skills/skills/swiftui-view-refactor/SKILL.md) | Stable layouts, state flow, and maintainable views |
| Reproduce a crash, performance issue, or memory leak | [`$ios-debugger-agent`](plugins/ios-application-development-skills/skills/ios-debugger-agent/SKILL.md) · ETTrace · Memgraph | Simulator evidence instead of guesswork |

## Install in under a minute

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

Then ask Codex naturally, for example:

```text
Audit this App Store listing and prepare an approved ASO handoff.
Create a release form from this Flutter project and translate it to Japanese.
Run the app in Simulator and diagnose why the onboarding screen crashes.
Refactor this large SwiftUI view without changing its behavior.
```

## What is included

### App Store delivery

| Skill | Best for | Guardrails |
| --- | --- | --- |
| `$app-store-aso` | Apple App Store listing audits, competition, keywords, screenshots, previews, and positioning | Apple-only; separates facts, official rules, non-official benchmarks, and evidence gaps |
| `$ios-appstore-release-manager` | Release forms, localization, Flutter/Xcode version detection, and App Store Connect drafting | Field-by-field approval, conflict checks, read-back after save, and stops before submission for review |

The two skills hand off through `aso-handoff.json` schema 1. Description, Promotional Text, Keywords, and What’s New must each be approved before an ASO handoff is marked `approved`. App Name and Subtitle remain recommendations; they are never changed automatically.

### OpenAI Build iOS Apps skills

| Area | Skills |
| --- | --- |
| System surfaces | `$ios-app-intents` for App Intents, entities, App Shortcuts, Siri, and Spotlight |
| Simulator workflow | `$ios-debugger-agent`, `$ios-simulator-browser` |
| Performance and memory | `$ios-ettrace-performance`, `$ios-memgraph-leaks` |
| SwiftUI implementation | `$swiftui-ui-patterns`, `$swiftui-view-refactor`, `$swiftui-performance-audit`, `$swiftui-liquid-glass` |

All nine upstream skills preserve their original names, instructions, agents, references, scripts, and templates from the tracked OpenAI `build-ios-apps` v0.1.2 snapshot.

## Release path: ASO to App Store Connect

```text
Public listing / product material
        ↓
$app-store-aso — audit, evidence, four field approvals
        ↓
approved aso-handoff.json
        ↓
$ios-appstore-release-manager — version binding, localization, validation
        ↓
App Store Connect draft — save and read back
        ↓
Stop before “Add for Review”
```

Create and finalize an ASO handoff:

```bash
python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  new --source-locale en-US --output /path/to/aso-handoff.json

python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  finalize /path/to/aso-handoff.json
```

Bind a release form to a Flutter or native Xcode project:

```bash
python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/flutter-project --source-locale zh-Hans

python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/xcode-project --project-type xcode \
  --workspace App.xcworkspace --scheme App --configuration Release
```

Release form schema 8 resolves versions in this order: explicit paired `--version` and `--build` arguments, Flutter `pubspec.yaml`, then native Xcode build settings. Existing schema 1–7 forms continue to be read and validated; this plugin never rewrites or migrates them automatically.

## Requirements and compatibility

The plugin configures XcodeBuildMCP, so macOS, Xcode, Node.js/npm/npx, and an available iOS Simulator are required for Simulator workflows. The MCP service may start even for non-development tasks; disable the plugin temporarily in Codex if that is not wanted.

> [!IMPORTANT]
> The byte-preserved OpenAI upstream MCP configuration uses `xcodebuildmcp@latest`. Its API can evolve independently of the skill text. Before Simulator work, inspect the currently exposed tool schema; if a required capability is missing or incompatible, stop and report it rather than guessing. See [the compatibility note](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md).

## Keep the upstream snapshot healthy

The repository checks OpenAI `main` weekly. A change creates a review PR only; it is never merged automatically.

```bash
python3 scripts/sync_openai_ios_skills.py \
  --target plugins/ios-application-development-skills --check

python3 -m unittest discover \
  -s plugins/ios-application-development-skills/skills/ios-appstore-release-manager/tests -v

python3 scripts/validate_bundle.py
```

Read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [`OPENAI_UPSTREAM.json`](plugins/ios-application-development-skills/OPENAI_UPSTREAM.json) for licenses, sources, fixed commits, and file hashes.

## Earn commission with the Flaq AI Affiliate Program

Developers, agent builders, reviewers, creative teams, and AI educators can [join the Flaq AI Affiliate Program](https://flaq.ai/affiliate-program/), create a referral link, and earn commission from eligible orders made by referred users. The current public structure lists 20% on the first valid paid order and 10% on following valid paid orders within 60 days after the referred user's registration.

Refunds, chargebacks, attribution, risk review, and policy rules can affect eligibility and payout. Disclose the affiliate relationship clearly when sharing a referral link, and check the live program terms before promoting. Read the [15-language Affiliate Program guide](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

## License

This repository is released under the [MIT License](LICENSE). Third-party notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

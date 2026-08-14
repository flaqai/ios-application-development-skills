<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">App Store リリース、ASO、SwiftUI、Simulator デバッグを一つにまとめた Codex 用 iOS スキル集。</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · <strong>日本語</strong> · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## 一つのプラグインで iOS リリースまで

`ios-application-development-skills` は、安全な App Store リリース、Apple App Store 専用の ASO、OpenAI Build iOS Apps の 9 スキルをまとめた公開 Codex Git Marketplace プラグインです。

## クイックスタート

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## できること

| 目的 | スキル | 成果物 |
| --- | --- | --- |
| App Store ページ、キーワード、スクリーンショットの監査 | `$app-store-aso` | 根拠に基づき承認された `aso-handoff.json` |
| リリース情報の作成、翻訳、検証 | `$ios-appstore-release-manager` | Flutter/Xcode のバージョン紐付けと schema 8 フォーム |
| SwiftUI の実装・リファクタリング | `$swiftui-ui-patterns`、`$swiftui-view-refactor` | 安定したレイアウトと保守しやすい View |
| クラッシュ、性能、メモリ問題の調査 | `$ios-debugger-agent`、ETTrace、Memgraph | Simulator に基づく調査結果 |

## 11 スキル

App Store 向けの二つに加え、`$ios-app-intents`、`$ios-debugger-agent`、`$ios-ettrace-performance`、`$ios-memgraph-leaks`、`$ios-simulator-browser`、`$swiftui-liquid-glass`、`$swiftui-performance-audit`、`$swiftui-ui-patterns`、`$swiftui-view-refactor` を収録しています。詳細は [English README](README.md) を参照してください。

## 安全なリリース境界

Description、Promotional Text、Keywords、What’s New はそれぞれ承認されてから `aso-handoff.json` を `approved` にできます。リリーススキルは項目別承認、競合確認、保存後の再読込を維持し、「審査に追加」の前で停止します。

## 互換性とライセンス

Simulator ワークフローには macOS、Xcode、Node.js/npm/npx、利用可能な iOS Simulator が必要です。事前に [XcodeBuildMCP 互換性メモ](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md) を確認してください。ライセンスは [MIT](LICENSE) です。

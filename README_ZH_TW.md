<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS 應用程式開發技能" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">整合 App Store 發布、ASO、SwiftUI 與 Simulator 偵錯的 Codex iOS 技能組。</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · <strong>繁體中文</strong> · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## 一個外掛，完整 iOS 交付流程

`ios-application-development-skills` 是公開的 Codex Git Marketplace 外掛，結合安全的 App Store 發布、僅支援 Apple App Store 的 ASO，以及 9 個 OpenAI Build iOS Apps 官方技能。

## 快速安裝

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## 你可以完成的工作

| 需求 | 技能 | 產出 |
| --- | --- | --- |
| 稽核 App Store 頁面、關鍵字與截圖 | `$app-store-aso` | 以證據為基礎、逐欄核准的 `aso-handoff.json` |
| 建立、翻譯與驗證版本資料 | `$ios-appstore-release-manager` | Flutter/Xcode 版本繫結與 schema 8 發布表單 |
| 建置或重構 SwiftUI | `$swiftui-ui-patterns`、`$swiftui-view-refactor` | 穩定版面、狀態流與可維護 View |
| 排查崩潰、效能或記憶體問題 | `$ios-debugger-agent`、ETTrace、Memgraph | 以 Simulator 證據定位問題 |

## 11 個技能

除兩個 App Store 技能外，外掛還包含 `$ios-app-intents`、`$ios-debugger-agent`、`$ios-ettrace-performance`、`$ios-memgraph-leaks`、`$ios-simulator-browser`、`$swiftui-liquid-glass`、`$swiftui-performance-audit`、`$swiftui-ui-patterns` 與 `$swiftui-view-refactor`。完整說明請見 [English README](README.md)。

## 安全發布邊界

ASO 交接需讓 Description、Promotional Text、Keywords 與 What’s New 分別核准後才可設為 `approved`。發布技能會保留逐欄核准、衝突確認與保存後回讀，並預設停止在「新增以供審查」之前。

## 相容性與授權

Simulator 工作流程需要 macOS、Xcode、Node.js/npm/npx 與可用的 iOS Simulator。使用前請閱讀 [XcodeBuildMCP 相容性說明](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md)。本專案採用 [MIT License](LICENSE)。

## 透過 Flaq AI Affiliate Program 賺取佣金

開發者、Agent 建構者、評測者、創意團隊與 AI 教育者可[加入 Flaq AI Affiliate Program](https://flaq.ai/affiliate-program/)，建立推薦連結，並從符合資格的推薦訂單獲得佣金。目前公開規則為：推薦使用者首筆有效付費訂單可獲 20%，註冊後 60 天內的後續有效付費訂單可獲 10%。

退款、拒付、歸因、風險審查與政策規則都可能影響資格及發放。分享推薦連結時請清楚揭露合作關係，並在推廣前確認最新條款。閱讀 [15 語言 Affiliate Program 指南](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md)。

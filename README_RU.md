<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Набор навыков Codex для релизов в App Store, ASO, SwiftUI и отладки в Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · <strong>Русский</strong> · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Один плагин для всего пути iOS

`ios-application-development-skills` — публичный плагин Codex Git Marketplace. Он объединяет безопасные операции релиза в App Store, ASO только для Apple App Store и все девять навыков OpenAI Build iOS Apps.

## Быстрая установка

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Возможности

| Задача | Навык | Результат |
| --- | --- | --- |
| Аудит страницы App Store, ключевых слов и скриншотов | `$app-store-aso` | `aso-handoff.json`, одобренный по полям и основанный на доказательствах |
| Создание, перевод и проверка релиза | `$ios-appstore-release-manager` | Привязка версии Flutter/Xcode и форма schema 8 |
| Создание или рефакторинг SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Стабильные макеты и поддерживаемые View |
| Анализ сбоев, производительности и памяти | `$ios-debugger-agent`, ETTrace, Memgraph | Диагностика на основе Simulator |

## 11 навыков

Помимо двух навыков App Store, плагин включает `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` и `$swiftui-view-refactor`. Полное описание — в [английском README](README.md).

## Безопасные границы релиза

Description, Promotional Text, Keywords и What’s New должны быть одобрены по отдельности, прежде чем `aso-handoff.json` получит статус `approved`. Навык релиза сохраняет поэтапное одобрение, подтверждение конфликтов и повторное чтение после сохранения и останавливается до «Add for Review».

## Совместимость и лицензия

Для сценариев Simulator нужны macOS, Xcode, Node.js/npm/npx и доступный iOS Simulator. Прочтите [заметку о совместимости XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Репозиторий распространяется по [лицензии MIT](LICENSE).

## Получайте комиссию с программой Flaq AI Affiliate Program

Разработчики, создатели агентов, обозреватели, творческие команды и преподаватели ИИ могут [присоединиться к партнёрской программе Flaq AI](https://flaq.ai/affiliate-program/), создать реферальную ссылку и получать комиссию с соответствующих требованиям заказов приглашённых пользователей. Текущая публичная структура указывает 20 % за первый действительный оплаченный заказ и 10 % за последующие действительные оплаченные заказы, сделанные в течение 60 дней после регистрации приглашённого пользователя.

Возвраты, чарджбэки, атрибуция, проверка рисков и правила политики могут влиять на право участия и выплату. Ясно раскрывайте партнёрские отношения при публикации реферальной ссылки и проверяйте актуальные условия перед продвижением. Прочтите [руководство по партнёрской программе на 15 языках](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

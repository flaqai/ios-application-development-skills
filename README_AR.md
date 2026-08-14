<p align="center"><img src="assets/ios-development-skills-hero.png" alt="مهارات تطوير تطبيقات iOS" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">حزمة مهارات Codex لإصدار تطبيقات App Store وتحسين ASO وSwiftUI وتصحيح الأخطاء عبر Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br><strong>العربية</strong> · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## إضافة واحدة لمسار iOS الكامل

`ios-application-development-skills` إضافة عامة في Codex Git Marketplace تجمع عمليات إصدار آمنة في App Store وASO المخصص لمتجر Apple App Store وتسع مهارات OpenAI Build iOS Apps.

## تثبيت سريع

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## ما الذي يمكنك إنجازه

| الحاجة | المهارة | النتيجة |
| --- | --- | --- |
| تدقيق صفحة App Store والكلمات المفتاحية ولقطات الشاشة | `$app-store-aso` | ملف `aso-handoff.json` معتمد لكل حقل ومدعوم بالأدلة |
| إنشاء الإصدار وترجمته والتحقق منه | `$ios-appstore-release-manager` | ربط إصدار Flutter/Xcode ونموذج schema 8 |
| بناء SwiftUI أو إعادة هيكلته | `$swiftui-ui-patterns`، `$swiftui-view-refactor` | تخطيطات مستقرة وواجهات سهلة الصيانة |
| فحص الأعطال أو الأداء أو الذاكرة | `$ios-debugger-agent`، ETTrace، Memgraph | تشخيص يعتمد على أدلة Simulator |

## المهارات الإحدى عشرة

إضافة إلى مهارتي App Store، تتضمن الإضافة `$ios-app-intents` و`$ios-debugger-agent` و`$ios-ettrace-performance` و`$ios-memgraph-leaks` و`$ios-simulator-browser` و`$swiftui-liquid-glass` و`$swiftui-performance-audit` و`$swiftui-ui-patterns` و`$swiftui-view-refactor`. راجع [README الإنجليزي](README.md) للتفاصيل الكاملة.

## حدود الإصدار الآمن

يجب اعتماد Description وPromotional Text وKeywords وWhat’s New بشكل منفصل قبل وضع `approved` في `aso-handoff.json`. تحتفظ مهارة الإصدار بالموافقة لكل حقل وتأكيد التعارض وقراءة البيانات بعد الحفظ، وتتوقف قبل “Add for Review”.

## التوافق والترخيص

تتطلب مسارات Simulator نظام macOS وXcode وNode.js/npm/npx ومحاكي iOS متاحًا. راجع [ملاحظة توافق XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). هذا المستودع مرخص بموجب [MIT](LICENSE).

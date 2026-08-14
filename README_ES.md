<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Un paquete de habilidades para Codex que reúne lanzamientos de App Store, ASO, SwiftUI y depuración con Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br><strong>Español</strong> · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Un plugin para el flujo completo de iOS

`ios-application-development-skills` es un plugin público de Codex Git Marketplace que combina publicación segura en App Store, ASO exclusivo para Apple App Store y las nueve habilidades OpenAI Build iOS Apps.

## Instalación rápida

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Qué puedes hacer

| Necesidad | Habilidad | Resultado |
| --- | --- | --- |
| Auditar una ficha de App Store, palabras clave y capturas | `$app-store-aso` | `aso-handoff.json` basado en evidencia y aprobado por campo |
| Crear, traducir y validar una versión | `$ios-appstore-release-manager` | Enlace de versión Flutter/Xcode y formulario schema 8 |
| Crear o refactorizar SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Diseño estable y vistas mantenibles |
| Investigar fallos, rendimiento o memoria | `$ios-debugger-agent`, ETTrace, Memgraph | Diagnóstico con evidencia de Simulator |

## Las 11 habilidades

Además de las dos habilidades de App Store, incluye `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` y `$swiftui-view-refactor`. Consulta el [README en inglés](README.md) para todos los detalles.

## Límites de seguridad para publicar

Description, Promotional Text, Keywords y What’s New deben aprobarse de forma individual antes de marcar `aso-handoff.json` como `approved`. La habilidad de publicación conserva aprobaciones por campo, confirmación de conflictos y lectura posterior al guardado; se detiene antes de “Add for Review”.

## Compatibilidad y licencia

Los flujos de Simulator requieren macOS, Xcode, Node.js/npm/npx y un iOS Simulator disponible. Revisa la [nota de compatibilidad de XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Este repositorio usa la [licencia MIT](LICENSE).

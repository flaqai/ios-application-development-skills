<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Paket skill Codex untuk rilis App Store, ASO, SwiftUI, dan debugging Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · <strong>Bahasa Indonesia</strong> · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md)</p>

## Satu plugin untuk seluruh alur iOS

`ios-application-development-skills` adalah plugin Codex Git Marketplace publik yang menggabungkan operasi rilis App Store yang aman, ASO khusus Apple App Store, dan sembilan skill OpenAI Build iOS Apps.

## Instalasi cepat

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Yang dapat Anda lakukan

| Kebutuhan | Skill | Hasil |
| --- | --- | --- |
| Audit halaman App Store, kata kunci, dan screenshot | `$app-store-aso` | `aso-handoff.json` berbasis bukti dan disetujui per bidang |
| Membuat, menerjemahkan, dan memvalidasi rilis | `$ios-appstore-release-manager` | Pengikatan versi Flutter/Xcode dan formulir schema 8 |
| Membangun atau memfaktorkan ulang SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Tata letak stabil dan View yang mudah dipelihara |
| Menyelidiki crash, performa, atau memori | `$ios-debugger-agent`, ETTrace, Memgraph | Diagnosis berbasis bukti Simulator |

## 11 skill

Selain dua skill App Store, plugin ini mencakup `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns`, dan `$swiftui-view-refactor`. Lihat [README bahasa Inggris](README.md) untuk detail lengkap.

## Batas rilis aman

Description, Promotional Text, Keywords, dan What’s New harus disetujui satu per satu sebelum `aso-handoff.json` ditandai `approved`. Skill rilis mempertahankan persetujuan per bidang, konfirmasi konflik, dan pembacaan kembali setelah penyimpanan; proses berhenti sebelum “Add for Review”.

## Kompatibilitas dan lisensi

Alur Simulator memerlukan macOS, Xcode, Node.js/npm/npx, dan iOS Simulator yang tersedia. Baca [catatan kompatibilitas XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Repositori ini menggunakan [lisensi MIT](LICENSE).

## Dapatkan komisi dengan Program Afiliasi Flaq AI

Developer, pembuat agen, reviewer, tim kreatif, dan pendidik AI dapat [bergabung dengan Program Afiliasi Flaq AI](https://flaq.ai/affiliate-program/), membuat tautan rujukan, dan memperoleh komisi dari pesanan yang memenuhi syarat oleh pengguna rujukan. Struktur publik saat ini menyebutkan 20% untuk pesanan berbayar valid pertama dan 10% untuk pesanan berbayar valid berikutnya yang dibuat dalam 60 hari setelah pendaftaran pengguna rujukan.

Pengembalian dana, chargeback, atribusi, peninjauan risiko, dan aturan kebijakan dapat memengaruhi kelayakan dan pembayaran. Ungkapkan hubungan afiliasi dengan jelas saat membagikan tautan rujukan dan periksa ketentuan terkini sebelum mempromosikannya. Baca [panduan Program Afiliasi dalam 15 bahasa](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

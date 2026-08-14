<p align="center">
  <img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills：App Store 发布、ASO、SwiftUI 与 Simulator 工作流" width="100%">
</p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">
  一个覆盖 App Store 发布、ASO、SwiftUI 与 Simulator 排错的 Codex iOS 技能整合包。
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/许可证-MIT-34C759.svg" alt="MIT 许可证"></a>
  <img src="https://img.shields.io/badge/插件-v0.1.0-007AFF.svg" alt="插件版本 0.1.0">
  <img src="https://img.shields.io/badge/技能-11-5856D6.svg" alt="11 个技能">
  <img src="https://img.shields.io/badge/平台-Codex-0A84FF.svg" alt="Codex Marketplace">
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong> · <a href="README_ZH_TW.md">繁體中文</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a><br>
  <a href="README_ES.md">Español</a> · <a href="README_FR.md">Français</a> · <a href="README_DE.md">Deutsch</a> · <a href="README_PT.md">Português</a> · <a href="README_IT.md">Italiano</a><br>
  <a href="README_AR.md">العربية</a> · <a href="README_RU.md">Русский</a> · <a href="README_ID.md">Bahasa Indonesia</a> · <a href="README_TH.md">ไทย</a> · <a href="README_VI.md">Tiếng Việt</a>
</p>

## 一个插件，贯穿 iOS 交付流程

`ios-application-development-skills` 是一个公开的 Codex Git Marketplace 插件。它将安全的 App Store 发布操作、仅面向 Apple App Store 的 ASO，以及 OpenAI Build iOS Apps 的全部 9 个官方技能整合为一条从产品文案到可调试 iOS 构建的实用工作流。

| 你的目标 | 首选技能 | 结果 |
| --- | --- | --- |
| 审计 App Store 页面，优化关键词、截图或定位 | [`$app-store-aso`](plugins/ios-application-development-skills/skills/app-store-aso/SKILL.md) | 基于证据的审计与逐字段审批的 `aso-handoff.json` |
| 创建、翻译、验证或安全填写版本 | [`$ios-appstore-release-manager`](plugins/ios-application-development-skills/skills/ios-appstore-release-manager/SKILL.md) | Flutter/Xcode 版本绑定与 schema 8 发布表单 |
| 实现或重构 SwiftUI 页面 | [`$swiftui-ui-patterns`](plugins/ios-application-development-skills/skills/swiftui-ui-patterns/SKILL.md) · [`$swiftui-view-refactor`](plugins/ios-application-development-skills/skills/swiftui-view-refactor/SKILL.md) | 稳定布局、清晰状态流与可维护 View |
| 复现崩溃、性能问题或内存泄漏 | [`$ios-debugger-agent`](plugins/ios-application-development-skills/skills/ios-debugger-agent/SKILL.md) · ETTrace · Memgraph | 基于 Simulator 证据定位问题 |

## 一分钟安装

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

安装后可以直接这样告诉 Codex：

```text
审计这个 App Store 页面，并生成完整获批的 ASO 交接文件。
从这个 Flutter 项目创建发布表单，并翻译为日语。
在 Simulator 运行 App，定位 onboawrding 页面为什么崩溃。
在不改变行为的前提下重构这个大型 SwiftUI View。
```

## 包含什么

### App Store 交付

| 技能 | 最适合的任务 | 安全边界 |
| --- | --- | --- |
| `$app-store-aso` | Apple App Store 页面审计、竞品、关键词、截图、预览和定位 | 仅支持 Apple；明确区分事实、官方规则、非官方基准与证据缺口 |
| `$ios-appstore-release-manager` | 发布表单、本地化、Flutter/Xcode 版本识别和 App Store Connect 草稿 | 逐字段审批、页面冲突确认、保存后回读，默认停在“添加以供审核”之前 |

两者使用 `aso-handoff.json` schema 1 交接。Description、Promotional Text、Keywords 和 What’s New 必须各自获批，交接才会标记为 `approved`。App Name 与 Subtitle 只作为建议，不会被自动修改。

### OpenAI Build iOS Apps 官方技能

| 领域 | 技能 |
| --- | --- |
| 系统入口 | `$ios-app-intents`：App Intents、实体、App Shortcuts、Siri 和 Spotlight |
| Simulator 工作流 | `$ios-debugger-agent`、`$ios-simulator-browser` |
| 性能与内存 | `$ios-ettrace-performance`、`$ios-memgraph-leaks` |
| SwiftUI 实现 | `$swiftui-ui-patterns`、`$swiftui-view-refactor`、`$swiftui-performance-audit`、`$swiftui-liquid-glass` |

9 个官方技能均保留原有名称、说明、agents、references、scripts 和模板，并固定跟踪 OpenAI `build-ios-apps` v0.1.2 快照。

## 发布路径：ASO 到 App Store Connect

```text
公开页面 / 产品资料
        ↓
$app-store-aso：审计、证据、四字段逐项审批
        ↓
approved aso-handoff.json
        ↓
$ios-appstore-release-manager：版本绑定、本地化、验证
        ↓
App Store Connect 草稿：保存并回读
        ↓
默认停止在“添加以供审核”之前
```

创建并完成 ASO 交接：

```bash
python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  new --source-locale en-US --output /path/to/aso-handoff.json

python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  finalize /path/to/aso-handoff.json
```

为 Flutter 或原生 Xcode 项目创建发布表单：

```bash
python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/flutter-project --source-locale zh-Hans

python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/xcode-project --project-type xcode \
  --workspace App.xcworkspace --scheme App --configuration Release
```

schema 8 依次使用成对传入的 `--version`、`--build` 参数，Flutter `pubspec.yaml`，以及原生 Xcode build settings 来识别版本。schema 1–7 既有表单仍可读取和验证，插件绝不会自动迁移或重写它们。

## 依赖与兼容性

插件会配置 XcodeBuildMCP。使用 Simulator 工作流需要 macOS、Xcode、Node.js/npm/npx 和可用的 iOS Simulator。MCP 可能在非开发任务中启动；不需要时可在 Codex 中暂时禁用整个插件。

> [!IMPORTANT]
> OpenAI 上游配置原样使用 `xcodebuildmcp@latest`，其 API 可能独立于技能文本升级。使用 Simulator 前应检查当前暴露的工具 schema；若能力缺失或参数不兼容，应停止并报告，不能猜测调用方式。详见 [兼容性说明](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md)。

## 上游同步与验证

仓库每周检查一次 OpenAI `main`。出现变化时只创建审核 PR，不会自动合并。

```bash
python3 scripts/sync_openai_ios_skills.py \
  --target plugins/ios-application-development-skills --check

python3 -m unittest discover \
  -s plugins/ios-application-development-skills/skills/ios-appstore-release-manager/tests -v

python3 scripts/validate_bundle.py
```

第三方许可证、来源、固定提交和文件哈希见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [`OPENAI_UPSTREAM.json`](plugins/ios-application-development-skills/OPENAI_UPSTREAM.json)。

## 加入 Flaq AI Affiliate Program，获得推广佣金

开发者、智能体构建者、评测者、创意团队和 AI 教育者可以[加入 Flaq AI Affiliate Program](https://flaq.ai/affiliate-program/)，创建推广链接，并从被推荐用户产生的符合条件订单中获得佣金。当前公开规则为：被推荐用户的首笔有效付费订单可获得 20% 佣金；注册后 60 天内的后续有效付费订单可获得 10% 佣金。

退款、拒付、归因、风控审核和政策规则可能影响资格与实际发放。分享推广链接时请清晰披露推广关系，并在推广前核对最新项目条款。详见 [15 语种 Affiliate Program 指南](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md)。

## 许可证

本项目采用 [MIT License](LICENSE)，第三方声明保留在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

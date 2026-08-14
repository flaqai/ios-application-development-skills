# iOS Application Development Skills

一个公开、可安装的 Codex Git Marketplace，提供单一插件 `ios-application-development-skills`。它把 App Store ASO、发布翻译与安全填表，以及 OpenAI 官方 Build iOS Apps 的完整 9 个技能整合在一起。

当前插件版本：`0.1.0`。OpenAI 官方技能初始基线：`build-ios-apps` v0.1.2；上游按周检查，有变化时只创建审核 PR，绝不自动合并。

## 安装

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

插件启用后会配置 XcodeBuildMCP：

```json
{
  "command": "npx",
  "args": ["-y", "xcodebuildmcp@latest", "mcp"]
}
```

因此需要 macOS、Xcode、Node.js/npm/npx；Simulator 开发还需要可用的 iOS Simulator。MCP 可能在非开发任务中启动，如暂时不需要，请在 Codex 中禁用整个插件。

OpenAI 上游的 `.mcp.json` 使用 `xcodebuildmcp@latest`，所以 MCP API 可能独立于技能文本发生变化。执行 Simulator 任务前必须检查当前暴露的工具 schema；若工具改名或参数不兼容，停止并报告，不猜测调用。当前已知边界见 [XCODEBUILDMCP_COMPATIBILITY.md](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md)。

## 11 个技能

| 技能 | 适用场景 | 触发示例 | 主要依赖 |
| --- | --- | --- | --- |
| `$app-store-aso` | Apple App Store 页面审计、关键词、竞品、截图与预览、ASO 交接 | “审计这个 App Store 页面并生成四字段交接” | Web/Browser；公开页面或用户材料 |
| `$ios-appstore-release-manager` | Flutter/Xcode 版本识别、发布文案、本地化、App Store Connect 安全填表 | “为 2.0.0 创建发布表单并翻译” | Python 3；可选 Browser/Computer Use |
| `$ios-app-intents` | App Intents、App Entities、App Shortcuts | “让这个操作出现在 Siri 和快捷指令中” | Xcode/Swift |
| `$ios-debugger-agent` | 构建、运行、UI 检查、日志和运行时排错 | “在 Simulator 运行并定位崩溃” | XcodeBuildMCP、Simulator |
| `$ios-ettrace-performance` | ETTrace 启动与运行时性能分析 | “比较优化前后的启动耗时” | XcodeBuildMCP、Simulator |
| `$ios-memgraph-leaks` | 泄漏、引用环、内存增长调查 | “抓取 memgraph 找 retain cycle” | XcodeBuildMCP、Simulator |
| `$ios-simulator-browser` | 在 Codex 浏览器镜像 Simulator、SwiftUI Preview 热更新 | “把 Simulator 显示在浏览器里” | XcodeBuildMCP、Simulator、Swift package preview |
| `$swiftui-liquid-glass` | iOS 26+ Liquid Glass 实现与审查 | “检查这个 Liquid Glass 界面是否正确” | Xcode/SwiftUI，iOS 26+ SDK |
| `$swiftui-performance-audit` | SwiftUI 卡顿、昂贵更新、滚动性能代码审计 | “审计列表滚动为什么掉帧” | SwiftUI 源码；可选性能工具 |
| `$swiftui-ui-patterns` | SwiftUI 导航、状态、布局、组件实现 | “按稳定模式实现这个 SwiftUI 页面” | Xcode/SwiftUI |
| `$swiftui-view-refactor` | 拆分大型 View、收紧数据流与 Observation 所有权 | “重构这个 800 行 SwiftUI View” | Xcode/SwiftUI |

## 如何选择

| 目标 | 首选技能 | 需要时追加 |
| --- | --- | --- |
| 优化 App Store 页面 | `$app-store-aso` | 获批后交给 `$ios-appstore-release-manager` |
| 创建、翻译或填写版本 | `$ios-appstore-release-manager` | Browser/Computer Use 仅用于已登录页面 |
| Simulator 中复现错误 | `$ios-debugger-agent` | 卡顿用 `$ios-ettrace-performance`，泄漏用 `$ios-memgraph-leaks` |
| 构建 SwiftUI 页面 | `$swiftui-ui-patterns` | 大文件用 `$swiftui-view-refactor`，性能问题用 `$swiftui-performance-audit` |
| iOS 26 视觉升级 | `$swiftui-liquid-glass` | 先用 `$swiftui-ui-patterns` 确认组件结构 |
| 系统级快捷入口 | `$ios-app-intents` | 用 `$ios-debugger-agent` 做 Simulator 验证 |
| 浏览器内展示 Simulator | `$ios-simulator-browser` | 运行时排错用 `$ios-debugger-agent` |

## App Store ASO → 发布交接

`$app-store-aso` 只支持 Apple App Store。它会把事实、Apple 官方规范、行业非官方基准和推测明确分开；缺少页面数据时必须列出证据缺口。

交接接口为 `aso-handoff.json` schema 1。Description、Promotional Text、Keywords、What's New 必须逐项获批，之后才能把总状态设为 `approved`。App Name 与 Subtitle 只作为 App Information 建议，不会自动写入发布表单。

```bash
python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  new --source-locale en-US --output /path/to/aso-handoff.json

python3 plugins/ios-application-development-skills/skills/app-store-aso/scripts/aso_handoff.py \
  finalize /path/to/aso-handoff.json

python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  import-aso /path/to/aso-handoff.json /path/to/release-form.md
```

## 发布表单

新表单使用 schema 8，并按以下顺序读取版本：

1. 成对提供的 `--version` 与 `--build`；
2. Flutter `pubspec.yaml`；
3. 原生 Xcode 的 `xcodebuild -showBuildSettings -json`。

原生工程出现多个 workspace、project 或 scheme 时会明确失败并要求指定，不会猜目标。schema 1–7 继续读取和验证，绝不自动迁移或重写已填写表单。关键词遵守 Apple 的完整字段 `100 UTF-8 bytes` 限制。

```bash
python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/flutter-project --source-locale zh-Hans

python3 plugins/ios-application-development-skills/skills/ios-appstore-release-manager/scripts/release_form.py \
  new --repo /path/to/xcode-project --project-type xcode \
  --workspace App.xcworkspace --scheme App --configuration Release
```

发布技能保留逐字段审批、页面现值冲突确认、保存后回读和默认停在“添加以供审核”之前的边界。它不会自动提交审核。

## 上游同步与验证

```bash
python3 scripts/sync_openai_ios_skills.py \
  --target plugins/ios-application-development-skills --check

python3 -m unittest discover \
  -s plugins/ios-application-development-skills/skills/ios-appstore-release-manager/tests -v

python3 scripts/validate_bundle.py
```

完整第三方来源、许可证、固定提交与哈希记录见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 `OPENAI_UPSTREAM.json`。

---

## English Summary

This repository is a public Codex Git Marketplace named `flaqai-ios`. Its single plugin, `ios-application-development-skills` v0.1.0, bundles two Flaq AI skills—Apple-only App Store ASO and safe App Store release localization—with all nine OpenAI Build iOS Apps v0.1.2 skills and XcodeBuildMCP configuration.

Install it with:

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

Use `$app-store-aso` for evidence-backed Apple listing audits and an approval-gated `aso-handoff.json`. Use `$ios-appstore-release-manager` for schema 8 Flutter/Xcode release forms, localization, validation, build binding, and safe App Store Connect drafting. Use the nine upstream-named skills for App Intents, Simulator debugging/browser mirroring, ETTrace, memgraphs, Liquid Glass, and SwiftUI implementation/refactoring/performance review.

Because the byte-preserved upstream MCP configuration uses `xcodebuildmcp@latest`, inspect the currently exposed MCP tool schemas before Simulator work and stop when a required capability is missing or incompatible. See the repository's XcodeBuildMCP compatibility note for the current point-in-time finding.

The weekly sync workflow opens a review PR when OpenAI `main` changes; it never auto-merges. This repository is MIT licensed, with third-party notices retained.

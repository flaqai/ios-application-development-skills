<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">Bộ kỹ năng Codex cho phát hành App Store, ASO, SwiftUI và gỡ lỗi bằng Simulator.</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · <strong>Tiếng Việt</strong></p>

## Một plugin cho toàn bộ quy trình iOS

`ios-application-development-skills` là plugin Codex Git Marketplace công khai, kết hợp quy trình phát hành App Store an toàn, ASO chỉ dành cho Apple App Store và toàn bộ chín kỹ năng OpenAI Build iOS Apps.

## Cài đặt nhanh

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## Bạn có thể làm gì

| Nhu cầu | Kỹ năng | Kết quả |
| --- | --- | --- |
| Kiểm tra trang App Store, từ khóa và ảnh chụp màn hình | `$app-store-aso` | `aso-handoff.json` dựa trên bằng chứng và được duyệt theo từng trường |
| Tạo, dịch và xác thực bản phát hành | `$ios-appstore-release-manager` | Liên kết phiên bản Flutter/Xcode và biểu mẫu schema 8 |
| Xây dựng hoặc tái cấu trúc SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | Bố cục ổn định và View dễ bảo trì |
| Điều tra crash, hiệu năng hoặc bộ nhớ | `$ios-debugger-agent`, ETTrace, Memgraph | Chẩn đoán dựa trên bằng chứng Simulator |

## 11 kỹ năng

Ngoài hai kỹ năng App Store, plugin gồm `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` và `$swiftui-view-refactor`. Xem [README tiếng Anh](README.md) để biết đầy đủ chi tiết.

## Ranh giới phát hành an toàn

Description, Promotional Text, Keywords và What’s New phải được phê duyệt riêng trước khi `aso-handoff.json` trở thành `approved`. Kỹ năng phát hành giữ nguyên phê duyệt theo trường, xác nhận xung đột và đọc lại sau khi lưu; nó dừng trước “Add for Review”.

## Tương thích và giấy phép

Quy trình Simulator cần macOS, Xcode, Node.js/npm/npx và iOS Simulator khả dụng. Hãy đọc [ghi chú tương thích XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md). Kho lưu trữ này dùng [giấy phép MIT](LICENSE).

## Kiếm hoa hồng với chương trình liên kết Flaq AI

Nhà phát triển, người xây dựng agent, người đánh giá, đội ngũ sáng tạo và nhà giáo dục AI có thể [tham gia chương trình liên kết Flaq AI](https://flaq.ai/affiliate-program/), tạo liên kết giới thiệu và kiếm hoa hồng từ các đơn hàng đủ điều kiện của người dùng được giới thiệu. Cấu trúc công khai hiện tại nêu 20% cho đơn hàng trả phí hợp lệ đầu tiên và 10% cho các đơn hàng trả phí hợp lệ tiếp theo được thực hiện trong vòng 60 ngày sau khi người dùng được giới thiệu đăng ký.

Hoàn tiền, bồi hoàn thẻ, ghi nhận nguồn giới thiệu, xét duyệt rủi ro và quy định chính sách có thể ảnh hưởng đến điều kiện và thanh toán. Hãy công khai rõ ràng mối quan hệ liên kết khi chia sẻ liên kết giới thiệu và kiểm tra điều khoản hiện hành trước khi quảng bá. Đọc [hướng dẫn chương trình liên kết bằng 15 ngôn ngữ](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md).

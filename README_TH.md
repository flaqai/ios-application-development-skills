<p align="center"><img src="assets/ios-development-skills-hero.png" alt="iOS Application Development Skills" width="100%"></p>

<h1 align="center">iOS Application Development Skills</h1>

<p align="center">ชุดทักษะ Codex สำหรับการปล่อยแอปบน App Store, ASO, SwiftUI และการดีบักด้วย Simulator</p>

<p align="center">[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH_TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md)<br>[Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)<br>[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · <strong>ไทย</strong> · [Tiếng Việt](README_VI.md)</p>

## ปลั๊กอินเดียวสำหรับเส้นทาง iOS ทั้งหมด

`ios-application-development-skills` คือปลั๊กอินสาธารณะของ Codex Git Marketplace ที่รวมการปล่อย App Store อย่างปลอดภัย, ASO สำหรับ Apple App Store เท่านั้น และทักษะ OpenAI Build iOS Apps ทั้งเก้ารายการ

## ติดตั้งอย่างรวดเร็ว

```bash
codex plugin marketplace add flaqai/ios-application-development-skills --ref main
codex plugin add ios-application-development-skills@flaqai-ios
```

## สิ่งที่คุณทำได้

| ความต้องการ | ทักษะ | ผลลัพธ์ |
| --- | --- | --- |
| ตรวจสอบหน้า App Store, คีย์เวิร์ด และภาพหน้าจอ | `$app-store-aso` | `aso-handoff.json` ที่มีหลักฐานและอนุมัติรายฟิลด์ |
| สร้าง แปล และตรวจสอบรีลีส | `$ios-appstore-release-manager` | การผูกเวอร์ชัน Flutter/Xcode และฟอร์ม schema 8 |
| สร้างหรือรีแฟกเตอร์ SwiftUI | `$swiftui-ui-patterns`, `$swiftui-view-refactor` | เลย์เอาต์ที่เสถียรและ View ที่ดูแลต่อได้ |
| ตรวจสอบแครช ประสิทธิภาพ หรือหน่วยความจำ | `$ios-debugger-agent`, ETTrace, Memgraph | การวินิจฉัยจากหลักฐานใน Simulator |

## 11 ทักษะ

นอกจากสองทักษะสำหรับ App Store แล้ว ปลั๊กอินยังมี `$ios-app-intents`, `$ios-debugger-agent`, `$ios-ettrace-performance`, `$ios-memgraph-leaks`, `$ios-simulator-browser`, `$swiftui-liquid-glass`, `$swiftui-performance-audit`, `$swiftui-ui-patterns` และ `$swiftui-view-refactor` ดูรายละเอียดทั้งหมดได้ที่ [README ภาษาอังกฤษ](README.md)

## ขอบเขตความปลอดภัยของรีลีส

Description, Promotional Text, Keywords และ What’s New ต้องได้รับอนุมัติทีละฟิลด์ก่อนที่ `aso-handoff.json` จะเป็น `approved` ทักษะรีลีสยังคงการอนุมัติรายฟิลด์ การยืนยันความขัดแย้ง และการอ่านกลับหลังบันทึก โดยหยุดก่อน “Add for Review”

## ความเข้ากันได้และสัญญาอนุญาต

เวิร์กโฟลว์ Simulator ต้องใช้ macOS, Xcode, Node.js/npm/npx และ iOS Simulator ที่พร้อมใช้งาน โปรดอ่าน [หมายเหตุความเข้ากันได้ของ XcodeBuildMCP](plugins/ios-application-development-skills/XCODEBUILDMCP_COMPATIBILITY.md) ที่เก็บนี้ใช้ [สัญญาอนุญาต MIT](LICENSE)

## รับค่าคอมมิชชันกับโปรแกรมพันธมิตร Flaq AI

นักพัฒนา ผู้สร้างเอเจนต์ ผู้รีวิว ทีมสร้างสรรค์ และผู้สอน AI สามารถ[เข้าร่วมโปรแกรมพันธมิตร Flaq AI](https://flaq.ai/affiliate-program/) สร้างลิงก์แนะนำ และรับค่าคอมมิชชันจากคำสั่งซื้อที่เข้าเกณฑ์ของผู้ใช้ที่ได้รับการแนะนำ โครงสร้างสาธารณะปัจจุบันระบุ 20% สำหรับคำสั่งซื้อแบบชำระเงินที่ถูกต้องครั้งแรก และ 10% สำหรับคำสั่งซื้อแบบชำระเงินที่ถูกต้องครั้งถัดไปภายใน 60 วันหลังผู้ใช้ที่ได้รับการแนะนำลงทะเบียน

การคืนเงิน การปฏิเสธการชำระเงิน การระบุแหล่งที่มา การตรวจสอบความเสี่ยง และกฎนโยบายอาจส่งผลต่อสิทธิ์และการจ่ายเงิน โปรดเปิดเผยความสัมพันธ์แบบพันธมิตรอย่างชัดเจนเมื่อแชร์ลิงก์แนะนำ และตรวจสอบข้อกำหนดล่าสุดก่อนโปรโมต อ่าน[คู่มือโปรแกรมพันธมิตร 15 ภาษา](https://github.com/flaqai/awesome_seedance_2_5/blob/main/docs/flaq-affiliate-program.md)

# Training_Package_Index.md

# Aximmetry Tracked Green Screen Training Package
## パッケージ構成一覧

---

## 1. このパッケージの目的
このパッケージは、Aximmetry を用いた Tracked Green Screen workflow の初心者向け講習を支える資料一式です。

目的は次の3つです。

1. 講習中に迷わず進行できること
2. 講習後に復習しやすいこと
3. 次回以降の production に向けて積み上げられること

---

## 2. 基本方針
- Slides は最小構成にする
- 講習本編の主教材は Aximmetry 公式 Learn と GUI にする
- Cheat Sheet は復習用資料として使う
- Day2 は normal path を成立させる日
- Day3 は replay / recover / extend を扱う日

---

## 3. 講習の進め方
講習中は、次の流れを基本とする。

1. Slides で Goal と Agenda を提示する
2. Aximmetry 公式 Learn ページで考え方を確認する
3. Aximmetry / Unreal GUI で実演する
4. 必要に応じて hands-on を行う
5. 講習後は Cheat Sheet で復習する

---

## 4. 受講者配布物

### 4-1. Day2_Slides_Minimum.md
役割：
- Day2 の開始時に Title / Goal / Agenda を提示する

内容：
- Title
- Goal
- Agenda

### 4-2. Day3_Slides_Minimum.md
役割：
- Day3 の開始時に Title / Goal / Agenda を提示する

内容：
- Title
- Goal
- Agenda

### 4-3. Day1_Review_CheatSheet.md
役割：
- Day1 の内容を復習する
- Day2 / Day3 の前提を確認する

主題：
- システム構成
- 固定IP
- Ping
- Remote Desktop
- 専用 Viewer での特徴点確認
- Bliss setting app での露出調整
- Bliss app 起動
- Aximmetry 入力確認
- CV Protocol
- SDI
- Tracking Calibration
- Nodal Offset
- ズレのない追従確認

### 4-4. Day2_Review_CheatSheet.md
役割：
- Day2 の normal path を復習する

主題：
- Unreal 背景
- Aximmetry の役割
- I/O setup
- Delay / Sync
- Keying
- Live Rec

### 4-5. Day3_Review_CheatSheet.md
役割：
- Day3 の replay / offline / troubleshooting / BP を復習する

主題：
- Replay / Playback
- Offline Workflow
- Troubleshooting
- BP入門：バーチャルスクリーンの基本

### 4-6. Keying_CheatSheet.md
役割：
- Keying を後から復習する
- 現場運用の積み上げに使う補助資料

主題：
- 物理条件
- Aximmetry 内の基本調整
- Despill
- Edge Color Corr Width
- Threshold
- Clean Plate
- Vignette Correction
- FAQ / Troubleshooting

---

## 5. 講師用資料

### 5-1. Instructor_RunSheet_Day2.md
役割：
- Day2 当日の進行管理
- 開く Learn ページと GUI 実演順を管理する

主題：
- 時間配分
- 開く Learn ページ
- GUI 実演箇所
- hands-on の回し方
- cut 候補

### 5-2. Instructor_RunSheet_Day3.md
役割：
- Day3 当日の進行管理
- replay / troubleshooting / BP の進行順を管理する

主題：
- 時間配分
- 開く Learn ページ
- GUI 実演箇所
- hands-on の回し方
- cut 候補

---

## 6. Day2 の定義
### テーマ
リアルタイム合成とライブ収録  
(Realtime Rendering and Live Rec)

### ゴール
- Tracked Green Screen の通常の進め方を理解する
- 背景合成と当日収録の流れを理解する
- 入力設定、キー合成、収録の基本を確認する

### Agenda
1. Unreal 背景セットの準備
2. 入力設定 (I/O Setup)
3. キー合成 (Keying)
4. ライブ収録 (Live Rec)
5. ハンズオン (Hands-on)

### 本編で扱うもの
- Unreal setup
- Flow Editor の最低限
- I/O setup
- Keying setup
- Live Rec setup

### 本編で扱わないもの
- AR
- deep Blueprint
- Virtual Screen を本流として扱うこと
- offline recording の深掘り
- advanced troubleshooting

---

## 7. Day3 の定義
### テーマ
記録データを活かし、BPで広げる  
(Replay / Offline Workflow / BP Basics / Troubleshooting)

### ゴール
- 記録した素材を使った再生確認の流れを理解する
- 後工程用収録の考え方を理解する
- BPでバーチャルスクリーンを扱う基本を理解する
- トラブル時の戻り方の基本を理解する

### Agenda
1. 再生確認 (Replay / Playback)
2. 後工程の流れ (Offline Workflow)
3. BP入門：バーチャルスクリーンの基本
4. トラブル対応 (Troubleshooting)
5. ハンズオン (Hands-on)

### 本編で扱うもの
- Replay / Playback
- Offline Workflow
- Troubleshooting
- BP入門：バーチャルスクリーンの基本

### BP の必須内容
1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

---

## 8. 進行の主役
### 主役
- Aximmetry 公式 Learn
- Aximmetry GUI
- Unreal / AX Scene Editor GUI

### 補助
- 最小 Slides
- Review Cheat Sheets
- Keying Cheat Sheet

---

## 9. Keying 資料の扱い
- Keying は Day2 本編の重要項目として扱う
- 講習本編では Aximmetry 公式 Learn と GUI を中心に進める
- Keying Cheat Sheet は配布資料として活用する
- 講習本編では要点を扱い、詳細な数値や補足は Cheat Sheet に逃がす

---

## 10. 最後の方針
このパッケージの目的は、資料を増やすことではなく、
**講習と復習の再現性を上げること** です。

- Slides は最小限
- Learn と GUI を主役
- Cheat Sheet は復習と積み上げに使う

この前提で、講習の理解と再利用性を両立させる。
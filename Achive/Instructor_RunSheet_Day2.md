# Instructor_RunSheet_Day2.md

# Instructor Run Sheet - Day 2
## リアルタイム合成とライブ収録
(Realtime Rendering and Live Rec)

※この資料は講師用です。受講者配布を前提としません。  
※本編の主教材は Aximmetry 公式 Learn と GUI です。  
※Slides は最小構成（Title / Goal / Agenda）のみ使用します。  
※Day 2 は **通常の進め方（normal path）を成立させる日** です。  
※トラブル対応や fallback の深掘りは Day 3 に回します。  
※Day 2 の前に、Day 1 の最後に行った **Tracking Calibration の再確認** を短く入れます。

---

## 1. Day 2 の到達目標
- Tracked Green Screen の通常の進め方を理解してもらう
- Unreal を背景側、Aximmetry を統合・合成・出力側として理解してもらう
- INPUTS における I/O / Delay / Sync の基本順を理解してもらう
- Keying の確認順を理解してもらう
- ライブ収録の位置づけを理解してもらう
- 最後に、全体の流れを通して確認してもらう

---

## 2. Day 2 の基本方針
- 最初に Day1 の土台を短く再確認する
- Slides では Goal / Agenda のみ見せる
- その後は公式 Learn と GUI を主に使う
- 通しデモは講師側の進行として入れるが、Slides の Agenda には書かない
- 1PC 共有前提なので、shared-rig guided training として進める
- 受講者には「細部の暗記」ではなく「何をどの順で見るか」を残す
- Keying は重要項目だが、詳細数値の深掘りは Keying Cheat Sheet に逃がす

---

## 3. 使用する Slides
### Day2_Slides_Minimum.md
#### Slide 1
Day 2  
リアルタイム合成とライブ収録  
(Realtime Rendering and Live Rec)

#### Slide 2
Goal
- Tracked Green Screen の通常の進め方を理解する
- 背景合成と当日収録の流れを理解する
- 入力設定、キー合成、収録の基本を確認する

#### Slide 3
Agenda
1. Unreal 背景セットの準備
2. 入力設定 (I/O Setup)
3. キー合成 (Keying)
4. ライブ収録 (Live Rec)
5. ハンズオン (Hands-on)

---

## 4. 事前に開いておくもの
### Aximmetry Learn
- Introduction to Green Screen Production
- Tracked Camera Compounds
- Tracked Camera Inputs
- Prerequisites of a Good Keying
- Keying
- Keying Setup (Tracked Camera)
- Preparing the Unreal Project
- Basics of the Flow Editor
- Unreal Scene Setup (Green Screen)

### ソフト / 機材
- Aximmetry Composer
- Unreal / AX Scene Editor
- Tracked Green Screen 用プロジェクト
- 外部 recorder（例: Video Assist）
- SDI 出力確認モニタ（あれば）

### 配布資料
- Day1_Review_CheatSheet
- Day2_Review_CheatSheet
- Keying_CheatSheet

---

## 5. 時間割
### 12:00–12:30
Day1 recap practical  
Tracking Calibration 再確認

### 12:30–12:40
オープニング  
Goal / Agenda 提示  
Day1 → Day2 の位置づけ共有

### 12:40–13:00
通しデモ  
最初に完成形を見せる

### 13:00–13:35
Unreal 背景セットの準備  
+ Flow Editor の最低限

### 13:35–14:20
入力設定 (I/O Setup)

### 14:20–14:30
休憩

### 14:30–15:00
キー合成：考え方の説明

### 15:00–15:30
キー合成：GUI 実演

### 15:30–15:50
ライブ収録 (Live Rec)

### 15:50–16:00
切り替え / 小休憩

### 16:00–17:20
ハンズオン (shared-rig guided)

### 17:20–18:00
まとめ / 質疑 / Day3 予告

---

## 6. セクション別進行

# 6-0. Day1 recap practical：Tracking Calibration 再確認
## 目的
- Day1 の土台を Day2 本編前に再確認する
- ズレのない追従状態から Day2 を始める
- 背景合成の前提条件を体験として思い出させる

## やること
- Day1 の最後に行った Tracking Calibration を短く再確認する
- 必要なら Nodal Offset との関係も一言触れる
- 「昨日の最後にやったことが今日の前提」であることを明確にする

## 受講者に残したいこと
- 背景の違和感は Day2 の問題だけではない
- Day1 の calibration が成立して初めて Day2 が安定する

## 講師メモ
- ここは深掘りしない
- Day1 を丸ごとやり直す時間ではなく、成功状態を思い出す時間
- 「ズレのない追従状態」ができたら Day2 本編へ進む

---

# 6-1. オープニング
## 目的
- Day 2 の主役を明確にする
- Day 1 との接続を作る
- 今日の到達点を先に見せる

## 言うこと
- Day 1 は「信号を正しく受ける日」
- Day 2 は「背景合成とライブ収録を成立させる日」
- 今日は Tracked Camera workflow の通常の進め方に集中する
- AR や deep Blueprint は本流ではない

## 見せるもの
- Slide 1
- Slide 2
- Slide 3

---

# 6-2. 通しデモ
## 目的
- 最初に完成形を見せる
- 以降の内容を「分解」として理解させる

## やること
- Unreal 背景を見せる
- Aximmetry の入力状態を見せる
- 背景合成を見せる
- ライブ出力を見せる
- recorder 側まで流れを見せる

## 注意
- ここでは細かく止まりすぎない
- 「今日はこれを順に分解します」で止める

---

# 6-3. Unreal 背景セットの準備
## 目的
- Unreal の役割を背景側に限定して理解してもらう
- Aximmetry 前提の scene 準備を理解してもらう
- Flow Editor を deep にしない

## 開く Learn
- Preparing the Unreal Project
- Basics of the Flow Editor
- Unreal Scene Setup (Green Screen)

## 見せること
- Unreal は背景を作る場所
- Aximmetry Camera 前提
- project / scene の準備
- cook → Aximmetry 読み込み
- Flow Editor は routing / playback の場所

## GUI で見せる箇所
- Unreal project
- scene
- Aximmetry Camera
- Flow Editor の位置だけ

## 受講者に残したいこと
- Unreal = 背景側
- Aximmetry = 統合・合成・出力側
- Flow Editor は deep に学ばなくてよい

## 受講者への問い
- 今回 Unreal は何の役割ですか？
- Aximmetry 側でやることは何ですか？

---

# 6-4. 入力設定 (I/O Setup)
## 目的
- 通常の進め方の順番を残す
- Delay / Sync を usual path として理解させる
- fallback に行きすぎない

## 開く Learn
- Tracked Camera Inputs
- Tracked Camera Compounds
- 必要に応じて Studio Control Panel / Scene Control Panel

## 基本順序
1. Camera Device
2. Tracking Device
3. Lens / Calibration 前提
4. Tracking Delay
5. Zoom Delay
6. Timecode Sync / Zoom Timecode Sync
7. Detect Tracking Delay / Detect Zoom Delay

## 強調すること
- Detect Tracking Delay / Detect Zoom Delay は fallback ではない
- まず「入力が来ているか」
- 次に「遅延と同期を合わせる」
- Day 2 は通常の進め方の確立が主役

## GUI で見せる箇所
- INPUTS
- Camera Device
- Tracking Device
- Delay / Sync 周辺

## 受講者への問い
- 次に何を確認しますか？
- いま合わせたいのは video / tracking / zoom のどれですか？
- まず見るべきは入力ですか、遅延ですか？

## 講師メモ
- fallback 詳細に脱線しない
- 症状ベース troubleshooting は Day 3 に回す

---

# 6-5. キー合成（考え方）
## 目的
- Keying はソフトだけで決まらないことを残す
- まず確認順を与える

## 開く Learn
- Prerequisites of a Good Keying
- Keying
- Keying Setup (Tracked Camera)

## 最初に出す agenda
1. まず物理条件
2. 次に Aximmetry の基本調整
3. 色かぶりと輪郭色の考え方
4. 条件が悪い時の補助策
5. 最後は Final Output で判断する

## 強調すること
- 背景条件
- lighting
- 被写体距離
- 衣装 / 反射物
- software だけで救おうとしない

## 講師メモ
- 詳細数値は Keying_CheatSheet に逃がす
- 本編では「何をどの順で見るか」を重視する

---

# 6-6. キー合成（GUI 実演）
## 目的
- 実際に何を見て調整するかを体験させる
- Final Output に戻る流れを残す

## GUI で見せる箇所
- Background Color
- Low Cut / High Cut
- 必要なら Despill
- 必要なら Edge Color Corr Width
- Monitor Mode
- Final Output

## 受講者への問い
- いまの問題は背景条件ですか、ソフト設定ですか？
- まずどこから戻るべきですか？
- Final Output で自然に見えていますか？

## 講師メモ
- Despill は触りすぎない
- Edge Color Corr Width は「次の一手」
- Threshold / Clean Plate / Vignette は存在だけ示すか、配布資料へ逃がす

---

# 6-7. ライブ収録 (Live Rec)
## 目的
- Day2 の rec の位置づけを明確にする
- Day3 の offline recording と混同させない

## 開く Learn
- Tracked Camera Inputs（Timecode Master 周辺）

## 強調すること
- Day 2 の rec は「当日に安全に残す」
- Aximmetry の合成映像を外部 recorder に送る
- Timecode Master を基準に考える
- Input Recording や Tracking Only は Day 3 で扱う

## GUI / 実機で見せる箇所
- output
- recorder 側確認
- timecode の関係

## 受講者への問い
- Day 2 の rec の目的は何ですか？
- Day 3 の recording と何が違いますか？

---

# 6-8. ハンズオン
## 目的
- Day 2 の flow を口頭で説明できる状態にする
- shared-rig で確認順を回す

## 形式
- 1PC 共有
- shared-rig guided training

## 役割
- Operator
- Navigator
- Checker
- Observer

## 回す順
1. Unreal 背景確認
2. INPUTS 確認
3. Delay / Sync 確認
4. Keying 確認
5. Live output 確認
6. recorder 側確認

## 受講者に残したいこと
- 通常の進め方が言える
- Keying の確認順が言える
- Day2 の rec の目的が言える

---

# 6-9. まとめ
## 最後に確認すること
- Unreal は背景側、Aximmetry は合成・出力側と説明できるか
- I/O の通常の進め方が分かるか
- Keying の確認順が分かるか
- Day2 の rec の目的が分かるか

## Day3 予告
- 再生確認 (Replay / Playback)
- 後工程の流れ (Offline Workflow)
- BP入門：バーチャルスクリーンの基本
- トラブル対応 (Troubleshooting)

---

## 7. 時間が押した時の cut 候補
### 最後まで残す
- Tracking Calibration 再確認
- I/O setup
- Keying の確認順
- Live Rec の位置づけ
- Hands-on の通し確認

### 短縮候補
- Unreal Scene Setup の細部
- Flow Editor の説明
- Keying の advanced 補助項目
- recorder 側の細部確認

---

## 8. 講師用メモ
- Day2 は「通常の進め方」を守る
- fallback に入りすぎない
- Keying は重要だが、講義本編で数値暗記にしない
- Slides は最小限、Learn と GUI を主役にする
- 受講者には「何をどの順で見るか」を残す
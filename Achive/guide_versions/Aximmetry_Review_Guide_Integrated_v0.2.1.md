# Aximmetry Tracked Green Screen Review Guide
## 受講者向け統合復習ガイド v0.2

> この資料は、Day 1–3 の内容を **日程単位ではなく概念単位** で復習し、Aximmetry公式Learnやデバイス資料を開きながら、独学でハンズオンを再走しやすくするためのガイドです。  
> 操作画面のすべてをここに書くのではなく、**何を理解し、どこを確認し、どの公式ページを次に開くべきか** を整理することを主目的にしています。

---

## この資料の使い方

### 1. まず全体像をつかむ
最初に **System Overview** を読み、映像・レンズ情報・トラッキング情報の3系統がどこから来て、どこで統合されるのかを理解します。

### 2. 次に「背景側」の前提を整える
AximmetryのGUIを触る前に、**AX Scene / Unreal Setup for Aximmetry** を確認します。  
ここでの目的は、Aximmetryに渡す前の **受け皿** を整えることです。

### 3. その後に「同期」の意味を理解する
**System Synchronization and Calibration** を読み、Tracking Calibration と Nodal Offset が何のために必要なのかを理解します。  
ここを飛ばすと、後段のズレや違和感が「何となく合わない」ままになります。

### 4. 本流の tracked camera workflow を通す
**Tracked Camera Standard Flow** から、Aximmetry側の INPUTS / delay / sync / keying / output を順番に復習します。

### 5. つまずいたら症状から引く
途中で詰まったら、**Troubleshooting by Symptom** に戻ります。

---

## Scope / この資料のスコープ

この資料の本流は、**Tracked Green Screen Production in Aximmetry** です。

- 対象: tracked camera を使った green screen workflow
- 主軸: AX Scene / Unreal 準備、Aximmetry入力、同期、keying、live output、recording / playback、troubleshooting
- 本流から外すもの: AR の詳細、LED Wall workflow の詳細、no-tracked Virtual Camera workflow の詳細

> これらを否定する意図ではなく、まず **1本の勝ち筋を理解し、再現できるようにする** ためにスコープを絞っています。

---

## Terminology / 用語ポリシー

- **AX Scene Editor**  
  Aximmetryが提供する、Unreal Editorをベースにしたカスタム版。古い資料では **Unreal Editor for Aximmetry** と表記される場合があります。  
  本資料では **AX Scene Editor** に統一します。

- **Tracked Camera Standard Flow**  
  本資料で扱う tracked green screen production の本流。旧来的な講師用メモの **Normal Path** に近い概念ですが、受講者向けに意味が伝わりやすい名称へ置き換えています。

- **Live Output / 当日収録**  
  当日に安全に残すための出力・収録。

- **Input Recording / Playback / Offline Review**  
  後で再確認したり、再生したり、後工程へつないだりするための記録と確認の流れ。

---

# 1. System Overview

## この章の目的

最初に、システム全体の **役割分担** と **情報の流れ** を頭の中で接続することです。

## まず頭に入れたいこと

この講習で重要なのは、1つのソフトを覚えることではありません。  
**複数の信号が、別経路で入り、Aximmetryで統合される** ことを理解することです。

### 3つの流れ

1. **映像信号**  
   例: Canon C400 からの SDI 映像

2. **レンズ情報**  
   例: Canon C400 の CV Protocol などによる lens / zoom 系データ

3. **トラッキング情報**  
   例: REtracker Bliss から来る position / rotation 系データ

Aximmetry は、これらを **統合して、合成し、出力する場所** です。  
AX Scene Editor / Unreal は、主に **背景側を作る場所** です。

## たとえ話 / Mental Model

- **AX Scene / Unreal = 舞台美術を作る場所**
- **Aximmetry = 本番の舞台監督 / スイッチャー / 合成卓**
- **Camera / Lens / Tracker = 現実世界の演者の情報源**

つまり、Unreal だけでも、Aximmetry だけでも成立しません。  
**背景の準備** と **現実入力の統合** の両方が必要です。

## チェックポイント

- [ ] Canon C400 / REtracker Bliss / Aximmetry / AX Scene Editor の役割を言葉で説明できる
- [ ] 映像・レンズ情報・トラッキング情報の3系統を説明できる
- [ ] なぜそれらが別経路で来るのかを理解している
- [ ] Aximmetry が「背景を作る場所」ではなく「統合・合成・出力の場所」だと説明できる

## よくある混線

- Aximmetry と Unreal の役割が混ざる
- 映像とレンズ情報が同じ経路で来ると思ってしまう
- tracking が来ていれば全部OKだと思ってしまう

## ここで開く公式ページ

- Aximmetry Learn: [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)

---

# 2. AX Scene / Unreal Setup for Aximmetry

## この章の目的

AximmetryのGUIへ入る前に、**背景側の受け皿** を整えることです。

## まず頭に入れたいこと

Aximmetry側で映像やtrackingを受けても、AX Scene / Unreal側の前提が崩れていると、後段で次のような問題に見えます。

- 背景スケールが不自然
- 床合わせがしにくい
- billboard や scene positioning が理解しにくい
- 何がAximmetry側の問題で、何がUnreal側の問題か分からない

> つまり、Aximmetryに入る前に **背景側の最低限の成立条件** を押さえる必要があります。

## この章で理解したいこと

- AX Scene Editor は、Aximmetry向けの Unreal 側編集環境である
- Aximmetry Camera 前提の scene 準備が必要である
- map / project settings / project conversion / cooking など、Aximmetry連携前提の準備がある
- この章は optional recipe ではなく、本流の前提条件である

## 最低限の確認観点

### A. Project / Version
- Aximmetry と AX Scene Editor の対応 version を意識する
- 既存 Unreal project を開く場合は convert の扱いに注意する
- version update は irreversible な場合があるため、copy / backup 前提で扱う

### B. Project Settings
- Startup Map / Game Default Map の確認
- Aximmetry向けに必要な project 設定を確認する
- 「普通のUnreal project」ではなく「Aximmetryに渡す project」である意識を持つ

### C. Aximmetry Camera 前提
- Aximmetry は Aximmetry Camera blueprint を通じて Unreal scene にアクセスする
- 単に Cine Camera があれば十分、とは考えない
- tracked workflow の前提に合った camera setup であることを確認する

### D. Scene 側の最低限
- 床の見え方
- scene scale
- 被写体が立つ想定位置
- billboard や compositing 前提で破綻しにくい構成

## たとえ話 / Mental Model

この章は、**背景セットを組む章** です。  
カメラ信号やtrackingがどれだけ正しくても、背景側の寸法感や入口が崩れていると、後で全部が不安定に見えます。

## チェックポイント

- [ ] AX Scene Editor が何か説明できる
- [ ] Aximmetry向け project は vanilla Unreal project と同じではないと理解している
- [ ] Aximmetry Camera 前提の scene 準備が必要だと説明できる
- [ ] scene scale / floor / 被写体位置の前提を見直せる
- [ ] recipe ではなく本流の前提条件だと理解している

## よくある混線

- Unreal の絵作りができていれば、そのままAximmetryで使えると思ってしまう
- tracked workflow なのに camera の前提が曖昧なまま進める
- Aximmetry GUI 側で頑張れば scene 側の問題も吸収できると思ってしまう

## ここで開く公式ページ

- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- Aximmetry Learn: [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

---

# 3. System Synchronization and Calibration

## この章の目的

Tracking Calibration と Nodal Offset を、単なる数値調整ではなく、**現実と仮想を同期させるための工程** として理解することです。

## まず頭に入れたいこと

この講習では、Calibration を早い段階で扱いました。  
理由は、profile がないと進みにくいからだけではありません。  
**全系統を同期するという概念** を、早めに理解してもらうためです。

## この章で理解したいこと

### Tracking Calibration
tracking 空間と virtual 側の基準を合わせる工程です。

### Nodal Offset
tracking point と実際のレンズ中心のズレを補正する工程です。

この2つは、後段の keying や playback の話とは別物に見えて、実はかなり深く関係しています。

- 背景位置が不自然
- pan / tilt / move で違和感が出る
- floor が滑るように見える
- 「何となく合わない」

こうした問題の原因が、ここにあることがあります。

## たとえ話 / Mental Model

- **Calibration = 現実と仮想の定規を合わせる**
- **Nodal Offset = センサーの位置とレンズの中心を一致させる**

tracking point は「カメラ本体のどこか」についていることが多く、レンズ中心そのものではありません。  
だから補正が必要です。

## Day 2 / Day 3 とのつながり

- Day 2 相当の live composite の自然さに直結する
- Day 3 相当の replay / troubleshooting でも、原因がここに戻ることがある
- zoom / sync / floor glide の違和感を、delay だけの問題と決めつけない

## チェックポイント

- [ ] Tracking Calibration の役割を説明できる
- [ ] Nodal Offset の役割を説明できる
- [ ] なぜこの理解を早い段階で持つのか説明できる
- [ ] 背景ズレ・floor glide・違和感がここに起因しうると理解している

## よくある混線

- Calibration を「設定が面倒なだけの工程」と見てしまう
- Nodal Offset を最後に詰める微調整だと思ってしまう
- 違和感の原因を全部 delay や keying に寄せてしまう

## ここで開く公式ページ / 参照先

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Scene Control Panel](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/scene-control-panel/)
- REtracker Bliss: **あなたの日本語マニュアル** を一次参照にすることを推奨
- REtracker Official Tutorials: [Tutorials](https://www.retracker.co/tutorials)

> Bliss については、英語動画だけで独学するのは日本語話者には負荷が高いため、ここはあなたの日本語マニュアルを主参照にする設計が適切です。

---

# 4. Tracked Camera Standard Flow

## この章の目的

本資料の本流である、**tracked camera を使った green screen production の標準的な流れ** を理解することです。

## まず頭に入れたいこと

この章でいう Standard Flow は、

- tracked camera を使う
- green screen production を行う
- Aximmetryで映像・tracking・lens を受ける
- 同期を取り、合成し、出力する

という本流を指します。

ここでは AR / LED / no-tracked virtual cam の詳細は扱いません。

## 流れの全体像

1. AX Scene / Unreal 側の背景準備
2. Aximmetry 側で映像・tracking・lens を受ける
3. calibration profile を前提に同期を確認する
4. tracking delay / zoom delay / timecode sync を確認する
5. keying を行う
6. live output を出す
7. recorder へ安全に残す

## I/O setup の基本順

Aximmetry 側では、まず INPUTS で通常の進め方を成立させます。

### 基本順序
1. Camera Device
2. Tracking Device
3. Lens / Calibration の前提確認
4. Tracking Delay
5. Zoom Delay
6. Timecode Sync / Zoom Timecode Sync
7. Detect Tracking Delay / Detect Zoom Delay

## ここで理解したいこと

- まず **来ているか** を確認する
- その後で **合っているか** を確認する
- Detect Tracking Delay / Detect Zoom Delay は fallback ではなく、標準的な確認フローの一部である

## たとえ話 / Mental Model

この章は、**配線確認 → 同期確認 → 本番成立** の章です。  
いきなり keying や output に進むのではなく、まず信号の成立を確認します。

## チェックポイント

- [ ] tracked camera workflow の本流を説明できる
- [ ] Camera / Tracking / Lens の順で前提確認できる
- [ ] 「来ているか」と「合っているか」を分けて考えられる
- [ ] Detect Tracking Delay / Detect Zoom Delay が通常フローの一部だと理解している

## よくある混線

- 映像が来ているので大丈夫だと思ってしまう
- tracking と lens が来ているかの確認が曖昧なまま進める
- delay 検出を「トラブル時の最後の手段」と誤解する

## ここで開く公式ページ

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

---

# 5. Keying and Live Output

## この章の目的

keying を「ソフトのつまみ調整」だけで捉えず、**素材条件 → keyer 調整 → final output 確認** の順番で理解することです。

## まず頭に入れたいこと

keying は、ソフトだけで決まりません。  
先に整えるべきは、次のような **物理条件** です。

- 背景の状態
- lighting
- 被写体と背景の距離
- 衣装や反射物の条件

その後で、Aximmetry 側の keying 調整に入ります。

## Keying の確認順

1. 背景条件を確認する
2. lighting を確認する
3. 被写体距離を確認する
4. Aximmetry 側で調整する
5. Final Output で確認する

## Live Output の考え方

Day2 相当で重要なのは、**当日に安全に残す** ことです。

- Aximmetry の合成映像を output する
- recorder 側で受ける
- timecode master を基準に運用をそろえる
- 「後で作り込む」より「当日に安全に残す」が主目的

## たとえ話 / Mental Model

keying は、**料理の味付け** に似ています。  
材料の状態が悪いまま、調味料だけで全部を解決しようとしても限界があります。

## チェックポイント

- [ ] keying は物理条件が先だと説明できる
- [ ] keying の確認順を説明できる
- [ ] final output を定期的に確認する意味を説明できる
- [ ] live output / recorder / 当日収録の目的を説明できる

## よくある混線

- software keyer だけで全部を解決しようとする
- monitor mode と final output の見分けが曖昧になる
- live rec と input recording の目的を混同する

## ここで開く公式ページ

- Aximmetry Learn: [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- Aximmetry Learn: [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)

---

# 6. Replay, Recording, and Offline Review

## この章の目的

当日収録と、後工程用の recording / playback を混同せず、**何を残し、何に使うのか** を理解することです。

## まず頭に入れたいこと

この章で重要なのは、

- 当日に安全に残すための収録
- 後で replay / review / offline rendering につなぐための recording

を分けて考えることです。

## ここで押さえる言葉

### Live Rec / 当日収録
Aximmetry の合成映像を外部 recorder に送り、本番中に安全に残す考え方。

### Input Recording
後で offline rendering や replay を行うために、**raw camera input image** と **raw tracking data** を残す考え方。

### Use Input TC
カメラからの timecode を使って、あとで pairing / replay / post に生かす考え方。

### Tracking Only
tracking を主目的として残したい時の考え方。

### Playback / Replay
prerecorded video と tracking data を使って、後から再生確認する流れ。

## 何のために使うか

- 当日の setup を見直す
- 違和感の原因を切り分ける
- production ごとの改善点を見つける
- HQ素材と tracking をあとで合わせる
- offline rendering / further post へつなぐ

## 何を見るか

- 背景とのなじみ
- tracking の違和感
- zoom / sync の違和感
- keying の破綻
- 当日見逃した問題

## たとえ話 / Mental Model

- **Live Rec = その日の完成料理を残す**
- **Input Recording = 後で別の調理ができるよう、素材を残す**

この違いが分かると、recording まわりの混線がかなり減ります。

## チェックポイント

- [ ] 当日収録と input recording の目的の違いを説明できる
- [ ] Use Input TC の意味を説明できる
- [ ] playback / replay が何のためにあるか説明できる
- [ ] offline review で何を見るか思い出せる

## よくある混線

- 合成映像を録ることと、tracking data を残すことを同じだと思ってしまう
- replay を単なる再生機能だと思ってしまう
- timecode を「なくても何とかなるもの」と軽く見てしまう

## ここで開く公式ページ

- Aximmetry Learn: [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

# 7. Troubleshooting by Symptom

## この章の目的

問題が起きた時に、**症状 → 見る場所 → 原因カテゴリ → 戻る順番** で考えられるようにすることです。

## 基本姿勢

いきなり全部を疑わず、**症状に応じて見る場所を絞る** ことが重要です。

---

## 症状A: tracker が来ない

### まず見る場所
- Tracking Device
- デバイス接続状態
- Bliss 側動作状態
- ネットワーク / 接続経路

### まず疑うこと
- tracker 自体が動いていない
- Aximmetry 側 mapping が違う
- Bliss 側の出力設定が違う
- ネットワーク疎通 / 接続が不安定

### 戻る順番
1. Bliss 側の状態確認
2. Host PC との接続確認
3. Aximmetry 側 Tracking Device 確認
4. calibration / profile の前提確認

### 開く資料
- あなたの日本語 Bliss マニュアル
- REtracker Official Tutorials: [Tutorials](https://www.retracker.co/tutorials)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

## 症状B: CV Protocol / lens 情報が来ない

### まず見る場所
- External Lens Data
- Camera 側 CV Protocol 設定
- Ethernet 系の接続

### まず疑うこと
- 映像は来ていても lens data は別経路なので未成立
- camera 側設定の見落とし
- Aximmetry 側の受け口が違う

### 戻る順番
1. Camera 側の protocol 設定
2. Ethernet 経路
3. Aximmetry 側 lens data 受信設定
4. lens update の確認

---

## 症状C: zoom だけ合わない

### まず見る場所
- Zoom Delay
- Zoom Timecode Sync
- lens data の更新状態

### まず疑うこと
- tracking は合っているが zoom の同期がズレている
- lens data 更新が不完全
- calibration / lens profile 側の前提

### 戻る順番
1. lens 情報の到着確認
2. zoom delay 確認
3. zoom timecode sync 確認
4. calibration の前提確認

---

## 症状D: AUTO で映像が来ない

### まず見る場所
- Camera Mode
- resolution / fps
- capture card 側の認識

### まず疑うこと
- older capture card や条件によって AUTO がうまく効かない
- manual resolution / fps 指定が必要

### 戻る順番
1. cable / capture side の確認
2. Camera Mode を見直す
3. manual resolution / fps 指定
4. 他入力と切り分ける

---

## 症状E: timecode が噛み合わない

### まず見る場所
- Timecode Sync
- Zoom Timecode Sync
- Use Input TC
- master 側の前提

### まず疑うこと
- 同じ timecode を見ていない
- input TC を使う前提が崩れている
- live rec と offline review の前提が混ざっている

### 戻る順番
1. master の確認
2. camera 由来 timecode の確認
3. Aximmetry 側 sync 設定確認
4. recording / playback の目的を再確認

---

## たとえ話 / Mental Model

Troubleshooting は、**暗闇で全部を探す作業** ではありません。  
**症状から部屋を絞って探す作業** です。

## チェックポイント

- [ ] 症状から見る場所を絞れる
- [ ] 全部を同時に疑わず、順番に戻れる
- [ ] 問題が calibration 起因か、signal 起因か、sync 起因かを切り分けようとできる

---

# 8. Practical Extensions

## この章の目的

本流の tracked green screen workflow を理解した上で、**AX Scene Editor / Unreal 側へ少しだけ手を伸ばす** ための入口を持つことです。

## この章の位置づけ

ここは main workflow の土台ではなく、**発展項目** です。  
ただし、「Aximmetry は live composite だけで終わらない」ことを実感するには有効です。

## 今回の必須レシピ

1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

## ここで理解したいこと

- Aximmetry の映像を Unreal / AX Scene 側で受ける考え方がある
- Unreal 側 object interaction の入口がある
- 深い Blueprint 理論に入らなくても、practical recipe として触れられる

## チェックポイント

- [ ] Virtual Screen Asset の役割を説明できる
- [ ] Get Aximmetry Video の意味を説明できる
- [ ] simple Transformation を practical recipe として位置づけられる
- [ ] ここが main workflow ではなく extension だと理解している

## ここで開く公式ページ

- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)

> Virtual Screen や Blueprint extension の細かな操作は version に影響されやすいため、本文では概念と役割に集中し、手順は公式Learnを参照してください。

---

# 9. Reference Map / 参照マップ

## Aximmetry 公式Learn

### 全体導入
- [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

### AX Scene / Unreal
- [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

### Inputs / Sync / Keying
- [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- [Scene Control Panel](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/scene-control-panel/)
- [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)

### Recording / Playback
- [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)

## REtracker Bliss

### 推奨する参照順
1. **あなたの日本語マニュアル**
2. 公式 product page
3. 公式 tutorials

### 公式ページ
- [REtracker BLISS product page](https://www.retracker.co/retracker-bliss)
- [REtracker Tutorials](https://www.retracker.co/tutorials)

> 日本語受講者にとっては、Bliss の英語動画だけで再現するのは難しいため、あなたの日本語マニュアルをこの資料の正規導線にするのが望ましいです。  
> 必要であれば、この章にあなたの日本語マニュアルのリンクやファイル名を差し込んでください。

---

# Final Review Checklist

- [ ] システム全体の3系統を説明できる
- [ ] AX Scene / Unreal 側の最低限準備を説明できる
- [ ] Calibration と Nodal Offset の役割を説明できる
- [ ] tracked camera の standard flow を説明できる
- [ ] keying は物理条件が先だと説明できる
- [ ] live rec と input recording の違いを説明できる
- [ ] playback / offline review の目的を説明できる
- [ ] 症状から見る場所を絞って考えられる
- [ ] extension と main workflow を混同していない

---

# Notes for Future Update

この資料は受講者向け review guide です。  
講師用の runbook は別資料として分離し、以下を別途持たせるとよいです。

- 当日の進行順
- つまずきやすいポイント
- 実演タイミング
- 受講者の反応を見た補足説明
- 機材固有の注意点
- 時間調整用の optional branch


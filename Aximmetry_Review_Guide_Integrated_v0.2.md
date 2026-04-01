# Aximmetry Tracked Green Screen Review Guide
## 学習者向け統合復習ガイド v0.2

> この資料は、本資料で扱う内容を **日程単位ではなく概念単位** で復習し、Aximmetry公式Learnやデバイス資料を開きながら、独学でハンズオンを再走しやすくするためのガイドです。  
> 操作画面のすべてをここに書くのではなく、**何を理解し、どこを確認し、どの公式ページを次に開くべきか** を整理することを主目的にしています。

---

## この資料の使い方

### 1. まず全体像をつかむ
最初に **システム概要** を読み、映像・レンズ情報・トラッキング情報の3系統がどこから来て、どこで統合されるのかを理解します。

### 2. 次に「背景側」の前提を整える
AximmetryのGUIを触る前に、**Aximmetry向けAX Scene / Unreal準備** を確認します。  
ここでの目的は、Aximmetryに渡す前の **受け皿** を整えることです。

### 3. その後に「同期」の意味を理解する
**システム同期とキャリブレーション** を読み、Tracking Calibration と Nodal Offset が何のために必要なのかを理解します。  
ここを飛ばすと、後段のズレや違和感が「何となく合わない」ままになります。

### 4. 本流のトラッキングカメラ標準フローを通す
**Tracked Camera Standard Flow** から、Aximmetry側の INPUTS / delay / sync / keying / output を順番に復習します。

### 5. つまずいたら症状から引く
途中で詰まったら、**症状別トラブルシューティング** に戻ります。

---

## Scope / この資料の対象範囲

この資料の本流は、**Aximmetryで行うトラッキング付きグリーンスクリーン制作** です。

- 対象: トラッキングカメラを使ったグリーンスクリーン合成のワークフロー
- 主軸: AX Scene / Unreal 準備、Aximmetry入力、同期、キーイング、ライブ出力、記録 / 再生、トラブルシューティング
- 本流から外すもの: AR の詳細、LED Wall ワークフローの詳細、トラッキングなしの Virtual Camera ワークフローの詳細

> これらを否定する意図ではなく、まず **1本の勝ち筋を理解し、再現できるようにする** ためにスコープを絞っています。

---

## Terminology / 用語整理

- **AX Scene Editor**  
  Aximmetryが提供する、Unreal Editorをベースにしたカスタム版。古い資料では **Unreal Editor for Aximmetry** と表記される場合があります。  
  本資料では **AX Scene Editor** に統一します。

- **Tracked Camera Standard Flow**  
  本資料で扱う、トラッキングカメラを使ったグリーンスクリーン制作の本流。本資料では、学習者が流れを追いやすいよう、この名称に統一します。

- **Live Output / ライブ出力**  
  当日に安全に残すための出力・収録。

- **Input Recording / Playback / Offline Review**  
  後で再確認したり、再生したり、後工程へつないだりするための記録と確認の流れ。

---

# 1. System Overview / システム概要

## この章の目的

最初に、システム全体の **役割分担** と **情報の流れ** を頭の中で接続することです。

## まず頭に入れたいこと

ここで重要なのは、1つのソフトを覚えることではありません。  
**複数の信号が、別経路で入り、Aximmetryで統合される** ことを理解することです。

### 3つの流れ

1. **映像信号**  
   例: Canon C400 からの SDI 映像

2. **レンズ情報**  
   例: Canon C400 の CV Protocol などによるレンズ / ズーム系データ

3. **トラッキング情報**  
   例: REtracker Bliss から来る位置 / 回転系データ

Aximmetry は、これらを **統合して、合成し、出力する場所** です。  
AX Scene Editor / Unreal は、主に **背景側を作る場所** です。

## たとえ話 / 理解のためのたとえ

- **AX Scene / Unreal = 舞台美術を作る場所**
- **Aximmetry = 本番の舞台監督 / スイッチャー / 合成卓**
- **カメラ / レンズ / トラッカー = 現実世界の演者の情報源**

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
- トラッキングが来ていれば全部OKだと思ってしまう

## ここで開く公式ページ

- Aximmetry Learn: [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)

---

# 2. AX Scene / Unreal Setup for Aximmetry / Aximmetry向けAX Scene / Unreal準備

## この章の目的

AximmetryのGUIへ入る前に、**背景側の受け皿** を整えることです。

## まず頭に入れたいこと

Aximmetry側で映像やトラッキングを受けても、AX Scene / Unreal側の前提が崩れていると、後段で次のような問題に見えます。

- 背景スケールが不自然
- 床合わせがしにくい
- billboard（常にカメラ正面を向く表示）やシーン配置が理解しにくい
- 何がAximmetry側の問題で、何がUnreal側の問題か分からない

> つまり、Aximmetryに入る前に **背景側の最低限の成立条件** を押さえる必要があります。

## この章で理解したいこと

- AX Scene Editor は、Aximmetry向けの Unreal 側編集環境である
- Aximmetry Camera 前提のシーン準備が必要である
- map / project settings / project conversion / cooking（実行用データ書き出し）など、Aximmetry連携前提の準備がある
- この章は補助的なレシピではなく、本流の前提条件である

## 最低限の確認観点

### A. Project / Version
- Aximmetry と AX Scene Editor の対応バージョンを意識する
- 既存 Unreal プロジェクトを開く場合は convert の扱いに注意する
- バージョン更新は元に戻せない場合があるため、copy / backup 前提で扱う

### B. Project Settings
- Startup Map / Game Default Map の確認
- Aximmetry向けに必要な project 設定を確認する
- 「普通のUnrealプロジェクト」ではなく「Aximmetryに渡すプロジェクト」である意識を持つ

### C. Aximmetry Camera 前提
- Aximmetry は Aximmetry Camera Blueprint を通じて Unreal シーンにアクセスする
- 単に Cine Camera があれば十分、とは考えない
- トラッキングワークフローの前提に合ったカメラ設定であることを確認する

### D. Scene 側の最低限
- 床の見え方
- シーンスケール
- 被写体が立つ想定位置
- billboard（常にカメラ正面を向く表示）や合成前提で破綻しにくい構成

## たとえ話 / 理解のためのたとえ

この章は、**背景セットを組む章** です。  
カメラ信号やトラッキングがどれだけ正しくても、背景側の寸法感や入口が崩れていると、後で全部が不安定に見えます。

## チェックポイント

- [ ] AX Scene Editor が何か説明できる
- [ ] Aximmetry向けプロジェクトは標準的な Unreal プロジェクトと同じではないと理解している
- [ ] Aximmetry Camera 前提のシーン準備が必要だと説明できる
- [ ] シーンスケール / floor / 被写体位置の前提を見直せる
- [ ] レシピではなく本流の前提条件だと理解している

## よくある混線

- Unreal の絵作りができていれば、そのままAximmetryで使えると思ってしまう
- トラッキングワークフローなのに camera の前提が曖昧なまま進める
- Aximmetry GUI 側で頑張ればシーン側の問題も吸収できると思ってしまう

## ここで開く公式ページ

- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- Aximmetry Learn: [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

---

# 3. System Synchronization and Calibration / システム同期とキャリブレーション

## この章の目的

Tracking Calibration と Nodal Offset を、単なる数値調整ではなく、**現実と仮想を同期させるための工程** として理解することです。

## まず頭に入れたいこと

この資料では、Calibration を早い段階で確認します。  
理由は、プロファイルがないと進みにくいからだけではありません。  
**全系統を同期するという概念** を、早めに理解してもらうためです。

## この章で理解したいこと

### Tracking Calibration
トラッキング空間と仮想側の基準を合わせる工程です。

### Nodal Offset
トラッキングポイントと実際のレンズ中心のズレを補正する工程です。

この2つは、後段のキーイングや再生確認の話とは別物に見えて、実はかなり深く関係しています。

- 背景位置が不自然
- パン / チルト / 移動で違和感が出る
- 床が滑るように見える
- 「何となく合わない」

こうした問題の原因が、ここにあることがあります。

## たとえ話 / 理解のためのたとえ

- **Calibration = 現実と仮想の定規を合わせる**
- **Nodal Offset = センサーの位置とレンズの中心を一致させる**

トラッキングポイントは「カメラ本体のどこか」についていることが多く、レンズ中心そのものではありません。  
だから補正が必要です。

## 後続工程とのつながり

- ライブ合成の自然さに直結する
- 再生確認やトラブルシューティングでも、原因がここに戻ることがある
- ズーム / 同期 / 床が滑るような違和感を、delay だけの問題と決めつけない

## チェックポイント

- [ ] Tracking Calibration の役割を説明できる
- [ ] Nodal Offset の役割を説明できる
- [ ] なぜこの理解を早い段階で持つのか説明できる
- [ ] 背景ズレ・床が滑るような違和感がここに起因しうると理解している

## よくある混線

- Calibration を「設定が面倒なだけの工程」と見てしまう
- Nodal Offset を最後に詰める微調整だと思ってしまう
- 違和感の原因を全部 delay やキーイングに寄せてしまう

## ここで開く公式ページ / 参照先

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Scene Control Panel](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/scene-control-panel/)
- REtracker Bliss: **日本語マニュアル（入手できる場合）** を一次参照にすることを推奨
- REtracker Official Tutorials: [Tutorials](https://www.retracker.co/tutorials)

> Bliss については、英語動画だけで独学するのは日本語話者には負荷が高いため、日本語マニュアルがある場合はそちらを優先して参照するのが適切です。

---

# 4. Tracked Camera Standard Flow / トラッキングカメラ標準フロー

## この章の目的

本資料の本流である、**トラッキングカメラを使ったグリーンスクリーン制作の標準的な流れ** を理解することです。

## まず頭に入れたいこと

この章でいう標準フローは、

- トラッキングカメラを使う
- グリーンスクリーン制作を行う
- Aximmetryで映像・トラッキング・レンズ情報を受ける
- 同期を取り、合成し、出力する

という本流を指します。

ここでは AR / LED / トラッキングなしの Virtual Camera の詳細は扱いません。

## 流れの全体像

1. AX Scene / Unreal 側の背景準備
2. Aximmetry 側で映像・トラッキング・レンズ情報を受ける
3. キャリブレーションプロファイルを前提に同期を確認する
4. tracking delay / zoom delay / timecode sync を確認する
5. キーイングを行う
6. ライブ出力を出す
7. レコーダーへ安全に残す

## I/O設定の基本順

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
- Detect Tracking Delay / Detect Zoom Delay は代替手段ではなく、標準的な確認フローの一部である

## たとえ話 / 理解のためのたとえ

この章は、**配線確認 → 同期確認 → 本番成立** の章です。  
いきなりキーイングや出力に進むのではなく、まず信号の成立を確認します。

## チェックポイント

- [ ] トラッキングカメラワークフローの本流を説明できる
- [ ] Camera / Tracking / Lens の順で前提確認できる
- [ ] 「来ているか」と「合っているか」を分けて考えられる
- [ ] Detect Tracking Delay / Detect Zoom Delay が通常フローの一部だと理解している

## よくある混線

- 映像が来ているので大丈夫だと思ってしまう
- トラッキングとレンズ情報が来ているかの確認が曖昧なまま進める
- delay 検出を「トラブル時の最後の手段」と誤解する

## ここで開く公式ページ

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

---

# 5. Keying and Live Output / キーイングとライブ出力

## この章の目的

キーイングを「ソフトのつまみ調整」だけで捉えず、**素材条件 → キーヤー調整 → 最終出力確認** の順番で理解することです。

## まず頭に入れたいこと

キーイングは、ソフトだけで決まりません。  
先に整えるべきは、次のような **物理条件** です。

- 背景の状態
- 照明
- 被写体と背景の距離
- 衣装や反射物の条件

その後で、Aximmetry 側のキーイング調整に入ります。

## キーイングの確認順

1. 背景条件を確認する
2. 照明を確認する
3. 被写体距離を確認する
4. Aximmetry 側で調整する
5. 最終出力で確認する

## ライブ出力の考え方

この段階で重要なのは、**当日に安全に残す** ことです。

- Aximmetry の合成映像を出力する
- レコーダー側で受ける
- タイムコードマスターを基準に運用をそろえる
- 「後で作り込む」より「当日に安全に残す」が主目的

## たとえ話 / 理解のためのたとえ

キーイングは、**料理の味付け** に似ています。  
材料の状態が悪いまま、調味料だけで全部を解決しようとしても限界があります。

## チェックポイント

- [ ] キーイングは物理条件が先だと説明できる
- [ ] キーイングの確認順を説明できる
- [ ] 最終出力を定期的に確認する意味を説明できる
- [ ] ライブ出力 / レコーダー / 当日収録の目的を説明できる

## よくある混線

- ソフトウェアキーヤーだけで全部を解決しようとする
- モニターモードと最終出力の見分けが曖昧になる
- live rec と input recording の目的を混同する

## ここで開く公式ページ

- Aximmetry Learn: [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- Aximmetry Learn: [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)

---

# 6. Replay, Recording, and Offline Review / 再生・記録・オフライン確認

## この章の目的

当日収録と、後工程用の記録 / 再生を混同せず、**何を残し、何に使うのか** を理解することです。

## まず頭に入れたいこと

この章で重要なのは、

- 当日に安全に残すための収録
- 後で replay / review / offline rendering につなぐための記録

を分けて考えることです。

## ここで押さえる言葉

### Live Rec / 当日収録
Aximmetry の合成映像を外部レコーダーに送り、本番中に安全に残す考え方。

### Input Recording
後で offline rendering や replay を行うために、**生のカメラ入力映像** と **生のトラッキングデータ** を残す考え方。

### Use Input TC
カメラからのタイムコードを使って、あとで pairing / replay / post に生かす考え方。

### Tracking Only
トラッキングを主目的として残したい時の考え方。

### Playback / Replay
事前収録した映像とトラッキングデータを使って、後から再生確認する流れ。

## 何のために使うか

- そのときの設定を見直す
- 違和感の原因を切り分ける
- 制作ごとの改善点を見つける
- 高画質素材とトラッキングをあとで合わせる
- offline rendering / 後工程へつなぐ

## 何を見るか

- 背景とのなじみ
- トラッキングの違和感
- ズーム / 同期の違和感
- キーイングの破綻
- 収録時に見逃した問題

## たとえ話 / 理解のためのたとえ

- **Live Rec = その日の完成料理を残す**
- **Input Recording = 後で別の調理ができるよう、素材を残す**

この違いが分かると、記録まわりの混線がかなり減ります。

## チェックポイント

- [ ] 当日収録と input recording の目的の違いを説明できる
- [ ] Use Input TC の意味を説明できる
- [ ] playback / replay が何のためにあるか説明できる
- [ ] offline review で何を見るか思い出せる

## よくある混線

- 合成映像を録ることと、トラッキングデータを残すことを同じだと思ってしまう
- replay を単なる再生機能だと思ってしまう
- タイムコードを「なくても何とかなるもの」と軽く見てしまう

## ここで開く公式ページ

- Aximmetry Learn: [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

# 7. Troubleshooting by Symptom / 症状別トラブルシューティング

## この章の目的

問題が起きた時に、**症状 → 見る場所 → 原因カテゴリ → 戻る順番** で考えられるようにすることです。

## 基本姿勢

いきなり全部を疑わず、**症状に応じて見る場所を絞る** ことが重要です。

---

## 症状A: トラッカーが来ない

### まず見る場所
- Tracking Device
- デバイス接続状態
- Bliss 側動作状態
- ネットワーク / 接続経路

### まず疑うこと
- トラッカー自体が動いていない
- Aximmetry 側のマッピングが違う
- Bliss 側の出力設定が違う
- ネットワーク疎通 / 接続が不安定

### 戻る順番
1. Bliss 側の状態確認
2. Host PC との接続確認
3. Aximmetry 側 Tracking Device 確認
4. calibration / プロファイルの前提確認

### 開く資料
- REtracker Bliss 日本語マニュアル
- REtracker Official Tutorials: [Tutorials](https://www.retracker.co/tutorials)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

## 症状B: CV Protocol / レンズ情報が来ない

### まず見る場所
- External Lens Data
- Camera 側 CV Protocol 設定
- Ethernet 系の接続

### まず疑うこと
- 映像は来ていてもレンズデータは別経路なので未成立
- camera 側設定の見落とし
- Aximmetry 側の受け口が違う

### 戻る順番
1. Camera 側のプロトコル設定
2. Ethernet 経路
3. Aximmetry 側レンズデータ受信設定
4. レンズデータ更新の確認

---

## 症状C: ズームだけ合わない

### まず見る場所
- Zoom Delay
- Zoom Timecode Sync
- レンズデータの更新状態

### まず疑うこと
- トラッキングは合っているがズームの同期がズレている
- レンズデータ更新が不完全
- calibration / レンズプロファイル側の前提

### 戻る順番
1. レンズ情報の到着確認
2. zoom delay 確認
3. zoom timecode sync 確認
4. calibration の前提確認

---

## 症状D: AUTO で映像が来ない

### まず見る場所
- Camera Mode
- resolution / fps
- キャプチャーカード側の認識

### まず疑うこと
- 古いキャプチャーカードや条件によって AUTO がうまく効かない
- manual resolution / fps 指定が必要

### 戻る順番
1. cable / capture side の確認
2. Camera Mode を見直す
3. manual resolution / fps 指定
4. 他入力と切り分ける

---

## 症状E: タイムコードが噛み合わない

### まず見る場所
- Timecode Sync
- Zoom Timecode Sync
- Use Input TC
- master 側の前提

### まず疑うこと
- 同じタイムコードを見ていない
- input TC を使う前提が崩れている
- live rec と offline review の前提が混ざっている

### 戻る順番
1. master の確認
2. camera 由来タイムコードの確認
3. Aximmetry 側 sync 設定確認
4. recording / playback の目的を再確認

---

## たとえ話 / 理解のためのたとえ

トラブルシューティングは、**暗闇で全部を探す作業** ではありません。  
**症状から部屋を絞って探す作業** です。

## チェックポイント

- [ ] 症状から見る場所を絞れる
- [ ] 全部を同時に疑わず、順番に戻れる
- [ ] 問題が calibration 起因か、signal 起因か、sync 起因かを切り分けようとできる

---

# 8. Practical Extensions / 実践的な発展項目

## この章の目的

本流のトラッキング付きグリーンスクリーンワークフローを理解した上で、**AX Scene Editor / Unreal 側へ少しだけ手を伸ばす** ための入口を持つことです。

## この章の位置づけ

ここはメインワークフローの土台ではなく、**発展項目** です。  
ただし、「Aximmetry は live composite だけで終わらない」ことを実感するには有効です。

## 今回の必須レシピ

1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

## ここで理解したいこと

- Aximmetry の映像を Unreal / AX Scene 側で受ける考え方がある
- Unreal 側オブジェクト操作の入口がある
- 深い Blueprint 理論に入らなくても、実践的なレシピとして触れられる

## チェックポイント

- [ ] Virtual Screen Asset の役割を説明できる
- [ ] Get Aximmetry Video の意味を説明できる
- [ ] simple Transformation を実践的なレシピとして位置づけられる
- [ ] ここがメインワークフローではなく発展項目だと理解している

## ここで開く公式ページ

- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)

> Virtual Screen や Blueprint を使った発展項目の細かな操作は version に影響されやすいため、本文では概念と役割に集中し、手順は公式Learnを参照してください。

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
1. **REtracker Bliss 日本語マニュアル（入手できる場合）**
2. 公式製品ページ
3. 公式チュートリアル

### 公式ページ
- [REtracker BLISS product page](https://www.retracker.co/retracker-bliss)
- [REtracker Tutorials](https://www.retracker.co/tutorials)

> 日本語話者にとっては、Bliss の英語動画だけで再現するのは難しいため、日本語マニュアルがある場合はそちらを優先して参照するのが望ましいです。

---

# Final Review Checklist / 最終確認チェックリスト

- [ ] システム全体の3系統を説明できる
- [ ] AX Scene / Unreal 側の最低限準備を説明できる
- [ ] Calibration と Nodal Offset の役割を説明できる
- [ ] トラッキングカメラの標準フローを説明できる
- [ ] キーイングは物理条件が先だと説明できる
- [ ] live rec と input recording の違いを説明できる
- [ ] playback / offline review の目的を説明できる
- [ ] 症状から見る場所を絞って考えられる
- [ ] 発展項目とメインワークフローを混同していない

---

# Notes for Future Update / 今後の更新メモ

この資料は学習者向けの復習ガイドです。  
学習用の本文とは別に、運用や進行に関するメモを分けて管理すると整理しやすくなります。

- 進行順メモ
- つまずきやすいポイント
- 実演やデモのタイミング
- 学習者がつまずきやすい箇所への補足説明
- 機材固有の注意点
- 時間や習熟度に応じた任意分岐

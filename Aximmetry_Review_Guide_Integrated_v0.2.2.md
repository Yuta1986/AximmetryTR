# Aximmetry Tracked Green Screen Learning and Review Roadmap
## 学習・復習ロードマップ v0.2.2

> この資料は、本資料で扱う内容を整理し、Aximmetry公式Learnやデバイス資料を開きながら、学習や復習を進めやすくするためのロードマップです。  
> 操作画面のすべてをここに書くのではなく、**何を理解し、どこを確認し、どの公式ページを次に開くべきか** を簡潔に整理することを主目的にしています。  
> 学習・復習の順路としても、用語や参照先を確認するための一覧としても使えるように構成しています。
> Trainingを受けた方の復習用としてはもちろん、一部の講義だけ受けた方や、導入説明後に抜けた内容を補いながら確認したい方にも使えるように構成しています。

---

## このロードマップの使い方

### 1. まず全体像をつかむ
最初に **System Overview / システム概要** を読み、映像・レンズ情報・トラッキング情報の3系統がどこから来て、どこで統合されるのかを理解します。

### 2. 次に「背景側」の前提を整える
Aximmetryの画面を触る前に、**AX Scene / Unreal Setup for Aximmetry / Aximmetry向けAX Scene / Unreal準備** を確認します。  
ここでの目的は、Aximmetryに渡す前の **受け皿** を整えることです。

### 3. その後に「同期」の意味を理解する
**System Synchronization and Calibration / システム同期とキャリブレーション** を読み、Tracking Calibration と Nodal Offset が何のために必要なのかを理解します。  
ここを飛ばすと、後段のズレや違和感が「何となく合わない」ままになります。

### 4. 本流のトラッキングカメラ標準フローを通す
**Tracked Camera Standard Flow / トラッキングカメラ標準フロー** から、Aximmetry側の INPUTS / delay / sync / keying / output を順番に復習します。

### 5. つまずいたら症状から引く
途中で詰まったら、**Troubleshooting by Symptom / 症状別トラブルシューティング** に戻ります。

---

## このロードマップの見取り図

1. **System Overview**: 3系統の信号と役割分担をつかむ
2. **AX Scene / Unreal Setup for Aximmetry**: 背景側の受け皿を整える
3. **System Synchronization and Calibration**: ズレの原因になる同期の意味を理解する
4. **Tracked Camera Standard Flow**: 本流の順番で I/O から出力まで追う
5. **Keying and Live Output**: キーイングと当日収録の考え方を押さえる
6. **Replay, Recording, and Offline Review**: 何を残し、何に使うかを分けて理解する
7. **Troubleshooting by Symptom**: 症状から見る場所を絞る
8. **Practical Extensions**: 本流の外側にある発展項目の入口を知る
9. **Reference Map**: 参照先を一覧で引けるようにする

---

## Scope / この資料の対象範囲

この資料の本流は、**Aximmetryで行うトラッキング付きグリーンバック制作** です。

- 対象: トラッキングカメラを使ったグリーンバック合成のワークフロー
- 主軸: AX Scene / Unreal 準備、Aximmetry入力、同期、キーイング、ライブ出力、記録 / 再生、トラブルシューティング
- 本流から外すもの: AR の詳細、LED Wall ワークフローの詳細、トラッキングなしの Virtual Camera ワークフローの詳細

> これらを否定する意図ではなく、まず **1本の勝ち筋を理解し、再現できるようにする** ためにスコープを絞っています。
> 本文中に出てくる機材名やデバイス名は、構成をイメージしやすくするための例です。実際の導入構成に応じて読み替えてください。

---

## Terminology / 用語辞書

先に言葉の意味を引きたいときは、このセクションを使ってください。

- **AX Scene Editor**  
  Aximmetryが提供する、Unreal Editorをベースにしたカスタム版。古い資料では **Unreal Editor for Aximmetry** と表記される場合があります。  
  本資料では **AX Scene Editor** に統一します。

- **グリーンバック / Green Screen**  
  日本語本文では **グリーンバック** と表記します。  
  ただし、Aximmetry公式Learnや公式ページ名では **Green Screen** という表記が使われるため、リンク名や正式名称はそのまま残します。

- **Tracked Camera Standard Flow**  
  本資料で扱う、トラッキングカメラを使ったグリーンバック制作の本流。  
  読み進めやすさのため、日本語では **トラッキングカメラ標準フロー** と呼びます。

- **Live Output / ライブ出力**  
  当日に安全に残すための出力・収録。

- **Input Recording**  
  後で replay や offline rendering を行うために、入力映像やトラッキングデータを記録しておく考え方です。

- **Playback / Offline Review**  
  記録した素材をあとで見直し、再生確認し、後工程へつなぐための確認の流れです。

- **Tracking Calibration**  
  トラッキング空間とヴァーチャル空間の基準を合わせる工程です。

- **Nodal Offset**  
  トラッキングデバイスの基準点と、実際のレンズ中心のズレを補正する工程です。

---

# 1. System Overview / システム概要

## この章でつかむこと

最初に、システム全体の **役割分担** と **情報の流れ** を頭の中で接続することです。

## 最初に押さえること

ここで重要なのは、1つのソフトを覚えることではありません。  
**複数の信号が、別経路で入り、Aximmetryで統合される** ことを理解することです。

### 3つの流れ

以下の機材名は、信号の流れを具体的にイメージしやすくするための例です。

1. **映像信号**  
   例: Canon C400 からの SDI 映像

2. **レンズ情報**  
   例: Canon C400 の CV Protocol などによる、ズームやフォーカス距離、歪みや絞りなどのレンズデータ

3. **トラッキング情報**  
   例: REtracker Bliss から来る位置 / 回転系データ

Aximmetry は、これらを **統合して、合成し、出力する場所** です。  
AX Scene Editor / Unreal は、主に **背景側を作る場所** です。

## たとえ話 / Mental Model

- **AX Scene / Unreal = 舞台美術を作る場所**
- **Aximmetry = 本番の舞台監督 / スイッチャー / 合成卓**
- **カメラ / レンズ / トラッカー = 現実世界の演者の情報源**

つまり、Unreal だけでも、Aximmetry だけでも成立しません。  
**背景の準備** と **現実入力の統合** の両方が必要です。

## チェックポイント

- [ ] カメラ / トラッカー / Aximmetry / AX Scene Editor の役割を言葉で説明できる
- [ ] 映像・レンズ情報・トラッキング情報の3系統を説明できる
- [ ] なぜそれらが別経路で来るのかを理解している
- [ ] Aximmetry が「背景を作る場所」ではなく「統合・合成・出力の場所」だと説明できる

## よくある誤解

- Aximmetry と Unreal の役割を同じものとして捉えてしまう
- 映像とレンズ情報も同じ経路で来ると思ってしまう
- トラッキングが来ていれば、それだけで成立していると思ってしまう

## 次に開くページ

- Aximmetry Learn: [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)

---

# 2. AX Scene / Unreal Setup for Aximmetry / Aximmetry向けAX Scene / Unreal準備

## この章でつかむこと

Aximmetryの画面へ入る前に、**背景側の受け皿** を整えることです。

## 最初に押さえること

Aximmetry側で映像やトラッキングを受けても、AX Scene / Unreal側の前提が崩れていると、後段で次のような問題に直面します。

- 背景スケールが不自然
- CGと実写の床が合わない
- シーン内の表示物やオブジェクトを、どう配置すべきか分かりにくい
- 何がAximmetry側の問題で、何がUnreal側の問題か分からない

> つまり、Aximmetryに入る前に **背景側の最低限の成立条件** を押さえる必要があります。

## この章で押さえること

- AX Scene Editor は、Aximmetry向けの Unreal 側編集環境である
- Aximmetry Camera 前提のシーン準備が必要である
- map / project settings / project conversion / cooking（実行用データ書き出し）など、Aximmetry連携前提の準備がある

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

## たとえ話 / Mental Model

この章は、**背景セットを組む章** です。  
カメラ信号やトラッキングがどれだけ正しくても、背景側の寸法感や入口が崩れていると、後で全部が不安定に見えます。

## チェックポイント

- [ ] AX Scene Editor が何か説明できる
- [ ] Aximmetry向けプロジェクトは標準的な Unreal プロジェクトと同じではないと理解している
- [ ] Aximmetry Camera 前提のシーン準備が必要だと説明できる
- [ ] シーンスケール / floor / 被写体位置の前提を見直せる

## よくある誤解

- Unreal で絵作りができていれば、そのままAximmetryでも使えると思ってしまう
- トラッキングワークフローなのに、カメラ前提を曖昧なまま進めてしまう
- Aximmetry側で頑張れば、シーン側の問題も吸収できると思ってしまう

## 次に開くページ

- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- Aximmetry Learn: [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

---

# 3. System Synchronization and Calibration / システム同期とキャリブレーション

## この章でつかむこと

Tracking Calibration と Nodal Offset を、単なる数値調整ではなく、**現実とヴァーチャルを同期させるための工程** として理解することです。

## 最初に押さえること

この資料では、Calibration を早い段階で確認します。  
理由は、プロファイルがないと進みにくいからだけではありません。  
**全系統を同期するという概念** を、早めに理解してもらうためです。

## この章で押さえること

### Tracking Calibration
トラッキング空間とヴァーチャル側の基準を合わせる工程です。

### Nodal Offset
トラッキングデバイスの基準点と、実際のレンズ中心のズレを補正する工程です。

この2つは、後段のキーイングや再生確認の話とは別物に見えて、実はかなり深く関係しています。

- 背景位置が不自然
- パン / チルト / 移動で違和感が出る
- 床が滑るように見える
- 「何となく合わない」

こうした問題の原因が、ここにあることがあります。

## たとえ話 / Mental Model

- **Calibration = 現実とヴァーチャルの定規を合わせる**
- **Nodal Offset = センサーの位置とレンズの中心を一致させる**

トラッキングデバイスの基準点は、カメラ本体上のどこかにあることが多く、レンズ中心そのものとは一致しません。  
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

## よくある誤解

- Calibration を、設定が面倒なだけの工程だと見てしまう
- Nodal Offset を、最後に詰める微調整だと思ってしまう
- 違和感の原因を、すべて delay やキーイングに寄せてしまう

## 次に開くページ / 参照先

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Scene Control Panel](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/scene-control-panel/)
- REtracker Bliss: **配布された REtracker Bliss 日本語マニュアル** を一次参照にすることを推奨
- REtracker Official Tutorials: [Tutorials](https://www.retracker.co/tutorials)

> Bliss については、英語動画だけで理解を進めるのは日本語話者には負荷が高いため、まずは **配布された REtracker Bliss 日本語マニュアル** を主参照にするのが適切です。

---

# 4. Tracked Camera Standard Flow / トラッキングカメラ標準フロー

## この章でつかむこと

本資料の本流である、**トラッキングカメラを使ったグリーンバック制作の標準的な流れ** を理解することです。

## 最初に押さえること

この章でいう標準フローは、

- トラッキングカメラを使う
- グリーンバック制作を行う
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

## この章で押さえること

- まず **来ているか** を確認する
- その後で **合っているか** を確認する
- Detect Tracking Delay / Detect Zoom Delay は代替手段ではなく、標準的な確認フローの一部である

## たとえ話 / Mental Model

この章は、**配線確認 → 同期確認 → 本番成立** の章です。  
いきなりキーイングや出力に進むのではなく、まず信号の成立を確認します。

## チェックポイント

- [ ] トラッキングカメラワークフローの本流を説明できる
- [ ] Camera / Tracking / Lens の順で前提確認できる
- [ ] 「来ているか」と「合っているか」を分けて考えられる
- [ ] Detect Tracking Delay / Detect Zoom Delay が通常フローの一部だと理解している

## よくある誤解

- 映像が来ているので、全体も成立していると思ってしまう
- トラッキングとレンズ情報の確認が曖昧なまま進めてしまう
- delay 検出を、トラブル時だけ使う最後の手段だと誤解する

## 次に開くページ

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

---

# 5. Keying and Live Output / キーイングとライブ出力

## この章でつかむこと

キーイングを「ソフトのつまみ調整」だけで捉えず、**素材条件 → キーヤー調整 → 最終出力確認** の順番で理解することです。

## 最初に押さえること

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

## たとえ話 / Mental Model

キーイングは、**料理の味付け** に似ています。  
材料の状態が悪いまま、調味料だけで全部を解決しようとしても限界があります。

## チェックポイント

- [ ] キーイングは物理条件が先だと説明できる
- [ ] キーイングの確認順を説明できる
- [ ] 最終出力を定期的に確認する意味を説明できる
- [ ] ライブ出力 / レコーダー / 当日収録の目的を説明できる

## よくある誤解

- ソフトウェアキーヤーだけで解決できると思ってしまう
- モニターモードと最終出力を同じものとして見てしまう
- live rec と input recording の目的を同じものだと思ってしまう

## 次に開くページ

- Aximmetry Learn: [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- Aximmetry Learn: [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)

---

# 6. Replay, Recording, and Offline Review / 再生・記録・オフライン確認

## この章でつかむこと

当日収録と、後工程用の記録 / 再生を混同せず、**何を残し、何に使うのか** を理解することです。

## 最初に押さえること

この章で重要なのは、

- 当日に安全に残すための収録
- 後で replay / review / offline rendering につなぐための記録

を分けて考えることです。

## この章のキーワード

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

## 使いどころ

- そのときの設定を見直す
- 違和感の原因を切り分ける
- 制作ごとの改善点を見つける
- 高画質素材とトラッキングをあとで合わせる
- offline rendering / 後工程へつなぐ

## 見るポイント

- 背景とのなじみ
- トラッキングの違和感
- ズーム / 同期の違和感
- キーイングの破綻
- 収録時に見逃した問題

## たとえ話 / Mental Model

- **Live Rec = その日の完成料理を残す**
- **Input Recording = 後で別の調理ができるよう、素材を残す**

この違いが分かると、記録まわりの混線がかなり減ります。

## チェックポイント

- [ ] 当日収録と input recording の目的の違いを説明できる
- [ ] Use Input TC の意味を説明できる
- [ ] playback / replay が何のためにあるか説明できる
- [ ] offline review で何を見るか思い出せる

## よくある誤解

- 合成映像を録ることと、トラッキングデータを残すことを同じだと思ってしまう
- replay を単なる再生機能として見てしまう
- タイムコードを、なくても何とかなるものだと軽く見てしまう

## 次に開くページ

- Aximmetry Learn: [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

# 7. Troubleshooting by Symptom / 症状別トラブルシューティング

## この章でつかむこと

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
- **配布された REtracker Bliss 日本語マニュアル**
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

## たとえ話 / Mental Model

トラブルシューティングは、**暗闇で全部を探す作業** ではありません。  
**症状から部屋を絞って探す作業** です。

## チェックポイント

- [ ] 症状から見る場所を絞れる
- [ ] 全部を同時に疑わず、順番に戻れる
- [ ] 問題が calibration 起因か、signal 起因か、sync 起因かを切り分けようとできる

---

# 8. Practical Extensions / 実践的な発展項目

## この章でつかむこと

本流のトラッキング付きグリーンバックワークフローを理解した上で、**AX Scene Editor / Unreal 側へ少しだけ手を伸ばす** ための入口を持つことです。

## この章の位置づけ

ここはメインワークフローの土台ではなく、**発展項目** です。  
最初の1周では無理に触れず、本流を通せてから戻ってくれば十分です。  
ただし、「Aximmetry は live composite だけで終わらない」ことを実感するには有効です。

## 最初に触れたい項目

1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

## この章で押さえること

- Aximmetry の映像を Unreal / AX Scene 側で受ける考え方がある
- Unreal 側オブジェクト操作の入口がある
- 深い Blueprint 理論に入らなくても、実践的なレシピとして触れられる

## チェックポイント

- [ ] Virtual Screen Asset の役割を説明できる
- [ ] Get Aximmetry Video の意味を説明できる
- [ ] simple Transformation を実践的なレシピとして位置づけられる
- [ ] ここがメインワークフローではなく発展項目だと理解している

## 次に開くページ

- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)

> Virtual Screen や Blueprint を使った発展項目の細かな操作は version に影響されやすいため、本文では概念と役割に集中し、手順は公式Learnを参照してください。

---

# 9. Purpose Index / 目的別索引

> 何をしたいかから引けるように整理しています。  
> 同じページが複数の目的にまたがる場合は、探しやすさを優先して重複して載せています。

## まず全体像をつかみたい
- [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

## 背景側の準備を確認したい
- [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

## Inputs / Sync を確認したい
- [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- [Scene Control Panel](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/scene-control-panel/)
- [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

## キーイングとライブ出力を確認したい
- [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)
- [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

## 記録 / 再生 / offline review を確認したい
- [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)
- [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

## 発展項目を確認したい
- [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

## REtracker Bliss を確認したい

### 推奨する参照順
1. **配布された REtracker Bliss 日本語マニュアル**
2. 公式製品ページ
3. 公式チュートリアル

### 公式ページ
- [REtracker BLISS product page](https://www.retracker.co/retracker-bliss)
- [REtracker Tutorials](https://www.retracker.co/tutorials)

> 日本語話者にとっては、Bliss の英語動画だけで再現するのは難しいため、まずは **配布された REtracker Bliss 日本語マニュアル** を主参照にするのが望ましいです。

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

# 学習・復習ロードマップ v0.2.3
## Aximmetry Tracked Green Screen Learning and Review Roadmap

> **補足**  
> この資料は、Aximmetry公式Learnを読み進めながら、トレーニング内容を復習しやすくするためのロードマップです。  
> 操作手順を網羅するのではなく、**何を理解し、どこを確認し、次に何を見るべきか** を整理しています。

---

## このロードマップの使い方

### 1. まず全体像をつかむ
最初に **システム概要** を読み、映像・レンズ情報・トラッキング情報の3系統がどこから来て、どこで統合されるのかを理解します。

### 2. 次に「背景側」の前提を整える
Aximmetryの画面を触る前に、**AX Scene / Unreal準備** を確認します。  
ここでの目的は、Aximmetryに渡す前の **受け皿** を整えることです。

### 3. その後に「同期」の意味を理解する
**システム同期とキャリブレーション** を読み、Tracking Calibration と Nodal Offset が何のために必要なのかを理解します。  
ここを飛ばすと、後段のズレや違和感が「何となく合わない」ままになります。

### 4. 本資料のトラッキングカメラワークフローを通す
**トラッキングカメラワークフロー** から、Aximmetry側の入力、遅延調整、同期、キーイング、出力を順番に復習します。

### 5. つまずいたら症状から引く
途中で詰まったら、**症状別トラブルシューティング** に戻ります。

---

## このロードマップの見取り図

1. **システム概要**: 3系統の信号と役割分担をつかむ
2. **AX Scene / Unreal準備**: 背景側の受け皿を整える
3. **システム同期とキャリブレーション**: ズレの原因になる同期の意味を理解する
4. **トラッキングカメラワークフロー**: 本資料の主題となる順番でI/Oから出力まで追う
5. **キーイングとライブ出力**: キーイングと当日収録の考え方を押さえる
6. **再生・記録・オフライン確認**: 何を残し、何に使うかを分けて理解する
7. **症状別トラブルシューティング**: 症状から見る場所を絞る
8. **実践的な発展項目**: やりたいこと別に、次に開く公式Learnの入口を選ぶ
9. **目的別索引**: 目的から参照先を引けるようにする

---

## この資料の対象範囲 / Scope

この資料の本流は、**Aximmetryで行うトラッキングカメラでのグリーンバック制作** です。

- 対象: トラッキングカメラを使ったグリーンバック合成のワークフロー
- 主軸: AX Scene / Unreal準備、Aximmetry入力、同期、キーイング、ライブ出力、記録と再生、トラブルシューティング
- 本資料で詳しく触れていないもの: ARの詳細、LED Wallワークフローの詳細、トラッキングなしのヴァーチャルカメラ運用の詳細

> **補足**  
> これらを否定する意図ではなく、まず **1本の勝ち筋を理解し、再現できるようにする** ためにスコープを絞っています。
> 本文中に出てくる機材名やデバイス名は、構成をイメージしやすくするための例です。実際の導入構成に応じて読み替えてください。

---

## 用語辞書 / Terminology

先に言葉の意味を引きたいときは、このセクションを使ってください。

- **AX Scene Editor**  
  Aximmetryが提供する、Unreal Editorをベースにしたカスタム版です。2026.1.0では、ライセンス体系の変更に伴って Unreal 関連コンポーネントの名称整理が行われ、現行資料では **AX Scene Editor** という名称が使われます。  
  一方で、**2025.3.0以前のバージョンを継続利用する場合** や、旧資料・動画チュートリアルでは **Unreal Editor for Aximmetry** という旧名称が使われます。  
  本資料では **AX Scene Editor** を基本表記とし、必要に応じて旧名称 **Unreal Editor for Aximmetry** も併記します。

- **グリーンバック / Green Screen**  
  日本語本文では **グリーンバック** と表記します。  
  ただし、Aximmetry公式Learnや公式ページ名では **Green Screen** という表記が使われるため、リンク名や正式名称はそのまま残します。

- **トラッキングカメラ / Tracked Camera**  
  実際のカメラの位置や回転をトラッキングしながら、AximmetryでCGと合成していく考え方です。  
  本資料では、この前提で進むワークフローを主題として扱います。

- **ヴァーチャルカメラ / Virtual Camera**  
  トラッキング付きの実写カメラを前提とせず、ヴァーチャルカメラを操作して画作りを進める考え方です。  
  たとえば、定点のカメラ素材に対して疑似的にカメラワークを加えるような考え方もここに含まれます。  
  本資料では詳細は扱わず、トラッキングカメラと区別して考えます。

- **トラッキングカメラワークフロー / Tracked Camera Workflow**  
  本資料で主題として扱う、トラッキングカメラで行うグリーンバック制作の流れです。  
  業界全体の標準名称としてではなく、この資料内での呼び方として使います。

- **ライブ出力 / Live Output**  
  当日に安全に残すための出力・収録。

- **入力記録 / Input Recording**  
  後で再生確認やオフラインレンダリングを行うために、入力映像やトラッキングデータを記録しておく考え方です。

- **再生確認 / Playback**  
  本資料では、現場でのプレイバック確認と、記録した素材をあとで見直す確認の両方を含む言葉として使います。  

- **トラッキングキャリブレーション / Tracking Calibration**  
  トラッキング空間とヴァーチャル空間の基準を合わせる工程です。

- **レンズキャリブレーション / Lens Calibration**  
  レンズの光学特性を計測する工程です。  
  歪みや視点位置の変化などを扱い、チェッカーボードなどと専用ソフトウェアで算出することが多いです。  
  カメラや連携方式によっては、この工程を前提にしない運用もあります。

- **レンズプロファイル / Lens Profile**  
  レンズキャリブレーションの結果をまとめたデータです。  
  ズームやフォーカスに応じた補正に使われます。  
  レンズキャリブレーション済みの環境では、レンズごとにこのプロファイルを切り替えて運用することがあります。

- **ノーダルオフセット / Nodal Offset / Tracking Offset**  
  トラッキングデバイスと、実際のカメラの視点（レンズ / センサー側の基準）とのズレを補正する考え方です。  
  本資料では、Aximmetryでいう **Delta Head Transf** に近い概念として扱います。  
  記事や機材によって **Tracking Offset** と呼ばれることもありますが、ここでは同じ系統の補正としてまとめて扱います。

---

# 1. システム概要 / System Overview

## この章でつかむこと

最初に、システム全体の **役割分担** と **情報の流れ** を頭の中で接続することです。

**まず開く参照先**

- **Day1配布スライド**

## 最初に押さえること

ここで重要なのは、1つのソフトを覚えることではありません。  
**複数の信号が別経路で入り、Aximmetryで統合される** と理解することです。

### 3つの流れ

以下の機材名は、信号の流れを具体的にイメージしやすくするための例です。

1. **映像信号**  
   例: Canon C400 からの SDI 映像

2. **レンズ情報**  
   例: Canon C400 の CV Protocol などによる、ズームやフォーカス距離、歪みや絞りなどのレンズデータ

3. **トラッキング情報**  
   例: REtracker Bliss から来る位置・回転系のデータ

Aximmetry は、これらを **統合して、合成し、出力する場所** です。  
AX Scene Editor や Unreal は、主に **背景側を作る場所** です。

## たとえ話 / Mental Model

- **AX SceneやUnreal = 舞台美術を作る場所**
- **Aximmetry = 本番の舞台監督やスイッチャー、合成卓の役割を担う場所**
- **カメラ・レンズ・トラッカー = 現実世界の演者の情報源**

つまり、Unreal だけでも、Aximmetry だけでも成立しません。  
**背景の準備** と **現実入力の統合** の両方が必要です。

## チェックポイント

- [ ] カメラ、トラッカー、Aximmetry、AX Scene Editor の役割を言葉で説明できる
- [ ] 映像・レンズ情報・トラッキング情報の3系統を説明できる
- [ ] なぜそれらが別経路で来るのかを理解している
- [ ] Aximmetry が「背景を作る場所」ではなく「統合・合成・出力の場所」だと説明できる

## よくある誤解

- Aximmetry と Unreal の役割を同じものとして捉えてしまう
- 映像とレンズ情報も同じ経路で来ると思ってしまう
- トラッキングが来ていれば、それだけで成立していると思ってしまう

---

# 2. AX Scene / Unreal準備 / AX Scene / Unreal Setup

## この章でつかむこと

Aximmetryの画面へ入る前に、**背景側の受け皿** を整えることです。

**まず開く参照先**

- Aximmetry Learn: [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-unreal-editor/introduction-to-unreal-editor-for-aximmetry/)
- Aximmetry Learn: [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- Aximmetry Learn: [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)

## 最初に押さえること

Aximmetry側で映像やトラッキングを受けても、背景側の前提が崩れていると、後段で次のような問題に直面します。

- 背景スケールが不自然
- CGと実写の床が合わない
- シーン内の表示物やオブジェクトを、どう配置すべきか分かりにくい
- 何がAximmetry側の問題で、何がUnreal側の問題か分からない

> **補足**  
> つまり、Aximmetryに入る前に **背景側の最低限の成立条件** を押さえる必要があります。

## この章で押さえること

- AX Scene Editor は、Aximmetry向けのUnreal側編集環境である
- Aximmetry Camera 前提のシーン準備が必要である
- マップ、プロジェクト設定、プロジェクト変換、実行用データの書き出しなど、Aximmetry連携前提の準備がある

## 最低限の確認観点

### A. Project / Version
- Aximmetry と AX Scene Editor の対応バージョンを意識する
- 既存のUnrealプロジェクトを開く場合は、変換の扱いに注意する
- バージョン更新は元に戻せない場合があるため、コピーやバックアップを前提に扱う

### B. Project Settings
- Startup Map と Game Default Map を確認する
- Aximmetry向けに必要なプロジェクト設定を確認する
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
- [ ] シーンスケール、床、被写体位置の前提を見直せる

## よくある誤解

- Unreal で絵作りができていれば、そのままAximmetryでも使えると思ってしまう
- トラッキングワークフローなのに、カメラ前提を曖昧なまま進めてしまう
- Aximmetry側で頑張れば、シーン側の問題も吸収できると思ってしまう

---

# 3. システム同期とキャリブレーション / System Synchronization and Calibration

## この章でつかむこと

Tracking Calibration と Nodal Offset を、単なる数値調整ではなく、**現実とヴァーチャルを同期させるための工程** として理解することです。

**まず開く参照先**

- Day1配布スライド
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- REtracker Bliss: 配布された REtracker Bliss 日本語マニュアル

## 最初に押さえること

この資料では、キャリブレーションを早い段階で確認します。  
理由は、レンズプロファイルや外部レンズデータの前提がないと進みにくいからだけではありません。  
**全系統を同期するという概念** を、早めに理解してもらうためです。

## この章で押さえること

### Tracking Calibration
トラッキング空間とヴァーチャル側の基準を合わせる工程です。

### Nodal Offset
トラッキングデバイスと、実際のカメラの視点（レンズ / センサー側の基準）とのズレを補正する工程です。  
本資料では、Tracking Offset と呼ばれることがある補正も、この系統のものとしてまとめて扱います。

この2つは、後段のキーイングや再生確認の話とは別物に見えて、実はかなり深く関係しています。

- 背景位置が不自然
- パン・チルト・移動で違和感が出る
- 床が滑るように見える
- 「何となく合わない」

こうした問題の原因が、ここにあることがあります。

## たとえ話 / Mental Model

- **Calibration = 現実とヴァーチャルの定規を合わせる**
- **Nodal Offset = トラッカーの基準位置と、実際のカメラの視点を一致させる**

トラッキングデバイスは、CG上ではカメラの視点の基準として扱われます。  
しかし実際には、トラッキングデバイスをレンズの視点そのもの（瞳入射位置）に取り付けることはできません。  
そのため、取り付け位置と実際の見え方のズレを補正する必要があります。

トラッキングセンサーとカメラセンサーの位置関係は、どのカメラやトラッキング構成でも初回測定が必要です。  
そのうえで、レンズ側をどう扱うかは構成によって異なります。  
Canon C400 では、瞳入射位置を含む補正情報が CV Metadata によって更新されるため、通常のレンズキャリブレーションを前提にしない運用が可能です。  
そのため、ズームやレンズ交換のたびに、オペレーターがレンズプロファイルを切り替えたり、レンズキャリブレーションをやり直したりする負担を減らせます。  
C400 以外でも、レンズキャリブレーション済みであれば、毎回すべてを手動で入れ直すのではなく、対応するレンズプロファイルを切り替えて運用するのが一般的です。

補足:

- Aximmetry公式Learn では、この系統の補正は **Delta Head Transf** として説明されています
- Tracking Offset という表現が使われる場合も、ここでは同じ系統の補正として扱います
- レンズキャリブレーションとレンズプロファイルは、レンズの光学特性を計測し、プロファイル化する考え方です
- Canon C400 では、瞳入射位置を含むレンズ側情報が CV Metadata により更新されるため、通常のレンズキャリブレーション工程を前提にしない運用ができます
- Nodal Offset は、それらを踏まえて最終的な見え方を合わせるための補正として理解すると入りやすいです

## 後続工程とのつながり

- ライブ合成の自然さに直結する
- 再生確認やトラブルシューティングでも、原因がここに戻ることがある
- ズームや同期、床が滑るような違和感を、単なる遅延の問題と決めつけない

## チェックポイント

- [ ] Tracking Calibration の役割を説明できる
- [ ] Nodal Offset の役割を説明できる
- [ ] なぜこの理解を早い段階で持つのか説明できる
- [ ] 背景ズレ・床が滑るような違和感がここに起因しうると理解している

## よくある誤解

- キャリブレーションを、設定が面倒なだけの工程だと見てしまう
- Nodal Offset を、最後に詰める微調整だと思ってしまう
- 違和感の原因を、すべて遅延やキーイングに寄せてしまう

> **補足**  
> Bliss については、英語動画だけで理解を進めるのは日本語話者には負荷が高いため、まずは **配布された REtracker Bliss 日本語マニュアル** を主参照にするのが適切です。

---

# 4. トラッキングカメラワークフロー / Tracked Camera Workflow

## この章でつかむこと

本資料の主題である、**トラッキングカメラで行うグリーンバック制作の流れ** を理解することです。

**まず開く参照先**

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- Aximmetry Learn: [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

## 最初に押さえること

この章でいうワークフローは、次の流れです。

- トラッキングカメラを使う
- グリーンバック制作を行う
- Aximmetryで映像・トラッキング・レンズ情報を受ける
- 同期を取り、合成し、出力する

ここでは、ARやLED、トラッキングなしのヴァーチャルカメラ運用の詳細は扱いません。

## 流れの全体像

1. 背景側の準備
2. Aximmetry 側で映像・トラッキング・レンズ情報を受ける
3. キャリブレーションとレンズ側補正の前提を踏まえて同期を確認する
4. トラッキング遅延、ズーム遅延、タイムコード同期を確認する
5. キーイングを行う
6. ライブ出力を出す
7. レコーダーへ安全に残す

## I/O設定の基本順

Aximmetry 側では、まず INPUTS で通常の進め方を成立させます。

### 基本順序
1. Camera Device
2. Tracking Device
3. レンズとキャリブレーションの前提確認
4. Tracking Delay
5. Zoom Delay
6. Timecode Sync と Zoom Timecode Sync
7. Detect Tracking Delay と Detect Zoom Delay

## この章で押さえること

- まず **来ているか** を確認する
- その後で **合っているか** を確認する
- Detect Tracking Delay と Detect Zoom Delay は、代替手段ではなく標準的な確認フローの一部である

## たとえ話 / Mental Model

この章は、**配線確認 → 同期確認 → 本番成立** の章です。  
いきなりキーイングや出力に進むのではなく、まず信号の成立を確認します。

## チェックポイント

- [ ] トラッキングカメラワークフローの流れを説明できる
- [ ] カメラ、トラッキング、レンズの順で前提確認できる
- [ ] 「来ているか」と「合っているか」を分けて考えられる
- [ ] Detect Tracking Delay と Detect Zoom Delay が通常フローの一部だと理解している

## よくある誤解

- 映像が来ているので、全体も成立していると思ってしまう
- トラッキングとレンズ情報の確認が曖昧なまま進めてしまう
- 遅延検出を、トラブル時だけ使う最後の手段だと誤解する

---

# 5. キーイングとライブ出力 / Keying and Live Output

## この章でつかむこと

キーイングを「ソフトのつまみ調整」だけで捉えず、**素材条件 → キーヤー調整 → 最終出力確認** の順番で理解することです。

**まず開く参照先**

- Aximmetry Learn: [Keying Setup (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/keying-setup-tracked-camera/)
- Aximmetry Learn: [Keying](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/keying/keying/)

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
- [ ] ライブ出力、レコーダー、当日収録の目的を説明できる

## よくある誤解

- ソフトウェアキーヤーだけで解決できると思ってしまう
- モニターモードと最終出力を同じものとして見てしまう
- 当日収録と Input Recording の目的を同じものだと思ってしまう

---

# 6. 再生・記録・オフライン確認 / Replay, Recording, and Offline Review

## この章でつかむこと

当日収録と、後工程用の記録と再生を混同せず、**何を残し、何に使うのか** を理解することです。

**まず開く参照先**

- Aximmetry Learn: [How to Record Camera Tracking Data](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/video/recording/how-to-record-camera-tracking-data/)
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

## 最初に押さえること

この章で重要なのは、次の2つを分けて考えることです。

- 当日に安全に残すための収録
- 後で再生確認やオフラインレンダリングにつなぐための記録

## この章のキーワード

### 当日収録 / Live Rec
Aximmetry の合成映像を外部レコーダーに送り、本番中に安全に残す考え方。

### Input Recording
後でオフラインレンダリングや再生確認を行うために、**生のカメラ入力映像** と **生のトラッキングデータ** を残す考え方。

### Use Input TC
カメラからのタイムコードを使って、あとで照合や再生確認、後工程に生かす考え方。

### Tracking Only
トラッキングを主目的として残したい時の考え方。

### Playback / Replay
事前収録した映像とトラッキングデータを使って、後から再生確認する流れ。

## 使いどころ

- そのときの設定を見直す
- 違和感の原因を切り分ける
- 制作ごとの改善点を見つける
- 高画質素材とトラッキングをあとで合わせる
- オフラインレンダリングや後工程につなぐ

## 見るポイント

- 背景とのなじみ
- トラッキングの違和感
- ズームや同期の違和感
- キーイングの破綻
- 収録時に見逃した問題

## たとえ話 / Mental Model

- **当日収録 = その日の完成料理を残す**
- **Input Recording = 後で別の調理ができるよう、素材を残す**

この違いが分かると、記録まわりの混線がかなり減ります。

## チェックポイント

- [ ] 当日収録と Input Recording の目的の違いを説明できる
- [ ] Use Input TC の意味を説明できる
- [ ] 再生確認が何のためにあるか説明できる
- [ ] オフライン確認で何を見るか思い出せる

## よくある誤解

- 合成映像を録ることと、トラッキングデータを残すことを同じだと思ってしまう
- Replay を単なる再生機能として見てしまう
- タイムコードを、なくても何とかなるものだと軽く見てしまう

---

# 7. 症状別トラブルシューティング / Troubleshooting by Symptom

## この章でつかむこと

問題が起きた時に、**症状 → 見る場所 → 原因カテゴリ → 戻る順番** で考えられるようにすることです。

**まず開く参照先**

- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)
- REtracker Bliss: 配布された REtracker Bliss 日本語マニュアル

## 基本姿勢

いきなり全部を疑わず、**症状に応じて見る場所を絞る** ことが重要です。

---

## 症状A: トラッカーが来ない

### まず見る場所
- Tracking Device
- デバイス接続状態
- Bliss 側動作状態
- ネットワークと接続経路

### まず疑うこと
- トラッカー自体が動いていない
- Aximmetry 側のマッピングが違う
- Bliss 側の出力設定が違う
- ネットワーク疎通や接続が不安定

### 戻る順番
1. Bliss 側の状態確認
2. Host PC との接続確認
3. Aximmetry側で Tracking Device を確認
4. キャリブレーションや補正前提の確認

### 開く資料
- **配布された REtracker Bliss 日本語マニュアル**
- Aximmetry Learn: [Inputs (Tracked Camera)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/inputs-tracked-camera/)

---

## 症状B: レンズ情報 / CV Protocol が来ない

### まず見る場所
- External Lens Data
- Camera 側 CV Protocol 設定
- Ethernet 系の接続

### まず疑うこと
- 映像は来ていてもレンズデータは別経路なので未成立
- カメラ側設定の見落とし
- Aximmetry 側の受け口が違う

### 戻る順番
1. カメラ側のプロトコル設定
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
- レンズ側補正の前提

### 戻る順番
1. レンズ情報の到着確認
2. zoom delay 確認
3. zoom timecode sync 確認
4. レンズ側補正の前提確認

---

## 症状D: AUTO で映像が来ない

### まず見る場所
- Camera Mode
- 解像度とfps
- キャプチャーカード側の認識

### まず疑うこと
- 古いキャプチャーカードや条件によって AUTO がうまく効かない
- 手動での解像度・fps指定が必要

### 戻る順番
1. ケーブルとキャプチャー側の確認
2. Camera Mode を見直す
3. 手動で解像度とfpsを指定
4. 他入力と切り分ける

---

## 症状E: タイムコードが噛み合わない

### まず見る場所
- Timecode Sync
- Zoom Timecode Sync
- Use Input TC
- マスター側の前提

### まず疑うこと
- 同じタイムコードを見ていない
- Use Input TC を使う前提が崩れている
- 当日収録とオフライン確認の前提が混ざっている

### 戻る順番
1. マスターの確認
2. カメラ由来タイムコードの確認
3. Aximmetry側の同期設定を確認
4. 記録と再生の目的を再確認

---

## たとえ話 / Mental Model

トラブルシューティングは、**暗闇で全部を探す作業** ではありません。  
**症状から部屋を絞って探す作業** です。

## チェックポイント

- [ ] 症状から見る場所を絞れる
- [ ] 全部を同時に疑わず、順番に戻れる
- [ ] 問題がキャリブレーション起因か、信号起因か、同期起因かを切り分けようとできる

---

# 8. 実践的な発展項目 / Practical Advanced Topics

## この章でつかむこと

本流であるトラッキングカメラでのグリーンバックワークフローを理解した上で、**次に何を広げたいか、あるいは別のProductionタイプへ進みたいかに応じて、追加学習の入口を選べる** と知ることです。

## この章の位置づけ

ここはメインワークフローを順番に復習する章ではなく、**やりたいこと別に、次に開く公式Learnを選ぶための章** です。  
トレーニングの本流を押さえたあとに、**自分の役割や興味に近い方向へ発展するための入口** として使います。  
また、本文では詳しく扱っていない **Virtual Camera / LED Wall / AR といった別のProductionタイプへ進む入口** もここで拾えるようにします。  
最初から全部を追う必要はなく、今の担当に近い項目から広げていけば十分です。

## やりたいこと別の入口

### Unreal Engine / AX Scene Editor側でインタラクションを広げたい人へ

**向いている人**

Unreal 側でオブジェクトや演出を動かしたい人、Aximmetry から値や映像を渡してインタラクションを増やしたい人、AX Scene Editor 側の表現を一歩進めたい人。

**まず開く参照先**

- [Interactive Editing with Live Sync](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-ax-scene-editor/interactive-editing-with-live-sync/)
- [Additional Control with Blueprints](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-ax-scene-editor/additional-control-with-blueprints/)

**つながる既存項目**

- Virtual Screen Asset
- Get Aximmetry Video
- simple Transformation

### AximmetryでGUI / Control Boardを作りたい人へ

**向いている人**

オペレーターが触りやすい画面を作りたい人、Flow Editor を直接見せずに操作用のパネルを整理したい人、現場向けのUIを整えたい人。

**まず開く参照先**

- [Basics of the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/starting-with-aximmetry/aximmetry-composer/basics-of-the-flow-editor/)
- [Special Compound: Control Board](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-compound-control-board/)
- [Special Compound: Pin Collector](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-compound-pin-collector/)
- [Special Pin Names](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-pin-names/)

### 外部コントローラー / Trigger運用を広げたい人へ

**向いている人**

現場で物理ボタンやダイヤルから操作したい人、オペレーター用のTrigger系導線を整えたい人、Stream Deck や Loupedeck、MIDI などを Aximmetry に結びつけたい人。

**まず開く参照先**

- [Controllers](https://aximmetry.com/learn/virtual-production-workflow/supported-hardware/controllers/controllers/)
- [Using Elgato Stream Deck to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-elgato-stream-deck-to-control-a-scene/)
- [Using Loupedeck consoles / Razer Stream Controller to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-loupedeck-consoles-razer-stream-controller-to-control-a-scene/)
- [Using MIDI with Aximmetry](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-midi-with-aximmetry/)
- [OSC In-, and Output Setup](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/osc-in-and-output-setup/)

### Aximmetry側で制御や自動化を広げたい人へ

**向いている人**

Flow Editor の考え方を理解したい人、制御ロジックを組みたい人、将来的にオペレーション自動化まで広げたい人。

**まず開く参照先**

- [Introduction to the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/introduction-to-the-flow-editor/)
- [Playlists](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/automation/playlists/)
- [Sequencer and Sequence Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/sequencing/sequencer-and-sequence-editor/)

### システム遅延や安定性を深く理解したい人へ

**向いている人**

トラッキング遅延や同期の先にある、Aximmetry 全体の遅延設計や安定性まで理解したい人、トラブル時に原因の切り分け精度を上げたい人。

**まず開く参照先**

- [In-to-Out Latency](https://aximmetry.com/learn/virtual-production-workflow/inner-workings-of-aximmetry/in-to-out-latency/)
- [Rendering Settings](https://aximmetry.com/learn/virtual-production-workflow/inner-workings-of-aximmetry/rendering-settings/)

### Camera Compound間の受け渡しや内部制御を理解したい人へ

**向いている人**

camera compound の中で値をどう渡すかを知りたい人、既存 compound を読んだり拡張したりするための足場を作りたい人、内部構造の理解を深めたい人。

**まず開く参照先**

- [Compound](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/compound/)
- [Transmit Tunnels in Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/transmit-tunnels-in-camera-compounds/)
- [Introduction to the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/introduction-to-the-flow-editor/)

### Virtual Camera / LED Wall / AR など別のProductionタイプを学びたい人へ

**向いている人**

トラッキングカメラのグリーンバック以外の運用も把握したい人、固定カメラ中心のVirtual Cameraを見たい人、LED WallやARの入口を整理して見たい人。

**まず開く参照先**

- [Stationary or Moving Cameras?](https://aximmetry.com/learn/virtual-production-workflow/different-studios-for-virtual-production/stationary-or-moving-cameras/)
- [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- [Table of Contents (LED Wall Production)](https://aximmetry.com/learn/virtual-production-workflow/led-wall-production/table-of-contents-led-wall-production/)
- [Introduction to AR Production](https://aximmetry.com/learn/virtual-production-workflow/ar-production/introduction-to-ar-production/)

**見分け方の目安**

- 固定カメラ中心で進めたいなら Virtual Camera Workflow
- LEDに背景を出して撮影したいなら LED Wall Production
- 実写映像の上にCG要素を重ねたいなら AR Production

## この章で押さえること

- 発展項目には、Unreal連携、GUI / Control Board作成、外部コントローラー / Trigger運用、Flow Editor / 自動化、遅延理解、Compound内部理解など複数の方向がある
- 本流の外側には、Virtual Camera / LED Wall / AR といった別のProductionタイプの入口もある
- 第8章は、やりたいこと別に次の参照先を選ぶための章である
- 本流の外側には、現在本文で詳しく扱っていない追加学習の入口がある
- 目的に応じて学ぶ方向を選べばよく、最初から全部を追う必要はない

## チェックポイント

- [ ] この章が、順番に復習する章ではなく、やりたいこと別に参照先を引く章だと理解している
- [ ] Unreal / AX Scene Editor側の連携を深めたい時の入口を説明できる
- [ ] AximmetryでGUI / Control Boardを作りたい時の入口を説明できる
- [ ] Stream Deck / Loupedeck / MIDI などの外部コントローラー導入の入口を説明できる
- [ ] Flow Editor / 自動化 / 遅延理解 / Compound間制御の入口を説明できる
- [ ] Virtual Camera / LED Wall / AR へ進みたい時の入口を説明できる

> **注意**  
> これらの発展項目はバージョンや運用構成の影響を受けやすいため、本文では位置づけと学習方向に集中し、具体的な手順は公式Learnを参照してください。

---

# 9. 目的別索引 / Purpose Index

> 何をしたいかから引けるように整理しています。  
> 同じページが複数の目的にまたがる場合は、探しやすさを優先して重複して載せています。

## まず全体像をつかみたい
- [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- [Tracked Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/tracked-camera-workflow/tracked-camera-compounds/)

## 背景側の準備を確認したい
- [Introduction to AX Scene Editor](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-ax-scene-editor/introduction-to-ax-scene-editor/)
- [Preparing the Unreal Project](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-for-aximmetry-de/preparing-the-unreal-project/)
- [Unreal Scene Setup (Green Screen)](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/unreal-scene-setup-green-scre)
- [Aximmetry Render Components](https://aximmetry.com/learn/virtual-production-workflow/which-aximmetry-is-right-for-you/aximmetry-render-components/)

## 入力と同期 / Inputs / Sync を確認したい
- [Mapping Devices](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/mapping-devices/)
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

## 別のProductionタイプを確認したい
**Virtual Camera Workflow を見たい:**

- [Stationary or Moving Cameras?](https://aximmetry.com/learn/virtual-production-workflow/different-studios-for-virtual-production/stationary-or-moving-cameras/)
- [Introduction to Green Screen Production](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/introduction-to-green-screen-production/)
- [Virtual Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/green-screen-production/virtual-camera-workflow/virtual-camera-compounds/)

**LED Wall Production を見たい:**

- [Introduction to LED Wall Production](https://aximmetry.com/learn/virtual-production-workflow/led-wall-production/introduction-to-led-wall-production/)
- [Table of Contents (LED Wall Production)](https://aximmetry.com/learn/virtual-production-workflow/led-wall-production/table-of-contents-led-wall-production/)

**AR Production を見たい:**

- [Introduction to AR Production](https://aximmetry.com/learn/virtual-production-workflow/ar-production/introduction-to-ar-production/)
- [AR Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/ar-production/ar-camera-compounds/)

## 外部コントローラー / Trigger運用を確認したい
**Stream Deck を使いたい:**

- [Using Elgato Stream Deck to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-elgato-stream-deck-to-control-a-scene/)

**Loupedeck / Razer Stream Controller を使いたい:**

- [Using Loupedeck consoles / Razer Stream Controller to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-loupedeck-consoles-razer-stream-controller-to-control-a-scene/)

**MIDI を使いたい:**

- [Using MIDI with Aximmetry](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-midi-with-aximmetry/)

**OSC / ネットワーク経由のTriggerを使いたい:**

- [OSC In-, and Output Setup](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/osc-in-and-output-setup/)
- [OSC Messages in Aximmetry](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/osc-messages-in-aximmetry/)

## 発展項目を確認したい
**Unreal Engine / AX Scene Editor側でインタラクションを広げたい:**

- [Interactive Editing with Live Sync](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-ax-scene-editor/interactive-editing-with-live-sync/)
- [Additional Control with Blueprints](https://aximmetry.com/learn/virtual-production-workflow/obtaining-graphics-and-virtual-assets/creating-content-in-ax-scene-editor/additional-control-with-blueprints/)

**AximmetryでGUI / Control Boardを作りたい:**

- [Basics of the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/starting-with-aximmetry/aximmetry-composer/basics-of-the-flow-editor/)
- [Special Compound: Control Board](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-compound-control-board/)
- [Special Compound: Pin Collector](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-compound-pin-collector/)
- [Special Pin Names](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/special-pin-names/)

**外部コントローラー / Trigger運用を広げたい:**

- [Controllers](https://aximmetry.com/learn/virtual-production-workflow/supported-hardware/controllers/controllers/)
- [Using Elgato Stream Deck to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-elgato-stream-deck-to-control-a-scene/)
- [Using Loupedeck consoles / Razer Stream Controller to control a scene](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-loupedeck-consoles-razer-stream-controller-to-control-a-scene/)
- [Using MIDI with Aximmetry](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/using-midi-with-aximmetry/)
- [OSC In-, and Output Setup](https://aximmetry.com/learn/virtual-production-workflow/setting-up-inputs-outputs-for-virtual-production/external-controllers/osc-in-and-output-setup/)

**Aximmetry側で制御や自動化を広げたい:**

- [Introduction to the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/introduction-to-the-flow-editor/)
- [Playlists](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/automation/playlists/)
- [Sequencer and Sequence Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/sequencing/sequencer-and-sequence-editor/)

**システム遅延や安定性を深く理解したい:**

- [In-to-Out Latency](https://aximmetry.com/learn/virtual-production-workflow/inner-workings-of-aximmetry/in-to-out-latency/)
- [Rendering Settings](https://aximmetry.com/learn/virtual-production-workflow/inner-workings-of-aximmetry/rendering-settings/)

**Camera Compound間の受け渡しや内部制御を理解したい:**

- [Compound](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/compound/)
- [Transmit Tunnels in Camera Compounds](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/transmit-tunnels-in-camera-compounds/)
- [Introduction to the Flow Editor](https://aximmetry.com/learn/virtual-production-workflow/scripting-in-aximmetry/flow-editor/introduction-to-the-flow-editor/)

## REtracker Bliss を確認したい

### 推奨する参照順
1. **配布された REtracker Bliss 日本語マニュアル**
2. 公式製品ページ

### 公式ページ
- [REtracker BLISS product page](https://www.retracker.co/retracker-bliss)

> **補足**  
> 日本語話者にとっては、Bliss の英語動画だけで再現するのは難しいため、まずは **配布された REtracker Bliss 日本語マニュアル** を主参照にするのが望ましいです。

---

# 最終確認チェックリスト / Final Review Checklist

- [ ] システム全体の3系統を説明できる
- [ ] 背景側の最低限準備を説明できる
- [ ] キャリブレーションと Nodal Offset の役割を説明できる
- [ ] トラッキングカメラワークフローを説明できる
- [ ] キーイングは物理条件が先だと説明できる
- [ ] 当日収録と Input Recording の違いを説明できる
- [ ] 再生確認とオフライン確認の目的を説明できる
- [ ] 症状から見る場所を絞って考えられる
- [ ] 発展項目とメインワークフローを混同していない

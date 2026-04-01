# Instructor_RunSheet_Day3.md

# 講師用進行台本 Day 3
## 記録データを活かし、BPで広げる
(Replay / Offline Workflow / BP Basics / Troubleshooting)

※この資料は講師用です。受講者配布を前提としません。  
※本編の主教材は Aximmetry 公式 Learn と GUI です。  
※Slides は最小構成（Title / Goal / Agenda）のみ使用します。  
※Day 3 は **再生確認・オフラインレンダリング・トラブル対応・BP入門** を扱う日です。  
※BP は必須ですが、理論講義ではなく **1つの実務レシピを再現する** 位置づけです。

---

## 1. Day 3 のゴール
- 記録した素材を使った再生確認の流れを理解してもらう
- Day 2 のライブ収録と、Day 3 の後工程用収録の違いを理解してもらう
- trouble 時に「どこを見るか」「どこへ戻るか」の基本を理解してもらう
- Aximmetry → Unreal の practical な BP レシピを1本体験してもらう
- 最後に、Day 3 の flow を通して確認してもらう

---

## 2. Day 3 の基本方針
- 最初に Day2 と Day3 の役割の違いを明確にする
- Slides ではゴール / アジェンダのみ見せる
- その後は公式 Learn と GUI を主に使う
- Day 3 は「記録したものを活かす日」として位置づける
- トラブル対応は症状ベースで進める
- BP は必須だが、deep Blueprint には入らない
- 受講者には「何をどの順で見るか」「どこへ戻るか」を残す

---

## 3. 使用する Slides
### Day3_Slides_Minimum.md
#### Slide 1
Day 3  
記録データを活かし、BPで広げる  
(Replay / Offline Workflow / BP Basics / Troubleshooting)

#### Slide 2
Goal
- 記録した素材を使った再生確認の流れを理解する
- 後工程用収録の考え方を理解する
- BPでバーチャルスクリーンを扱う基本を理解する
- トラブル時の戻り方の基本を理解する

#### Slide 3
Agenda
1. 再生確認 (Replay / Playback)
2. 後工程の流れ (Offline Workflow)
3. BP入門：バーチャルスクリーンの基本
4. トラブル対応 (Troubleshooting)
5. ハンズオン (Hands-on)

---

## 4. 事前に開いておくもの
### Aximmetry Learn
- Tracked Camera Inputs
- How to Record Camera Tracking Data
- Additional Control with Blueprints
- Virtual Screens in Unreal from Aximmetry

### ソフト / データ
- Aximmetry Composer
- Unreal / AX Scene Editor
- Day2 で使ったプロジェクト
- 再生確認に使う recorded 素材
- BP 用の Unreal project / scene

### 配布資料
- Day2_Review_CheatSheet
- Day3_Review_CheatSheet
- Keying_CheatSheet

---

## 5. 時間割
### 12:00–12:15
オープニング  
ゴール / アジェンダ提示  
Day2 → Day3 の位置づけ共有

### 12:15–13:00
再生確認 (Replay / Playback)

### 13:00–13:45
オフラインレンダリング / 後工程の流れ

### 13:45–13:55
休憩

### 13:55–14:45
BP入門：バーチャルスクリーンの基本

### 14:45–14:55
休憩 / 切り替え

### 14:55–15:45
トラブル対応 (Troubleshooting)

### 15:45–17:10
ハンズオン（ガイド付き）

### 17:10–18:00
まとめ / 質疑 / 全体振り返り

---

## 6. セクション別進行

# 6-1. オープニング
## 目的
- Day 3 の主役を明確にする
- Day 2 と Day 3 の役割の違いを作る
- 今日は「記録したものを活かす日」だと伝える

## 言うこと
- Day 2 は「通常の進め方で、背景合成とライブ収録を成立させる日」
- Day 3 は「記録したものを使って、振り返り・復旧・拡張する日」
- BP は今日の必須項目だが、深い理論ではなく recipe として扱う

## 見せるもの
- Slide 1
- Slide 2
- Slide 3

---

# 6-2. 再生確認
## 目的
- replay / playback の役割を理解してもらう
- live がなくても review できることを理解してもらう
- production ごとの改善ループをイメージしてもらう

## 開く Learn
- Tracked Camera Inputs（internal input / prerecorded input 周辺）

## 強調すること
- prerecorded video と tracking data を internal input として扱える
- replay は「本番の代わり」ではなく「振り返りと改善の入口」
- 再生確認で見るべきものは、背景とのなじみ、tracking、zoom / sync、keying

## GUI で見せる箇所
- internal input の場所
- replay の入口
- recorded 素材の確認
- live との違い

## 受講者への問い
- replay で最初に何を見ますか？
- live の時と replay の時で、見たいポイントは同じですか？
- なぜ replay が必要だと思いますか？

---

# 6-3. オフラインレンダリング / 後工程の流れ
## 目的
- Day 2 のライブ収録と、Day 3 の後工程用収録の違いを明確にする
- Input Recording / Use Input TC / Tracking Only の位置づけを理解してもらう

## 開く Learn
- How to Record Camera Tracking Data

## 強調すること
- Day 2 の rec は「当日に安全に残す」
- Day 3 の recording は「後で再利用するために残す」
- Input Recording は offline rendering / replay 用
- Use Input TC は timecode 対応づけのため
- Tracking Only は後工程との役割分担を作る時に有効

## GUI で見せる箇所
- recording 関連設定
- Use Input TC
- Tracking Only
- recorded data の扱い

## 受講者への問い
- Day 2 の live rec と Day 3 の recording は何が違いますか？
- 後工程で何を再利用したいかで、残すべきものは変わりますか？

## 講師メモ
- NLE の操作講義にはしない
- FBX や外部3D post の深掘りには行かない
- workflow mindset として説明する

---

# 6-4. BP入門：バーチャルスクリーンの基本
## 目的
- Aximmetry → Unreal の practical な拡張を1つ体験してもらう
- BP を「理論」ではなく「実務レシピ」として理解してもらう

## 開く Learn
- Virtual Screens in Unreal from Aximmetry
- Additional Control with Blueprints

## 必須レシピ
1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

## 強調すること
- バーチャルスクリーンは背景合成そのものではなく、Unreal 側 object interaction の例
- Aximmetry から Unreal 側へ映像や変形を渡せる
- 今日は deep Blueprint ではなく、1 recipe を再現する

## GUI で見せる箇所
- Virtual Screen Asset
- Level Blueprint の最小構成
- Get Aximmetry Video
- simple Transformation の接続
- 必要なら object を Movable にする話

## 受講者への問い
- これは背景そのものですか、拡張要素ですか？
- Aximmetry から Unreal に何を渡していますか？
- 今日のレシピで覚えるべき3要素は何ですか？

## 講師メモ
- Trigger / animation / multi-object 制御には広げない
- 「できることの入口」として見せる
- corporate use-case と結びつけると入りやすい

---

# 6-5. トラブル対応
## 目的
- 問題が起きた時の考え方を症状ベースで残す
- fallback を「裏技」ではなく、戻るための手順として理解してもらう

## 開く Learn
- Tracked Camera Inputs
- 必要なら Day1_Review_CheatSheet / Day2_Review_CheatSheet も参照

## 基本の考え方
症状 → 見る場所 → 原因カテゴリ → 戻る順番

## 扱う代表症状
- tracker が来ない
- CV Protocol が来ない
- zoom だけ合わない
- timecode が噛み合わない
- AUTO で映像が来ない

## まず見る場所
- Camera Device
- Tracking Device
- External Lens Data
- Timecode Sync
- manual resolution / fps
- manual override
- fixed/default values

## 強調すること
- Detect Tracking Delay / Detect Zoom Delay は fallback ではなく usual path
- いきなり全部を疑わない
- 症状に応じて見る場所を絞る
- Day1 側に原因がある可能性もある

## 受講者への問い
- いま起きている症状は何ですか？
- まずどこを見るべきですか？
- 入力、同期、背景、keying、どのカテゴリの問題ですか？

---

# 6-6. ハンズオン
## 目的
- Day 3 の flow を口頭で説明できる状態にする
- replay / recover / extend の流れを共有PCで回す

## 形式
- 1PC 共有
- ガイド付きハンズオン

## 役割
- Operator
- Navigator
- Checker
- Observer

## 回す順
1. replay / playback
2. review
3. BP recipe 確認
4. trouble を想定した確認
5. 戻る場所の確認

## 受講者に残したいこと
- replay の目的が言える
- live rec と後工程用 recording の違いが言える
- symptom-based に戻る場所が言える
- BP レシピの3要素が言える

---

# 6-7. まとめ
## 最後に確認すること
- Day 2 と Day 3 の役割の違いが分かるか
- replay / playback の役割が分かるか
- 後工程用収録の考え方が分かるか
- trouble の時に「どこを見るか」が分かるか
- BP レシピの3要素が分かるか

## 全体の締め
- Day 1 は土台
- Day 2 は通常の進め方
- Day 3 は振り返り・復旧・拡張

---

## 7. 時間が押した時の短縮候補
### 最後まで残す
- replay / playback の位置づけ
- Day 2 rec と Day 3 recording の違い
- BP レシピの3要素
- トラブル対応の症状ベース思考
- ハンズオンの通し確認

### 短縮候補
- recorded 素材の細かな説明
- post workflow の補足
- BP の補足説明
- トラブル対応で扱う症状の数

---

## 8. 講師用メモ
- Day 3 は「記録したものを使って強くなる日」
- トラブル対応は menu ではなく症状ベースで見せる
- BP は必須だが、理論ではなく recipe
- Slides は最小限、Learn と GUI を主役にする
- 受講者には「どこへ戻るか」を残す
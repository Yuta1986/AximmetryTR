# Day3_Review_CheatSheet.md

# Day 3 Review Cheat Sheet
## Day 3 の復習用シート

※この資料は、Day 3 の内容をあとから思い出しやすくするための復習用資料です。  
※実際の運用は、案件の目的・機材構成・収録条件に合わせて調整してください。  
※Day 3 は **再生確認・後工程用収録・トラブル切り分け・BP レシピ** を扱う日です。  
※Troubleshooting の詳細は、このシートと講師用資料に持たせます。

---

## 1. Day 3 の目的
Day 3 の目的は、

**記録した素材を使って再生確認し、  
後工程用収録の考え方を理解し、  
トラブル時の戻り方と BP レシピの基本を押さえること**

です。

---

## 2. Day 3 の全体フロー
1. Day 2 を短く振り返る
2. replay / playback を理解する
3. 後工程用収録の考え方を理解する
4. トラブルの切り分けを理解する
5. BP レシピを体験する
6. 最後に通しで確認する

---

## 3. Day 2 と Day 3 の役割の違い
### Day 2
- 通常の進め方で背景合成と当日収録を成立させる
- live output を安全に残す

### Day 3
- 記録したものを使って再生確認する
- 後工程での使い方を考える
- trouble の時にどこへ戻るかを理解する
- Unreal 側への practical な拡張を1つ体験する

### Day 3 で理解したいこと
**Day 2 が live、Day 3 が review / recover / extend**

---

## 4. Replay / Playback
### 何をやるか
- prerecorded video と tracking data を使って再生確認する
- live がない状態でも確認・振り返りができるようにする

### 何のために使うか
- 当日の setup を見直す
- 違和感の原因を切り分ける
- production ごとに改善点を見つける

### 何を見るか
- 背景とのなじみ
- tracking の違和感
- zoom / sync の違和感
- keying の破綻
- 当日見逃した問題

### 覚え方
**replay は、講習後や本番後に戻れる確認ループ**

---

## 5. 後工程用収録の考え方
### Day 2 の当日収録との違い
- 当日収録 = 当日に安全に残すための収録
- 後工程用収録 = 後で再生確認・振り返り・再レンダリングに使う収録

### Day 3 で押さえること
- Input Recording
- Use Input TC
- Tracking Only
- 後工程で何を再利用したいかを意識する

### 重要ポイント
- Day 2 の rec と Day 3 の recording は目的が違う
- Day 3 では「あとで使うために何を残すか」を考える

---

## 6. Troubleshooting の基本
### 基本の考え方
問題が起きた時は、

**症状 → 見る場所 → 原因カテゴリ → 戻る順番**

で確認する。

### 先に理解しておくこと
- Day 2 は通常の進め方を成立させる日
- Day 3 は trouble の時に戻る場所を理解する日
- `Detect Tracking Delay` / `Detect Zoom Delay` は fallback ではなく、通常の進め方の一部

---

## 7. 代表的な症状と見る場所
### 症状
- tracker が来ない
- CV Protocol が来ない
- zoom だけ合わない
- timecode が噛み合わない
- AUTO で映像が来ない

### まず見る場所
- Camera Device
- Tracking Device
- External Lens Data
- Timecode Sync
- manual resolution / fps
- manual override
- fixed/default values

### 覚え方
**いきなり全部を疑わず、症状に応じて見る場所を絞る**

---

## 8. BP レシピ
### Day 3 の必須レシピ
1. Virtual Screen Asset
2. Get Aximmetry Video
3. simple Transformation

### このレシピで理解したいこと
- Aximmetry は live composite だけで終わらない
- Unreal 内 object にも少し介入できる
- ただし、深い Blueprint 理論ではなく practical recipe として理解する

### ここでの位置づけ
- 背景合成そのものではなく、Unreal 側 object interaction の例
- corporate production などで応用しやすい発展項目

---

## 9. Final Hands-on の意味
### 何をやるか
- replay
- review
- diagnose
- fallback の判断
- BP recipe の確認

### 目的
- Day 3 の内容を、単なる知識ではなく flow としてつなげる
- 通常の進め方と trouble 時の戻り方を一緒に理解する

---

## 10. Day 3 を一言でまとめると
**記録したものを使って、振り返り・復旧・拡張する日**

---

## 11. 復習チェック
- [ ] replay / playback の目的を説明できる
- [ ] 当日収録と後工程用収録の目的の違いを説明できる
- [ ] Input Recording / Use Input TC / Tracking Only の役割を大まかに説明できる
- [ ] trouble が起きた時に「症状 → 見る場所 → 戻る順番」で考える意味を説明できる
- [ ] 代表的な症状と、まず見る場所を思い出せる
- [ ] BP レシピの3要素を説明できる
- [ ] Day 3 のゴールである「振り返り・復旧・拡張」が確認できたか
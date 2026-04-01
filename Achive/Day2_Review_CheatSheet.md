# Day 2 Review Cheat Sheet
## Day 2 の復習用シート

※この資料は、Day 2 の内容をあとから思い出しやすくするための復習用資料です。  
※実際の運用は、案件の目的・機材構成・収録条件に合わせて調整してください。  
※Day 2 は **通常の進め方（normal path）を成立させる日** です。  
※トラブル対応や fallback の詳細は Day 3 で扱います。

---

## 1. Day 2 の目的
Day 2 の目的は、

**Tracked Green Screen の通常の進め方で、  
背景合成と当日収録を成立させること**

です。

---

## 2. Day 2 の全体像
Day 2 では、次の流れを扱いました。

1. Unreal Engine 側で背景（virtual set）を準備する  
2. Aximmetry 側で映像・トラッキング・レンズ情報を受ける  
3. 遅延と同期を確認する  
4. キー合成を確認する  
5. 合成映像を外部出力する  
6. 外部 recorder で当日収録する  

---

## 3. Unreal と Aximmetry の役割
### Unreal Engine の役割
- virtual set の背景を作る
- Aximmetry で使う前提の scene を準備する

### Aximmetry の役割
- 映像・トラッキング・レンズ情報を受ける
- 背景と合成する
- 出力する
- 当日収録や再確認につなぐ

### Day 2 での理解
Day 2 では、Unreal Engine を **背景側**、Aximmetry を **統合・合成・出力側** として理解することが重要です。

---

## 4. Unreal setup のポイント
### Day 2 で押さえること
- Unreal project / scene が Aximmetry 前提で準備されている
- Aximmetry Camera 前提で scene が組まれている
- 床・スケール・見え方の前提が大きく崩れていない
- Flow Editor は deep に学ぶのではなく、最低限の役割だけ理解する

### 覚え方
**Unreal は背景を作る場所、Aximmetry はそれを使って合成する場所**

---

## 5. I/O setup の基本順
Day 2 では、まず Aximmetry の `INPUTS` で通常の進め方を確認しました。

### 基本順序
1. Camera Device
2. Tracking Device
3. レンズ情報 / Calibration の前提確認
4. Tracking Delay
5. Zoom Delay
6. Timecode Sync / Zoom Timecode Sync
7. Detect Tracking Delay / Detect Zoom Delay

### 重要ポイント
- `Detect Tracking Delay` / `Detect Zoom Delay` は fallback ではなく、通常の進め方の一部
- まずは **正常に来ているか** を確認する
- その後で **遅延と同期** を合わせる

---

## 6. I/O で最初に見ること
### 入力確認
- 映像が来ているか
- トラッキングが来ているか
- レンズ情報が来ているか

### その次に見ること
- tracking の遅れがないか
- zoom の遅れがないか
- timecode の同期が崩れていないか

### Day 2 の基本姿勢
Day 2 では、まず **通常の進め方を成立させること** を優先する。  
異常系や救済策の深掘りは Day 3 に回す。

---

## 7. Keying の基本
Day 2 の Keying で一番大事なのは、  
**キー合成はソフトだけで決まらない**  
ということです。

### 先に整えるもの
- 背景の状態
- lighting
- 被写体と背景の距離
- 衣装 / 反射物の条件

### その後で Aximmetry
- Background Color
- Low Cut / High Cut
- 必要に応じた色かぶり補正
- Final Output での確認

---

## 8. Keying の確認順
Day 2 では、次の順番で確認するのが基本です。

1. 背景条件を確認する  
2. lighting を確認する  
3. 被写体距離を確認する  
4. Aximmetry 側で調整する  
5. Final Output で確認する  

### 覚え方
**まず素材条件、次にソフト、最後に全体の見え方**

---

## 9. Live Rec の基本
Day 2 の rec は、

**Aximmetry の合成映像を外部 recorder に送り、  
本番中に安全に残すこと**

が目的です。

### ここで押さえること
- Aximmetry の output を外へ出す
- recorder 側で受ける
- Timecode Master を基準に運用をそろえる
- Day 2 は「後で作り込む」より「当日に安全に残す」が主目的

### 注意
- Input Recording
- Tracking Only
- `.xdata`
- replay / offline rendering

これらは Day 3 で扱う

---

## 10. Day 2 でまだ深掘りしないもの
Day 2 では、次の内容は本流として扱いません。

- AR
- deep Blueprint
- Virtual Screen を本流として扱うこと
- offline recording の深掘り
- advanced troubleshooting
- external 3D post / FBX の深掘り

### 理由
Day 2 は、まず **通常の進め方で成功状態を作る日** だからです。

---

## 11. Day 2 を一言でまとめると
**通常の進め方で、背景合成と当日収録を成立させる日**

---

## 12. 復習チェック
- [ ] Unreal は背景側、Aximmetry は統合・合成・出力側と説明できる
- [ ] Day 2 の全体フローを説明できる
- [ ] I/O setup の基本順序を説明できる
- [ ] Detect Tracking Delay / Detect Zoom Delay が通常の進め方の一部だと理解している
- [ ] Keying はまず物理条件が重要だと説明できる
- [ ] Keying の確認順を説明できる
- [ ] Day 2 の rec は「当日に安全に残すための収録」だと説明できる
- [ ] Day 2 のゴールである「背景合成と当日収録」が成立したか確認できたか
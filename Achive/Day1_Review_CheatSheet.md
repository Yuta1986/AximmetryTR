# Day1_Review_CheatSheet.md

# Day 1 Review Cheat Sheet
## Day 1 基礎の振り返り

※Day 2・Day 3 の内容は、Day 1 の基礎が成立している前提で進みます。  
※必要に応じて、このシートに戻って前提を確認してください。

---

## 1. Day 1 の目的
Day 1 の最重要ゴールは、

**Canon C400 の映像とレンズ情報、ReTracker Bliss のトラッキング情報を Aximmetry で正しく受け、  
Tracking Calibration と Nodal Offset を完了した「ズレのない追従状態」を作ること**

です。

---

## 2. Day 1 の基本方針
- Day 1 は、深い理解よりも「成功状態の体験」を優先する
- 基本操作は講師が実施する
- Day 2・Day 3 で、意味や再現性を深める

---

## 3. Day 1 の全体フロー
1. システム構成と概念説明
2. ネットワーク設定・固定IP
3. Ping による疎通確認
4. Windows Remote Desktop 接続
5. 専用 Viewer で特徴点（緑色の点）の取得状態を確認
6. Bliss setting app で露出設定を調整
7. Bliss app を起動・状態確認
8. Aximmetry 起動・入力確認
9. Canon C400 の CV Protocol 設定
10. 映像（SDI）入力確認
11. Tracking Calibration
12. Nodal Offset 調整
13. ズレのない追従確認

---

## 4. システム構成と役割
### Canon C400
- SDI：映像信号
- Ethernet（CV Protocol）：レンズ情報

### ReTracker Bliss
- トラッキング情報を出す

### Aximmetry
- 映像 / レンズ情報 / トラッキング情報の統合点

### Day 1 で理解したいこと
- 何がどこから来るか
- 映像とレンズ情報は別経路で来ること
- Aximmetry でそれらを統合すること

---

## 5. ネットワーク設定と疎通確認
### やること
- Aximmetry Host PC
- ReTracker Bliss MiniPC
- Canon C400

この3者に必要な固定IPを設定し、疎通確認を行う。

### なぜ重要か
ここが崩れると、
- Bliss に入れない
- CV Protocol が来ない
- 後段の確認が不安定になる

### 思い出すべきこと
- 固定IPは本番安定の土台
- Ping 確認は最初の切り分け

---

## 6. 専用 Viewer で特徴点を確認
### やること
- Host PC から Bliss MiniPC に Remote Desktop 接続する
- 専用 Viewer を開く
- 特徴点（緑色の点）が安定して取得できているか確認する

### なぜ重要か
特徴点が安定して取れていないと、その後の tracking の安定性が崩れやすい。  
まずは Viewer 上で、tracking に必要な見え方が得られているかを確認する。

### 到達点
**専用 Viewer 上で、特徴点（緑色の点）が安定して見えている状態**

---

## 7. Bliss setting app で露出設定を調整
### やること
- Auto Exposure を切る
- Gain / Brightness / Exposure Time などを調整する
- Viewer で確認した特徴点の取得状態が安定する設定値を反映する

### なぜ重要か
tracking の安定性は、センサー露出条件の影響を大きく受ける。  
まず Viewer で確認し、その結果を設定側へ反映する流れが重要。

### 到達点
**特徴点が安定して取得できる露出設定が入った状態**

---

## 8. Bliss app を起動・状態確認
### やること
- Bliss app を起動する
- tracking が動作していることを確認する
- Aximmetry 側で tracking データ到着を確認する

### 到達点
**Aximmetry 上でトラッキング情報が見えている状態**

---

## 9. Aximmetry 起動と入力確認
### やること
- Aximmetry を起動する
- プロジェクトを開く
- 今日使う箇所だけを見る
- 映像 / トラッキング / レンズ情報の到着を確認する

### 重要ポイント
- UI 全体を覚える必要はない
- まずは「今日使う場所」に絞る
- データ到着確認は Aximmetry 上で行う

---

## 10. Canon C400 の CV Protocol と映像入力
### やること
- C400 側で CV Protocol を設定する
- Ethernet 経由でレンズ情報が来ていることを確認する
- Aximmetry 側でレンズ情報更新を確認する
- SDI 映像入力を確認する

### 重要ポイント
- 映像（SDI）とレンズ情報（Ethernet）は別経路
- 後段で Aximmetry 上でそろえる必要がある

### 到達点
**映像 / レンズ情報 / トラッキング情報の3系統がそろった状態**

---

## 11. Tracking Calibration
### 何をやるか
トラッキング空間と virtual 側の基準を合わせる。

### なぜ重要か
ここが崩れると、
- 背景位置が不自然になる
- カメラ移動時の整合が崩れる
- Day 2 以降の合成品質に影響する

---

## 12. Nodal Offset
### 何をやるか
tracking point と実際のレンズ中心のズレを補正する。

### なぜ重要か
ここが合っていないと、
- 背景がずれて見える
- pan / tilt / move で違和感が出る
- 「なんとなく合わない」状態になる

### Day 2・Day 3 との関係
- Day 2 の背景合成の自然さに直結する
- Day 3 の replay / troubleshooting にも関係する
- 原因が Day 1 にある場合がある

---

## 13. Day 1 の完了条件
- カメラを振ってもズレのない追従が確認できる
- 参加者が Day 1 の流れを言葉で説明できる

### Day 1 を一言でいうと
**Day 2・Day 3 の土台を整える日**

---

## 14. 復習チェック
- [ ] Canon C400 / ReTracker Bliss / Aximmetry の役割を説明できる
- [ ] 映像・レンズ情報・トラッキング情報の3系統を説明できる
- [ ] 固定IPと Ping 確認の意味を説明できる
- [ ] 専用 Viewer で特徴点（緑色の点）の取得状態を確認する意味を説明できる
- [ ] Bliss setting app で露出設定を調整する意味を説明できる
- [ ] Aximmetry 上でデータ到着確認を行う意味を説明できる
- [ ] Tracking Calibration の役割を説明できる
- [ ] Nodal Offset の役割を説明できる
- [ ] Day 1 のゴールである「ズレのない追従状態」が確認できたか
# Aximmetry Review Guide Notes

このファイルは内部向けメモです。クライアント配布版には含めません。

## 現在の配布版

- 対象ファイル: `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- 主対象:
  `トレーニング受講済み` または `導入説明を一度受けたクライアント初学者`
- 資料の役割:
  初学者が復習・再確認・公式ページ参照に使うロードマップ

## 本文に入れないもの

- 社内メモ
- 運用メモ
- 機材固有設定
- 完全手順

## 維持方針

- 本文は「学習順路」「概念整理」「公式Learnへの導線」に集中させる
- UI差分や機材固有差分は、本文へ詰め込みすぎず別資料へ分ける
- 配布版ではプレースホルダや編集指示を残さない

## Bliss 参照メモ

- 配布版本文では `配布された REtracker Bliss 日本語マニュアル` と記載する
- 実運用では、クライアントへ渡す日本語マニュアルのファイル名と保管場所を別途管理する
- 日本語マニュアルが未配布の案件では、案内文の整合性を配布前に確認する

## Version違いを作るなら

Version違いを増やす前に、まず本文共通化で吸収できないかを確認する。

### 分岐を作る価値があるケース

- UI名称や画面構成が大きく変わる
- 手順順序が変わる
- 機能の有無や推奨方法が変わる
- 参照すべき公式Learnが大きく変わる

### 分岐を作らなくてよいケース

- 文言の微修正
- 軽微なUI差
- スクリーンショット差し替えだけで吸収できる差
- 注記1つで吸収できる差

### 推奨運用

- まずは本文の共通版を1本保つ
- 差分が少ない場合は、本文分岐より「差分注記」または「別表」で対応する
- 差分が大きい場合だけ、Version別ファイルを作る
- Version別ファイルを作る場合も、章構成と見出し順は可能な限りそろえる

### 推奨命名

- 共通版:
  `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- Aximmetry version別:
  `Aximmetry_Review_Guide_Integrated_v0.2.3_for_Aximmetry_2025.x.md`
- 対象別:
  `Aximmetry_Review_Guide_Integrated_v0.2.3_for_Training_Recap.md`
  `Aximmetry_Review_Guide_Integrated_v0.2.3_for_Intro_Client.md`

## 今後の改善候補

- 公式Learnの導線変更時にリンクを更新する
- 学習者がつまずきやすい症状例を `Troubleshooting` に継続追加する
- 必要なら「最短ルート」と「参照辞書的な使い方」の2モード案内を強める
- スクリーンショットを追加する場合は、操作手順の代替ではなく確認ポイント用途に絞る

## Session Handoff 2026-04-02

- 最新コミット: `e23ab66` `Normalize roadmap headings to Japanese-first`
- 今回触った主ファイル: `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- 反映内容:
  - `このロードマップの使い方` 内の章名参照を `日本語 / English` に統一
  - `このロードマップの見取り図` の章名を本文の章タイトルと合わせて統一
  - 章タイトル、`この資料の対象範囲 / Scope`、`用語辞書 / Terminology`、`最終確認チェックリスト / Final Review Checklist` を日本語優先に整理
  - 第2章タイトルを `AX Scene / Unreal準備 / AX Scene / Unreal Setup` に短縮
  - 見取り図の9項目目は `Reference Map` ではなく、実際の章名に合わせて `目的別索引 / Purpose Index` に修正
- 今回あえて触っていないもの:
  - 本文の章構成、説明順、各段落の内容
  - 用語辞書の各用語見出しや、`Mental Model` など下位レベルの併記順
  - export / PDF 生成確認
- 次回の再開候補:
  - さらに統一するなら、用語辞書項目や下位見出しの `日本語 / English` 順をそろえるか判断する
  - 最上段タイトルの扱いは、後続セッションでユーザー判断により日本語先行へ整理済み
  - 見出し調整後に必要なら export して PDF のしおり表示を確認する

## Session Handoff 2026-04-02 (Resume)

- 今回触った主ファイル:
  - `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
  - `Docs/memory.md`
  - `Aximmetry_Review_Guide_Notes.md`
- 反映内容:
  - 用語辞書内の **既存の日英併記項目** を、可能な範囲で `日本語 / English` 順に統一
  - 本文中の `Virtual Camera / ヴァーチャルカメラ` を `ヴァーチャルカメラ / Virtual Camera` に統一
  - 第6章の小見出し `当日収録 / Live Rec` と関連チェック項目を統一
  - 今後の判断基準として、「自然な日本語見出しを作りにくい用語は英語維持でよい」ことを `Docs/memory.md` に追記
  - `tools/export_pdf.py` で HTML / PDF export を実行し、生成成功を確認
- 今回あえて触っていないもの:
  - `Input Recording` `Tracking Calibration` `Nodal Offset` など、英語のまま残した用語の見出し化
- 次回の再開候補:
  - 必要なら生成済みの PDF / HTML を開いて、見出し表示や PDF しおりの見え方を確認する
  - 英語単独で残した用語をどこまで和文併記へ寄せるか、必要性ベースで判断する

## Session Handoff 2026-04-02 (Language Rule)

- ユーザー判断:
  - 日英併記は基本的に `左日本語 / 右英語` を採用する
- 今回の反映:
  - 最上段タイトルを日本語先行に整理
  - `再生確認 / Playback / Offline Review`
  - `レンズ情報 / CV Protocol`
  - `入力と同期 / Inputs / Sync`
  - `Docs/memory.md` に運用ルールを明文化
- 維持する例外:
  - `Input Recording` `Tracking Calibration` `Nodal Offset` など、自然な日本語見出しが不安定な語は英語単独可

## Session Handoff 2026-04-02 (Export Pattern Folders)

- ユーザー判断:
  - `exports/` はパターンごとにフォルダ分けする
- 今回の反映:
  - `tools/export_pdf.py` を更新し、出力先を `exports/<pattern>/` に変更
  - `<pattern>` は `theme + toc_mode` の組み合わせで管理
  - 各フォルダ内のファイル名は元 Markdown のベース名をそのまま使う
  - `Docs/Export_Workflow.md` と `Docs/memory.md` に新ルールを追記
- 想定される例:
  - `exports/default/`
  - `exports/default_with_inline_toc/`
  - `exports/default_with_sidebar_toc/`
  - `exports/mobeon/`
  - `exports/mobeon-dark_with_inline_toc/`

## Session Handoff 2026-04-02 (Pattern Drift Diagnosis)

- 原因:
  - 各 `exports/<pattern>/` はその時点の個別 snapshot であり、本文更新後も未再生成の他パターンは古いまま残る
- 今回の確認結果:
  - source: `Aximmetry_Review_Guide_Integrated_v0.2.3.md` は `2026-04-02 16:31:06`
  - `exports/default/` は `2026-04-02 16:46:39` で再生成済み
  - `exports/mobeon/` は `2026-04-02 15:37:37`
  - `exports/mobeon-dark/` は `2026-04-02 15:23:27`
  - inline 系も `15:23-15:37` 台で、最新本文より古かった
  - そのため、`default` だけ新しい文言を持ち、他パターンは旧文言のままだった
- 旧文言の例:
  - `Playback / Offline Review`
  - `症状B: CV Protocol / レンズ情報が来ない`
  - `Inputs / Sync を確認したい`
- 再発防止:
  - 内容更新後にパターン比較する前は `Export: Sync Active Markdown (All Patterns)` を使う
  - `Docs/memory.md` と `Docs/Export_Workflow.md` に snapshot 運用ルールを追記

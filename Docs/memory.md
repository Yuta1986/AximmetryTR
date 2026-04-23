# Project Memory

## 対象読者

- 主対象は、トレーニング受講済み、または導入説明を一度受けた日本人の初学者クライアント
- すべての講義を受けているとは限らないため、復習だけでなく抜けた内容の補完にも使える必要がある

## メインガイドの役割

- 復習、再確認、公式 Aximmetry ページ参照のためのロードマップ
- 完全な操作マニュアルではない
- 講師向けの内部メモではない
- 機材固有設定の一覧ではない
- 完全手順の runbook ではない

## 文体と用語のルール

- 日本語話者向けの一般語は、できるだけ自然な日本語に寄せる
- `Training` は本文では `トレーニング` にする
- 日英併記は原則 `日本語 / English` とし、左日本語 / 右英語で統一する
- 改行で重ねるタイトルでも、日本語を先に置く
- UI 名や専門用語は、英語のまま、または英語併記を維持してよい
- 自然な日本語見出しが不安定な用語は、無理に和訳せず英語単独でもよい
- 明示依頼がない限り、メインガイドの設計や粒度は変えない

## Aximmetry 固有の名称ルール

- `AX Scene Editor` が最初に出る箇所では、`2026.1.0` でライセンス体系変更とともに名称変更があったことを注記する
- `2025.3.0` 以前を継続利用している環境や旧資料では `Unreal Editor for Aximmetry` が使われる

## リポジトリ構成メモ

- 現行の生成物: `build/exports/<theme>/<toc-mode>/`
- 旧生成物の退避先: `Achive/exports/`
- 旧版のソース保管先: `Achive/guide_versions/`
- 運用メモと補助資料: `Docs/`
- 既存フォルダ名は `Achive` なので、明示依頼がない限り repo-wide rename はしない

## Export フローの前提

- PDF 配布では、PDF のしおり / アウトラインを主役にする
- `Inline TOC` は本文内に見せる目次
- `Sidebar TOC` は HTML ブラウザ表示用
- export 生成物は `build/exports/<theme>/<toc-mode>/` に分ける
- `<pattern>` は `theme + toc_mode` の組み合わせで管理する
- 各 `build/exports/<theme>/<toc-mode>/` は live view ではなく、その時点の snapshot
- Markdown 本文を更新しても、再 export していない他パターンは自動更新されない
- 内容更新後にパターン間比較をする前は、`Export: Sync Active Markdown (All Patterns)` で全パターンを再生成する
- source と export のずれを疑うときは、Markdown と各 `build/exports/<theme>/<toc-mode>/` の更新時刻を比較する
- VS Code タスク名は `.vscode/tasks.json` に定義されている
- 維持するテーマは 3 系統:
- `default` = 白ベース + 青系アクセントの中立テーマ
- `mobeon` = 白ベース + ブロンズ / 赤系アクセント
- `mobeon-dark` = ダークベース + オレンジ / ブロンズ系アクセント

## 編集時の注意

- ファイル編集は `apply_patch` を使う
- 文言調整、注記追加、Export フロー改善の依頼では、構成変更をしない
- クライアント向け本文と内部メモは分けて管理する
- 版番号ルールは `Docs/Versioning_Policy.md` を基準にする

## 再開時の手がかり

- 進行中の本文は `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- 2026-04-02 時点で、章タイトルとロードマップ導線は `日本語 / English` の順に統一済み
- 2026-04-02 時点で、最上段タイトルも日本語先行に整理済み
- 第2章の短縮表記は `AX Scene / Unreal準備 / AX Scene / Unreal Setup`
- `このロードマップの見取り図` の章名は、本文の章タイトルと一致させる
- 2026-04-02 の再開作業で、用語辞書と本文中の **既存の日英併記項目** は `日本語 / English` を優先する方針に寄せた
- `Input Recording` `Tracking Calibration` `Nodal Offset` など、自然な日本語見出しを無理に作りにくい用語は英語表記を維持してよい
- セッション固有の handoff は `Aximmetry_Review_Guide_Notes.md` に残す

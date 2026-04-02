# Export Workflow

## 目的

このメモは、VS Code から現在の Markdown ガイドを書き出す方法と、各出力モードの違いを整理するためのものです。

## 関連ファイル

- 元原稿: ルート直下の Markdown。例: `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- VS Code タスク定義: `.vscode/tasks.json`
- 書き出しスクリプト: `tools/export_pdf.py`
- スタイル: `tools/pdf_style.css`
- 現行の出力先: `exports/`
- 旧生成物の退避先: `Achive/exports/`

注記:
リポジトリ内には既存の `Achive` フォルダ名があるため、今回は構成を崩さずこの表記を維持しています。

## VS Code タスク

### 1. PDF: Install Markdown Dependency

Python の `markdown` パッケージが未導入の端末で、最初に一度だけ実行します。

### 2. PDF: Export Active Markdown

- 通常の HTML と PDF を生成します
- PDF 配布の基本用途として推奨です
- PDF を開く環境が対応していれば、しおり / アウトラインも使えます

### 3. PDF: Export Active Markdown (with Inline TOC)

- 本文先頭付近にクリック可能な目次を入れた HTML と PDF を生成します
- PDF の本文内にも目次ページ相当を見せたい場合に向いています

### 4. HTML: Export Active Markdown

- TOC なしの HTML を生成します
- シンプルなブラウザ確認用です

### 5. HTML: Export Active Markdown (with Sidebar TOC)

- 左サイドバー付きの HTML を生成します
- ブラウザ表示時に TOC を常時見せたいときに使います
- サイドバーの表示 / 非表示を切り替えるボタンも入ります
- このモードは HTML 確認用であり、PDF 配布用ではありません

## TOC の考え方

- `Inline TOC` は本文の一部なので、ページ上部に表示されます
- `Sidebar TOC` は HTML 表示専用のレイアウトです
- PDF ビューア左側のナビゲーションは、HTML サイドバーではなく PDF のしおり / アウトラインで制御されます
- そのため、PDF と HTML では TOC の見せ方を意図的に分けています

## 推奨用途

- クライアント配布 PDF: `PDF: Export Active Markdown`
- 本文内にも目次を入れたい PDF: `PDF: Export Active Markdown (with Inline TOC)`
- ブラウザでの内部確認: `HTML: Export Active Markdown (with Sidebar TOC)`

## アーカイブ運用

- 現行の生成物は `exports/` に置きます
- 廃止した出力形式や置き換え済みの生成物は `Achive/exports/` に移します
- 旧 `with_toc` フローの生成物は、すでに `Achive/exports/` へ移動済みです

## 更新時の流れ

1. 元の Markdown を修正する
2. 目的に合う VS Code タスクを実行する
3. `exports/` の結果を確認する
4. 古い出力形式が不要になったら、該当ファイルを `Achive/exports/` へ移す

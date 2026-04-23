# Export Workflow

## 目的

このメモは、VS Code から現在の Markdown ガイドを書き出す方法と、各出力モードの違いを整理するためのものです。

## 関連ファイル

- 元原稿: ルート直下の Markdown。例: `Aximmetry_Review_Guide_Integrated_v0.2.3.md`
- VS Code タスク定義: `.vscode/tasks.json`
- 書き出しスクリプト: `tools/export_pdf.py`
- Pages 同期スクリプト: `tools/sync_pages_site.py`
- スタイル: `tools/pdf_style.css`, `tools/pdf_style_mobeon.css`, `tools/pdf_style_mobeon_dark.css`
- 現行の出力先: `build/exports/<theme>/<toc-mode>/`
- Pages 公開用の固定出力先: `site/`
- 旧生成物の退避先: `Achive/exports/`

注記:
リポジトリ内には既存の `Achive` フォルダ名があるため、今回は構成を崩さずこの表記を維持しています。

`<pattern>` は、テーマと TOC モードの組み合わせです。例:

- `default/none`
- `default/inline`
- `default/sidebar`
- `mobeon/none`
- `mobeon/inline`
- `mobeon/sidebar`
- `mobeon-dark/none`
- `mobeon-dark/inline`
- `mobeon-dark/sidebar`

## Mobeon テーマの位置づけ

`Mobeon` テーマは、公式サイトのブランドトーンを参照しつつ、**長文ドキュメント向けに落ち着かせた追加テーマ** です。

- LP やコーポレートサイト向けの演出を、そのまま持ち込むものではありません
- 学習資料、レビュー資料、SOP の可読性を優先します
- 既存の Markdown 構造や粒度を変えず、見せ方だけを追加で整える方針です

派生として、次の2系統を使い分けます。

- `mobeon`: 明るい背景にブロンズ / 赤みのアクセントを置く標準版
- `mobeon-dark`: ダーク背景にオレンジ / ブロンズを効かせる比較用の派生版

あわせて、ベースラインとして次も維持します。

- `default`: `main` と同じ、白ベース + 青系アクセントの中立テーマ

## VS Code タスク

### 1. PDF: Install Markdown Dependency

Python の `markdown` パッケージが未導入の端末で、最初に一度だけ実行します。

### 2. Export: Sync Active Markdown (All Patterns)

- 現在の Markdown を、全パターンに対してまとめて再生成します
- 内容更新後に `default / mobeon / mobeon-dark` を見比べる前は、このタスクを先に使います
- パターンごとの content drift を防ぐための基準タスクです

### 3. PDF: Export Active Markdown

- 通常の HTML と PDF を生成します
- PDF 配布の基本用途として推奨です
- PDF を開く環境が対応していれば、しおり / アウトラインも使えます

### 4. PDF: Export Active Markdown (with Inline TOC)

- 本文先頭付近にクリック可能な目次を入れた HTML と PDF を生成します
- PDF の本文内にも目次ページ相当を見せたい場合に向いています

### 5. HTML: Export Active Markdown

- TOC なしの HTML を生成します
- シンプルなブラウザ確認用です

### 6. HTML: Export Active Markdown (with Sidebar TOC)

- 左サイドバー付きの HTML を生成します
- ブラウザ表示時に TOC を常時見せたいときに使います
- サイドバーの表示 / 非表示を切り替えるボタンも入ります
- このモードは HTML 確認用であり、PDF 配布用ではありません

### 7. Mobeon テーマ系タスク

- `PDF: Export Active Markdown (Mobeon)`
- `PDF: Export Active Markdown (Mobeon with Inline TOC)`
- `PDF: Export Active Markdown (Mobeon Dark)`
- `PDF: Export Active Markdown (Mobeon Dark with Inline TOC)`
- `HTML: Export Active Markdown (Mobeon)`
- `HTML: Export Active Markdown (Mobeon with Sidebar TOC)`
- `HTML: Export Active Markdown (Mobeon Dark)`
- `HTML: Export Active Markdown (Mobeon Dark with Sidebar TOC)`

これらは、現行の中立テーマを壊さずに、Mobeon 向けの追加デザインで書き出すためのタスクです。  
生成物は `build/exports/<theme>/<toc-mode>/` に分かれて保存され、各フォルダ内のファイル名は元 Markdown のベース名をそのまま使います。

中立テーマを使う場合は、既存の次を使います。

- `PDF: Export Active Markdown`
- `PDF: Export Active Markdown (with Inline TOC)`
- `HTML: Export Active Markdown`
- `HTML: Export Active Markdown (with Sidebar TOC)`

### 8. Pages: Sync Active Markdown Site

- `build/exports/` に生成済みの HTML / PDF から、GitHub Pages 用の `site/` を更新します
- `site/index.html` には `build/exports/default/sidebar/` の HTML を使います
- `site/latest.pdf` には `build/exports/default/none/` の PDF を使います
- `site/versions/` には version 付きの HTML / PDF を残します

## callout 記法

Mobeon テーマでは、通常の blockquote をそのまま使いながら、補足や注意を見やすくできます。

例:

```md
> **補足**  
> この資料はロードマップとして使います。
```

```md
> **注意**  
> この項目は version によって挙動が変わることがあります。
```

現在のエクスポータでは、次のラベルを認識します。

- `補足` / `INFO`
- `注意` / `WARNING`
- `重要` / `CRITICAL`

Markdown 側の構造は変えず、HTML / PDF の見た目だけを強めるための仕組みです。

## TOC の考え方

- `Inline TOC` は本文の一部なので、ページ上部に表示されます
- `Sidebar TOC` は HTML 表示専用のレイアウトです
- HTML 上の見出し表示は日本語向けに `目次` として表示されます
- PDF ビューア左側のナビゲーションは、HTML サイドバーではなく PDF のしおり / アウトラインで制御されます
- そのため、PDF と HTML では TOC の見せ方を意図的に分けています

## 推奨用途

- クライアント配布 PDF: `PDF: Export Active Markdown`
- 本文内にも目次を入れたい PDF: `PDF: Export Active Markdown (with Inline TOC)`
- ブラウザでの内部確認: `HTML: Export Active Markdown (with Sidebar TOC)`
- 青系アクセントの中立資料: `default`
- 白ベースの Mobeon 資料: `mobeon`
- Mobeon デザイン確認: `PDF / HTML` の Mobeon 系タスク
- ダーク背景の比較確認: `PDF / HTML` の Mobeon Dark 系タスク

## 出力フォルダの考え方

- `build/exports/` 直下には、テーマ別フォルダだけを置きます
- 同じ Markdown を別パターンで書き出しても、ファイル名ではなくフォルダで見分けます
- `Sidebar TOC` は HTML 専用なので、該当フォルダには HTML のみが入ることがあります
- 通常確認時は、比較したいパターンのフォルダ同士を見比べます
- ただし、各フォルダは個別 export の snapshot なので、再生成時刻がずれていると content もずれます
- 本文修正後に比較する前は、`Export: Sync Active Markdown (All Patterns)` を実行して全パターンをそろえます
- 更新漏れを疑うときは、元 Markdown と各パターン出力の更新時刻を確認します

## GitHub Pages 用の考え方

- Windows 環境では既存の `Docs/` と GitHub Pages 用の `/docs` を分けにくいため、公開用フォルダは `site/` を使います
- GitHub Pages への公開は `.github/workflows/deploy-pages.yml` から行います
- 公開用の安定URLは `site/index.html` と `site/latest.pdf` です
- 共有用の HTML はブラウザ閲覧向けに `build/exports/default/sidebar/` を採用します
- 共有用の PDF は配布向けに `build/exports/default/none/` を採用します

## アーカイブ運用

- 現行の生成物は `build/exports/<theme>/<toc-mode>/` に置きます
- 廃止した出力形式や置き換え済みの生成物は `Achive/exports/` に移します
- 旧 `with_toc` フローの生成物は、すでに `Achive/exports/` へ移動済みです

## 更新時の流れ

1. 元の Markdown を修正する
2. `Export: Sync Active Markdown (All Patterns)` を実行する
3. 必要に応じて `Pages: Sync Active Markdown Site` を実行する
4. 対象パターンの `build/exports/<theme>/<toc-mode>/` と `site/` を確認する
5. 古い出力形式が不要になったら、該当フォルダ内の生成物を `Achive/exports/` へ移す

# Mobeon Documentation Theme Pattern v1.0
**Date:** 2026-04-02  
**Status:** Draft for `feature/mobeon-theme-pattern`  
**Target:** HTML / PDF export theme for training manuals, technical SOPs, and architecture-style docs

---

## 1. Positioning

This document defines an **optional Mobeon-branded export pattern**.

- It does **not** replace the current neutral documentation style on `main`
- It is an **additional presentation pattern** for selected documents
- It must work as a **non-destructive layer** over existing Markdown content
- It should preserve the current strengths of the guide:
  - clear hierarchy
  - Japanese-first readability
  - AI-readable heading structure
  - stable PDF export

## 2. Design Goal

### Theme Name
**Cognitive Clarity**

### Core Intent
- Minimize cognitive load for operators and learners
- Convey technical trust and infrastructure safety
- Keep the document plain, durable, and professional rather than flashy
- Make long-form reading easier for Japanese users

### Visual Reference
- Notion Docs
- GitHub Docs
- Enterprise product documentation

This means:
- strong heading hierarchy
- restrained color usage
- generous whitespace
- obvious grouping of warnings and key information

## 3. Scope

This pattern is suitable for:
- training manuals
- review roadmaps
- technical SOPs
- architecture overview documents

This pattern is **not** a rule that every document must follow.

For the current Aximmetry review guide, the Mobeon version should be treated as:
- an alternate branded export pattern
- not a rewrite of the document structure
- not a change to the guide's granularity or instructional scope

## 4. Implementation Constraints

The current export flow is:

`Markdown -> python-markdown -> inline CSS -> HTML -> LibreOffice -> PDF`

So the first implementation should stay compatible with the current toolchain.

### Required Constraints
- no destructive change to the Markdown source structure
- no assumption that custom fonts are always installed
- PDF readability must remain as important as HTML appearance
- bookmark / outline behavior must remain intact
- Japanese title should remain primary when both Japanese and English titles exist

### Practical Rule
Phase 1 should be achievable with:
- CSS changes
- minimal export script changes
- optional theme switching in the export flow

Phase 1 should **not** require:
- a custom Markdown parser
- heavy JavaScript
- browser-only interactions that degrade PDF quality

## 5. Typography

The visual tone should be modern and technical, but reading comfort comes first.

### Body
- Preferred: `Noto Sans JP`, `Inter`
- Fallback-first implementation: `"Segoe UI Variable Text"`, `"Yu Gothic UI"`, `"Meiryo"`, sans-serif`

### Code / Paths
- Preferred: `JetBrains Mono`, `Cascadia Mono`
- Safe fallback: `Consolas`, monospace

### Rules
- UI names, paths, commands, IP addresses, and code identifiers should remain in inline code
- UI labels should use bold when needed for operational clarity
- Italic should be used sparingly for conceptual notes only

## 6. Callout Pattern

Information importance should be visually distinct, but still readable in PDF and print.

### Principle
- use **label + border + background** as the main signal
- use color as a support signal
- do not rely only on emoji or color

### Callout Levels

| Level | Primary Signal | Meaning |
| :--- | :--- | :--- |
| `INFO` | Blue / neutral border | prerequisite, tip, shortcut, operator note |
| `WARNING` | Amber border | configuration risk, version mismatch, likely mistake |
| `CRITICAL` | Red border | asset loss risk, infrastructure safety, destructive action |

### Phase 1 Markup Rule

Use normal Markdown blockquotes with a leading label.

Example:

```md
> **INFO**  
> この設定は収録前に確認します。
```

```md
> **WARNING**  
> バージョン違いにより挙動が変わる場合があります。
```

```md
> **CRITICAL**  
> 同期中に強制終了しないでください。
```

This fits the current exporter better than introducing a new syntax immediately.

## 7. Structure Guidance

The Mobeon theme should not force one rigid scaffold onto every document.

Instead, define **recommended section families**:
- Overview
- Scope / Assumptions
- Procedure / Workflow
- Verification
- Troubleshooting
- Reference Links

For SOP-heavy documents, `Procedure` and `Verification` may dominate.  
For roadmap-style learning documents, `Overview`, `Workflow`, and `Reference Links` may dominate.

This is safer than saying "all manuals must use one exact structure."

## 8. Mobeon-Specific Visual Direction

### Desired Tone
- calm
- trustworthy
- technical
- infrastructure-aware
- learner-friendly

### Avoid
- LP-style visual impact
- excessive gradients
- decorative icons as primary meaning
- strong dark-mode bias
- overly marketing-like copy

### Good Signals
- precise spacing
- stable grid
- understated accents
- clear status colors
- strong heading rhythm

## 9. Rollout Plan

### Step 1
Keep the current neutral style on `main`.

### Step 2
Implement the Mobeon theme on `feature/mobeon-theme-pattern`.

### Step 3
Add theme selection to the export flow if needed.

Suggested future direction:
- default theme: current neutral export
- optional theme: Mobeon export

Possible naming:
- `--theme default`
- `--theme mobeon`

### Step 4
When the branded output is stable, decide whether to:
- keep it as an alternate export only
- or adopt it for selected client-facing materials

## 10. Definition of Done

The Mobeon theme pattern is ready when:
- existing Markdown can be exported without structural rewrites
- Japanese titles remain primary in the rendered header
- HTML and PDF both look intentional and readable
- warnings are more visually distinct than the default theme
- the current guide's content and granularity remain unchanged
- the alternate theme can coexist with the neutral baseline

---

**Keywords:** `#MobeonTheme` `#TechDocs` `#TrainingDocs` `#ExportDesign` `#NonDestructiveTheme`

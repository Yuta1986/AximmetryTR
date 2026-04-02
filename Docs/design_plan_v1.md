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
- It adapts Mobeon's official brand direction for **long-form documentation**, not for LP-style marketing pages
- It should preserve the current strengths of the guide:
  - clear hierarchy
  - Japanese-first readability
  - AI-readable heading structure
  - stable PDF export

### Theme Portfolio

The export system should keep **multiple parallel presentation patterns**.

- `default`: clean white base + blue accents, aligned with the current `main` baseline
- `mobeon`: clean white base + orange-led bronze / red accents
- `mobeon-dark`: dark base + orange / bronze accents

These should coexist without forcing a single visual answer for every document.

### Brand Source Boundary

The official Mobeon sites suggest a strong brand direction built around:
- `Transform Reality`
- `Immersive`
- virtual production with `Aximmetry` and `Unreal Engine`

That direction should inform the documentation theme, but not dominate it.

So this plan is intentionally:
- influenced by the official brand tone
- separated from corporate LP / web application design rules
- optimized for reading, review, and procedural clarity rather than visual impact

## 2. Design Goal

### Theme Name
**Cognitive Clarity**

### Core Intent
- Minimize cognitive load for operators and learners
- Convey technical trust and infrastructure safety
- Keep the document plain, durable, and professional rather than flashy
- Make long-form reading easier for Japanese users
- Translate Mobeon's "immersive / future-facing" identity into a calmer documentation language

### Brand Reference
- Mobeon global site: immersive XR / interactive / future-facing positioning
- Mobeon Japan site: `Transform Reality`, Aximmetry-led virtual production, operational trust

### Documentation Reference
- Notion Docs
- GitHub Docs
- Enterprise product documentation

This means:
- strong heading hierarchy
- restrained color usage
- generous whitespace
- obvious grouping of warnings and key information
- subtle dark-tech cues may be used, but readability remains the priority

### Logo-Derived Color Direction

The currently available Mobeon logo suggests a palette closer to:
- copper / bronze
- restrained warm off-white
- deep red as a secondary accent
- dark graphite text

So the documentation theme should prefer:
- a light document canvas
- orange-led bronze as the main structural accent
- muted red as a highlight or header accent
- neutral semantic colors for warning states when needed

It should avoid drifting into:
- cool blue product UI language
- neon cyberpunk contrast
- dark backgrounds used only for drama

### Variant Strategy

To keep comparison safe and non-destructive, the Mobeon documentation pattern may have:
- `default`: neutral light canvas + blue-led structure
- `mobeon`: light canvas + orange-led bronze structure
- `mobeon-dark`: dark canvas + orange / bronze-led structure

The dark variant should remain:
- optional
- comparison-friendly
- clearly separate from the neutral baseline on `main`

It should be judged more strictly for:
- long-form readability
- PDF stability
- fatigue during extended reading

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

This pattern is **not** the same thing as:
- a corporate landing page design system
- a marketing website art direction
- a general rule that all Mobeon web properties must share one exact look

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
| `INFO` | Bronze / neutral border | prerequisite, tip, shortcut, operator note |
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
- immersive, but controlled
- premium, but not luxurious for its own sake

### Brand Translation Rule

Official Mobeon web properties can support a darker and more cinematic presentation.

For documentation exports, that should be translated as:
- warmer bronze accents should lead the structure
- restrained deep red may appear as a secondary highlight
- contrast should support reading, not theatrical mood
- visual polish should appear in spacing, rhythm, and hierarchy first
- "tech company" should feel present without making the document feel like a landing page

### Avoid
- LP-style visual impact
- excessive gradients
- decorative icons as primary meaning
- strong dark-mode bias
- overly marketing-like copy
- giant hero-style typography inside the document body
- glassmorphism that reduces PDF clarity

### Good Signals
- precise spacing
- stable grid
- understated accents
- clear status colors
- strong heading rhythm
- subtle reference to advanced imaging / XR infrastructure without visual noise

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
- `--theme mobeon-dark`

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
- the official Mobeon brand is felt in tone, without turning the document into LP-style output

---

**Keywords:** `#MobeonTheme` `#TechDocs` `#TrainingDocs` `#ExportDesign` `#NonDestructiveTheme`

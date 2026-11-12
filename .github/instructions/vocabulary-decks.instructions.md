---
description: "Use when creating or updating Japanese Estonian vocabulary or kanji flashcard decks from a pasted list. Covers source-faithful card data, back-only particle hints, original illustrations, Japanese text-to-speech, unique study storage, validation, and publishing."
---

# Japanese deck workflow

- Read [README.md](../../README.md) for the student-facing behavior and publishing overview.
- Use [chapter23_words.html](../../chapter23_words.html) for a new words deck and [chapter23_kanji.html](../../chapter23_kanji.html) for a new kanji deck. Preserve the existing responsive layout, study controls, accessible inline illustration pattern, and flashcard interaction.
- Create a separate root-level file named `chapter<N>_words.html` or `chapter<N>_kanji.html`. Update its browser title and visible heading for the chapter and deck type. Leave existing decks untouched.

## Vocabulary and source fidelity

- Convert each supplied row into one `INITIAL_CARDS` entry in the supplied order. Keep IDs sequential starting at 1.
- Preserve the teacher-supplied Japanese form, kana reading, and Estonian wording exactly. Do not normalize spellings or readings.
- Ignore a separate English-translation column; do not put it in a card. If an English note is embedded in the supplied Estonian text, retain that source text rather than silently rewriting it.
- If the kanji field is blank, use its supplied kana form for both `kanji` and `reading`.
- For words decks, keep a particle hint out of `estonian` and put it in the optional `particles` property so it appears only on the answer side below the reading. Preserve the Estonian meaning itself. The particle element must be hidden when there is no hint.
- Do not silently correct a supplied Estonian gloss. If a clarification is useful, append it in square brackets after the complete original gloss, for example `original wording [clarification]`.

## Illustrations and card behavior

- Add exactly one matching, original illustration to `WORD_ILLUSTRATIONS` (words) or `CARD_ILLUSTRATIONS` (kanji) for every card, in the same order. Check that the actual symbols and accessible description convey the card's meaning, not merely a loosely related theme.
- Keep art self-contained as inline SVG and/or emoji. Do not hotlink images or use copyrighted manga/anime artwork.
- Give each deck unique `STORAGE_KEY` and `ORDER_STORAGE_KEY` values so study progress remains independent.
- Keep the front as the Estonian prompt and the answer as the Japanese form and reading. Preserve the existing study navigation, randomized range, study/scope controls, ARIA labels, and responsive layout.

## Japanese pronunciation

- Keep pronunciation behavior consistent with the current decks:
  - Reveal with the cat **フリップ** button or **Space** and speak the current Japanese answer once. Loading or selecting an unflipped card must not reveal or speak its answer.
  - Include the accessible **🔊 Replay** button on the revealed side and support **R** while the answer is revealed, except when focus is in an input, textarea, select, or editable field.
  - Keep Japanese audio controlled by the switch and persist its state across decks in the shared `localStorage` key `est_jp_flashcards_audio_v1`; ignore storage errors.
  - Use `window.speechSynthesis` and `SpeechSynthesisUtterance`, cancel queued speech immediately before speaking, set `lang` to `ja-JP` and `rate` to `0.95`, and fail silently when browser speech synthesis is unavailable.
  - Refresh the available voices on `voiceschanged`; prefer a local Japanese voice and favor familiar Japanese voices such as Kyoko, Otoya, Nanami, Haruka, Ichiro, or Google Japanese when available. Allow the browser's default Japanese voice when no matching voice is available.
  - `getJapaneseSpeechText(card)` prefers nonempty `card.kanji` over `card.reading` to preserve Japanese word boundaries and pitch-accent cues. Preserve `(する)`, `(な)`, and `(の)` suffixes, but remove other parenthetical furigana/annotation text together with its parentheses so readings are not spoken twice. Remove brackets and iteration markers, replace separators (including `⇄`) with spaces, and normalize whitespace. Do not use Estonian or romaji as a speech target.

## Validation and publishing

Before finishing:

1. Compare card count, order, Japanese forms/readings, and Estonian wording against the supplied list. Check sequential IDs, one illustration per card, and particle hints absent from front-side meanings.
2. Check JavaScript syntax, unique storage keys, title/heading, and the HTML's browser-rendered front/back. Verify representative illustrations and particle visibility. Run `python3 generate_index.py`; it validates deck filenames, titles/headings, keys, card IDs, illustration counts, and speech helper requirements before regenerating the index.
3. Test TTS on reveal, replay button, **R** replay, and **Space** reveal. Confirm card selection/loading and a new unflipped card do not speak; verify a sensible Japanese speech target and no errors when TTS is unsupported.
4. Run `python generate_index.py` from the repository root to regenerate the menu. Do not edit the generated `index.html` manually. The Pages workflow builds its own index and publishes on pushes to `main`.
5. Commit and push only when the user asks to upload, publish, or otherwise requests it.

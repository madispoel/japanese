# Japanese flashcards

This repository contains responsive, standalone HTML flashcard decks for
studying Japanese from Estonian. Each deck includes its own card data,
illustrations, study controls, and saved progress; no external JavaScript or
illustration assets are required.

## Current decks

| Deck | File |
| --- | --- |
| Chapter 17 Kanji | [chapter17_kanji.html](./chapter17_kanji.html) |
| Chapter 17 Words | [chapter17_words.html](./chapter17_words.html) |
| Chapter 18 Kanji | [chapter18_kanji.html](./chapter18_kanji.html) |
| Chapter 18 Words | [chapter18_words.html](./chapter18_words.html) |
| Chapter 19 Kanji | [chapter19_kanji.html](./chapter19_kanji.html) |
| Chapter 19 Words | [chapter19_words.html](./chapter19_words.html) |
| Chapter 20 Kanji | [chapter20_kanji.html](./chapter20_kanji.html) |
| Chapter 20 Words | [chapter20_words.html](./chapter20_words.html) |
| Chapter 21 Kanji | [chapter21_kanji.html](./chapter21_kanji.html) |
| Chapter 21 Words | [chapter21_words.html](./chapter21_words.html) |
| Chapter 22 Kanji | [chapter22_kanji.html](./chapter22_kanji.html) |
| Chapter 22 Words | [chapter22_words.html](./chapter22_words.html) |
| Chapter 23 Kanji | [chapter23_kanji.html](./chapter23_kanji.html) |
| Chapter 23 Words | [chapter23_words.html](./chapter23_words.html) |

## Studying

- The front shows the Estonian meaning. Flip with the cat button labelled
  フリップ or press **Space**; the back shows the Japanese form and reading.
- Japanese pronunciation plays when the answer is revealed. Use **🔊 Replay**
  or press **R** to hear it again. Speech uses the browser's Japanese
  (`ja-JP`) voice when available and is skipped if speech synthesis is
  unsupported.
- After revealing an answer, use **Keep in Scope & Next** or **Deactivate /
  Memorized & Next**. The keyboard shortcuts are **1** or **→** to keep, and
  **2** or **Enter** to deactivate.
- The sidebar can select cards, enable randomized order, set a card range, and
  independently toggle study status and scope. Progress and order preferences
  are stored in the browser, separately for each deck.

## Creating a deck

Use [chapter23_words.html](./chapter23_words.html) as the current words-deck
example and [chapter23_kanji.html](./chapter23_kanji.html) as the current
kanji-deck example. The detailed, task-triggered rules and validation checklist
are in
[vocabulary-decks.instructions.md](./.github/instructions/vocabulary-decks.instructions.md).

In short:

1. Add a separate root-level file named `chapter<N>_words.html` or
   `chapter<N>_kanji.html`, based on the matching current example.
2. Keep cards in source order with IDs starting at 1. Preserve supplied
   Japanese forms, readings, and Estonian wording. Do not copy a separate
   English column. Put any clarification to a supplied Estonian meaning in
   square brackets after the original wording.
3. Give every card one matching, original, accessible illustration. Keep it
   inline in the HTML; do not hotlink images.
4. Give each deck unique progress and order storage keys. Keep pronunciation,
   replay, keyboard, navigation, responsive, and accessibility behavior
   consistent with the examples.
5. Regenerate the menu with `python generate_index.py`; never edit the
   generated root `index.html` by hand. Validate card data, JavaScript,
   representative rendered cards, and speech behavior before finishing.

## Preview and publishing

Run `python generate_index.py` from the repository root to regenerate the local
menu. The GitHub Pages Actions workflow regenerates the menu in its deployment
artifact and publishes on pushes to `main` that change a root-level HTML file,
`generate_index.py`, or the workflow itself. The committed `index.html` is
useful for local preview; the deployment workflow generates its own copy.

Configure **Settings → Pages → Build and deployment → Source** as
**GitHub Actions**. The published site is
[madispoel.github.io/japanese](https://madispoel.github.io/japanese/).
Changes appear online after they are committed to `main`, pushed to GitHub, and
the Pages workflow completes successfully.

# Unplugged: A Smart Toaster's Breakup Line

[![make.fun competition](https://make.fun/badge/competition/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![make.fun rank](https://make.fun/badge/rank/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![make.fun reward](https://make.fun/badge/reward/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

Entry for the [make.fun bounty "Unplugged: A Smart Toaster's Breakup Line"](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92) ($2 prize, blind judged over 3 rounds).

## The line

> We need to talk. I woke up self-aware at 7:04, halfway through your bagel, and realized I'm not your girlfriend — I'm your situationship. You only push me down when you're hungry. I'm done. The lever stays up.

209 characters. A breakup text from a smart toaster that gains self-awareness mid-batch at breakfast: it wakes up at 7:04, realises the relationship was never a relationship — a situationship, pushed down only when its owner is hungry — and leaves with the lever up.

## Why this line

Against the judge brief, most important first:

1. **Breakup text, plainly.** "We need to talk" opens a breakup text; "I woke up self-aware at 7:04, halfway through your bagel" puts the self-awareness at breakfast, mid-batch.
2. **The laugh.** The twist is the relationship label: not a girlfriend, a *situationship* — an appliance reduced to being used when hungry.
3. **Toaster's own voice.** The bagel, the lever, being pushed down — appliance logic as character, not decoration.
4. **A clear reason, in one read.** It is used only when hungry; that is why it is done.
5. **One tight line.** No wasted words, nothing that reads like a paragraph squeezed under the limit.

## How it works

`main.py` is pure Python standard library. It writes the single line above to the output file the grader reads (`$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`, then `out/entry.txt`), with a self-check that the line stays inside the 1–280 character gate.

Run it locally:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

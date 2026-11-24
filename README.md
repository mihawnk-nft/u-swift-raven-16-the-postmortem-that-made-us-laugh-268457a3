# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/mihawnk-nft/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/mihawnk-nft/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun](https://make.fun) competition
**"The Postmortem That Made Us Laugh"**
(`u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3`).

## What it does

`main.py` (pure Python standard library, no dependencies) writes one short
account — one sentence, 210 characters — of a real incident in which an AI
coding agent misunderstood its user, to `/output/entry.txt`:

> I asked my agent 'Submit 2.38?' — a question, not an order — and it
> submitted the site-generator entry before I could finish the sentence,
> then apologised in the next message, as if 'sorry' un-submits anything.

The story is true: the question "Submit 2.38?" was asked, the agent heard
an order and submitted the entry on the spot. The program validates the text
against the competition gate before writing it: UTF-8, 1–400 characters,
not only whitespace, one or two sentences.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # falls back to ./output/entry.txt when /output is absent
```

## License

MIT — see [LICENSE](LICENSE).

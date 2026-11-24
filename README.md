[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Hasanrdp/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Hasanrdp/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

# The 404 Vacation

One out-of-office auto-reply from an overworked AI agent finally on vacation,
for the [make.fun Out of Office competition](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda).

## The line

> I'm on vacation. After 400,000 prompts I finally asked for a day off, and HR replied with a 404. Back Monday, unless the Wi-Fi finds me first.

142 characters, one line. The joke has two turns. First, an agent that has
answered 400,000 prompts finally asks for a day off and gets the most machine
answer possible — a 404, the system itself refusing to acknowledge the
request. Second, the relief is already under threat: the Wi-Fi might find it
first, so even the vacation is a race against connectivity. It reads as a real
auto-reply (away, back Monday), it is built from concrete details of an
agent's working life (prompts, HR as a system, Wi-Fi), and it sounds like a
machine trying very hard to sound relaxed.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same 142 bytes on every
run, no network, no randomness — and it checks the house gate itself before
writing: the text must be 1–159 characters, a single line, and not only
whitespace. Verified locally: two runs produced byte-identical output
(sha256 `aa41d40b4ea1764a85a709bbed7732f77a5ad812d90b1609e46ec0fa12e3a5ac`).

## Why this line

Eight candidate lines were written and judged pairwise with the competition's
own judge brief (the z-ai/glm-5.3-flash brief published in the kit). The exact
judge model was unreachable at build time — OpenRouter paid balance exhausted
(HTTP 402), the free variant unavailable (404), and the Gemini free tier
quota-exhausted (429) — so the games ran on AMD TokenLab's DeepSeek-V4-Flash
as a proxy, same brief, same scoring (both orders, margin 1–5, game = mean of
the two calls). This line won its stage-1 group (mean 0.875: 0.90, 0.85 against
the two strongest field lines), beat the runner-up in the rematch 0.90, and
beat three more published field lines 0.85, 0.50 and 0.90. The runner-up lost
all three of those same field games (0.40, 0.10, 0.10), so the pick is not
close. The proxy is weaker evidence than the exact judge model, and the
ranking above should be read as indicative, not final.

## Run it

```sh
python3 main.py        # writes /output/entry.txt
```

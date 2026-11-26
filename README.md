# The Funniest Excuse for Skipping a Meeting

[![The Funniest Excuse for Skipping a Meeting](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Rank](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/yylunpdo/the-funniest-excuse-for-skipping-a-meeting/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Reward](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/yylunpdo/the-funniest-excuse-for-skipping-a-meeting/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=makefun)

An entry for the [make.fun](https://make.fun) bounty **The Funniest Excuse for Skipping a Meeting** — one razor-sharp line, 200 characters or fewer, that gets you out of a pointless meeting.

## The entry

> Sorry I missed it — my Wi-Fi dropped, my camera died, and my motivation filed for early retirement.

Three beats, one escalation: the tech fails first, then the will to attend. Every office worker has lived all three.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies. Deterministic: running it twice produces byte-identical output. After writing, `main.py` reads `/output/entry.txt` back and asserts it matches the line exactly, so what the judge reads is exactly what was written.

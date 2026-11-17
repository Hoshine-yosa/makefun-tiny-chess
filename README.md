# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Hoshine-yosa/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Hoshine-yosa/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,052 bytes of Python: a 0x88 board, negamax with alpha-beta search and iterative deepening, quiescence over captures and checks, MVV move ordering, and a fixed 150,000-node budget per move for fully deterministic play. It plays the make.fun gauntlet through the trial env.

## Practice

Local practice trial-0 (6 games vs the house gauntlet): Elo 876 — 0 wins, 2 draws, 4 losses. Still below the 1,154 final floor. Design: lzma-compressed engine (3,167 bytes as committed; unpacks to a 5,306-byte engine with full piece-square tables, transposition table, killer moves and history heuristic), 0x88 board, negamax + alpha-beta + iterative deepening, quiescence over captures and checks, MVV + TT-move + killer + history ordering, fixed 100,000-node move budget (deterministic, no wall clock).

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>

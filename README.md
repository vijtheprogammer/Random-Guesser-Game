# 🎮 Random Guesser Game

Welcome to the **Random Guesser Game** — a terminal-based Python guessing game with a level-based scoring system and a persistent leaderboard.

---

## 📋 Features

- 🎯 **Four Game Levels** with increasing difficulty
- 🏆 **Scoring System** with bonus points for first-attempt success
- 📈 **Leaderboard Management**:
  - View current standings
  - Add or remove player entries
- 🧠 **Rule Display** for new players
- 🧹 Cross-platform **Terminal Clear Functionality**
- 🗃️ Persistent file-based **score tracking**
- 🛠️ Modular and extensible code structure

---

## 🧠 Game Rules

### 🎯 Objective:
Guess the correct number within the allotted number of attempts to earn points. The fewer guesses you take, the better.

---

### 🕹️ Levels & Scoring:

| Level | Number Range | Guess Limit | Base Points | First-Try Bonus |
|-------|---------------|--------------|--------------|-----------------|
| 1     | 1 - 5         | 3 guesses    | 1 point      | 2x multiplier   |
| 2     | 1 - 10        | 5 guesses    | 3 points     | 2x multiplier   |
| 3     | 1 - 50        | 10 guesses   | 5 points     | 2x multiplier   |
| 4     | 1 - 100       | 20 guesses   | 10 points    | 2x multiplier   |

> ⚠️ Guessing the correct number on the **first attempt** gives you **double points** for that level!

---

### 🧾 Leaderboard Rules:
- Player name, ID, and score are recorded.
- Score is not cumulative across levels yet — each leaderboard entry reflects the most recent round only.
- Leaderboard stored in `leaderboard.txt`.
- You can **remove your own score** using your unique player ID.

---

## ▶️ How to Run

### Requirements:
- Python 3.6 or higher

### Run the Game:
```bash
git clone https://github.com/your-username/random-guesser-game.git
cd random-guesser-game
python main.py

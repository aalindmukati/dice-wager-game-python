# 🎲 Dice Prediction Betting Game (Python)

A simple command-line **dice betting game** written in Python.
Players predict the outcome of a dice roll and wager money on their guess. If the prediction is correct, the player wins double the wager; otherwise, the bet is deducted from their balance.

This project demonstrates **Python fundamentals**, including functions, loops, exception handling, and random number generation.

---

## 📌 Features

* 🎲 Dice prediction betting system
* 💰 Random starting balance for each player
* 🧾 Input validation for safe gameplay
* 🏦 One-time loan system when funds are exhausted
* 📊 Game statistics (rounds played, wins, losses)
* 🧠 Structured code using functions and a `main()` entry point
* 💬 Professional command-line interaction

---

## 🛠 Technologies Used

* **Python 3**
* Python Standard Library:

* `random`

---

## 🎮 How the Game Works

1. The player enters their name.
2. The system assigns a **random starting balance** between `$1000` and `$20000`.
3. Each round:

   * The player places a wager.
   * The player predicts a dice value between **1 and 6**.
   * The program rolls a dice randomly.
4. Results:

   * ✅ Correct guess → Player **wins double the bet**
   * ❌ Incorrect guess → Bet is **deducted**
5. If the balance reaches **$0**, the player may take a **one-time loan** between `$100` and `$1500`.
6. The player can continue playing until they decide to stop or run out of funds.

---

## ▶️ How to Run the Game

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/dice-betting-game.git
```

### 2. Navigate to the project folder

```bash
cd dice-betting-game
```

### 3. Run the program

```bash
python dice_game.py
```

---

## 📂 Project Structure

```
dice-betting-game/
│
├── dice_game.py     # Main game source code
└── README.md        # Project documentation
```

---

## 📸 Example Gameplay

```
Good evening, may I have your name? Aalind

Welcome Mr/Ms Aalind
Your starting balance is: $7421

Enter your wager: $500
Predict the dice outcome (1-6): 3

The dice rolled: 3
Congratulations! Your prediction was correct.
You win double your wager.
```

---

## 🚀 Future Improvements

Possible upgrades for the project:

* 🎨 Colored terminal interface
* 💾 Save player statistics to a file
* 🏆 Leaderboard system
* 📊 Balance history graph
* 🎰 Multiple casino-style games

---

## 👨‍💻 Author

**Aalind**

---

## 📜 License

This project is open-source and available for educational purposes.

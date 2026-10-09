\# 🎮 Tic-Tac-Toe AI



A Python-based Tic-Tac-Toe game where a human player competes against an AI opponent powered by the Minimax algorithm.



This project was developed as \*\*Task 2\*\* for the \*\*CodeOrbit Tech Artificial Intelligence Internship\*\*.



\## ✨ Features



\- Human vs Computer gameplay

\- Minimax-based AI

\- Win detection

\- Loss detection

\- Draw detection

\- Invalid input handling

\- Clear console board

\- Automated unit tests

\- No external Python dependencies



\## 🧠 AI Algorithm



The computer uses the \*\*Minimax algorithm\*\* to evaluate possible future moves.



The scoring system is:



| Result | Score |

|---|---:|

| Computer wins | +1 |

| Draw | 0 |

| Human wins | -1 |



The AI attempts to maximize its score while assuming that the human player will make the best possible move.



\## 📁 Project Structure



```text

Tic-Tac-Toe-AI/

│

├── tic\_tac\_toe.py

├── README.md

├── requirements.txt

│

└── tests/

&#x20;   └── test\_tic\_tac\_toe.py


# Synonym Master

A desktop quiz game to master C1-level English synonyms. Built with Python and Tkinter — no external dependencies.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## What is this?

Synonym Master helps you learn and memorize advanced English vocabulary through a simple quiz format. Each session gives you 30 rounds — a word appears on screen and you pick its synonym from four options.

**Key features:**

- C1-level words with multiple synonyms each
- Words and their synonyms both appear as questions (not just one direction)
- Score tracker in the top-right corner
- Notebook that collects your mistakes so you can review them
- End-of-game summary with all missed words and their synonyms
- Dark themed UI

## Quick Start

```bash
git clone https://github.com/gorkemparadise/synonym-master.git
cd synonym-master
python main.py
```

That's it. No `pip install`, no setup. Tkinter comes built-in with Python.

## How to Play

1. A word appears at the top of the screen
2. Pick the correct synonym from four cards
3. Green = correct, Red = wrong
4. Wrong answers are saved to your notebook (bottom-right)
5. After 30 rounds, review your results and missed words

## Adding Your Own Words

Open `main.py` and add entries to the `DICTIONARY` list:

```python
{"word": "increase", "synonyms": ["rise", "ascend", "go up", "soar"]},
```

Any word in the list (both `word` and its `synonyms`) can appear as a question.

## Requirements

- Python 3.8+
- Tkinter (included with standard Python installations)

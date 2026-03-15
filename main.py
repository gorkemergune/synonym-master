import tkinter as tk
import random

# ─── WORD DICTIONARY ───
DICTIONARY = [
    # ══════════════════════════════════
    #  LESSON 1
    # ══════════════════════════════════
    {"word": "abroad", "synonyms": ["overseas", "internationally"]},
    {"word": "abrupt", "synonyms": ["sudden", "unexpected"]},
    {"word": "acceptable", "synonyms": ["permissible", "allowable"]},
    {"word": "acclaim", "synonyms": ["praise", "commendation"]},
    {"word": "actually", "synonyms": ["truly", "really", "in fact"]},
    {"word": "adverse", "synonyms": ["unfavorable", "harmful"]},
    {"word": "advice", "synonyms": ["suggestion", "recommendation", "guidance"]},
    {"word": "attractive", "synonyms": ["appealing", "alluring", "charming", "gripping", "engaging"]},
    {"word": "autonomous", "synonyms": ["independent", "self-governing", "self-directed"]},
    {"word": "chronic", "synonyms": ["constant", "continual", "persistent"]},
    {"word": "disapproval", "synonyms": ["objection", "criticism"]},
    {"word": "disruptive", "synonyms": ["disturbing", "unsettling"]},
    {"word": "persistent", "synonyms": ["constant", "steady"]},
    {"word": "postpone", "synonyms": ["reschedule", "delay", "defer", "put off"]},
    {"word": "valid", "synonyms": ["convincing", "legitimate", "acceptable"]},
    {"word": "withdraw", "synonyms": ["extract", "remove", "take out"]},

    # ══════════════════════════════════
    #  LESSON 2
    # ══════════════════════════════════
    {"word": "advent", "synonyms": ["arrival", "emergence", "onset"]},
    {"word": "agile", "synonyms": ["nimble", "quick", "dexterous"]},
    {"word": "albeit", "synonyms": ["although", "even though", "though"]},
    {"word": "appealing", "synonyms": ["alluring", "enticing"]},
    {"word": "celebrated", "synonyms": ["renowned", "famous",]},
    {"word": "circumvent", "synonyms": ["evade", "bypass", "dodge"]},
    {"word": "collide", "synonyms": ["crash", "clash", "smash"]},
    {"word": "contemporary", "synonyms": ["current", "modern", "present-day"]},
    {"word": "distribute", "synonyms": ["dispense", "hand out"]},
    {"word": "encourage", "synonyms": ["stimulate", "motivate", "inspire", "boost", "promote", "foster", "support"]},
    {"word": "energetic", "synonyms": ["vigorous", "dynamic", "lively"]},
    {"word": "frail", "synonyms": ["fragile", "delicate", "weak"]},
    {"word": "heyday", "synonyms": ["pinnacle", "prime", "peak"]},
    {"word": "myth", "synonyms": ["legend", "fable"]},
    {"word": "refine", "synonyms": ["perfect", "purify", "improve"]},
    {"word": "worthwhile", "synonyms": ["rewarding", "valuable", "beneficial"]},

    # ══════════════════════════════════
    #  LESSON 3
    # ══════════════════════════════════
    {"word": "alter", "synonyms": ["modify", "change", "adjust"]},
    {"word": "analyze", "synonyms": ["examine", "inspect", "evaluate"]},
    {"word": "ancient", "synonyms": ["old", "archaic", "antique"]},
    {"word": "annoying", "synonyms": ["bothersome", "irritating", "frustrating"]},
    {"word": "anticipate", "synonyms": ["predict", "expect"]},
    {"word": "ascertain", "synonyms": ["determine", "discover", "find out"]},
    {"word": "conform", "synonyms": ["adapt", "comply", "follow"]},
    {"word": "enrich", "synonyms": ["enhance", "improve", "elevate"]},
    {"word": "intensify", "synonyms": ["heighten", "strengthen"]},
    {"word": "intolerable", "synonyms": ["unbearable", "insufferable", "unendurable", "unacceptable"]},
    {"word": "ongoing", "synonyms": ["current", "continuing", "in progress"]},
    {"word": "potential", "synonyms": ["possibility", "prospect", "capability"]},
    {"word": "propose", "synonyms": ["suggest", "recommend", "put forward"]},
    {"word": "restore", "synonyms": ["revitalize", "renew", "repair", "revive"]},
    {"word": "staple", "synonyms": ["essential", "fundamental", "basic", "main"]},
    {"word": "turbulent", "synonyms": ["chaotic", "stormy"]},
    {"word": "vital", "synonyms": ["indispensable", "crucial", "essential"]},

    # ══════════════════════════════════
    #  LESSON 4
    # ══════════════════════════════════
    {"word": "ambiguous", "synonyms": ["vague", "unclear", "uncertain"]},
    {"word": "arbitrary", "synonyms": ["haphazard", "random", "capricious", "subjective"]},
    {"word": "assert", "synonyms": ["declare", "state", "affirm", "claim"]},
    {"word": "astounding", "synonyms": ["astonishing", "amazing"]},
    {"word": "astute", "synonyms": ["perceptive", "shrewd", "sharp"]},
    {"word": "concur", "synonyms": ["agree", "confirm", "correspond"]},
    {"word": "deceptively", "synonyms": ["misleadingly", "falsely", "dishonestly"]},
    {"word": "designate", "synonyms": ["assign", "appoint"]},
    {"word": "elicit", "synonyms": ["extract", "draw out", "obtain"]},
    {"word": "embody", "synonyms": ["exemplify", "represent", "express"]},
    {"word": "instigate", "synonyms": ["initiate", "provoke", "trigger"]},
    {"word": "mundane", "synonyms": ["ordinary", "routine", "commonplace"]},
    {"word": "petition", "synonyms": ["appeal", "request"]},
    {"word": "relinquish", "synonyms": ["abdicate", "surrender", "give up"]},
    {"word": "resilient", "synonyms": ["tenacious", "adaptable"]},
    {"word": "tempt", "synonyms": ["entice", "lure", "attract"]},

    # ══════════════════════════════════
    #  LESSON 5
    # ══════════════════════════════════
    {"word": "baffle", "synonyms": ["puzzle", "confuse", "overwhelm"]},
    {"word": "bear", "synonyms": ["produce", "tolerate", "carry"]},
    {"word": "blur", "synonyms": ["cloud"]},
    {"word": "brilliant", "synonyms": ["radiant", "bright", "intelligent"]},
    {"word": "caution", "synonyms": ["warn", "alert", "advise"]},
    {"word": "enhance", "synonyms": ["strengthen", "boost", "augment", "improve", "enrich"]},
    {"word": "facilitate", "synonyms": ["assist", "ease", "simplify"]},
    {"word": "incessant", "synonyms": ["constant", "nonstop", "persistent"]},
    {"word": "in conjunction with", "synonyms": ["along with", "together with", "combined with"]},
    {"word": "intrigue", "synonyms": ["fascinate", "interest"]},
    {"word": "obstruct", "synonyms": ["block", "hinder"]},
    {"word": "recompense", "synonyms": ["compensation", "repayment"]},
    {"word": "well-suited", "synonyms": ["compatible", "appropriate", "fitting"]},

    # ══════════════════════════════════
    #  LESSON 6
    # ══════════════════════════════════




    # ══════════════════════════════════
    #  LESSON 7
    # ══════════════════════════════════




    # ══════════════════════════════════
    #  LESSON 8
    # ══════════════════════════════════



    # ══════════════════════════════════
    #  LESSON 9
    # ══════════════════════════════════



    # ══════════════════════════════════
    #  EXTRA WORDS
    # ══════════════════════════════════
]

# ─── COLORS (Dark theme) ───
BG = "#0f1117"
SURFACE = "#191c24"
CARD = "#1e222d"
CARD_HOVER = "#262b38"
BORDER = "#2a2f3d"
TEXT = "#e8eaed"
TEXT_DIM = "#8b92a5"
ACCENT = "#6c5ce7"
ACCENT_LIGHT = "#a29bfe"
CORRECT = "#00b894"
CORRECT_BG = "#0d2e26"
WRONG = "#d63031"
WRONG_BG = "#2e1415"
GOLD = "#fdcb6e"

TOTAL_ROUNDS = 30


def get_all_words():
    words = set()
    for entry in DICTIONARY:
        words.add(entry["word"])
        for s in entry["synonyms"]:
            words.add(s)
    return list(words)


def generate_rounds():
    all_words = get_all_words()
    entries = random.sample(DICTIONARY, min(TOTAL_ROUNDS, len(DICTIONARY)))
    rounds = []
    for entry in entries:
        pool = [entry["word"]] + entry["synonyms"]
        question_word = random.choice(pool)
        remaining = [w for w in pool if w != question_word]
        correct_answer = random.choice(remaining)

        distractors = []
        shuffled = random.sample(all_words, len(all_words))
        for w in shuffled:
            if w not in pool and w not in distractors:
                distractors.append(w)
            if len(distractors) == 3:
                break

        options = [correct_answer] + distractors
        random.shuffle(options)
        rounds.append({
            "question": question_word,
            "correct": correct_answer,
            "options": options,
            "all_synonyms": pool,
        })
    return rounds


class SynonymGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Synonym Master — C1 Level")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # Pencere boyutu ve ortalama
        w, h = 700, 680
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

        self.rounds = []
        self.current = 0
        self.score = 0
        self.notebook = []  # yanlış bilinenler
        self.selected = False
        self.option_buttons = []
        self.notebook_visible = False

        # Main container
        self.main_frame = tk.Frame(root, bg=BG)
        self.main_frame.pack(fill="both", expand=True)

        self.show_home()

    # ────────────────────────────────
    #  HOME SCREEN
    # ────────────────────────────────
    def show_home(self):
        self.clear_frame()

        spacer = tk.Frame(self.main_frame, bg=BG, height=80)
        spacer.pack()

        # Badge
        badge = tk.Label(
            self.main_frame, text="  C1 LEVEL  ", font=("Segoe UI", 11, "bold"),
            bg="#1c1638", fg=ACCENT_LIGHT, padx=16, pady=4
        )
        badge.pack(pady=(0, 20))

        # Title
        title = tk.Label(
            self.main_frame, text="Synonym", font=("Georgia", 48, "bold"),
            bg=BG, fg=TEXT
        )
        title.pack(pady=(0, 0))

        subtitle = tk.Label(
            self.main_frame, text="Master", font=("Georgia", 36),
            bg=BG, fg=ACCENT
        )
        subtitle.pack(pady=(0, 20))

        # Description
        desc = tk.Label(
            self.main_frame,
            text="30 rounds. Match each word with its synonym.\nLearn from your mistakes in the notebook.",
            font=("Segoe UI", 13), bg=BG, fg=TEXT_DIM, justify="center"
        )
        desc.pack(pady=(0, 36))

        # Start button
        start_btn = tk.Label(
            self.main_frame, text="  Start Game  ", font=("Segoe UI", 16, "bold"),
            bg=ACCENT, fg="#ffffff", padx=40, pady=14, cursor="hand2"
        )
        start_btn.pack()
        start_btn.bind("<Enter>", lambda e: start_btn.config(bg=ACCENT_LIGHT))
        start_btn.bind("<Leave>", lambda e: start_btn.config(bg=ACCENT))
        start_btn.bind("<Button-1>", lambda e: self.start_game())

        # Footer
        footer = tk.Label(
            self.main_frame, text=f"{len(DICTIONARY)}+ words in the dictionary",
            font=("Segoe UI", 10), bg=BG, fg="#555b6e"
        )
        footer.pack(pady=(30, 0))

    # ────────────────────────────────
    #  GAME START
    # ────────────────────────────────
    def start_game(self):
        self.rounds = generate_rounds()
        self.current = 0
        self.score = 0
        self.notebook = []
        self.selected = False
        self.notebook_visible = False
        self.show_game()

    # ────────────────────────────────
    #  GAME SCREEN
    # ────────────────────────────────
    def show_game(self):
        self.clear_frame()
        rnd = self.rounds[self.current]
        self.selected = False

        # ── Top bar ──
        top_frame = tk.Frame(self.main_frame, bg=BG)
        top_frame.pack(fill="x", padx=30, pady=(20, 0))

        # Progress bar
        progress_bg = tk.Frame(top_frame, bg=CARD, height=6)
        progress_bg.pack(fill="x", pady=(0, 12))
        pct = self.current / TOTAL_ROUNDS
        self.progress_fill = tk.Frame(progress_bg, bg=ACCENT, height=6,
                                       width=max(1, int(640 * pct)))
        self.progress_fill.place(x=0, y=0, relheight=1)

        # Round & Score row
        info_frame = tk.Frame(top_frame, bg=BG)
        info_frame.pack(fill="x")

        round_label = tk.Label(
            info_frame, text=f"Round {self.current + 1} / {TOTAL_ROUNDS}",
            font=("Segoe UI", 12), bg=BG, fg=TEXT_DIM
        )
        round_label.pack(side="left")

        score_label = tk.Label(
            info_frame, text=f"{self.score} / {TOTAL_ROUNDS}",
            font=("Georgia", 16, "bold"), bg=BG, fg=GOLD
        )
        score_label.pack(side="right")

        # ── Question area ──
        q_frame = tk.Frame(self.main_frame, bg=BG)
        q_frame.pack(pady=(40, 10))

        hint_label = tk.Label(
            q_frame, text="FIND THE SYNONYM OF",
            font=("Segoe UI", 11, "bold"), bg=BG, fg=TEXT_DIM, anchor="center"
        )
        hint_label.pack()

        word_label = tk.Label(
            q_frame, text=rnd["question"],
            font=("Georgia", 40, "bold"), bg=BG, fg=TEXT
        )
        word_label.pack(pady=(10, 0))

        # ── Options (2x2 grid) ──
        options_frame = tk.Frame(self.main_frame, bg=BG)
        options_frame.pack(pady=(30, 0))

        self.option_buttons = []
        self.option_frames = []
        letters = ["A", "B", "C", "D"]

        for i, opt in enumerate(rnd["options"]):
            row = i // 2
            col = i % 2

            card = tk.Frame(
                options_frame, bg=CARD, padx=2, pady=2,
                highlightbackground=BORDER, highlightthickness=2,
                cursor="hand2"
            )
            card.grid(row=row, column=col, padx=10, pady=10,
                      ipadx=30, ipady=18, sticky="nsew")

            letter_lbl = tk.Label(
                card, text=letters[i], font=("Segoe UI", 10, "bold"),
                bg=CARD, fg=TEXT_DIM
            )
            letter_lbl.pack(pady=(8, 2))

            word_lbl = tk.Label(
                card, text=opt, font=("Segoe UI", 16, "bold"),
                bg=CARD, fg=TEXT
            )
            word_lbl.pack(pady=(2, 10))

            # Hover effects
            def on_enter(e, c=card, ll=letter_lbl, wl=word_lbl):
                if not self.selected:
                    c.config(bg=CARD_HOVER)
                    ll.config(bg=CARD_HOVER)
                    wl.config(bg=CARD_HOVER)

            def on_leave(e, c=card, ll=letter_lbl, wl=word_lbl):
                if not self.selected:
                    c.config(bg=CARD)
                    ll.config(bg=CARD)
                    wl.config(bg=CARD)

            card.bind("<Enter>", on_enter)
            card.bind("<Leave>", on_leave)

            def on_click(e, option=opt, idx=i):
                self.handle_answer(option, idx)

            card.bind("<Button-1>", on_click)
            letter_lbl.bind("<Button-1>", on_click)
            word_lbl.bind("<Button-1>", on_click)

            self.option_buttons.append((card, letter_lbl, word_lbl, opt))
            self.option_frames.append(card)

        # Sütunları eşit genişlikte yap
        options_frame.columnconfigure(0, weight=1, minsize=260)
        options_frame.columnconfigure(1, weight=1, minsize=260)

        # ── Feedback label (boş başlıyor) ──
        self.feedback_label = tk.Label(
            self.main_frame, text="", font=("Segoe UI", 14, "bold"),
            bg=BG, fg=BG
        )
        self.feedback_label.pack(pady=(20, 0))

        # ── Notebook button (yanlış varsa göster) ──
        if self.notebook:
            self.nb_btn = tk.Label(
                self.main_frame,
                text=f"  📓 {len(self.notebook)} missed  ",
                font=("Segoe UI", 11, "bold"), bg=SURFACE, fg=TEXT_DIM,
                padx=14, pady=8, cursor="hand2",
                highlightbackground=BORDER, highlightthickness=1
            )
            self.nb_btn.pack(side="bottom", anchor="se", padx=20, pady=10)
            self.nb_btn.bind("<Button-1>", lambda e: self.toggle_notebook())

    # ────────────────────────────────
    #  HANDLE ANSWER
    # ────────────────────────────────
    def handle_answer(self, chosen, idx):
        if self.selected:
            return
        self.selected = True
        rnd = self.rounds[self.current]
        is_correct = chosen == rnd["correct"]

        if is_correct:
            self.score += 1
            self.feedback_label.config(text="✓  Correct!", fg=CORRECT)
        else:
            self.feedback_label.config(
                text=f"✗  Correct answer: {rnd['correct']}", fg=WRONG
            )
            self.notebook.append({
                "question": rnd["question"],
                "correct": rnd["correct"],
                "all_synonyms": rnd["all_synonyms"],
            })

        # Kartları renklendir
        for i, (card, letter_lbl, word_lbl, opt) in enumerate(self.option_buttons):
            card.config(cursor="")
            if opt == rnd["correct"]:
                card.config(bg=CORRECT_BG, highlightbackground=CORRECT)
                letter_lbl.config(bg=CORRECT_BG, fg=CORRECT)
                word_lbl.config(bg=CORRECT_BG, fg=CORRECT)
            elif opt == chosen and not is_correct:
                card.config(bg=WRONG_BG, highlightbackground=WRONG)
                letter_lbl.config(bg=WRONG_BG, fg=WRONG)
                word_lbl.config(bg=WRONG_BG, fg=WRONG)
            else:
                card.config(bg=CARD)
                letter_lbl.config(fg="#444a5a")
                word_lbl.config(fg="#444a5a")

        # Sonraki soruya geç
        self.root.after(1300, self.next_round)

    def next_round(self):
        if self.current + 1 >= TOTAL_ROUNDS:
            self.show_result()
        else:
            self.current += 1
            self.show_game()

    # ────────────────────────────────
    #  NOTEBOOK POPUP
    # ────────────────────────────────
    def toggle_notebook(self):
        if self.notebook_visible:
            if hasattr(self, "nb_popup") and self.nb_popup.winfo_exists():
                self.nb_popup.destroy()
            self.notebook_visible = False
            return

        self.notebook_visible = True
        self.nb_popup = tk.Toplevel(self.root)
        self.nb_popup.title("Notebook — Words to Review")
        self.nb_popup.configure(bg=SURFACE)
        self.nb_popup.resizable(False, False)

        pw, ph = 420, min(50 + len(self.notebook) * 52, 500)
        sx = self.root.winfo_x() + self.root.winfo_width() - pw - 30
        sy = self.root.winfo_y() + self.root.winfo_height() - ph - 80
        self.nb_popup.geometry(f"{pw}x{ph}+{sx}+{sy}")

        self.nb_popup.protocol("WM_DELETE_WINDOW", self.toggle_notebook)

        title = tk.Label(
            self.nb_popup, text="📓  Words to Review",
            font=("Segoe UI", 13, "bold"), bg=SURFACE, fg=ACCENT_LIGHT,
            anchor="w"
        )
        title.pack(fill="x", padx=16, pady=(14, 8))

        canvas = tk.Canvas(self.nb_popup, bg=SURFACE, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.nb_popup, orient="vertical",
                                  command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=SURFACE)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for item in self.notebook:
            row = tk.Frame(scroll_frame, bg=SURFACE)
            row.pack(fill="x", padx=16, pady=4)

            q_lbl = tk.Label(
                row, text=item["question"], font=("Segoe UI", 12, "bold"),
                bg=SURFACE, fg=WRONG, anchor="w"
            )
            q_lbl.pack(side="left")

            arrow = tk.Label(
                row, text="  ≈  ", font=("Segoe UI", 12),
                bg=SURFACE, fg=TEXT_DIM
            )
            arrow.pack(side="left")

            syns = [w for w in item["all_synonyms"] if w != item["question"]]
            syn_lbl = tk.Label(
                row, text=", ".join(syns), font=("Segoe UI", 11),
                bg=SURFACE, fg=TEXT_DIM, anchor="w", wraplength=240
            )
            syn_lbl.pack(side="left", fill="x")

            sep = tk.Frame(scroll_frame, bg=BORDER, height=1)
            sep.pack(fill="x", padx=16)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ────────────────────────────────
    #  RESULT SCREEN
    # ────────────────────────────────
    def show_result(self):
        self.clear_frame()
        pct = round((self.score / TOTAL_ROUNDS) * 100)

        if pct >= 90:
            emoji, msg = "🏆", "Outstanding!"
        elif pct >= 70:
            emoji, msg = "🌟", "Great job!"
        elif pct >= 50:
            emoji, msg = "👍", "Good effort!"
        else:
            emoji, msg = "📖", "Keep practicing!"

        spacer = tk.Frame(self.main_frame, bg=BG, height=30)
        spacer.pack()

        # Result card
        card = tk.Frame(self.main_frame, bg=SURFACE, padx=40, pady=30,
                        highlightbackground=BORDER, highlightthickness=2)
        card.pack(padx=60, fill="x")

        emoji_lbl = tk.Label(card, text=emoji, font=("Segoe UI", 48), bg=SURFACE)
        emoji_lbl.pack(pady=(10, 4))

        msg_lbl = tk.Label(card, text=msg, font=("Georgia", 28, "bold"),
                           bg=SURFACE, fg=TEXT)
        msg_lbl.pack()

        score_lbl = tk.Label(
            card, text=f"{self.score} / {TOTAL_ROUNDS}",
            font=("Georgia", 42, "bold"), bg=SURFACE, fg=GOLD
        )
        score_lbl.pack(pady=(8, 2))

        pct_lbl = tk.Label(
            card, text=f"{pct}% correct",
            font=("Segoe UI", 14), bg=SURFACE, fg=TEXT_DIM
        )
        pct_lbl.pack(pady=(0, 16))

        # Notebook summary
        if self.notebook:
            nb_frame = tk.Frame(card, bg=CARD, padx=16, pady=12,
                                highlightbackground=BORDER, highlightthickness=1)
            nb_frame.pack(fill="x", pady=(0, 16))

            nb_title = tk.Label(
                nb_frame, text="📓  Words to Review",
                font=("Segoe UI", 12, "bold"), bg=CARD, fg=ACCENT_LIGHT,
                anchor="w"
            )
            nb_title.pack(fill="x", pady=(0, 8))

            # Canvas for scroll
            canvas = tk.Canvas(nb_frame, bg=CARD, highlightthickness=0,
                               height=min(len(self.notebook) * 38, 180))
            scroll_inner = tk.Frame(canvas, bg=CARD)
            scroll_inner.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=scroll_inner, anchor="nw")
            canvas.pack(fill="x")

            for item in self.notebook:
                row = tk.Frame(scroll_inner, bg=CARD)
                row.pack(fill="x", pady=2)

                q = tk.Label(row, text=item["question"],
                             font=("Segoe UI", 11, "bold"), bg=CARD, fg=WRONG)
                q.pack(side="left")

                a = tk.Label(row, text="  →  ", font=("Segoe UI", 11),
                             bg=CARD, fg=TEXT_DIM)
                a.pack(side="left")

                syns = [w for w in item["all_synonyms"] if w != item["question"]]
                s = tk.Label(row, text=", ".join(syns),
                             font=("Segoe UI", 10), bg=CARD, fg=TEXT_DIM,
                             wraplength=340)
                s.pack(side="left")

        # Play again
        again_btn = tk.Label(
            card, text="  Play Again  ", font=("Segoe UI", 15, "bold"),
            bg=ACCENT, fg="#ffffff", padx=36, pady=12, cursor="hand2"
        )
        again_btn.pack(pady=(10, 10))
        again_btn.bind("<Enter>", lambda e: again_btn.config(bg=ACCENT_LIGHT))
        again_btn.bind("<Leave>", lambda e: again_btn.config(bg=ACCENT))
        again_btn.bind("<Button-1>", lambda e: self.start_game())

    # ────────────────────────────────
    #  UTILITY
    # ────────────────────────────────
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        if hasattr(self, "nb_popup") and self.nb_popup.winfo_exists():
            self.nb_popup.destroy()
        self.notebook_visible = False


if __name__ == "__main__":
    root = tk.Tk()
    app = SynonymGame(root)
    root.mainloop()
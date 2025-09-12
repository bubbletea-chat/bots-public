import bubbletea_chat as bt


def question_1():
    """Q1: How do you spend your ideal weekend?"""
    return [
        bt.Markdown("**Q1. How do you spend your ideal weekend?**"),
        bt.Pills(pills=[
            bt.Pill(text="A. 🌲 Exploring outdoors or going on an adventure", pill_value="A: Exploring outdoors or going on an adventure"),
            bt.Pill(text="B. 🧑‍🤝‍🧑 Hanging out with close friends", pill_value="B: Hanging out with close friends"),
            bt.Pill(text="C. 🍿 Relaxing at home with good food/entertainment", pill_value="C: Relaxing at home with good food/entertainment"),
            bt.Pill(text="D. 🎨 Working on a creative or personal project", pill_value="D: Working on a creative or personal project")
        ])
    ]


def question_2():
    """Q2: What's your natural approach to challenges?"""
    return [
        bt.Markdown("**Q2. What's your natural approach to challenges?**"),
        bt.Pills(pills=[
            bt.Pill(text="A. 💪 Charge head-on with courage", pill_value="A: Charge head-on with courage"),
            bt.Pill(text="B. 🧘 Stay calm and strategize", pill_value="B: Stay calm and strategize"),
            bt.Pill(text="C. 🫂 Work with others to solve it", pill_value="C: Work with others to solve it"),
            bt.Pill(text="D. 🌊 Adapt and go with the flow", pill_value="D: Adapt and go with the flow")
        ])
    ]


def question_3():
    """Q3: Which environment makes you feel most alive?"""
    return [
        bt.Markdown("**Q3. Which environment makes you feel most alive?**"),
        bt.Pills(pills=[
            bt.Pill(text="A. 🏞️ Forests, mountains, or open fields", pill_value="A: Forests, mountains, or open fields"),
            bt.Pill(text="B. 🏙️ Social settings with people buzzing around", pill_value="B: Social settings with people buzzing around"),
            bt.Pill(text="C. ☕ Cozy spots like your favorite café or couch", pill_value="C: Cozy spots like your favorite café or couch"),
            bt.Pill(text="D. ✈️ Unfamiliar places full of surprises", pill_value="D: Unfamiliar places full of surprises")
        ])
    ]


def question_4():
    """Q4: Pick your favorite meal vibe"""
    return [
        bt.Markdown("**Q4. Pick your favorite meal vibe:**"),
        bt.Pills(pills=[
            bt.Pill(text="A. 🥩 A big hearty feast", pill_value="A: A big hearty feast"),
            bt.Pill(text="B. 🍤 Something light and social like tapas", pill_value="B: Something light and social like tapas"),
            bt.Pill(text="C. 🍜 Comfort food (mac & cheese, ramen, etc.)", pill_value="C: Comfort food (mac & cheese, ramen, etc.)"),
            bt.Pill(text="D. 🌮 Something exotic and new you've never tried", pill_value="D: Something exotic and new you've never tried")
        ])
    ]


def question_5():
    """Q5: What best describes your energy?"""
    return [
        bt.Markdown("**Q5. What best describes your energy?**"),
        bt.Pills(pills=[
            bt.Pill(text="A. 🔥 Bold and adventurous", pill_value="A: Bold and adventurous"),
            bt.Pill(text="B. 🛡️ Loyal and protective", pill_value="B: Loyal and protective"),
            bt.Pill(text="C. 🌙 Calm and nurturing", pill_value="C: Calm and nurturing"),
            bt.Pill(text="D. 🌟 Curious and playful", pill_value="D: Curious and playful")
        ])
    ]

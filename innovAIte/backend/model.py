def score_idea(text):
    score = 0

    keywords = ["ai", "innovation", "smart", "automation", "future"]

    for word in keywords:
        if word in text.lower():
            score += 20

    length_score = min(len(text) // 20, 20)
    score += length_score

    return score

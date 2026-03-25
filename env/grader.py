from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def text_similarity(a, b):
    vect = CountVectorizer().fit([a, b])
    vectors = vect.transform([a, b]).toarray()
    return cosine_similarity([vectors[0]], [vectors[1]])[0][0]

def compute_reward(action, gt):
    score = 0

    if action.classification == gt["classification"]:
        score += 0.3

    if action.priority == gt["priority"]:
        score += 0.3

    similarity = text_similarity(action.response, gt["response"])
    score += 0.4 * similarity

    return round(score, 2)

def grader(action, gt, task="hard"):
    if task == "easy":
        return 1.0 if action.classification == gt["classification"] else 0.0

    elif task == "medium":
        score = 0
        if action.classification == gt["classification"]:
            score += 0.5
        if action.priority == gt["priority"]:
            score += 0.5
        return score

    elif task == "hard":
        return compute_reward(action, gt)

    return 0.0
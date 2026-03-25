import requests

BASE_URL = "http://127.0.0.1:8000"

def run():
    results = {}

    for task in ["easy", "medium", "hard"]:
        requests.get(f"{BASE_URL}/reset")

        action = {
            "classification": "query",
            "priority": "medium",
            "response": "Thanks for your email"
        }

        res = requests.post(f"{BASE_URL}/grader?task={task}", json=action)
        results[task] = res.json()

    print(results)

if __name__ == "__main__":
    run()
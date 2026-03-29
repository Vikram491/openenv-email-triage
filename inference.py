import requests

BASE_URL = "https://vikram1412-openenv-email-triage.hf.space"

def run_inference():
    res = requests.post(f"{BASE_URL}/reset")
    obs = res.json()

    action = {
        "classification": "query",
        "priority": "medium",
        "response": "Thanks for your email."
    }

    res = requests.post(f"{BASE_URL}/step", json=action)
    return res.json()


if __name__ == "__main__":
    print(run_inference())
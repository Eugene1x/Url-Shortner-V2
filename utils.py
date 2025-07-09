import hashlib

def generate_short_code(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:6]



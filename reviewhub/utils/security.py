import hashlib
import os

def hash_senha(senha: str) -> str:
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + senha).encode()).hexdigest()
    return f"{salt}:{hashed}"


def verifica_senha(stored_hash: str, password_attempt: str) -> bool:
    salt, hash = stored_hash.split(":")
    attempt_hash = hashlib.sha256((salt + password_attempt).encode()).hexdigest()
    return attempt_hash == hash

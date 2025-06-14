def singleton(cls):
    instancias = {}
    def wrapper(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return wrapper

@singleton
class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")

import redis

def clear_redis():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.delete("todo_urls")  # Elimina la lista de URLs pendientes
    r.delete("done_urls")  # Elimina el conjunto de URLs procesadas
    print("Redis keys 'todo_urls' y 'done_urls' han sido eliminadas.")

if __name__ == "__main__":
    clear_redis()

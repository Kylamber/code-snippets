import string, hashlib, random

def generate(seed, name):
  seed = hashlib.sha512(seed.encode('utf-8')).hexdigest()
  chars = string.ascii_letters + string.digits
  for _ in range(len(name)):
    name = hashlib.sha512(name.encode('utf-8')).hexdigest()
  seed += name
  random.seed(seed)
  length = random.randrange(12, 20)
  return ''.join([random.choice(chars) for _ in range(length)])

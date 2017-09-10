def normalize(x):
  return x.lower()[:1].upper() + x.lower()[1:]
print(list(map(normalize, ['adam', 'LISA', 'barT'])))

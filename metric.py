import string

pct = string.punctuation
articles = ['a','an','the']

def _clean_string(x):
    # lowercase, remove articles, remove punctuation, 
    # and return as a single string without whitespace
    toks = filter(lambda t:t not in articles, x.lower().split())
    return ''.join([''.join(filter(lambda c:c not in pct, list(t))) 
        for t in toks])

def exact_match(x1, x2):
    xc1 = _clean_string(x1)
    xc2 = _clean_string(x2)
    return xc1==xc2

def f1_match(x1, x2):
    # x1 is treated as Ground Truth.
    tok1 = set(map(lambda t:_clean_string(t), x1.split()))
    tok2 = set(map(lambda t:_clean_string(t), x2.split()))
    l1 = len(tok1)
    l2 = len(tok2)
    ovr = len(tok1.intersection(tok2))
    if ovr==0: return 0.
    prec = float(ovr)/l2
    rec = float(ovr)/l1
    return 2*prec*rec/(prec+rec)

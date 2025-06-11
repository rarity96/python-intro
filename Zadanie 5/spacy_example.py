import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying a startup in the UK.")

print("Tokens:", [token.text for token in doc])

print("Named Entities:", [(ent.text, ent.label_) for ent in doc.ents])

print("POS Tags:", [(token.text, token.pos_) for token in doc])
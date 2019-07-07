import spacy
from spacy.lang.es import Spanish
from spacy.pipeline import EntityRuler
from spacy_lookup import Entity

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)

patterns = [{"label": "luis", "pattern": "luis"},
            {"label": "luis", "pattern": [{"lower": "san"}, {"lower": "luis"}]},
            {"label": "pollo", "pattern": "pollo"},
            {"label": "pollo", "pattern": [{"lower": "el"}, {"lower": "pollo"}]},
            {"label": "pollo", "pattern": [{"lower": "via"}, {"lower": "el"},{"lower": "pollo"}]},
            {"label": "pollo", "pattern": [{"lower": "variante"}, {"lower": "romelia"}]},
            {"label": "pollo", "pattern": [{"lower": "variante"}, {"lower": "el"}, {"lower": "pollo"} ]},
            {"label": "pollo", "pattern": [{"lower": "variante"}, {"lower": "romelia"}, {"lower": "el"}, {"lower":"pollo"}]},
            {"label": "invico", "pattern": "invico"},
            {"label": "victoria", "pattern": "victoria"},
            {"label": "montelibano", "pattern": "montelibano"},
            {"label": "nicolas", "pattern": "nicolás"},
            {"label": "nicolas", "pattern": "nicolas"},
            {"label": "utp", "pattern": "utp"},
            {"label": "utp", "pattern": "tecnologica"},
            {"label": "dosquebradas", "pattern": "dosquebradas"},
            {"label": "terminal", "pattern": "terminal"},
            {"label": "terminal", "pattern": [{"lower": "la"}, {"lower": "terminal"}]},
            {"label": "terminal", "pattern": [{"lower": "el"}, {"lower": "terminal"}]}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

puntos = []
#doc = nlp(u"rutas que me lleven de san luis a pollo")
def clasification(texto):
    doc = nlp(texto)
    for ent in doc.ents:
        puntos.append(ent.label_)
    return puntos

"""
for token in doc:
    if token._.is_entity:
        print(token.text)
for ent in doc.ents:
    print(ent.text,ent.label_)
"""
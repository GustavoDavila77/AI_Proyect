import spacy
from spacy.lang.es import Spanish
from spacy.pipeline import EntityRuler
from spacy_lookup import Entity

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)

{"label": "frailes", "pattern": "frailes"},
{"label": "luis", "pattern": [{"lower": "san"}, {"lower": "luis"}]},
{"label": "pollo", "pattern": [{"lower": "via"}, {"lower": "el"},{"lower": "pollo"}]},

patterns = [{"label": "frailes", "pattern": "frailes"},
        {"label": "santiago londoño", "pattern": [{"lower": "santiago"}, {"lower": "londoño"}]},
        {"label": "camilo mejia", "pattern": [{"lower": "camilo"}, {"lower": "mejía"}]},
        {"label": "naranjales", "pattern": "naranjales"},
        {"label": "los rosales", "pattern": [{"lower": "los"}, {"lower": "rosales"}]},
        {"label": "las violetas", "pattern": [{"lower": "las"}, {"lower": "violetas"}]},        
        {"label": "los lagos", "pattern": [{"lower": "los"}, {"lower": "lagos"}]},
        {"label": "la pradera", "pattern": [{"lower": "la"}, {"lower": "pradera"}]},
        {"label": "carrera 21", "pattern": [{"lower": "carrera"}, {"lower": "21"}]},
        {"label": "av santa monica", "pattern": [{"lower": "avenida"}, {"lower": "santa"},{"lower":"monica"}]},
        {"label": "carrera 19 a", "pattern": [{"lower": "carrera"}, {"lower": "19"},{"lower": "a"}]},
        {"label": "calle 12", "pattern": [{"lower": "calle"}, {"lower": "12"}]},
        {"label": "calle 13", "pattern": [{"lower": "calle"}, {"lower": "13"}]},
        {"label": "carrera 17", "pattern": [{"lower": "carrera"}, {"lower": "17"}]},
        {"label": "calle 8", "pattern": [{"lower": "calle"}, {"lower": "8"}]},
        {"label": "la popa", "pattern": [{"lower": "la"}, {"lower": "popa"}]},
        {"label": "interseccion viaducto", "pattern": "viaducto"},
        {"label": "puente mosquera", "pattern": [{"lower": "puente"}, {"lower": "mosquera"}]},
        {"label": "av del rio", "pattern": [{"lower": "avenida"}, {"lower": "del"},{"lower": "rio"}]},
        {"label": "interseccion turin", "pattern": "turin"},
        {"label": "av 30 de agosto", "pattern": [{"lower": "avenida"}, {"lower": "30"},{"lower": "de"},{"lower":"agosto"}]},
        {"label": "calle 50", "pattern": [{"lower": "calle"}, {"lower": "50"}]},
        {"label": "popa", "pattern": "popa"},
        {"label": "luis", "pattern": "luis"},
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

#doc = nlp(u"rutas que me lleven de san luis a pollo")
def clasification(texto):
    puntos = []
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
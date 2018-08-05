# Zadanie #11
# Zaimplementuj klasy odpowiedzialne za tworzenie dokumenty w
# składni MarkDown. Stwórz klase bazowa Element zawierajaca
# podstawowa implementacje metody render() oraz kilka jej klas
# pochodnych. Stwórz klase Document umozliwiajaca wyrendorowanie
# dodanych elementów.
# Przykład uzycia:
# >>> document = Document()
# >>> document.add_element(HeaderElement('Header'))
# >>> document.add_element(LinkElement('ABC', 'abc.com'))
# >>> document.add_element(Element('Simple'))
# >>> document.render()
# Header
# ======
# (ABC)[http://abc.com]
# Simple


class Element:
    def __init__(self, element):
        self.element = element

    def render(self):
        return (self.element)


class HeaderElement(Element):
    def render(self):
        return self.element + "\n======"


class LinkElement(Element):
    def __init__(self, link1, link2):
        self.link1 = link1
        self.link2 = link2

    def render(self):
        return "(" + self.link1 + ")" + "[http://" + self.link2 + "]"


class Document:
    def __init__(self):
        self.document = []

    def add_element(self, element):
        self.document.append(element.render())

    def render(self):
        for i in self.document:
            print(i)


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()

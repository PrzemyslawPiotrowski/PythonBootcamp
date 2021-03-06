class Element:
    def __init__(self, element):
        self.element = element

    def render(self):
        return self.element


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
        print('\n'.join(self.document))


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()

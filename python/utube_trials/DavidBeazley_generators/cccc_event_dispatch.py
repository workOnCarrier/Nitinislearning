# xml parsing with corotines

# sample SAX parser
import xml.sax

from utube_trials.DavidBeazley_generators.building_blocks import coroutine


class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(f"start element \t\t {name}")

    def endElement(self, name):
        print(f"end element \t\t {name}")

    def characters(self, text):
        print(f"characters \t\t {repr(text)[:40]}")


def play_with_oo_sax():
    xml.sax.parse("sample_xml.xml", MyHandler())


class CoEventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target

    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))

    def endElement(self, name):
        self.target.send(('end', name))

    def characters(self, text):
        self.target.send(('text', text))


@coroutine
def printer():
    while True:
        event = yield
        print(event)

@coroutine
def buses_to_dict(target):
    while True:
        event, value = yield
        if event == 'start' and value[0] == 'bus':
            bus_dict = {}
            fragments = []
            while True:
                event, value = yield
                if event == 'start': fragments = []
                elif event == 'text': fragments.append(value)
                elif event == 'end':
                    if value != 'bus':
                        bus_dict[value] = "".join(fragments)
                    else:
                        target.send(bus_dict)
                        break



def play_with_co_sax():
    xml.sax.parse("sample_xml.xml", CoEventHandler(printer()))

def play_with_co_dict_sax():
    xml.sax.parse("sample_xml.xml", CoEventHandler(buses_to_dict(printer())))

if __name__ == "__main__":
    # play_with_co_sax()
    play_with_co_dict_sax()

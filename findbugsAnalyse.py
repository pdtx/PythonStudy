from xml.dom import minidom
import operator


def is_same():
    if sourceLines.__len__() == 1:
        return
    if sourceLines.__len__() == 2:
        if sourceLines[0].getAttribute('start') ==  sourceLines[1].getAttribute('start') and sourceLines[0].getAttribute('end') == sourceLines[1].getAttribute('end'):
            return
        else:
            print(str(sourceLines[0].toxml()))
            print(str(sourceLines[1].toxml()))
    else:
        return


doc = minidom.parse('findbugs.xml')
root = doc.documentElement
bugInstances = root.getElementsByTagName('BugInstance')

for bugInstance in bugInstances:
    sourceLines = bugInstance.getElementsByTagName('SourceLine')
    is_same()

# print(root)

if __name__ == '__main__':
    print("a")
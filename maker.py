from bs4 import BeautifulSoup
from urllib.request import urlopen


class Course():
    name = ""
    id = 0
    required = []
    topics = []

    def __init__(self, name, id, prereq, coreq, topics):
        self.name = name
        self.id = id
        self.prereq = prereq
        self.coreq = coreq
        self.topics = topics

def contains(text, substr):
    for s in substr:
        if(s in text):
            return True
    return False

def set_courses(soup, courses):
    table = soup.find('div', {'id':'contentleft'}).find_all('table')[0].find_all('tr')[2].find('td').find_all('table')[1]
    ps = table.find('tr').find('td')
    current = -1

    for p in ps.children:
        if(p.name == 'h3'):
            current += 1
            course = Course(str(p.get_text()).rstrip(), current, [], [], [])
            courses.append(course)
        elif(p.name == 'a'):
            if(p.previous_sibling == 'Prereq: '):
                pres = [p.get_text()]
                while(contains(str(p.next_sibling), [',', ';', 'or', 'permission'])):
                    p = p.next_sibling.next_sibling
                    if(p.name != 'i'):
                        pres.append(p.get_text())
                courses[current].prereq = pres
        elif(p.name == 'i'):
            c = []
            links = p.find_all('a')
            for l in links:
                c.append(l.get_text())
            if(len(c) != 0):
                courses[current].coreq = c

def print_courses(courses):
    for c in courses:
        print('name: ', c.name)
        print('id: ', c.id)
        print('prereq: ')
        if(len(c.prereq) != 0):
            for r in c.prereq:
                print(r)
        else:
            print('none')
        print('coreq: ')
        if(len(c.coreq) != 0):
            for co in c.coreq:
                print(co)
        else:
            print('none')
        print('\n\n')

cs_requirements = "http://student.mit.edu/catalog/m6a.html"
r = urlopen(cs_requirements)
soup = BeautifulSoup(r, 'html5lib')
courses = []

set_courses(soup, courses)
print_courses(courses)
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        print('Object to be encoded : ', type(o))
        obj = dict()
        if type(o) == Course:
            obj = o.__dict__
            obj['class'] = 'Course'
            return obj
        if type(o) == Student:
            obj = o.__dict__
            obj['class'] = 'Student'
            return obj

class CustomDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)
        
    def dict_to_object(self, o):
        print('Object to be decoded : ', o)
        obj = None
        if o['class'] == 'Course':
            obj = Course(o['_courseName'], o['_grade'])
        if o['class'] == 'Student':
            obj = Student(o['_cwid'], o['_firstName'], o['_lastName'])
            obj._courses = o['_courses']
        return obj

class Course:
    def __init__(self, cn, g):
        self._courseName = cn
        self._grade = g

class Student:
    def __init__(self, cw, fn, ln):
        self._cwid = cw
        self._firstName = fn
        self._lastName = ln
        self._courses = []

    def addCourse(self, cn, g):
        self._courses.append(Course(cn, g))

lObj = list()
pObj = Student(12345, 'John', 'Chen')
print(pObj)
pObj.addCourse('math', 'b')
pObj.addCourse('english', 'a')
pObj.addCourse('art', 'a')
print(pObj)

outString = json.dumps(pObj, cls=CustomEncoder, indent=4)
print(outString)

inObj = json.loads(outString, cls=CustomDecoder)
print(inObj)
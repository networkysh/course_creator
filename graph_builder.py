class GraphNode(object):
    def __init__(name="", prereqs=[]):
        self.name = name
        self.prereqs = prereqs
class Elective(GraphNode):
class MajorElective(GraphNode):
class Required(GraphNode):
class SomeOf(GraphNode):
    def __init__(groupName="", num=0, options=[]):
        super(groupName, [])
        self.num = num
        self.options = options

def annotateCourseList(courseList, major):
    def annotate(course, major):
        if course.name in major.required:
            return Required(course.name, course.prereqs)
        else:
            for option in major.optionals:
                num = option.numRequired
                options = filter(courseList, lambda x: x.name == course)[0] for course in option.courses
    return annotate(course, major) for course in courseList:
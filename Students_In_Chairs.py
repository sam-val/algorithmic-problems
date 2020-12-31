class Pos:
    def __init__(self, pos_n, student=None):
        self.student = student
        self.pos_n = pos_n
        self.children = []

    def make_tree(self, students, chairs_n):
        if chairs_n == 0:
            return

        for s in students:
            pos = Pos(pos_n=self.pos_n+1, student=s)
            self.insert(pos)
            temp = students.copy()
            temp.remove(s)
            self.children[-1].make_tree(temp,chairs_n-1)
            # print(f'pos: {pos}', f'set: {students}')

    def insert(self, pos):
        # print(f'appending {pos}')
        self.children.append(pos)

    def print(self, rs):
        if not self.children:
            rs.append(self.student)
            print(rs)
        else:
            if self.student is not None:
                rs.append(self.student)
            for child in self.children:
                child.print(rs[:])

    def __str__(self):
        return f"pos {self.pos_n}, student: {self.student}"

class MyTree():
    def __init__(self, students, chairs_n):
        self.students = students
        self.chairs_n = chairs_n
        self.root = Pos(pos_n=0, student=None)

    def create_tree(self):
         self.root.make_tree(self.students,self.chairs_n)

    def print_tree(self):
        rs = []
        self.root.print(rs)


students = {'A', 'B', 'C'}
chairs = 2
t = MyTree(students, chairs)
t.create_tree()
t.print_tree()

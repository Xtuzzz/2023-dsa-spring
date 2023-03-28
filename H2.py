class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class LinkStack():
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def push(self, item):
        a = Node(item)
        a.setNext(self.head)
        self.head = a
        self.length += 1

    def pop(self):
        a = self.head.getData()
        self.head = self.head.getNext()
        self.length -= 1
        return a

    def peek(self):
        return self.head.getData()

    def size(self):
        return self.length


class LinkQueue():
    def __init__(self):
        self.head = None
        self.di = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def enqueue(self, a):
        di = Node(a)
        if self.length == 0:
            self.head = self.di = di
        else:
            self.di.setNext(di)
            self.di = self.di.getNext()
        self.length += 1

    def dequeue(self):
        assert self.length >= 1
        a = self.head.getData()
        if self.length == 1:
            self.head = self.di = None
        else:
            self.head = self.head.getNext()
        self.length -= 1
        return a

    def size(self):
        return self.length


# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__
class DoublyLinkedList():
    def __init__(self, item=None):
        self.a = []
        self.count = 0
        self.head = None
        self.tail = None
        self.length = 0
        if item is not None:
            if hasattr(item, "__iter__"):
                for i in item:
                    self.append(i)
            else:
                self.append(item)

    def isEmpty(self):
        return self.head is None

    def getTail(self):
        return self.tail

    def add(self, s):
        a = Node(s)
        if self.head is None:
            self.head = self.tail = a
        else:
            self.head.setPrev(a)
            a.setNext(self.head)
            self.head = a
        self.length += 1

    def search(self, s):
        a = self.head
        while a is not None:
            if a.getData() == s:
                return True
            else:
                a = a.getNext()
        else:
            return False

    def size(self):
        return self.length

    __len__ = size

    def remove(self, s):
        a = self.head
        while not a is None:
            if a.getData() == s:
                if a == self.head:
                    self.head = self.head.getNext()
                    self.head.prev = None
                elif a == self.tail:
                    self.tail = self.tail.getPrev()
                    self.tail.next = None
                else:
                    a.getPrev().setNext(a.getNext())
                    a.getNext().setPrev(a.getPrev())
                self.length -= 1
                break
            else:
                a = a.getNext()

    def append(self, s):
        a = Node(s)
        if self.head is None:
            self.head = self.tail = a
        else:
            self.tail.setNext(a)
            a.setPrev(self.tail)
            self.tail = a
        self.length += 1

    def index(self, s):
        a = self.head
        n = 0
        while a is not None:
            if a.getData() == s:
                break
            a = a.getNext()
            n += 1
        else:
            return None
        return n

    def pop(self, n=None):
        assert self.length >= 1

        if n is None:
            n = self.length - 1
        a = self.head
        for i in range(n):
            a = a.getNext()
        b = a.getData()

        if self.length == 1:
            self.head = self.tail = None
        else:
            if a == self.head:
                self.head = a.getNext()
                self.head.prev = None
            elif a == self.tail:
                self.tail = a.getPrev()
                self.tail.next = None
            else:
                if a.getPrev() is not None:
                    a.getPrev().setNext(a.getNext())
                if a.getNext() is not None:
                    a.getNext().setPrev(a.getPrev())
        self.length -= 1
        return b

    def insert(self, n, s):
        if abs(n) >= self.length:
            n = abs(n) // n * self.length
        if n < 0:
            n += self.length

        a = self.head
        for i in range(n):
            a = a.getNext()
        if a is None:
            if self.head is None:
                self.add(s)
            else:
                self.append(s)
        else:
            b = Node(s)
            b.setNext(a)
            b.setPrev(a.getPrev())
            if a != self.head:
                b.getPrev().setNext(b)
            a.setPrev(b)
        self.length += 1

    def __str__(self):
        a = []
        b = self.head
        while b is not None:
            a.append(b.getData())
            b = b.getNext()
        if len(a) > 1:
            return f'DoublyLinkedList({a})'
        else:
            return repr(a[0])

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, s):
        a = []
        b = self.head
        for i in range(self.length):
            a.append(b.getData())
            b = b.getNext()
        c = a[s]
        if isinstance(c, list):
            return DoublyLinkedList(c)
        else:
            return c

    def __eq__(self, others):
        if others is None or not isinstance(others, DoublyLinkedList):
            return False
        if len(self) != len(others):
            return False
        a, b = self.head, others.head
        for i in range(self.length):
            if a.getData() == b.getData():
                a, b = a.getNext(), b.getNext()
            else:
                return False
        else:
            return True

    def __iter__(self):
        self.a.append(0)
        self.count += 1
        return self

    def __next__(self):
        if self.a[self.count - 1] < self.length:
            out = self.__getitem__(self.a[self.count - 1])
            self.a[self.count - 1] += 1
            return out
        self.count -= 1
        self.a.pop()
        raise StopIteration
    # 检验


# uuid_share#  dad110f3-7cd9-4957-ba45-9e2a5165a722  #
# PKUDSA H2 随机测试样例P1

from random import randrange, shuffle, choice
from sys import stderr, stdout

print_bak = globals().get('print_bak', print)  # 使用另行备份的print函数

from collections import Counter


class Node:  # 检测规范调用接口
    invalid_key = Counter()

    def __init__(self, initdata=None):
        self.__data = initdata
        self.__next = None
        self.__prev = None

    for k in ('data', 'next', 'prev'):
        exec(
            f'''@property
def {k}(self):
    self.invalid_key['get_'+'{k}']+=1
    return getattr(self,'get'+'{k.capitalize()}')()
@{k}.setter
def {k}(self,val):
    self.invalid_key['set_'+'{k}']+=1
    getattr(self,'set'+'{k.capitalize()}')(val)''', globals(), locals())

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

    def setPrev(self, newprev):
        self.__prev = newprev


# SESSDSA20 H3 随机测试样例P2
LINE_WIDTH = 50
N_TESTS = 10
N_OPS = 20

from collections import deque
from random import randrange, choice
from sys import stderr

if 'ref ds':

    class ref_node:
        def __init__(self, lst, ind):
            self.lst = lst
            self.ind = ind

        def getData(self):
            return self.lst[self.ind]

        def getNext(self):
            return ref_node(self.lst, self.ind + 1)

        def getPrev(self):
            return ref_node(self.lst, self.ind - 1)

        def setData(self, newdata):
            self.lst[self.ind] = newdata

        def __eq__(self, other):
            try:
                return self.getData() == other.getData()
            except:
                return False


    ref_node.__str__ = lambda self: 'Node(%r)' % self.getData()
    Node.__str__ = Node.__repr__ = ref_node.__repr__ = ref_node.__str__


    class ref_list:
        isEmpty = lambda self: not self.lst
        add = lambda self, item: self.lst.insert(0, item)
        search = lambda self, item: item in self.lst
        size = __len__ = lambda self: len(self.lst)

        def __init__(self, ref_type, it=None):
            self.ref_type = ref_type
            self.lst = []
            if it:
                for i in it:
                    self.lst.append(i)

        def getTail(self):
            assert self.size() > 0
            return ref_node(self.lst, len(self) - 1)

        def __getitem__(self, arg):
            res = self.lst[arg]
            if isinstance(arg, slice):
                res = ref_list(self.ref_type, res)
            return res

        def __eq__(self, other):
            try:
                if len(self) != len(other):
                    return False
                tmp = [(self[i], other[i]) for i in range(len(self))]
                return all(i == j for i, j in tmp)
            except:
                return False

        __str__ = __repr__ = lambda self: f'{self.ref_type.__name__}({self.lst})'


    class ref_deque(deque):
        push = deque.append
        peek = lambda self: self[-1]
        enqueue = deque.append
        dequeue = deque.popleft
        isEmpty = lambda self: not bool(self)
        size = deque.__len__


def test(i, t_lst, r_lst, op_write, op_read):
    print_bak('TEST #%d' % i, end='')
    _SIZE = 0
    passed = True
    ops = []
    params = []

    def get(param):
        if param == 'num':
            return randrange(N_OPS)
        elif param == 'numstr':
            if randrange(2):
                return randrange(N_OPS)
            return str(randrange(10))
        elif param == 'len':
            return randrange(_SIZE)
        elif param == '-len':
            return randrange(_SIZE) - _SIZE
        elif param == 'slice':
            a = randrange(_SIZE - 1)
            b = randrange(a, _SIZE + 1)
            return slice(a, b, randrange(1, 10))

    def one_check(op):
        ref_exec = True
        op = op.split()

        try:
            params.clear()
            params.extend(map(get, op[1:]))
            r_ref = getattr(r_lst, op[0])(*params)
        except:
            ref_exec = False

        if ref_exec:
            r_test = getattr(t_lst, op[0])(*params)
            if r_ref != None:
                assert r_ref == r_test, '输出: %r;\n应该输出: %r' % (r_test, r_ref)
                if isinstance(r_ref, ref_list):
                    assert type(
                        r_test) == r_ref.ref_type, '输出类型错误: %s;\n应为: %s' % (
                        type(r_test).__name__, r_ref.ref_type.__name__)

            ops.append((op[0], *params))

    def output(op):
        func = op[0]
        params = ','.join(map(repr, op[1:]))
        return '%s(%s)' % (func, params)

    try:
        for i in range(N_OPS):
            # write one
            curr_op = choice(op_write)
            one_check(curr_op)

            # update size
            _SIZE = len(r_lst)

            # read one
            curr_op = choice(op_read)
            one_check(curr_op)

        print_bak(' PASS')
    except Exception as e:
        print_bak('\n出错的操作:', output((curr_op.split()[0], *params)))
        print_bak('历史操作:', ','.join(map(output, ops)))
        print_bak('报错: (%s: %s)' % (type(e).__name__, str(e)), file=stderr)
        try:
            print_bak('LAST LISTS'.center(LINE_WIDTH, '.'))
            print_bak('参考列表:', r_lst)
            print_bak('测试列表:', t_lst)
        except Exception as e:
            print_bak('打印报错 (%s: %s)' % (type(e).__name__, str(e)),
                      file=stderr)
        print_bak('END'.center(LINE_WIDTH, '.'))


def test_code(title, code):
    print_bak(title, end=':\n')
    # print_bak('Code'.center(LINE_WIDTH, '.'))
    # print_bak(code)
    try:
        exec(code, globals())
    except Exception as e:
        print_bak('报错 (%s: %s)' % (type(e).__name__, str(e)), file=stderr)


def prev_iter(lst):
    node = lst.getTail()
    res = []
    for i in range(len(lst)):
        res.append(node.getData())
        node = node.getPrev()
    return res


def safe_iter(lst):
    lst_iter = iter(lst)
    try:
        for i in range(len(lst)):
            yield next(lst_iter)
    except Exception as e:
        yield '报错 (%s: %s)' % (type(e).__name__, str(e))
    try:
        not_end = next(lst_iter)
        yield 'NOT END'
    except:
        pass


# push pop peek
print_bak('\n' + "1 LinkStack".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    test(i, LinkStack(), ref_deque(), (
        'push num',
        'pop',
    ), (
             'isEmpty',
             'peek',
             'size',
         ))

# enqueue dequeue
print_bak('\n' + "2 LinkQueue".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    test(i, LinkQueue(), ref_deque(), (
        'enqueue num',
        'dequeue',
    ), (
             'isEmpty',
             'size',
         ))

# getTail
print_bak('\n' + "3 DoublyLinkedList".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    l1 = DoublyLinkedList()
    l2 = ref_list(DoublyLinkedList)
    test(i, l1, l2, (
        'append numstr',
        'add numstr',
        'insert len numstr',
        'pop len',
        'pop',
        'remove numstr',
    ), (
             'isEmpty',
             'search numstr',
             'size',
             '__len__',
             'index numstr',
             '__getitem__ len',
             '__getitem__ slice',
             'getTail',
         ))
    test_code(
        'prev link test', r'''r1=prev_iter(l1)
r2=l2[::-1]
if r1==r2:
    print_bak('PASS')
else:
    print_bak('双链表倒序结果: ',r1,file=stderr)
    print_bak('参考结果: ',r2,file=stderr)''')

comment = '''
注：prev link test用于测试双链表反向连接情况
以上为必做内容，以下为选做内容
'''
try:
    from browser import document

    target = document['py_stdout']
    target.innerHTML += f'<span style="color:blue">{comment}</span>'
except ImportError:
    print_bak(comment, file=stderr)


# Additional


def print_helper(text, cond):
    print_bak(text, end=' ')
    print_bak(cond, file=stdout if cond else stderr)


print_bak('\n' + "Ex DoublyLinkedList".center(LINE_WIDTH, '='))
test_code(
    '__eq__+__iter__ test', '''lst=DoublyLinkedList(range(5))
print_bak('lst:',lst)
print_helper('lst==DoublyLinkedList(range(5)) -> T:',lst==DoublyLinkedList(range(5)))
print_helper('lst!=DoublyLinkedList(range(6)) -> T:',lst!=DoublyLinkedList(range(6)))
print_helper('lst!=list(range(5)) -> T:',lst!=list(range(5)))
print_helper('lst!=None -> T:',lst!=None)
print_helper('lst==DoublyLinkedList(lst) -> T:',lst==DoublyLinkedList(safe_iter(lst)))
print_helper('多iter测试 -> T:',
    [
        (x,y) for x in safe_iter(lst) for y in safe_iter(lst)
    ]==[
        (x,y) for x in range(5) for y in range(5)
    ])''')

if Node.invalid_key:
    print_bak('非法调用:', dict(Node.invalid_key), file=stderr)

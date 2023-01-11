0x0B. Python - Input/Output
===================================

Tasks
-----

### 0. Read file

Write a function that reads a text file (`UTF8`) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ 
```

Notest cases needed

Repo: 

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `0-read_file.py`

### 1. Write to a file

Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ 

```

No test cases needed

Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0B-python-input_output`
- File: `1-write_file.py`

### 2. Append to a file

Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:~/0x0B$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/0x0B$

```

No test cases needed

Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0B-python-input_output`
- File: `2-append_write.py`

### 3. To JSON string

Write a function that returns the JSON representation of an object (string):

- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

```

guillaume@ubuntu:~/0x0B$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ 

```

No test cases needed

Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0B-python-input_output`
- File: `3-to_json_string.py`

### 4. From JSON string to Object

Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

```
guillaume@ubuntu:~/0x0B$ cat 4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/0x0B$ 
```

No test cases needed

Repo:

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `4-from_json_string.py`

### 5. Save Object to a file

Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.

```
guillaume@ubuntu:~/0x0B$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./5-main.py
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/0x0B$ cat my_set.json ; echo ""

guillaume@ubuntu:~/0x0B$ 
```

No test cases needed

Repo: 

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `5-save_to_json_file.py`

### 6. Create object from a JSON file

Write a function that creates an Object from a “JSON file”:

Prototype: `def load_from_json_file(filename):`
You must use the `with` statement
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
You don’t need to manage file permissions / exceptions.

```
guillaume@ubuntu:~/0x0B$ cat my_fake.json
{"is_active": true, 12 }
guillaume@ubuntu:~/0x0B$ cat 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/0x0B$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
guillaume@ubuntu:~/0x0B$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/0x0B$ 

```

No test cases needed

Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0B-python-input_output`
- File: `6-load_from_json_file.py`

### 7. Load, add, save

Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.

```
guillaume@ubuntu:~/0x0B$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/0x0B$ ./7-add_item.py
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
[]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py Best School
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School"]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
guillaume@ubuntu:~/0x0B$ 

```

No test cases needed

Repo:

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `7-add_item.py`

### 8. Class to JSON

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 8-my_class.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

guillaume@ubuntu:~/0x0B$ cat 8-main.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/0x0B$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/0x0B$ 
guillaume@ubuntu:~/0x0B$ cat 8-my_class_2.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

guillaume@ubuntu:~/0x0B$ cat 8-main_2.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/0x0B$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
guillaume@ubuntu:~/0x0B$

```

No test cases Needed

Repo:

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `8-class_to_json.py`

### 9. Student to JSON

Write a class `Student` that defines a student by:

* Public instance attributes:

- `first_name`
- `last_name`
- `age`

- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 9-main.py 
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

guillaume@ubuntu:~/0x0B$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
guillaume@ubuntu:~/0x0B$

```

No test cases needed

Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0B-python-input_output`
- File: `9-student.py`

### 10. Student to JSON with filter

Write a class `Student` that defines a student by: (based on `9-student.py`)

* Public instance attributes:

- `first_name`
- `last_name`
- `age`

- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
* Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
 - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
 - Otherwise, all attributes must be retrieved
- You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 10-main.py 
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

guillaume@ubuntu:~/0x0B$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
guillaume@ubuntu:~/0x0B$

```

No test cases Needed

Repo:

GitHub repository: `alx-higher_level_programming`
Directory: `0x0B-python-input_output`
File: `10-student.py`


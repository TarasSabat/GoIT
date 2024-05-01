from jinja2 import Template


name = 'Bill'
age = 28

tm = Template("<h1> My name is {{ name }} and I am {{ age }} </h1>")
msg = tm.render(name=name, age=age)

print(msg)

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

rows_tmp = Template("""<ul> {% for person in persons -%}
    <li> {{ person.name }} {{ person.age }} </li>
{% endfor %} </ul>""")

print(rows_tmp.render(persons=persons))

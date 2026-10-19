# Working with sets
from pyscript import display
from js import document

# Members per grade
grade7 = {'Arkin San Agustin', 'Bela Allas', 'Athena Alfaro'}
grade8 = {'Lucian Veran', 'Miguel Velarde', 'Gabe Pua'}
grade9 = {'Keona Valdez', 'Sam Jose', 'Denise Villostas'}
grade10 = {'Alyanna Barlisan', 'Mohammad Calaca', 'Shiloh Briones'}

# Combining all members
members = grade7 | grade8 | grade9 | grade10

# Display members
def show_members():
    names = ''.join(map(lambda n: f'<li>{n}</li>', sorted(members)))
    document.getElementById('output').innerHTML = f"""
        <b>All Members:</b><ul>{names}</ul>
        Total members: {len(members)}
    """

# Add a new member
def add_member(event):
    global members
    fname = document.getElementById('fname').value.strip().title()
    lname = document.getElementById('lname').value.strip().title()
    members = members | {f'{fname} {lname}'}
    show_members()

# Show initial members
show_members()

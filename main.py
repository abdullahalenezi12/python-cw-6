# write your code here

person = {
    'name': 'Abdullah',
    'age': 15,
    'hobbies': ['Boxing', 'Weaghtlifting','Coding'] 
}
person['Country'] = 'Kuwait'
person['hobbies'].append('Volleyball')

def check_hobbies(hobby):
    if len(hobby['hobbies']) > 3:
        print("WOW YOU ARE AMAZING")

print(person)
check_hobbies(person)

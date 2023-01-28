from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hellow')
def hellow( ):
    return 'this is flask string'

@FAI.route('/wish/<name>')
def wish(name):
    return f'hai how are u  {name}'

@FAI.route('/first')
def first():
    return render_template('first.html')


if __name__=='__main__':
    FAI.run(debug=True)

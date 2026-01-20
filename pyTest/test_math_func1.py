from math_fun1 import StudentDB
import pytest

@pytest.fixture(scope =  'module')
def db():
    db = StudentDB()
    db.connect('data.json')
    print('--------------setup---------------')
    yield db
    print('---------------teardown------------')
    db.close()

"""def setup_module(module):
    global db
    db = StudentDB()
    db.connect('data.json')
    print('--------------setup---------------')

def teardown_module(module):
    print('---------------teardown------------')
    db.close()
    """

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
 
def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
    
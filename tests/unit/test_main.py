from src import main

def test_increase_person_age(get_person):
    person = get_person

    main.increase_person_age(10, person)
    actual_result =  person["age"]
    
    expected_result = 33
    assert actual_result == expected_result

def test_decrease_person_age(get_person):
    person = get_person

    main.decrease_person_age(1, person)
    actual_result = person["age"]
    expected_result = 22
    assert actual_result == expected_result
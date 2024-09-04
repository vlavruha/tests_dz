from typing import List

#ФИО
def fio(initials: List[str]) -> str:

    initials = initials[0][0] + initials[1][0] + initials [2][0]
    return initials


    #Победители конкурса


receipts = [123, 145, 346, 246, 235, 166, 112, 351, 436]

def solve(receipts: list):

    result = receipts[2:9:3]
    return result, len(result)


#стоимость доставки

def get_cost(weight: int):
    if weight <= 10:
        result = "Стоимость доставки: 200 руб."
    else:
        result = "Стоимость доставки: 500 руб."

    return result
    # Напишите здесь свой код для задания, используйте конструкцию вывода как в примере выше


# if __name__ == '__main__':
#     # Этот код менять не надо
#     delivery = get_cost(9)
#     assert '200' in delivery, "Стоимость доставки должна быть 200 руб. если вес 9 кг"
#     print('Вес посылки 9 кг', delivery)
#     delivery = get_cost(12)
#     assert '500' in delivery, "Стоимость доставки должна быть 500 руб. если вес 12 кг"
#     print('Вес посылки 12 кг', delivery)
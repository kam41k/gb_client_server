import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('orders.json', 'w', encoding='utf-8', ) as f:
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        data['orders'].append(order_info)
        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json('Компьютер', '1', '67000', 'Ivanov I.I.', '12.08.2022')
write_order_to_json('Монитор', '2', '15000', 'Petrov P.P.', '11.04.2022')
write_order_to_json('Память', '4', '7000', 'Sidorov S.S.', '22.09.2022')

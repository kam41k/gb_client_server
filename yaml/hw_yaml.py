import yaml

data = {'items': ['processor', 'memory', 'motherboard', 'video_card'],
           'items_quantity': 3,
           'items_price': {'processor': '100€-1000€',
                           'memory': '50€-200€',
                           'motherboard': '50€-300€',
                           'video_card': '400€-3000€'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    read_data = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data == read_data)

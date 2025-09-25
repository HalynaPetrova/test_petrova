sales_data = [
    {'product': 'Ноутбук', 'category': 'Електроніка', 'price': 25000, 'quantity': 2},
    {'product': 'Миша', 'category': 'Електроніка', 'price': 500, 'quantity': 5},
    {'product': 'Стіл', 'category': 'Меблі', 'price': 3000, 'quantity': 1},
    {'product': 'Стілець', 'category': 'Меблі', 'price': 1200, 'quantity': 4},
    {'product': 'Телефон', 'category': 'Електроніка', 'price': 15000, 'quantity': 3},
    {'product': 'Шафа', 'category': 'Меблі', 'price': 8000, 'quantity': 1}
]

def calculate_total_sales(data):
    return sum(item['price'] * item['quantity'] for item in data)

def find_most_popular_product(data):
    most_popular = max(data, key=lambda x: x['quantity'])
    return most_popular['product']

def calculate_average_order_value(data):
    total_sales = calculate_total_sales(data)
    total_quantity = sum(item['quantity'] for item in data)
    return total_sales / total_quantity if total_quantity > 0 else 0

def generate_category_report(data):
    report = {}
    for item in data:
        category = item['category']
        sales = item['price'] * item['quantity']
        if category not in report:
            report[category] = {'quantity': 0, 'sales': 0}
        report[category]['quantity'] += item['quantity']
        report[category]['sales'] += sales
    return report

def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target = "Apple"
result = linear_search_product(products, target)
print(result)  

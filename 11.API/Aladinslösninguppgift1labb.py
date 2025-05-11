import requests
import json

# Funktion för att hämta och visa alla produkter
def show_all_products():
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"{product['id']}. {product['title']}")
        # return products
    else:
        print(f"Error fetching products. Status code: {response.status_code}")
        return []

# Funktion för att visa detaljer om en specifik produkt
def show_product_details(product_id):
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    if response.status_code == 200:
        product = response.json()
        print(f"Produktnamn: {product['title']}")
        print(f"Pris: {product['price']}")
        print(f"Beskrivning: {product['description']}")
        print(f"Kategori: {product['category']}")
    else:
        print(f"Error fetching product. Status code: {response.status_code}")

# Funktion för att lägga till en ny produkt
def add_product():
    new_product = {
        "title": input("Ange produktnamn: "),
        "price": float(input("Ange pris: ")),
        "description": input("Ange produktbeskrivning: "),
        "category": input("Ange kategori: "),
        "image": "https://fakestoreapi.com/img/placeholder.png"
    }
    
    response = requests.post(
        'https://fakestoreapi.com/products',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(new_product)
    )
    
    if response.status_code == 200 or response.status_code == 201:
        product = response.json()
        print("Produkt tillagd:", product)
    else:
        print(f"Error adding product. Status code: {response.status_code}")

# Huvudprogrammet med meny
def main():
    while True:
        print("\nMeny:")
        print("1. Visa alla produkter")
        print("2. Visa produktdetaljer")
        print("3. Lägg till en ny produkt")
        print("4. Avsluta")
        
        choice = input("Välj ett alternativ (1-4): ")
        
        if choice == '1':
            products = show_all_products()
        elif choice == '2':
            product_id = input("Ange produkt-ID du vill se: ")
            show_product_details(product_id)
        elif choice == '3':
            add_product()
        elif choice == '4':
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")

# Kör huvudprogrammet
if __name__ == '__main__':
    main()
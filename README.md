# The Online Store

---
## This is the conclusive project of the Django backend framework course. This project is about an online store.

---
#### Footages show the project, which was done with React frontend framework, using the fake API. In Django it will be implemented with a working server-side and database. Main features are navigation, authorization, good quality templates and design.

## Models

1. AbstractStoreItem: An ancestor for different store entities.
	Fields: id: Integer.

2. Category: A category of the product.
	Fields: id: Integer, name: String.

3. Product: An item of a specific category.
	Fields: id: Integer, name: String, description: String, rating: Double, reviews: Integer, price: Double, category: Foreign Key (Category).

4. User: A customer of the online store service.
	Fields: id: Integer, name: String, username: String, password: String, cart: Foreign Key (Cart).

5. Cart: Cart which contains chosen products.
	Fields: id: Integer, products: Product [ ], user: Foreign Key (User).

6. Guidebook: A directive for a user.
	Fields: id: Integer, content: String [ ].
from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_restaurants(restaurants_data):
    print("Seeding restaurants...")
    for restaurant_data in restaurants_data:
        existing_restaurant = Restaurant.query.filter_by(name=restaurant_data['name']).first()
        if not existing_restaurant:
            restaurant = Restaurant(**restaurant_data)
            db.session.add(restaurant)
    
    db.session.commit()  # Commit changes after adding all restaurants
    print("Restaurant seeding completed.")

def seed_pizzas(pizzas_data):
    print("Seeding pizzas...")
    for pizza_data in pizzas_data:
        existing_pizza = Pizza.query.filter_by(name=pizza_data['name']).first()
        if not existing_pizza:
            pizza = Pizza(**pizza_data)
            db.session.add(pizza)

    db.session.commit()  # Commit changes after adding all pizzas
    print("Pizza seeding completed.")

def seed_restaurant_pizzas(restaurant_pizzas_data):
    print("Seeding restaurant_pizzas...")
    for rp_data in restaurant_pizzas_data:
        existing_rp = RestaurantPizza.query.filter_by(restaurant_id=rp_data['restaurant_id'], pizza_id=rp_data['pizza_id']).first()
        if not existing_rp:
            restaurant_pizza = RestaurantPizza(**rp_data)
            db.session.add(restaurant_pizza)
    
    db.session.commit()  # Commit changes after adding all restaurant_pizzas
    print("RestaurantPizza seeding completed.")

if __name__ == '__main__':
    restaurants_data = [
    {"name": "Sycamore Supreme", "address": "5041 Pine Plaza, Supreme Sycamore, State 97531"},
    {"name": "Bamboo Bistro", "address": "5142 Elm Avenue, Blissful Bamboo, State 75309"},
    {"name": "Redwood Retreat", "address": "5243 Walnut Drive, Retreat Redwood, State 24680"},
    {"name": "Magnolia Mansion", "address": "5344 Pine Way, Magnificent Magnolia, State 13579"},
    {"name": "Willow Wonderland", "address": "5445 Elm Lane, Whimsical Willow, State 86420"},
    {"name": "Cypress Chateau", "address": "5546 Oak Boulevard, Charming Cypress, State 97531"},
    {"name": "Fir Fusion", "address": "5647 Birch Crescent, Fusion Fir, State 75309"},
    {"name": "Juniper Junction", "address": "5748 Maple Plaza, Jubilant Juniper, State 24680"},
    {"name": "Palm Perfection", "address": "5849 Cedar Cul-de-sac, Perfect Palm, State 13579"},
    {"name": "Chestnut Castle", "address": "5950 Elm Square, Castle Chestnut, State 86420"},
    {"name": "Aspen Acres", "address": "6051 Walnut Avenue, Amazing Aspen, State 97531"},
    {"name": "Birch Bliss", "address": "6152 Maple Drive, Blissful Birch, State 75309"},
    {"name": "Pine Pavilion", "address": "6253 Cedar Lane, Picturesque Pine, State 24680"},
    {"name": "Maple Manor", "address": "6354 Elm Boulevard, Marvelous Maple, State 13579"},
    {"name": "Oak Oasis", "address": "6455 Birch Bistro, Oasis Oak, State 86420"},
    {"name": "Sycamore Serenity", "address": "6556 Pine Plaza, Serene Sycamore, State 97531"},
    {"name": "Bamboo Boutique", "address": "6657 Elm Avenue, Boutique Bamboo, State 75309"},
    {"name": "Redwood Ridge", "address": "6758 Walnut Drive, Ridge Redwood, State 24680"},
    {"name": "Magnolia Meadows", "address": "6859 Pine Way, Majestic Magnolia, State 13579"},
    {"name": "Willow Wharf", "address": "6960 Elm Lane, Whimsical Willow, State 86420"},
    {"name": "Sycamore Serenity", "address": "13121 Elm Avenue, Serene Sycamore, State 97531"},
    {"name": "Bamboo Boutique", "address": "13222 Walnut Drive, Boutique Bamboo, State 75309"},
    {"name": "Redwood Ridge", "address": "13323 Pine Way, Ridge Redwood, State 24680"},
    {"name": "Magnolia Meadows", "address": "13424 Elm Lane, Majestic Magnolia, State 13579"},
    {"name": "Willow Wharf", "address": "13525 Cedar Lane, Whimsical Willow, State 86420"},
    {"name": "Pine Paradise", "address": "13626 Maple Plaza, Paradise Pine, State 97531"},
    {"name": "Maple Mingle", "address": "13727 Elm Bistro, Merry Maple, State 75309"},
    {"name": "Oak Outlook", "address": "13828 Birch Boulevard, Optimistic Oak, State 24680"},
    {"name": "Sycamore Spot", "address": "13929 Pine Plaza, Spacious Sycamore, State 13579"},
    {"name": "Bamboo Haven", "address": "14030 Elm Avenue, Heavenly Bamboo, State 86420"},
    {"name": "Redwood Roost", "address": "14131 Walnut Drive, Cozy Redwood, State 97531"},
    {"name": "Magnolia Manor", "address": "14232 Pine Way, Elegant Magnolia, State 75309"},
    {"name": "Willow Whimsy", "address": "14333 Elm Lane, Whimsical Willow, State 24680"},
    {"name": "Cypress Charm", "address": "14434 Cedar Square, Charming Cypress, State 13579"},
    {"name": "Fir Fusion", "address": "14535 Birch Crescent, Fusion Fir, State 86420"},
    {"name": "Juniper Joy", "address": "14636 Maple Plaza, Joyful Juniper, State 97531"},
    {"name": "Palm Palace", "address": "14737 Elm Avenue, Palatial Palm, State 75309"},
    {"name": "Cedar Crest", "address": "14838 Walnut Drive, Crested Cedar, State 24680"},
    {"name": "Alder Arcade", "address": "14939 Pine Plaza, Amusing Alder, State 13579"},
    {"name": "Spruce Serenity", "address": "15040 Elm Lane, Serene Spruce, State 86420"},
]


    pizzas_data = [
    {"name": "Truffle Mushroom Madness", "ingredients": "Truffle Oil, Mozzarella, Mushrooms, Parmesan, Thyme"},
    {"name": "Cajun Shrimp Sensation", "ingredients": "Cajun Sauce, Mozzarella, Shrimp, Andouille Sausage, Bell Peppers, Red Onion"},
    {"name": "Caprese Classic", "ingredients": "Tomato, Fresh Mozzarella, Basil, Balsamic Glaze, Olive Oil"},
    {"name": "Sausage and Peppers Parade", "ingredients": "Tomato, Mozzarella, Italian Sausage, Bell Peppers, Onions"},
    {"name": "Garlic White Sauce Wonder", "ingredients": "White Garlic Sauce, Mozzarella, Chicken, Spinach, Sun-Dried Tomatoes"},
    {"name": "Mediterranean Magic", "ingredients": "Tomato, Mozzarella, Kalamata Olives, Feta Cheese, Red Onion, Oregano"},
    {"name": "Pesto Chicken Perfection", "ingredients": "Pesto Sauce, Mozzarella, Chicken, Cherry Tomatoes, Pine Nuts"},
    {"name": "Balsamic Bacon Bliss", "ingredients": "Balsamic Glaze, Mozzarella, Bacon, Caramelized Onions, Gorgonzola"},
    {"name": "Prosciutto Pear Elegance", "ingredients": "Olive Oil, Mozzarella, Prosciutto, Pears, Arugula, Honey"},
    {"name": "Smoky BBQ Pulled Pork", "ingredients": "BBQ Sauce, Mozzarella, Pulled Pork, Red Onion, Cilantro"},
    {"name": "Zesty Buffalo Chicken", "ingredients": "Buffalo Sauce, Mozzarella, Chicken, Ranch Dressing, Celery"},
    {"name": "Sunflower Seed Pesto Pleasure", "ingredients": "Sunflower Seed Pesto, Mozzarella, Cherry Tomatoes, Arugula, Sunflower Seeds"},
    {"name": "Gouda and Caramelized Onion Delight", "ingredients": "Olive Oil, Mozzarella, Gouda Cheese, Caramelized Onions, Thyme"},
    {"name": "Eggplant Parmesan Paradise", "ingredients": "Tomato, Mozzarella, Eggplant, Parmesan, Basil"},
    {"name": "Lemon Herb Chicken Heaven", "ingredients": "Olive Oil, Mozzarella, Chicken, Lemon Zest, Fresh Herbs"},
    {"name": "Pesto Artichoke Amore", "ingredients": "Pesto Sauce, Mozzarella, Artichokes, Spinach, Parmesan"},
    {"name": "Buffalo Cauliflower Bonanza", "ingredients": "Buffalo Sauce, Mozzarella, Cauliflower, Blue Cheese, Celery"},
    {"name": "Maple Bacon Brussels Sprouts", "ingredients": "Maple Dijon Sauce, Mozzarella, Bacon, Brussels Sprouts, Red Onion"},
    {"name": "Cranberry Brie Beauty", "ingredients": "Cranberry Sauce, Mozzarella, Brie Cheese, Walnuts, Arugula"},
    {"name": "Prosciutto Fig Fantasy", "ingredients": "Fig Jam, Mozzarella, Prosciutto, Goat Cheese, Balsamic Glaze"},
    {"name": "Sun-Dried Tomato Basil Bliss", "ingredients": "Tomato Sauce, Mozzarella, Sun-Dried Tomatoes, Fresh Basil"},
    {"name": "Chicken Alfredo Artistry", "ingredients": "Alfredo Sauce, Mozzarella, Chicken, Broccoli, Parmesan"},
    {"name": "Pineapple Jalapeño Paradise", "ingredients": "Tomato, Mozzarella, Pineapple, Jalapeños, Bacon"},
    {"name": "Mushroom Spinach Marvel", "ingredients": "Tomato, Mozzarella, Mushrooms, Spinach, Garlic"},
    {"name": "Balsamic Strawberry Brie", "ingredients": "Balsamic Glaze, Mozzarella, Strawberries, Brie Cheese, Basil"},
    {"name": "Southwest Chipotle Carnival", "ingredients": "Chipotle Sauce, Mozzarella, Chicken, Black Beans, Corn, Red Onion"},
    {"name": "Garlic Parmesan Perfection", "ingredients": "White Garlic Sauce, Mozzarella, Parmesan, Fresh Parsley"},
    {"name": "Mango Habanero Heatwave", "ingredients": "Tomato, Mozzarella, Mango, Habanero, Chicken, Red Onion"},
    {"name": "Caprese with a Twist", "ingredients": "Tomato, Mozzarella, Avocado, Basil, Balsamic Glaze"},
    {"name": "Spinach Artichoke Delight", "ingredients": "White Garlic Sauce, Mozzarella, Spinach, Artichokes, Parmesan"},
    {"name": "Tandoori Tikka Temptation", "ingredients": "Tandoori Sauce, Mozzarella, Chicken, Bell Peppers, Red Onion, Cilantro"},
    {"name": "Maple Sriracha Madness", "ingredients": "Maple Sriracha Sauce, Mozzarella, Chicken, Bacon, Green Onions"},
]


    restaurant_pizzas_data = [
    {"price": 20.50, "restaurant_id": 9, "pizza_id": 18},
    {"price": 18.99, "restaurant_id": 3, "pizza_id": 5},
    {"price": 22.99, "restaurant_id": 2, "pizza_id": 7},
    {"price": 16.50, "restaurant_id": 1, "pizza_id": 3},
    {"price": 21.99, "restaurant_id": 6, "pizza_id": 12},
    {"price": 19.50, "restaurant_id": 25, "pizza_id": 23},
    {"price": 18.99, "restaurant_id": 12, "pizza_id": 28},
    {"price": 20.50, "restaurant_id": 16, "pizza_id": 31},
    {"price": 17.99, "restaurant_id": 23, "pizza_id": 25},
    {"price": 19.99, "restaurant_id": 20, "pizza_id": 24},
    {"price": 15.50, "restaurant_id": 15, "pizza_id": 31},
    {"price": 17.99, "restaurant_id": 7, "pizza_id": 14},
    {"price": 21.50, "restaurant_id": 16, "pizza_id": 43},
    {"price": 16.00, "restaurant_id": 18, "pizza_id": 35},
    {"price": 19.50, "restaurant_id": 19, "pizza_id": 36},
    {"price": 15.99, "restaurant_id": 24, "pizza_id": 33},
    {"price": 18.50, "restaurant_id": 17, "pizza_id": 32},
    {"price": 20.99, "restaurant_id": 22, "pizza_id": 24},
    {"price": 17.00, "restaurant_id": 8, "pizza_id": 17},
    {"price": 18.50, "restaurant_id": 8, "pizza_id": 16},
    {"price": 19.99, "restaurant_id": 10, "pizza_id": 20},
    {"price": 21.99, "restaurant_id": 4, "pizza_id": 9},
    {"price": 19.99, "restaurant_id": 13, "pizza_id": 25},
    {"price": 16.50, "restaurant_id": 14, "pizza_id": 27},
    {"price": 14.99, "restaurant_id": 21, "pizza_id": 30},
    {"price": 17.50, "restaurant_id": 11, "pizza_id": 20},
    {"price": 19.50, "restaurant_id": 5, "pizza_id": 11},
    {"price": 20.99, "restaurant_id": 9, "pizza_id": 19},
    {"price": 18.99, "restaurant_id": 3, "pizza_id": 6},
    {"price": 22.99, "restaurant_id": 2, "pizza_id": 8},
    {"price": 16.50, "restaurant_id": 1, "pizza_id": 4},
    {"price": 21.99, "restaurant_id": 6, "pizza_id": 11},
    {"price": 19.50, "restaurant_id": 25, "pizza_id": 22},
    {"price": 18.99, "restaurant_id": 12, "pizza_id": 29},
    {"price": 20.50, "restaurant_id": 16, "pizza_id": 39},
    {"price": 17.99, "restaurant_id": 23, "pizza_id": 47},
    {"price": 19.99, "restaurant_id": 20, "pizza_id": 33},
    {"price": 15.50, "restaurant_id": 15, "pizza_id": 32},
    {"price": 17.99, "restaurant_id": 7, "pizza_id": 13},
    {"price": 21.50, "restaurant_id": 16, "pizza_id": 22},
    {"price": 16.00, "restaurant_id": 18, "pizza_id": 34},
    {"price": 19.50, "restaurant_id": 19, "pizza_id": 35},
    {"price": 15.99, "restaurant_id": 24, "pizza_id": 28},
    {"price": 18.50, "restaurant_id": 17, "pizza_id": 33},
    {"price": 20.99, "restaurant_id": 22, "pizza_id": 45},
    {"price": 17.00, "restaurant_id": 8, "pizza_id": 16},
    {"price": 18.50, "restaurant_id": 8, "pizza_id": 15},
    {"price": 19.99, "restaurant_id": 10, "pizza_id": 19},
    {"price": 21.99, "restaurant_id": 4, "pizza_id": 8},
    {"price": 19.99, "restaurant_id": 13, "pizza_id": 26},
    {"price": 16.50, "restaurant_id": 14, "pizza_id": 28},
    {"price": 14.99, "restaurant_id": 21, "pizza_id": 30},
    {"price": 17.50, "restaurant_id": 11, "pizza_id": 21},
    {"price": 19.50, "restaurant_id": 5, "pizza_id": 10},
    {"price": 20.50, "restaurant_id": 9, "pizza_id": 18},
    {"price": 18.99, "restaurant_id": 3, "pizza_id": 5},
]


    with app.app_context():
        seed_restaurants(restaurants_data)
        seed_pizzas(pizzas_data)
        seed_restaurant_pizzas(restaurant_pizzas_data)
To initialize database run the following:

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py init_db


When designing the API for your recipe app, ensure it supports the necessary operations:

	•	GET /api/recipes: Fetch all recipes.
	•	GET /api/recipes/:id: Fetch a specific recipe by ID.
	•	POST /api/recipes: Create a new recipe.
	•	PUT /api/recipes/:id: Update an existing recipe.
	•	DELETE /api/recipes/:id: Delete a recipe.
	•	GET /api/recipes/:id/ingredients: Fetch ingredients for a specific recipe.
	•	GET /api/tags: Fetch all tags.
	•	POST /api/recipes/:id/tags: Add a tag to a recipe.


STEPS:

Start with SQLite file
Then switch over to PostgreSQL


Example of Cheesecake recipe cheryl sent:

{
    "title": "Classic Cheesecake Recipe",
    "description": "This Classic Cheesecake Recipe is smooth, creamy, and topped on a homemade graham cracker crust. Includes helpful tips to get the perfect cheesecake!",
    "course": "Dessert",
    "cuisine": "American",
    "keyword": [
        "classic cheesecake recipe",
        "homemade cheesecake recipe"
    ],
    "prep_time": "40 mins",
    "cook_time": "1 hr 5 mins",
    "total_time": "1 hr 40 mins",
    "servings": "10 slices",
    "author": "Danielle",
    "ingredients": {
        "graham_cracker_crust": [
            {
                "ingredient": "crushed graham cracker crumbs",
                "quantity": "1 and 1/2 cups",
                "grams": 180
            },
            {
                "ingredient": "granulated sugar",
                "quantity": "1/3 cup",
                "grams": 65
            },
            {
                "ingredient": "unsalted butter, melted",
                "quantity": "5 tablespoons",
                "grams": 70
            }
        ],
        "cheesecake_filling": [
            {
                "ingredient": "brick-style cream cheese, softened to room temperature",
                "quantity": "32 ounces"
            },
            {
                "ingredient": "full-fat sour cream, room temperature",
                "quantity": "1 cup",
                "grams": 230
            },
            {
                "ingredient": "granulated sugar",
                "quantity": "1 cup",
                "grams": 200
            },
            {
                "ingredient": "pure vanilla extract",
                "quantity": "2 teaspoons"
            },
            {
                "ingredient": "large eggs, room temperature",
                "quantity": "4"
            }
        ]
    },
    "instructions": {
        "graham_cracker_crust": [
            "Preheat oven to 325\u00b0F (163\u00b0C). Combine the crushed graham cracker crumbs and granulated sugar in a medium-sized mixing bowl and stir until well combined. Add the melted butter and mix until all of the crumbs are moistened.",
            "Scoop the mixture into a 9-inch springform pan and firmly press it down into one even layer. Bake at 325\u00b0F (163\u00b0C) for 10 minutes, then remove from the oven and set aside to cool slightly while you make the filling."
        ],
        "cheesecake_filling": [
            "Set a large pot of water to boil for the water bath before getting started with the filling.",
            "In the bowl of a stand mixer fitted with the paddle attachment, or in a large mixing bowl using a handheld mixer, beat the cream cheese on low-medium speed until smooth. Add the sour cream and mix until fully combined, stopping to scrape down the sides of the bowl as needed. Then add the granulated sugar and pure vanilla extract and mix until well combined.",
            "In a separate small mixing bowl, lightly beat the eggs. Add the beaten eggs to the mixing bowl with the cheesecake filling and mix on low speed until just combined. Use a rubber spatula to turn the filling a few times to make sure everything is fully mixed together. Set aside.",
            "Wrap the springform pan with the pre-baked graham cracker crust in aluminum foil, then place into a large oven bag. Fold the oven bag down the sides of the springform pan.",
            "Pour the cheesecake filling into the springform pan and smooth it out into one even layer. Tap the pan on the counter a couple of times to bring any air bubbles to the top, then use a toothpick or skewer to remove any large air bubbles and smooth them out.",
            "Add the boiling water you started before the filling to a large roasting pan until it is about 1-inch deep. Carefully place the wrapped springform pan into the roasting pan.",
            "Transfer the roasting pan with the cheesecake to the oven and bake at 325\u00b0F (163\u00b0C) for 60-65 minutes or until the edges of the cheesecake are set and the center is still slightly jiggly. Turn the oven off, crack the oven door slightly, and allow the cheesecake to cool in the warm oven for 1 hour.",
            "After the cheesecake has cooled for 1 hour in the oven, remove it from the oven and transfer to a wire rack to cool completely. Once cooled, cover tightly and transfer to the refrigerator to chill for 5-6 hours or overnight. Run a thin knife around the outside of the cheesecake to loosen it from the pan, carefully release the springform pan, then slice into pieces, serve, and enjoy!"
        ]
    },
    "notes": [
        "Room temperature ingredients: Before getting started, make sure the cream cheese, sour cream, and eggs are at room temperature.",
        "Graham cracker crumbs: 1 and 1/2 cups of graham cracker crumbs is equal to about 11-12 full-sheets of graham crackers.",
        "Cream cheese: Make sure to use full-fat cream cheese bricks, not the cream cheese spread in a tub.",
        "Store leftover cheesecake in an airtight container in the refrigerator for up to 4 days.",
        "Freezing instructions: This cheesecake will freeze well for up to 3 months. Wrap tightly and store in a large freezer bag or container. Thaw overnight in the refrigerator."
    ]
}
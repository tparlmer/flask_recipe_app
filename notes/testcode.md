Index route test code

def index():
    print("Index route hit")
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    
    cursor = conn.cursor()
    try:
        print("Executing SQL Query")
        cursor.execute('SELECT * FROM Recipes')
        recipes = cursor.fetchall()
        print(f"Query executed, fetched {len(recipes)} recipes")
        
        # Print each recipe
        for recipe in recipes:
            print(f"Recipe: {dict(recipe)}")

        print(f"Passing to template: {recipes}")

    except Exception as e:
        print(f"Error executing query: {e}")
        return "Database query failed", 500
    finally:
        conn.close()
    
    return render_template('index.html', recipes=recipes)

index template test code

{% block content %}
    <h1>Recipes</h1>
    <p>Debug: recipes variable type: {{ recipes.__class__.__name__ }}</p>
    <p>Debug: recipes length: {{ recipes|length if recipes else 'N/A' }}</p>
    {% if recipes %}
        <p>Number of recipes: {{ recipes|length }}</p>
        <ul>
        {% for recipe in recipes %}
            <li>{{ recipe['name'] }} (ID: {{ recipe['id'] }})</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No recipes found</p>
    {% endif %}
    <h2>Raw Recipe Data:</h2>
    <pre>{{ recipes }}</pre>
{% endblock %}
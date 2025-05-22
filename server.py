from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

places = {
    "1":{
        "id": "1",
        "image":"https://tb-static.uber.com/prod/image-proc/processed_images/b58b7e067434d056bd528d6808cf6533/783282f6131ef2258e5bcd87c46aa87e.jpeg",
        "name": "King Barka Jamaican and American Restaurant",
        "rating": "4.5",
        "address": "2733 Frederick Douglass Blvd",
        "Prices": "$$",
        "popular": ["Oxtail", "Curry Goat", "Fry Chicken"],
        "country": "Jamaican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["3", "4", "8"],
    },

    "2":{
        "id": "2",
        "name": "Le Soleil Restaurant",
        "image":"https://cdn.vox-cdn.com/thumbor/expl6fAoGo1mis_0qF47zfkB_Xk=/0x468:5084x3010/fit-in/1200x600/cdn.vox-cdn.com/uploads/chorus_asset/file/13064317/LES_ext.0.0.1488180549.jpg",
        "rating": "4.0",
        "address": "858 10th Ave",
        "Prices": "$$$",
        "popular": ["Fried MeatBall", "Oxtail"],
        "country": "Haitian",
        "online": ["Grubhub", "Doordash"],
        "similar": ["7"],
    },

    "3":{
        "id": "3",
        "name": "Freda's Caribbean & Soul Cuisine",
        "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiLvXkF-X_kuF5Ig9InG6fGJGuzAeg5FoY3w&s",
        "rating": "3.8",
        "address": "993 Columbus Ave",
        "Prices": "$$",
        "popular": ["Curry Shrimp", "Jerk Salmon"],
        "country": "Jamaican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["1", "4", "8"],
    },

    "4":{
        "id": "4",
        "name": "Caribbean Starr",
        "image":"https://tb-static.uber.com/prod/image-proc/processed_images/42f82894bf2c3f0e11c9e625ecfa6547/a19bb09692310dfd41e49a96c424b3a6.jpeg",
        "rating": "4.5",
        "address": "280 Lenox Ave",
        "Prices": "$$",
        "popular": ["Mac and Cheese"],
        "country": "Jamaican",
        "online": ["Grubhub"],
        "similar": ["1", "3", "8"],
    },

    "5":{
        "id": "5",
        "name": "Mofongo del Valle",
        "image":"https://media-cdn.grubhub.com/image/upload/d_search:browse-images:default.jpg/w_150,q_auto:low,fl_lossy,dpr_2.0,c_fill,f_auto,h_150/mjziac2boh6wdxtfdfmh",
        "rating": "4.3",
        "address": "3340 Broadway Ave",
        "Prices": "$$",
        "popular": ["Chuleta Ahumada", "Picadera", "Chicharon de Pollo sin Hueso"],
        "country": "Dominican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["6", "9", "10"],
    },

    "6":{
        "id": "6",
        "name": "Sofrito",
        "image":"https://cdn.vox-cdn.com/thumbor/dMvLyCPYoksJv1txg5TPnUc1e-s=/0x184:763x756/1400x788/filters:focal(0x184:763x756):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/50177079/Sofrito_20Rico_20Authentic_20Puerto_20Rican_20Cuisine_207-21.0.jpg",
        "rating": "4.6",
        "address": "679 Riverside Dr",
        "Prices": "$$$",
        "popular": ["Sancocho Criollo Soup", "Empanadas"],
        "country": "Boricua",
        "online": ["Grubhub"],
        "similar": ["5", "9", "10"],
    },

    "7":{
        "id": "7",
        "name": "DejaVu Haitian Fusion Restaurant Lounge",
        "image":"https://s3-media0.fl.yelpcdn.com/bphoto/FnkgbzPZ9sR-dZZftTVQeQ/348s.jpg",
        "rating": "4.1",
        "address": "301 W 151st",
        "Prices": "$$$",
        "popular": ["Okap Nou Prale", "Shrim n Grits"],
        "country": "Haitian",
        "online": ["Grubhub", "Doordash"],
        "similar": ["2"],
    },

    "8":{
        "id": "8",
        "name": "Jerk House Carribean Restaurant",
        "image":"https://harlemonestop.com/images/organizations/2436.jpg?v=1587413478",
        "rating": "4.6",
        "address": "2143 Adam Clayton Powell jr Blvd",
        "Prices": "$$",
        "popular": ["Jerk Pork Meal"],
        "country": "Jamaican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["1", "3", '4'],
    },

    "9":{
        "id": "9",
        "name": "Malecon Restaurant",
        "image":"https://s3-media0.fl.yelpcdn.com/bphoto/V6z0b5myLVFCNrpEAi69zA/348s.jpg",
        "rating": "4.7",
        "address": "4141 Broadway",
        "Prices": "$$$",
        "popular": ["Whole Chicken", "Beans", "Egg, Spanish, and avocado Sandwich"],
        "country": "Dominican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["5", "6", "10"],
    },

    "10":{
        "id": "10",
        "name": "Santiago's Beer Garden",
        "image":"https://images.sideways.nyc/4eChKKLgl8YeKtItzdfLlw/santiagos-beer-garden-1.jpg?auto=format&w=768&fit=crop",
        "rating": "4.6",
        "address": "2337 1st Ave",
        "Prices": "$$$",
        "popular": ["Grilled Chicken/ Pechuga a la Plancha", "Stewed Codfish/Bacalao"],
        "country": "Dominican",
        "online": ["Grubhub", "Doordash"],
        "similar": ["5", "6", "9"],
    }

}


# ajax for people.js
@app.route('/', endpoint='homepage')
def hello_world():
   return render_template('homepage.html', items=list(places.values()))   


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    print(f"Search Query: '{query}'")  # Debugging print
    if not query:
        return render_template('search.html', query=query, results=[])

    results = [
        place for place in places.values()
        if query.lower() in place['name'].lower() or query in place['country'].lower()
    ]
    print(f"Results Found: {len(results)}")  # Debugging print
    
    return render_template('search.html', query=query, results=results)



@app.route('/view/<id>')
def view_item(id):
    item = places.get(id)
    if item is None:
        return "Item not found", 404
    return render_template('view.html', item=item, places=places)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        data = request.get_json()

        new_id = str(len(places) + 1)
        name = data.get('name', '').strip()
        address = data.get('address', '').strip()
        rating = data.get('rating', '').strip()
        image = data.get('image', '').strip()
        prices = data.get('prices', '').strip()
        popular_items = [p.strip() for p in data.get('popular', [])] 
        country = data.get('country', '').strip()
        online = [o.strip() for o in data.get('online', [])]
        
        if not name or not address or not rating:
            return jsonify({"error": "Name, address, and rating are required."}), 400
        
        places[new_id] = {
            "id": new_id,
            "name": name,
            "image": image,
            "rating": rating,
            "address": address,
            "Prices": prices,
            "Popular Items": popular_items,
            "country": country,
            "online": online,
            "similar": []
        }
        return jsonify({"message": "Item added successfully!", "id": new_id})
    return render_template('add.html')



@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id):
    item = places.get(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    if request.method == 'POST':
        data = request.get_json()  # ✅ Correct way to get JSON data
        
        item['name'] = data.get('name', item['name']).strip()
        item['image'] = data.get('image', item['image']).strip()
        item['rating'] = data.get('rating', item['rating']).strip()
        item['address'] = data.get('address', item['address']).strip()
        item['Prices'] = data.get('prices', item['Prices']).strip()
        item['popular'] = [p.strip() for p in data.get('popular', item['popular'])]  # ✅ Ensure list format
        item['country'] = data.get('country', item['country']).strip()
        item['online'] = [o.strip() for o in data.get('online', item['online'])]  # ✅ Ensure list format
        
        return jsonify({"message": "Item updated successfully!"})
    
    return render_template('edit.html', item=item)





if __name__ == '__main__':
   app.run(debug = True, port=5001)
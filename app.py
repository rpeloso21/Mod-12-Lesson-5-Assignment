from flask import Flask, jsonify, request

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

video_titles.sort()


#This POST woul be to replace the hard coded titles if the user wanted to.
@app.route('/add_titles', methods=['POST'])
def add_titles():
    global video_titles

    data = request.get_json()

    if not data or 'titles' not in data:
        return jsonify({"error": "No titles provided."}), 400
    
    video_titles = data['titles']
    video_titles.sort()
    return jsonify({"message": "Titles added succesfully."}), 200

# The search route will run by posting the title into the url... (ex: http://127.0.0.1:5000/Fitness%20Fundamentals:%20Strength%20Training)
@app.route('/<string:title>', methods=['GET'])
def search_video(title):
    low = 0
    high = len(video_titles) -1

    while low <= high:
        mid = (low + high) // 2
        if video_titles[mid] == title:
            return jsonify(f"'{title}' found at index {mid}"), 200
        elif video_titles[mid] < title:
            low = mid + 1
        else:
            high = mid - 1

    return jsonify({"error": "Title not found."}), 404



@app.route('/sorted_titles', methods=['GET'])
def get_sorted_titles():
    sorted_titles = merge_sort(video_titles)
    if sorted_titles != None:
        return jsonify(sorted_titles), 200
    else:
        return jsonify("No titles found."), 404


def merge_sort(video_titles):
    if len(video_titles) > 1:
        mid = len(video_titles)//2
        left_half = video_titles[:mid]
        right_half = video_titles[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                video_titles[k] = left_half[i]
                i += 1
            else:
                video_titles[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            video_titles[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            video_titles[k] = right_half[j]
            j += 1
            k += 1
            
    return video_titles



if __name__ == '__main__':
    app.run(debug=True)
def search(video_list, search_item):
    video_list.sort()
    low = 0
    high = len(video_list) -1

    while low <= high:
        mid = (low + high) // 2
        if video_list[mid] == search_item:
            return mid
        elif video_list[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1





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

for title in video_titles:
    print(title)

searched_title = "Financial Planning for Beginners"

index = search(video_titles, searched_title)
if index == -1:
    print("Title not found.")
else:
    print(f"\n'{searched_title}' found at index {index}")


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

merged_titles = merge_sort(video_titles)
for title in merged_titles:
    print(title)
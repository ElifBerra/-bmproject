import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 1), (9, 7)]

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) * 2 + (point1[1] - point2[1]) * 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması ve yazdırılması
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
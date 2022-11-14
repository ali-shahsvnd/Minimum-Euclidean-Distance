import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('C:/Users/ALI/Desktop/points.txt', usecols=0)
y = np.loadtxt('C:/Users/ALI/Desktop/points.txt', usecols=1)

# x = np.random.randint(-10 ,10, 5)
# y = np.random.randint(-10 ,10, 5)
# x = np.append(x, np.random.randint(10000, 10010, 20))
# y = np.append(y, np.random.randint(10000, 10010, 20))


# ternaery search to find point on x axis with minimum ecludian distance to all given points
def find_min_dist_point_ternary(xpoints, ypoints):
    l = xpoints.min()
    r = xpoints.max()
    while(r - l > 0.001):
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        dist1 = np.sum(np.sqrt((xpoints[:] - m1) ** 2 + ypoints[:] ** 2))
        dist2 = np.sum(np.sqrt((xpoints[:] - m2) ** 2 + ypoints[:] ** 2))
        if dist1 < dist2:
            r = m2
        else:
            l = m1
    return (l + r) / 2

print("x point for min ecludin distance to all :", find_min_dist_point_ternary(x, y))


# ternary search to find point on x axis on center of circle with minimum radius including all given points
def find_min_radius_point_ternary(xpoints, ypoints):
    l = xpoints.min()
    r = xpoints.max()
    while(r - l > 0.001):
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        radius1 = np.max(np.sqrt((xpoints[:] - m1) ** 2 + ypoints[:] ** 2))
        radius2 = np.max(np.sqrt((xpoints[:] - m2) ** 2 + ypoints[:] ** 2))
        if radius1 < radius2:
            r = m2
        else:
            l = m1
    return (l + r) / 2

print("x point for min radius :", find_min_radius_point_ternary(x, y))


# plot 
min_radius_x = find_min_radius_point_ternary(x, y)
min_radius = np.sqrt(np.max((x[:] - min_radius_x) ** 2 + y[:] ** 2))

plt.scatter(x, y)
plt.plot(x, y, 'ro')
plt.plot(min_radius_x, 0, 'bo')
plt.plot(find_min_dist_point_ternary(x, y), 0, 'go')
plt.gca().add_patch(plt.Circle((min_radius_x, 0),min_radius , fill=False))
plt.show()



# point on x axis on with minimum euclidean distance to all given points
# def find_min_dist_point(xpoints, ypoints):
#     min_dist = np.inf
#     min_dist_point = None
#     for x in np.arange(xpoints.min(), xpoints.max(), 0.1):
#         dist = np.sum(np.sqrt((xpoints[:] - x) ** 2 + ypoints[:] ** 2))
#         if dist < min_dist:
#             min_dist = dist
#             min_dist_point = x
#     return min_dist_point

# print("min ecludin distance point :", find_min_dist_point(x, y))

# point on x axis on with minimum euclidean distance to all given points with derivation method
# def find_min_dist_point2(xpoints, ypoints):
#     min_dist = np.inf
#     min_dist_point = None
#     for x in np.arange(xpoints.min(), xpoints.max()+1, 0.1):
#         dist = np.sum((xpoints[:] - x)/(np.sqrt((xpoints[:] - x) ** 2 + ypoints[:] ** 2)))
#         if (dist - 0 < 1 and dist - 0 > -1):
#             min_dist_point = x
#             break   
#     return min_dist_point        
    
# print("min ecludin distance point 2 :", find_min_dist_point2(x, y))


# point on x axis on center of circle with minimum radius including all given points
# def find_min_radius_point(xpoints, ypoints):
#     min_radius = np.inf
#     min_radius_point = None
#     i = 0
#     for x in np.arange(xpoints.min(), xpoints.max(), 0.01):
#         radius = np.max(np.sqrt((xpoints[:] - x) ** 2 + ypoints[:] ** 2))
#         # print(radius)
#         # radius = (xpoints[:] - x)/(np.sqrt((xpoints[:] - x) ** 2 + ypoints[:] ** 2))
#         # xrad[i] = x
#         # yrad[i] = radius
#         i += 1
#         if radius < min_radius:
#             min_radius = radius
#             min_radius_point = x
#     return min_radius_point

# print("min radius point :", find_min_radius_point(x, y))

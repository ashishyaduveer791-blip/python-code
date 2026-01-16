# class DemoClass:
#     a = 10
#     def showvalue(self):
#        self.c=self.a*self.a 
#        print(self.c)
#        def showvalue(self):
#            print("Welcome to Ashish")

#        obj = DemoClass()
#        obj = showvalue()
#        obj = showvalue()
# class student:
#     _name="hello"
#     def_init_(self):
#     print(self._name)
#     obj = student()
#   obj._display  
import matplotlib.pyplot as plt
import numpy as np

# Golden ratio
phi = (1 + 5**0.5) / 2

# Function to generate points for golden spiral
def golden_spiral(theta_max=4*np.pi, a=1):
    theta = np.linspace(0, theta_max, 1000)  # angle
    r = a * phi**(theta/(2*np.pi))          # radius grows exponentially
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Generate spiral points
x, y = golden_spiral(theta_max=6*np.pi)

# Plot
plt.figure(figsize=(8,8))
plt.plot(x, y, color='gold', linewidth=2)
plt.title("Golden Spiral (φ)")
plt.axis('equal')
plt.grid(True, linestyle='--', alpha=0.3)

# Optional: overlay on a background map image
# Uncomment below if you have a map image called 'map.png'
# img = plt.imread('map.png')
# plt.imshow(img, extent=[min(x), max(x), min(y), max(y)], alpha=0.5)

plt.show()

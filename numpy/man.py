import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20, r=2, x_center=-0.5, y_center=0, zoom=1):
    """Returns an image of the Mandelbrot fractal of size (h,w) with zoom and centering."""
    # Adjust these ranges to zoom in or out and pan around the fractal
    x_width = 4.0 / zoom
    y_height = 3.0 / zoom

    x = np.linspace(x_center - x_width/2, x_center + x_width/2, 4*h+1)
    y = np.linspace(y_center - y_height/2, y_center + y_height/2, 3*w+1)

    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = r

    return divtime

# Zoom function
def zoom(event):
    global x_center, y_center, zoom_level

    # Zoom factor
    zoom_factor = 0.1

    # Determine zoom direction
    if event.key == 'up':
        zoom_level *= (1 - zoom_factor)
    elif event.key == 'down':
        zoom_level *= (1 + zoom_factor)
    else:
        # Ignore other keys
        return

    # Update the image with the new zoom level
    ax.images[0].set_data(mandelbrot(400, 400, zoom=zoom_level, x_center=x_center, y_center=y_center))
    
    plt.draw()

# Initial plot parameters
x_center, y_center, zoom_level = -0.5, 0, 1

# Initial plot
fig, ax = plt.subplots()
plt.imshow(mandelbrot(400, 400, zoom=zoom_level, x_center=x_center, y_center=y_center))

# Bind the zoom function to key press events
fig.canvas.mpl_connect('key_press_event', zoom)


plt.show()
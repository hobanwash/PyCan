# your_script.py
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Save the plot to a file
plt.savefig('/tmp/plot.png')  # Save to a temporary file
plt.close()

# Print the path to the saved plot (you can later use this to show it in the browser)
print('<img src="/tmp/plot.png" />')
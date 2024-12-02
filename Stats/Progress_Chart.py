import matplotlib.pyplot as plt

# Example data
labels = ['Easy', 'Medium', 'Hard']
solved_counts = [0, 0, 0]  # Number of problems solved per difficulty
colors = ['#8bc34a', '#03a9f4', '#f44336']

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(solved_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('LeetCode Progress by Difficulty')
plt.savefig('progress_pie_chart.png')  # Save the chart as an image
plt.show()

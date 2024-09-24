# anomaly-detection-project
 

# Efficient Data Stream Anomaly Detection

## Project Overview
Hi! This project is about detecting unusual or strange values in a continuous flow of numbers. Imagine watching a live stream of numbers, and whenever something odd happens (like a big jump), we want to catch it!

I’ve created this flow of numbers using Python, which could represent things like tracking bank transactions or system activity in real life. To find these strange values (called anomalies), I used a simple method called Z-score.

## What the project does:
- **Simulates a Flow of Numbers**: Creates a series of numbers that follow a regular pattern, with some random changes (to make it more like real-world data), and some big jumps or drops (which are the unusual values).
- **Finds Unusual Values**: Uses the Z-score method to spot any numbers that are way different from the usual pattern.
- **Shows a Graph**: Draws a graph of the number flow and highlights the unusual points in red, so it’s easy to spot where the odd things happened.

## How It Works:
1. **Generating the Numbers**: I made a set of numbers that behave like real-world data, with repeating patterns (like waves) and random small changes.
2. **Finding the Anomalies**: I used a technique called Z-score to figure out how far each new number is from the usual ones. If it’s too far away (based on a limit), I mark it as unusual.
3. **Drawing the Graph**: After finding the unusual points, the program creates a graph with the normal numbers in blue and the strange ones in red, so you can easily see when something unexpected happened.

## Instructions to Run the Project:
1. Download or clone the project files.
2. Make sure you have Python 3.x installed.
3. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python anomaly_detection.py
   ```

## Example Output:
- In the terminal, it will show the positions (index numbers) where the unusual values were found.
- A graph will pop up showing the flow of numbers with red ‘x’ markers for each unusual value.

## Libraries Required:
- **numpy**: To create and handle the numbers.
- **matplotlib**: To draw and show the graph with the unusual values.

## Why I Chose This Approach:
I decided to use the Z-score method because it’s easy to understand and use. It checks how far a number is from the average of recent numbers. If a number is too far off, it’s marked as strange. This method works well for real-time data and is simple to calculate, making it a good fit for this project.

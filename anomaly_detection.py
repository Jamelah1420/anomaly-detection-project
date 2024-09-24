
import numpy as np
import random
import matplotlib.pyplot as plt

# Step 1: Simulate Flow of Numbers
def simulate_data_stream(n_points=1000):
    """
    Creates a flow of numbers that follow a repeating pattern, with random changes and some big jumps.
    """
    # Time series to track the flow of numbers
    time = np.arange(0, n_points)

    # Create a wave-like pattern for regular behavior
    seasonal = np.sin(0.1 * time) * 10

    # Add some randomness (small changes in the numbers)
    noise = np.random.normal(0, 2, n_points)

    # Combine the wave pattern and randomness
    stream = seasonal + noise

    # Add some unusual values (big jumps)
    for _ in range(10):
        index = random.randint(0, n_points - 1)
        stream[index] += np.random.normal(50, 10)  # Big jump added at random spot

    return stream

# Step 2: Find Unusual Values (Anomalies)
def z_score_anomaly_detection(data_stream, threshold=3):
    """
    Uses the Z-score method to spot any numbers that are way different from the usual pattern.
    """
    if data_stream is None or len(data_stream) == 0:
        raise ValueError("The data stream is empty or None.")
    
    if not all(isinstance(x, (int, float, np.float64)) for x in data_stream):
        raise ValueError("The data stream must contain only numeric values.")

    anomalies = []  # Where we store the unusual values (big jumps)
    window_size = 50  # How many points we look at to get the usual pattern

    # Find the average and standard deviation of the first 50 points
    mean = np.mean(data_stream[:window_size])
    std_dev = np.std(data_stream[:window_size])

    if std_dev == 0:
        raise ValueError("Standard deviation is zero in the initial window, cannot proceed with Z-score calculation.")

    # Go through the data points one by one after the first 50
    for i in range(window_size, len(data_stream)):
        # Avoid dividing by zero if the std_dev is zero
        if std_dev == 0:
            continue

        # Find how different the current number is from the average (Z-score)
        z_score = (data_stream[i] - mean) / std_dev

        # If the number is too different, mark it as unusual
        if abs(z_score) > threshold:
            anomalies.append(i)

        # Update the average and standard deviation with new data
        mean = 0.9 * mean + 0.1 * data_stream[i]
        std_dev = 0.9 * std_dev + 0.1 * abs(data_stream[i] - mean)

    return anomalies

# Step 3: Show the Graph
def visualize_data_with_anomalies(data_stream, anomalies):
    """
    Draws a graph of the number flow and highlights the unusual points in red.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data_stream, label='Data Stream', color='blue')  # Draw the flow of numbers
    # Highlight the unusual points in red
    plt.scatter(anomalies, [data_stream[i] for i in anomalies], color='red', label='Anomalies', marker='x')

    # Add a title and labels
    plt.title('Data Stream with Detected Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')

    # Show a legend for the graph
    plt.legend()

    # Display the graph
    plt.show()

# Step 4: Run the Project
if __name__ == "__main__":
    try:
        # Step 1: Create the flow of numbers
        data_stream = simulate_data_stream(n_points=1000)

        # Step 2: Find the unusual numbers (anomalies)
        anomalies = z_score_anomaly_detection(data_stream)

        # Step 3: Show where the unusual numbers are on a graph
        print("Anomalies detected at indices:", anomalies)
        visualize_data_with_anomalies(data_stream, anomalies)

    except ValueError as e:
        print(f"Error: {e}")

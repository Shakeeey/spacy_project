import pandas as pd

# Load the original CSV file
data = pd.read_csv('test_textcat_project/textcat_data/training_data.csv')

# Split the data into three chunks
chunk_size = len(data) // 3
chunk1 = data[:chunk_size]
chunk2 = data[chunk_size:2*chunk_size]
chunk3 = data[2*chunk_size:]

# Save each chunk as a separate CSV file
chunk1.to_csv('test_textcat_project/textcat_data/training_data_chunk1.csv', index=False)
chunk2.to_csv('test_textcat_project/textcat_data/training_data_chunk2.csv', index=False)
chunk3.to_csv('test_textcat_project/textcat_data/training_data_chunk3.csv', index=False)
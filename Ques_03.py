import numpy as np

def element_wise_operations(A, B):
    """Perform element-wise operations on matrices A and B."""
    # Element-wise addition
    addition = A + B
    
    # Element-wise subtraction
    subtraction = A - B
    
    # Element-wise multiplication
    multiplication = A * B
    
    # Element-wise division
    division = A / B
    
    return addition, subtraction, multiplication, division

def broadcasting_operations(A, vector):
    """Perform broadcasting operations between matrix A and vector."""
    # Adding vector to each row of the matrix
    row_addition = A + vector
    
    # Adding vector to each column of the matrix
    column_addition = A + vector[:, np.newaxis]
    
    return row_addition, column_addition

def custom_operations(A, B, scalars):
    """Perform custom operations that combine vectorized operations and broadcasting."""
    # Scaling each row of matrix A by a different scalar
    scaled_rows_A = A * scalars[:, np.newaxis]
    
    # Scaling each column of matrix B by a different scalar (assuming scalars is 1D)
    scaled_columns_B = B * scalars
    
    return scaled_rows_A, scaled_columns_B

def print_summary(matrix, name):
    """Print a summary of the matrix."""
    print(f"\n{name} Summary:")
    print(f"Shape: {matrix.shape}")
    print(f"First element: {matrix[0, 0]}")
    print(f"First row: {matrix[0, :5]}")  # Print first 5 elements of the first row
    print(f"First column: {matrix[:5, 0]}")  # Print first 5 elements of the first column

def main():
    # Define the size of the matrices
    size = 1000
    
    # Generate two large random matrices
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    # Generate a random vector for broadcasting operations
    vector = np.random.rand(size)
    
    # Generate random scalars for custom operations
    scalars = np.random.rand(size)
    
    # Perform element-wise operations
    addition, subtraction, multiplication, division = element_wise_operations(A, B)
    print("Element-wise operations completed.")
    
    # Perform broadcasting operations
    row_addition, column_addition = broadcasting_operations(A, vector)
    print("Broadcasting operations completed.")
    
    # Perform custom operations
    scaled_rows_A, scaled_columns_B = custom_operations(A, B, scalars)
    print("Custom operations completed.")
    
    # Print summaries of results
    print_summary(addition, "Element-wise Addition")
    print_summary(subtraction, "Element-wise Subtraction")
    print_summary(multiplication, "Element-wise Multiplication")
    print_summary(division, "Element-wise Division")
    print_summary(row_addition, "Row-wise Addition with Vector")
    print_summary(column_addition, "Column-wise Addition with Vector")
    print_summary(scaled_rows_A, "Scaled Rows of A")
    print_summary(scaled_columns_B, "Scaled Columns of B")

if __name__ == "__main__":
    main()

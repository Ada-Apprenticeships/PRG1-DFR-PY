import os.path
from tda import (
    valid_number,
    data_dimensions,
    calculate_mean,
    find_total,
    convert_to_number,
    flatten,
    load_csv,
    calculate_median,
    create_slice
)


def test_valid_number01():
    """Tests for the valid_number function"""
    # Should identify valid numbers
    valid_cases = [
        0,
        1.5,
        -1.12,
        100,
        -100,
        "1.5",
        "-1.12",
        "100"
    ]
    for number in valid_cases:
        assert valid_number(number) == True, f"Expected {number} to be identified as a valid number."
    
    # Handles invalid number formats and special characters
    invalid_cases = [
        "+1.5",
        "5.",
        "1.2.3",
        "ABC",
        "12ABC",
        "",
        ".",
        "-",
        "+-1.1"
    ]
    for number in invalid_cases:
        assert valid_number(number) == False, f"Expected {number} to be identified as invalid."


def test_data_dimensions02():
    """Tests for the data_dimensions function"""
    # Should return correct dimensions for 2D array
    sales_data = [
        ["date", "region", "sales"],
        ["2024-01", "North", 1000],
        ["2024-01", "South", 1500]
    ]
    assert data_dimensions(sales_data) == [3, 3], "Failed to calculate correct dimensions for standard 2D list."
    
    # Should return correct dimensions for 1D array (treated as 1 row)
    monthly_sales = [1000, 1500, 2000]
    assert data_dimensions(monthly_sales) == [1, 3], "Failed to calculate dimensions for 1D list (should be 1 row)."
    
    # Handles empty and undefined inputs
    assert data_dimensions("") == None, "Should return None for empty string input."
    assert data_dimensions(None) == None, "Should return None for NoneType input."


def test_find_total03():
    """Tests for the find_total function"""
    # Should calculate correct sum for valid datasets
    sales_figures = [1500.5, 1900.25, "2000.00", 1750.75]
    assert find_total(sales_figures) == 7151.5, "Total sum calculation incorrect for mixed float/string data."
    
    single_sale = [1500.0]
    assert find_total(single_sale) == 1500.0, "Total sum incorrect for single-item list."
    
    # Handles invalid inputs and 2D arrays
    assert find_total([[1500.5]]) == None, "Should return None for 2D array (function expects 1D)."
    assert find_total("") == None, "Should return None for empty string input."
    
    mixed_data = [1500.5, 1900.25, "invalid", 1750.75]
    assert find_total(mixed_data) == 5151.5, "Failed to skip invalid values during summation."


def test_calculate_mean04():
    """Tests for the calculate_mean function"""
    # Should calculate correct average for valid datasets
    temperatures = [20.5, 21.0, "22.5", 19.8, 20.2]
    assert calculate_mean(temperatures) == 20.8, "Mean calculation incorrect for mixed float/string data."
    
    single_value = ["-5.5"]
    assert calculate_mean(single_value) == -5.5, "Mean calculation incorrect for single value list."
    
    # Handles empty arrays and invalid data types
    assert calculate_mean([]) == None, "Should return None for empty list."
    assert calculate_mean([[20.5, 21.0]]) == None, "Should return None for 2D list (expects 1D)."
    
    mixed_data = [20.5, 21.0, "invalid", 19.8, 20.2]
    assert calculate_mean(mixed_data) == 20.375, "Failed to calculate mean correctly when skipping invalid entries."


def test_calculate_median05():
    """Tests for the calculate_median function"""
    # Should find correct middle value for valid datasets
    odd_dataset = [10, 20, 30, 40, 50]
    assert calculate_median(odd_dataset) == 30.0, "Median incorrect for sorted, odd-length dataset."
    
    even_dataset = [10, 20, 30, 40]
    assert calculate_median(even_dataset) == 25.0, "Median incorrect for sorted, even-length dataset."
    
    single_value = ["19"]
    assert calculate_median(single_value) == 19.0, "Median incorrect for single value."

    # Handles Unsorted Odd Length
    unsorted_odd = [3, 5, 1, 4, 2] 
    assert calculate_median(unsorted_odd) == 3.0, "Failed to sort odd-length dataset (likely picked middle index of unsorted list)."

    # Handles Unsorted Even Length
    unsorted_even = [4, 1, 2, 3]
    assert calculate_median(unsorted_even) == 2.5, "Failed to sort even-length dataset before calculating."

    # Handles Unsorted with Strings/Invalid Data
    mixed_unsorted = [100, "invalid", 5, 50, 10]
    assert calculate_median(mixed_unsorted) == 30.0, "Failed to handle sorting with invalid data interspersed."
    
    # Handles empty arrays
    assert calculate_median([]) == None, "Should return None for empty list."
    

def test_convert_to_number06():
    """Tests for the convert_to_number function"""
    # Should convert string numbers to actual numbers
    sales_data = [
        ["region", "sales", "units"],
        ["North", "1000", "50"],
        ["South", "1500", "75"]
    ]
    
    count = convert_to_number(sales_data, 1)
    assert count == 2, f"Expected 2 conversions, got {count}."
    assert isinstance(sales_data[1][1], (int, float)), "Data at [1][1] was not converted to a number type."
    assert sales_data[1][1] == 1000, "Value at [1][1] incorrect after conversion."
    assert sales_data[2][1] == 1500, "Value at [2][1] incorrect after conversion."
    
    # Handles non-numeric strings in conversion
    mixed_data = [
        ["region", "sales"],
        ["North", "invalid"],
        ["South", "1500"]
    ]
    assert convert_to_number(mixed_data, 1) == 1, "Should only convert valid numbers (expected count 1)."

    # Test: Mixed valid/invalid data in column
    mixed = [
    ["header"],
    ["10"],
    ["abc"],
    ["20.5"],
    [""],
    ["30"]
    ]
    count = convert_to_number(mixed, 0)
    assert count == 3, f"Should convert 3 valid numbers, got {count}."
    assert mixed[1][0] == 10, "Should convert '10' to number."
    assert mixed[2][0] == "abc", "Should leave 'abc' unchanged."
    assert mixed[3][0] == 20.5, "Should convert '20.5' to number."
    assert mixed[4][0] == "", "Should leave empty string unchanged."
    assert mixed[5][0] == 30, "Should convert '30' to number."

    # Test: Out of range column index (positive)
    data = [["A", "B"], 
            ["1", "2"], 
            ["3", "4"]]
    
    assert convert_to_number(data, 5) == 0, "Should return 0 for out of range column index."
    assert data == [["A", "B"], ["1", "2"], ["3", "4"]], "Should not modify data when column is out of range."
    
    # Test: Out of range column index (negative)
    data = [["A", "B"], ["1", "2"]]
    assert convert_to_number(data, -1) == 0, "Should return 0 for negative column index."
    
    # Test: None dataframe
    assert convert_to_number(None, 0) == 0, "Should return 0 for None dataframe."
    
    # Test: Empty dataframe
    assert convert_to_number([], 0) == 0, "Should return 0 for empty dataframe."
    
    # Test: 1D list instead of 2D (invalid structure)
    assert convert_to_number([1, 2, 3], 0) == 0, "Should return 0 for 1D list (expects 2D)."
    
    # Test: Empty 2D list (has structure but no rows)
    assert convert_to_number([[]], 0) == 0, "Should return 0 for 2D list with no data rows."
  


def test_flatten07():
    """Tests for the flatten function and checks for non-destructive operation."""
    # Should convert single-column 2D List to 1D List
    monthly_temperatures = [[20.5], [21.0], [22.5], [19.8], [20.2]]
    # Store a deep copy of the original data to ensure immutability
    original_data_copy = [row[:] for row in monthly_temperatures] 
    
    result = flatten(monthly_temperatures)
    
    assert result == [20.5, 21.0, 22.5, 19.8, 20.2], "Flattened list content does not match expected output."
    assert data_dimensions(result) == [1, 5], "Dimensions of flattened list are incorrect."
    
    # Check if the original data structure was not mutated
    assert monthly_temperatures == original_data_copy, "Original list was mutated (side effect detected)."
    
    # Handles invalid data structures (1D list or multi-column 2D list)
    multi_column_data = [20.5, 21.0, 22.5]
    assert flatten(multi_column_data) == None, "Should return None when input is already 1D."
    
    # Won't flatten multi-column 2D Lists
    invalid_data = [
        [23.5, 45],
        [25.1, 42]
    ]
    assert flatten(invalid_data) == None, "Should return None for multi-column 2D lists."


def test_create_slice08():
    """Tests for the create_slice function"""
    # Should create correct 2D List slices
    sales_data = [
        ["date", "region", "product", "sales"],
        ["2024-01", "North", "Laptop", 1000],
        ["2024-01", "South", "Phone", 1500],
        ["2024-01", "North", "Tablet", 2000]
    ]
    
    expected_slice = [
        ["North", 1000],
        ["North", 2000]
    ]
    assert create_slice(sales_data, 1, "North", [1, 3]) == expected_slice, "Sliced data content incorrect for specific match."
    
    # Should handle wildcard selections (includes header row)
    wildcard_data = [
        ["date", "region", "product", "sales"],
        ["2024-01", "North", "Laptop", 1000],
        ["2024-01", "South", "Phone", 1500]
    ]
    
    expected_wildcard = [
        ["region", "sales"],
        ["North", 1000],
        ["South", 1500]
    ]
    # Note: Wildcard includes ALL rows including header
    assert create_slice(wildcard_data, 0, "*", [1, 3]) == expected_wildcard, "Sliced data content incorrect for wildcard (*) match."

    # Ensure create_slice does not modify the original list."""
    original_data = [
        ["region", "sales"],
        ["North", 100],
        ["South", 200]
    ]
    # Create a deep copy manually for comparison
    copy_of_data = [row[:] for row in original_data]
    
    create_slice(original_data, 0, "North")
    
    # Assert the original data is exactly as it was
    assert original_data == copy_of_data, "Function modified the input list (side effect)"


def test_load_csv09():
    """Tests for the load_csv function and checks for non-destructive editing of parameters."""
    # Define mutable inputs
    ignore_rows_list = [0]
    ignore_cols_list = []
    
    # Store copies to check against later
    original_ignore_rows = ignore_rows_list[:]
    original_ignore_cols = ignore_cols_list[:]
    
    # Should correctly load and process CSV files
    sales_data, total_rows, total_columns = load_csv(
        "./sales_data.csv",
        ignore_rows_list, # Use the mutable input list
        ignore_cols_list
    )
    
    assert total_rows == 7, f"Expected 7 rows, got {total_rows}."
    assert total_columns == 7, f"Expected 7 columns, got {total_columns}."
    
    expected_first_row = [
        "2024-01-15",
        "North",
        "Laptop",
        "5",
        "999.99",
        "4999.95",
        "completed"
    ]
    assert sales_data[0] == expected_first_row, "First row of loaded CSV does not match expected data."
    
    # Check if input parameters were not mutated
    assert ignore_rows_list == original_ignore_rows, "Input parameter 'ignore_rows_list' was mutated."
    assert ignore_cols_list == original_ignore_cols, "Input parameter 'ignore_cols_list' was mutated."

    # Handles nonexistent file paths
    empty_data, rows, cols = load_csv("./nonexistent.csv")
    assert empty_data == None, "Should return None data for nonexistent file."
    assert rows == None, "Should return None rows for nonexistent file."
    assert cols == None, "Should return None cols for nonexistent file."


def test_integration10():
    """Integration tests combining multiple functions"""
    # Should load CSV, slice data, and calculate totals
    sales_data, total_rows, total_columns = load_csv(
        "./sales_data.csv",
        [0],
        []
    )
    
    convert_to_number(sales_data, 3)
    north_sales = create_slice(sales_data, 1, "North", [5])
    north_sales_data = flatten(north_sales)
    total_north_sales = find_total(north_sales_data)
    
    assert total_north_sales == 7099.92, f"Integration test failed. Expected total 7099.92, got {total_north_sales}"
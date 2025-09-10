import pytest
import os.path
from dfr import (
    file_exists,
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

class TestDataFrameProject:
    
    def test_file_exists01(self):
        """Tests for the file_exists function"""
        # Should identify existing files
        assert file_exists("./sales_data.csv") == True
        
        # Handles nonexistent and empty file paths
        assert file_exists("./assets/testing/nonexistent.csv") == False
        assert file_exists("") == False
    
    def test_valid_number02(self):
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
            assert valid_number(number) == True
        
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
            assert valid_number(number) == False
    
    def test_data_dimensions03(self):
        """Tests for the data_dimensions function"""
        # Should return correct dimensions for 2D array
        sales_data = [
            ["date", "region", "sales"],
            ["2024-01", "North", 1000],
            ["2024-01", "South", 1500]
        ]
        assert data_dimensions(sales_data) == [3, 3]
        
        # Should return correct dimensions for 1D array
        monthly_sales = [1000, 1500, 2000]
        assert data_dimensions(monthly_sales) == [3, -1]
        
        # Handles empty and undefined inputs
        assert data_dimensions("") == [-1, -1]
        assert data_dimensions(None) == [-1, -1]
    
    def test_find_total04(self):
        """Tests for the find_total function"""
        # Should calculate correct sum for valid datasets
        sales_figures = [1500.5, 1900.25, "2000.00", 1750.75]
        assert find_total(sales_figures) == 7151.5
        
        single_sale = [1500.0]
        assert find_total(single_sale) == 1500.0
        
        # Handles invalid inputs and 2D arrays
        assert find_total([[1500.5]]) == 0  # 2D array not allowed
        assert find_total("") == 0
        mixed_data = [1500.5, 1900.25, "invalid", 1750.75]
        assert find_total(mixed_data) == 5151.5  # Should skip invalid value
    
    def test_calculate_mean05(self):
        """Tests for the calculate_mean function"""
        # Should calculate correct average for valid datasets
        temperatures = [20.5, 21.0, "22.5", 19.8, 20.2]
        assert calculate_mean(temperatures) == 20.8
        
        single_value = ["-5.5"]
        assert calculate_mean(single_value) == -5.5
        
        # Handles empty arrays and invalid data types
        assert calculate_mean([]) == 0
        assert calculate_mean([[20.5, 21.0]]) == 0
        mixed_data = [20.5, 21.0, "invalid", 19.8, 20.2]
        assert calculate_mean(mixed_data) == 20.375  # Should skip invalid value
    
    def test_calculate_median06(self):
        """Tests for the calculate_median function"""
        # Should find correct middle value for valid datasets
        odd_dataset = [10, 20, 30, 40, 50]
        assert calculate_median(odd_dataset) == 30.0
        
        even_dataset = [10, 20, 30, 40]
        assert calculate_median(even_dataset) == 25.0
        
        single_value = ["19"]
        assert calculate_median(single_value) == 19.0
        
        # Handles empty arrays and invalid values
        assert calculate_median([]) == 0
        mixed_dataset = [10, 20, "30", "invalid", 40, 50]
        assert calculate_median(mixed_dataset) == 30.0
    
    def test_convert_to_number07(self):
        """Tests for the convert_to_number function"""
        # Should convert string numbers to actual numbers
        sales_data = [
            ["region", "sales", "units"],
            ["North", "1000", "50"],
            ["South", "1500", "75"]
        ]
        
        assert convert_to_number(sales_data, 1) == 2
        assert isinstance(sales_data[1][1], (int, float))
        assert sales_data[1][1] == 1000
        assert sales_data[2][1] == 1500
        
        # Handles non-numeric strings in conversion
        mixed_data = [
            ["region", "sales"],
            ["North", "invalid"],
            ["South", "1500"]
        ]
        assert convert_to_number(mixed_data, 1) == 1  # Should only convert valid numbers
    
    def test_flatten(self):
        """Tests for the flatten function"""
        # Should convert single-column DataFrame to Dataset
        monthly_temperatures = [[20.5], [21.0], [22.5], [19.8], [20.2]]
        assert flatten(monthly_temperatures) == [20.5, 21.0, 22.5, 19.8, 20.2]
        
        # Handles invalid data structures
        multi_column_data = [20.5, 21.0, 22.5]
        assert flatten(multi_column_data) == []
    
    def test_create_slice08(self):
        """Tests for the create_slice function"""
        # Should create correct DataFrame slices
        sales_data = [
            ["date", "region", "product", "sales"],
            ["2024-01", "North", "Laptop", 1000],
            ["2024-01", "South", "Phone", 1500],
            ["2024-01", "North", "Tablet", 2000]
        ]
        
        assert create_slice(sales_data, 1, "North", [1, 3]) == [
            ["North", 1000],
            ["North", 2000]
        ]
        
        # Should handle wildcard selections
        wildcard_data = [
            ["date", "region", "product", "sales"],
            ["2024-01", "North", "Laptop", 1000],
            ["2024-01", "South", "Phone", 1500]
        ]
        
        assert create_slice(wildcard_data, 0, "*", [1, 3]) == [
            ["region", "sales"],
            ["North", 1000],
            ["South", 1500]
        ]
    
    def test_load_csv09(self):
        """Tests for the load_csv function"""
        # Should correctly load and process CSV files
        sales_data, total_rows, total_columns = load_csv(
            "./sales_data.csv",
            [0],
            []
        )
        
        assert total_rows == 7
        assert total_columns == 7
        assert sales_data[0] == [
            "2024-01-15",
            "North",
            "Laptop",
            "5",
            "999.99",
            "4999.95",
            "completed"
        ]
        
        # Handles nonexistent file paths
        empty_data, rows, cols = load_csv("./nonexistent.csv")
        assert empty_data == []
        assert rows == -1
        assert cols == -1
    
    def test_integration10(self):
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
        
        assert total_north_sales == 7099.92
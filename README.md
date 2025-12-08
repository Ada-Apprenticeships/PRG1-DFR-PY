# 2D List Project Documentation (Python) 🐍

### This project uses many of the same techniques you've already completed in the previous tasks. This project has been specifically designed to be a challenging task. Don't forget - you do not need to complete ALL tasks in this assignment to PASS this module overall.

## Overview and Key Concepts

### What is a 2D List?

A **2D List** is a 2-dimensional array, similar to a spreadsheet with rows and columns. You can think of it as a table of data.

```python
# Example 2D List
weather_data = [
  ["date", "temp", "humidity"], # Headers
  ["2024-01", 23.5, 45], # Row 1
  ["2024-02", 25.1, 42], # Row 2
]

# Accessing elements using [row][column]:
weather_data[1][1]  # → 23.5 (First data row, temperature column)
weather_data[2][2]  # → 42 (Second data row, humidity column)
```

### What is a 1D List?

A **1D List** is a 1-dimensional array - like a single row or column of data.

```python
# Example 1D List
temperatures = [23.5, 25.1, 24.8, 26.2]

# Accessing elements:
temperatures[0]  # → 23.5 (First temperature)
temperatures[3]  # → 26.2 (Fourth temperature)
```

## Core Functions

### Valid Number Check (valid_number)

Determines if a value represents a valid number. Works with positive/negative numbers and integers/decimals.

```python
valid_number("0.1")      # → True
valid_number("-1.12")    # → True
valid_number(5)          # → True
valid_number(-10)        # → True
valid_number("5.")       # → False (decimal point must be followed by digits)
valid_number("+5")       # → False (explicit plus sign not allowed)
valid_number("0.0.1")    # → False (multiple decimal points)
valid_number("three")    # → False (not a number)
```

### Data Dimensions (data_dimensions)

Returns the dimensions [rows, columns] of a 2D List or 1D List. Returns `None` if the input is not 1D or 2D list.

```python
sales_data = [
  ["Q1", 1000, 1200, 950],
  ["Q2", 1100, 1300, 975],
  ["Q3", 1200, 1400, 1000],
]

data_dimensions(sales_data)      # → [3, 4] (3 rows, 4 columns)
data_dimensions([1000, 1100])    # → [1, 2] (1 row, 2 columns)
data_dimensions(None)            # → None (No data / Invalid input)
```

### Find Total (find_total)

Sums all valid numbers in a 1D List. Returns `None` for anything other than a 1D List.

```python
monthly_revenue = [1500.5, 1900.25, "2000.00", 1750.75, "pending"]
find_total(monthly_revenue)  # → 7151.50

invalid_input = [[100], [200]]  # 2D array instead of 1D List
find_total(invalid_input)  # → None (invalid dimensions)
```

### Calculate Mean (calculate_mean)

Calculates the average of all valid numbers in a 1D List. Returns None for invalid dimensions or if no valid numbers are present.

```python
sales_figures = [1500, 1900, 2000, 1750, "1800", "invalid"]
calculate_mean(sales_figures)  # → 1790

invalid_data = [["not"], ["a"], ["1D"], ["List"]]
calculate_mean(invalid_data)  # → None (invalid dimensions)
```

### Calculate Median (calculate_median)

Finds the middle value of a sorted 1D List. Returns None for invalid dimensions or if no valid numbers are present.

```python
response_times = [1.5, 1.9, 10.0, 50, -10, "3", "1"]
calculate_median(response_times)  # → 1.9

even_dataset = [1, 2, 3, 4]
calculate_median(even_dataset)  # → 2.5 (average of 2 and 3)

invalid_data = [[1], [2]]  # 2D list instead of 1D List
calculate_median(invalid_data)  # → None
```

### Convert To Number (convert_to_number)

Converts string numbers to actual numbers in a specified column.

```python
traffic_data = [
  ["protocol", "requests", "latency"], # Column indices: 0, 1, 2
  ["tcp", "1000", "2.5"], #                ↓  ↓  ↓
  ["udp", "1500", "1.8"], #                0  1  2
]

# Convert string numbers in 'requests' column (index 1)
convert_to_number(traffic_data, 1)  # → 2 (converted '1000' and '1500' to numbers)
# traffic_data is now:
# [
#   ['protocol', 'requests', 'latency'],
#   ['tcp',       1000,     '2.5'    ],  # '1000' → 1000
#   ['udp',       1500,     '1.8'    ]   # '1500' → 1500
# ]

# Convert string numbers in 'latency' column (index 2)
convert_to_number(traffic_data, 2)  # → 2 (converted '2.5' and '1.8' to numbers)
# traffic_data is now:
# [
#   ['protocol', 'requests', 'latency'],
#   ['tcp',       1000,      2.5     ],  # '2.5' → 2.5
#   ['udp',       1500,      1.8     ]   # '1.8' → 1.8
# ]
```

### Flatten 2D List (flatten)

Converts a single-column 2D List into a 1D List. Only works on 2D Lists with exactly one column. Returns `None` for invalid inputs.

```python
temperatures = [[23.5], [25.1], [24.8]]

flatten(temperatures)  # → [23.5, 25.1, 24.8]
data_dimensions(temperatures)  # → [3, 1]
data_dimensions(flatten(temperatures))  # → [1, 3]

# Won't flatten multi-column 2D Lists
invalid_data = [
  [23.5, 45],
  [25.1, 42],
]
flatten(invalid_data)  # → None (Invalid dimensions)
```

### Load CSV (load_csv)

#### Parameters

- **filepath** (string)

  - The path to the CSV file to load
  - Can be relative (e.g., './data/sales.csv') or absolute
  - Required parameter
  - Example: `'./sales_data.csv'`

- **ignore_rows** (list of integers, optional)

  - List of row indices to skip when loading the data
  - Zero-based indexing (0 = first row, 1 = second row, etc.)
  - Common use: `[0]` to skip header row
  - Default value: `[]` (include all rows)
  - Examples:
    - `[0]` - Skip first row
    - `[0, 1]` - Skip first and second rows
    - `[]` - Skip no rows

- **ignore_cols** (list of integers, optional)
  - List of column indices to exclude from the loaded data
  - Zero-based indexing (0 = first column, 1 = second column, etc.)
  - Default value: `[]` (include all columns)
  - Examples:
    - `[0]` - Exclude first column
    - `[0, 2]` - Exclude first and third columns
    - `[]` - Exclude no columns

#### Return Value

Returns a tuple containing three elements: `(two_d_list, total_rows, total_columns)`.

- On successful load: `two_d_list` (2D list), `total_rows` (int), `total_columns` (int).
- On failure (e.g., file not found): `(None, None, None)`

**Implementation Note:** You must use a `try...except FileNotFoundError` block when attempting to open the file. This is the idiomatic Python way to handle non-existent files. If this exception is caught, the function should return the failure signal `(None, None, None)`.

#### Sample CSV File (sales_data.csv):

```csv
date,region,product,quantity,unit_price,total_sales,status
2024-01-15,North,Laptop,5,999.99,4999.95,completed
2024-01-15,South,Phone,10,499.99,4999.90,completed
2024-01-16,North,Tablet,3,699.99,2099.97,pending
2024-01-16,East,Laptop,7,999.99,6999.93,completed
2024-01-17,West,Phone,4,499.99,1999.96,completed
2024-01-17,South,Tablet,6,699.99,4199.94,cancelled
```

#### Example 1: Load entire CSV (skip header)

```python
sales_data, total_rows, total_columns = load_csv(
  "./sales_data.csv",
  [0],  # Ignore first row (headers)
  []    # Include all columns
)

# total_rows → 7 (6 data rows + 1 header)
# total_columns → 7
# sales_data will be:
# [
#   ['2024-01-15', 'North', 'Laptop', '5', '999.99', '4999.95', 'completed'],
#   ['2024-01-15', 'South', 'Phone',  '10', '499.99', '4999.90', 'completed'],
#   ['2024-01-16', 'North', 'Tablet', '3', '699.99', '2099.97', 'pending'],
#   ['2024-01-16', 'East',  'Laptop', '7', '999.99', '6999.93', 'completed'],
#   ['2024-01-17', 'West',  'Phone',  '4', '499.99', '1999.96', 'completed'],
#   ['2024-01-17', 'South', 'Tablet', '6', '699.99', '4199.94', 'cancelled']
# ]
```

#### Example 2: Load CSV (skip header and ignore some columns)

```python
filtered_data, rows, cols = load_csv(
  "./sales_data.csv",
  [0],  # Ignore header row
  [0, 5, 6]  # Ignore date, total_sales, and status columns
)

# rows → 7 (original row count unchanged)
# cols → 7 (original column count unchanged)
# filtered_data will be:
# [
#   ['North', 'Laptop', '5', '999.99'],
#   ['South', 'Phone',  '10', '499.99'],
#   ['North', 'Tablet', '3', '699.99'],
#   ['East',  'Laptop', '7', '999.99'],
#   ['West',  'Phone',  '4', '499.99'],
#   ['South', 'Tablet', '6', '699.99']
# ]
```

#### Example 3: Loading a non-existent file

```python
empty_data, rows, cols = load_csv("./nonexistent.csv")
# Returns: (None, None, None)
```

#### Common Usage Pattern:

```python
# Load data and convert numeric columns
sales_data, rows, cols = load_csv("./sales_data.csv", [0], [])
if sales_data is not None: # Check for None
  # Convert quantity column (index 3) to numbers
  convert_to_number(sales_data, 3)

  # Convert unit_price column (index 4) to numbers
  convert_to_number(sales_data, 4)

  # Convert total_sales column (index 5) to numbers
  convert_to_number(sales_data, 5)
```

### Creating a slice (create_slice)

#### Function Signature

```python
create_slice(two_d_list, column_index, pattern, export_columns=[])
```

#### Parameters Explained

**1. two_d_list**

- The source 2D List to slice from
- Must be a 2D array (list of lists)

**2. column_index**

- Which column to check for matches
- Zero-based index (0 = first column, 1 = second column, etc.)
- Used to identify which rows to include based on the pattern

**3. pattern**

- The value to match in the specified column
- Special case: `'*'` matches any value (includes all rows)
- Case-sensitive for string matches

**4. export_columns** (optional)

- List of column indices to include in the result
- If omitted or empty list (`[]`), includes all columns
- Zero-based indices

#### Detailed Examples

**Example 1: Basic Filtering**

```python
sales_data = [
  ["region", "product", "sales", "profit"], # Column indices: 0, 1, 2, 3
  ["north", "laptop", 1000, 200],
  ["south", "phone", 500, 100],
  ["north", "tablet", 750, 150],
  ["east", "laptop", 1200, 240],
]

# Get all rows where region (column 0) is 'north'
create_slice(sales_data, 0, "north")
# Returns:
# [
#   ['north', 'laptop', 1000, 200],
#   ['north', 'tablet', 750, 150]
# ]
```

**Example 3: Using Wildcard Pattern**

```python
# Get all rows (*) but only product and sales columns (1 and 2)
create_slice(sales_data, 0, "*", [1, 2])
# Returns:
# [
#   ['laptop', 1000],
#   ['phone',  500],
#   ['tablet', 750],
#   ['laptop', 1200]
# ]
```

**Example 4: Filtering by Non-First Column**

```python
# Get all rows where product (column 1) is 'laptop'
create_slice(sales_data, 1, "laptop", [0, 2])
# Returns:
# [
#   ['north', 1000],  # Region and sales for laptop rows
#   ['east',  1200]
# ]
```

#### Key Points to Remember

**Column Indexing:**

- Always zero-based
- First column is 0, second is 1, etc.
- Invalid column indices are ignored

**Pattern Matching:**

- Case sensitive ('SALE' ≠ 'sale')
- `'*'` is special wildcard character
- Exact match required for all other patterns

**Export Columns:**

- Optional parameter
- If omitted, all columns are included
- Order matters: `[2, 0]` will return columns in that order
- Invalid indices are ignored

**Return Value:**

- Always returns a new 2D List
- Original 2D List is unchanged
- Empty 2D List (`[]`) if no matches found

## Implementation Requirements

- No external libraries allowed except those specifically provided
- All functions must handle invalid inputs gracefully
- Use `None` to indicate 'no data' or 'invalid input' for functions returning a single value or tuple.
- The `load_csv` function must use `try...except FileNotFoundError` and return `(None, None, None)` on failure.
- Functions should validate input dimensions before processing
- Maintain consistent type handling (strings vs numbers)

## Testing Guidelines

- Create small test files during development
- Test edge cases: Empty arrays, invalid numbers, mixed data types, missing/undefined values.
- Verify dimension handling: Single-row/column/empty 2D Lists, 1D Lists vs 2D Lists, and inputs that should result in a return value of `None`.
- Check type conversions: String to number conversions, valid vs invalid number formats.
- Test with both valid and invalid inputs:
  - Correct file paths
  - Incorrect file paths (verify that `FileNotFoundError` is caught and `(None, None, None)` is returned)
  - Valid/invalid column indices and patterns for slicing.
import pandas as pd
import numpy as np

# Creating an extended dictionary
data = {
    'FirstName': ['Alice','Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Mallory', 'Nia', 'Oscar', 'Peggy', 'Sybil', 'Trent', 'Victor', 'Walter', 'Xavier', 'Yvonne'],
    'LastName': ['Smith','Smith', 'Brown', 'Davis', 'Johnson', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis'],
    'Age': [24, 24, 30, np.nan, np.nan, 28, 40, 27, 29, 31, 23, 26, 34, 25, 32, 21, 33, 36, 28, 27, 29],
    'City': ['New York','New York', 'Los Angeles', 'Chicago', 'New York', 'Phoenix', 'Philadelphia', 'New York', 'Philadelphia', 'Dallas', 'Philadelphia', 'Austin', 'Philadelphia', 'Fort Worth', 'Columbus', 'San Francisco', 'Charlotte', 'San Francisco', 'Seattle', 'Denver', 'San Francisco'],
    'State': ['NY','NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA', 'TX', 'FL', 'TX', 'OH', 'CA', 'NC', 'IN', 'WA', 'CO', 'DC'],
    'Gender': ['Female','Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Female'],
    'Salary': [70000,70000, 85000, 60000, 95000, 75000, 80000, 68000, 72000, 69000, 71000, 67000, 74000, 80000, 76000, 82000, 83000, 86000, 87000, 91000, 94000],
    'DOB': ['1997-01-15','1997-01-15', '1992-04-22', '1999-07-09', '1986-11-05', '1993-03-14', '1981-08-23', '1994-12-01', '1992-10-11', '1990-02-24', '1998-06-17', '1995-09-30', '1987-02-18', '1996-05-21', '1989-07-08', '2000-11-12', '1988-01-03', '1985-04-28', '1993-06-16', '1994-08-05', '1992-10-19'],
    'Email': ['alice.smith@example.com','alice.smith@example.com', 'bob.brown@example.com', 'charlie.davis@example.com', 'david.johnson@example.com', 'eve.wilson@example.com', 'frank.moore@example.com', 'grace.taylor@example.com', 'heidi.anderson@example.com', 'ivan.thomas@example.com', 'judy.jackson@example.com', 'mallory.white@example.com', 'nia.harris@example.com', 'oscar.martin@example.com', 'peggy.thompson@example.com', 'sybil.garcia@example.com', 'trent.martinez@example.com', 'victor.robinson@example.com', 'walter.clark@example.com', 'xavier.rodriguez@example.com', 'yvonne.lewis@example.com']
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
df.head()
df.duplicated().sum()


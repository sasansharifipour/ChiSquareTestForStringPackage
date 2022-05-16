# ChiSquareTestForStringPackage

Pyspark has a function named ChiSquareTest which calculates the chi-square between two columns, but this function only accepts the numerical columns; by this package, a function called ChiSquareTestForString will be added to pyspark, which calculates the chi-square for string columns.

1: Install the package by this command : pip install ChiSquareTestForString <br />
2. Import the package like this: import ChiSquareTestForString <br />
3. Use the package like this : chi_square, dof = pyspark.ml.stat.ChiSquareTestForString(df, col1_name, col2_name) <br />
 <br />
As you can see, this function will accept three inputs,  df, a pyspark DataFrame, and two strings, which are the names of two columns that exist in df, and will return the chi-square between these columns and the degree of freedom.
 <br />
I hope it can help you.

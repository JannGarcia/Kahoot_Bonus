## How to use
1. Clone the repository (duh)
2. Add all Kahoot reports to the reports/ folder
    - Make sure that each report file is in xlsx format!
    - The spreadsheet should contain a sheet labeled: `"Final Scores"`
    - This code expects each row to be of the format: 
        - `Rank | Player | Player Identifier | Total Score | Correct | Incorrect`
3. Delete the sample_report.xlsx from the reports folder, it's only meant to be for demonstration. Keeping it might cause issues.
4. Run the code
5. The code will output a file containing the amount of bonus points each student has earned
    - If a student has not earned any bonus points, they will not be included in the output file
    - The output file will be in the format: 
        - `Name | Bonus Points`
6. Done!
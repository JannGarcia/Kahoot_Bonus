## How to use
1. Clone the repository (duh)
2. Add all Kahoot reports to the reports/ folder
    - Make sure that each report file is in xlsx format!
    - The spreadsheet should contain a sheet labeled: `"Final Scores"`
    - This code expects each row to be of the format: 
        - `Rank | Player | Total Score | Correct | Incorrect`
3. Run the code
4. The code will output a file containing the amount of bonus points each student has earned
    - If a student has not earned any bonus points, they will not be included in the output file
    - The output file will be in the format: 
        - `Player | Bonus Points`
5. Done!
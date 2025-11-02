🧹 Data Cleaner Tool (Python + Pandas + Docker)

A simple and lightweight **Data Cleaning CLI Tool** built with **Python** and **Pandas**, designed to quickly remove missing values from CSV files.
The tool can be run locally or inside a Docker container for consistent and portable execution.

🚀 Features

✅ Reads CSV files
✅ Removes rows with missing (`NaN`) values
✅ Saves the cleaned data into a new CSV file
✅ Supports command-line arguments (`--input` and `--output`)
✅ Dockerized for easy deployment and reproducibility

 🧱 Project Structure

data-cleaner/
├── data_cleaner.py       # Main Python script
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image definition
└── README.md             # Project documentation

🧠 How It Works
The script:

1. Reads the input CSV file using **Pandas**
2. Drops any rows that contain missing values
3. Saves the cleaned data to the specified output file

Example Flow:

```
Input CSV → [Rows with NaN] → Data Cleaner → Output CSV (cleaned)
```
⚙️ Installation and Usage
🐍 Run Locally (Without Docker)

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
2. Run the script

   ```bash
   python data_cleaner.py --input data.csv --output cleaned.csv
   ```
3. Expected Output

   ```
   ✅ Cleaned data saved to cleaned.csv
   🧾 Rows before: 1000, after: 920, removed: 80
   ```
🐳 Run Inside Docker

 1. Build the Docker image

```bash
docker build -t data-cleaner .
```
2. Run the container

```bash
docker run -v $(pwd):/app data-cleaner --input data.csv --output cleaned.csv
```
 `-v $(pwd):/app` mounts your current directory to `/app` inside the container,
  allowing access to your CSV files.

3. Verify Output
After running, you’ll find the cleaned file in your current folder:

```
cleaned.csv
```
🧾 License
This project is open-source and available under the MIT License.

👨‍💻 Author
Name: Unaid Abdullah
Created:2025
Tech Stack: Python, Pandas, Docker
GitHub: [@unaidabdullah-ui](https://github.com/unaidabdullah-ui)

> 🧹 “Clean data is happy data — automate your data cleaning and save time!”

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF



# Step 1: Load Excel file
file_path = input("Enter the Excel file name (e.g. data.xlsx): ")
df = pd.read_excel("E:\excel_analuzer\data.xlsx.xlsx")

# Step 2: Show preview
print("\nPreview of the data:")
print(df.head())

# Step 3: Basic analysis
print("\nData Analysis:")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nStatistical Summary:")
print(df.describe())

# Step 4: Plot a histogram for a numeric column
column = input("\nEnter the name of a numeric column to plot (e.g. Age, Salary): ")

if column in df.columns:
    plt.figure(figsize=(8, 5))
    df[column].hist(bins=10, color='skyblue', edgecolor='black')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()
    print("\nChart saved as chart.png")
else:
    print("Column not found!")


# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Excel Data Analysis Report", ln=True, align='C')

# Basic info
pdf.cell(200, 10, txt=f"Rows: {df.shape[0]}, Columns: {df.shape[1]}", ln=True)

# Add column names
pdf.cell(200, 10, txt="Columns:", ln=True)
for col in df.columns:
    pdf.cell(200, 8, txt=f"- {col}", ln=True)

# Save chart image to PDF (if created)
try:
    pdf.image("chart.png", x=10, y=None, w=180)
except:
    pdf.cell(200, 10, txt="No chart image found.", ln=True)

# Save the PDF file
pdf.output("report.pdf")
print("\nPDF report saved as report.pdf")
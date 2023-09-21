import os
import glob
import pandas as pd


def create_report() -> None:
	
	# Define the folder path where your CSV files are located
	folder_path = 'C:\\Projects\\VFCorp_Reports'
	
	# Define the patterns for matching CSV files of different prefixes
	prefix_patterns = {
		'TNF': 'report_TNF_Onboarding Report_*.csv',
		'TBL': 'report_TBL_Onboarding Report_*.csv',
		'VANS': 'report_VANS_Onboarding Report_*.csv',
	}
	
	# Loop through the prefix patterns and matching CSV files
	for prefix, pattern in prefix_patterns.items():
		# Get a list of CSV files for the current prefix
		csv_files = glob.glob(os.path.join(folder_path, pattern))
		
		# Check if any CSV files were found for the current prefix
		if csv_files:
			# Read and concatenate the CSV files for the current prefix
			df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
			# Creating Blank Output excel file
			output_excel_file = os.path.join(folder_path + '\\Reports', f"{prefix}_Onboarding_Report.xlsx")
			# Converting csv file to excel file
			df.to_excel(output_excel_file, index=False)
			# Printing Logs
			print(f'[INFO] Merged {len(csv_files)} {prefix} CSV files into {output_excel_file}')
		else:
			print(f'[INFO] Not found any {prefix} reports')


if __name__ == '__main__':
	create_report()

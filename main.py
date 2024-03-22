import pandas as pd

# 1. Show the first 5 lines of the TSV file.
data = pd.read_csv('04_gap-merged.tsv', sep='\t')
print(data.head())
print("--------------------------------------------------------------------------------------------------------------")
# 2. Find the number of rows and columns.
num_rows, num_columns = data.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)
print("--------------------------------------------------------------------------------------------------------------")
# 3. Print the name of the columns.
print("Column names:")
print(data.columns)
print("--------------------------------------------------------------------------------------------------------------")
# 4. Type of column names
print("Type of column names:", type(data.columns))
print("--------------------------------------------------------------------------------------------------------------")
# 5. Get the country column and save it to its own variable. Show the first 5 observations.
country_column = data['country']
print("First 5 observations of country column:")
print(country_column.head())
print("--------------------------------------------------------------------------------------------------------------")
# 6. Show the last 5 observations of this column.
print("Last 5 observations of country column:")
print(country_column.tail())
print("--------------------------------------------------------------------------------------------------------------")
# 7. Show the first 5 observations of 'country', 'continent', and 'year' columns, and the last 5 observations.
print("First 5 observations of 'country', 'continent', and 'year' columns:")
print(data[['country', 'continent', 'year']].head())

print("Last 5 observations of 'country', 'continent', and 'year' columns:")
print(data[['country', 'continent', 'year']].tail())
print("--------------------------------------------------------------------------------------------------------------")
print("Lấy hàng dầu tiên")
first_row = data.iloc[0]
print(f'Lấy hàng dầu tiên: {first_row}')
print("--------------------------------------------------------------------------------------------------------------")
print("Lấy hàng thứ 100")
hundredth_row = data.iloc[99]
print(f'Lấy hàng thứ 100: {hundredth_row}')
print("--------------------------------------------------------------------------------------------------------------")

print("Thử lấy cột đầu tiên bằng chỉ mục số nguyên. Và lấy cột đầu tiên và cuối cùng bằng cách truyền chỉ mục số nguyên:")
first_column = data.iloc[:, 0]
last_column = data.iloc[:, -1]
print(f'{first_column}, {last_column}')
print("--------------------------------------------------------------------------------------------------------------")

print("Để lấy hàng cuối cùng bằng .loc, bạn nên sử dụng chỉ mục -1:")
last_row = data.loc[len(data)-1]
print(f'{last_row}')
print("--------------------------------------------------------------------------------------------------------------")

print("Lấy các hàng đầu tiên, hàng thứ 100 và hàng thứ 1000 bằng hai phương pháp:")
# Phương pháp 1: Sử dụng .iloc
rows_method1 = data.iloc[[0, 99, 999]]
print(f'{rows_method1}')

# Phương pháp 2: Sử dụng .loc
rows_method2 = data.loc[[0, 99, 999]]
print(f'{rows_method2}')

print("--------------------------------------------------------------------------------------------------------------")
print("Lấy quốc gia thứ 43 trong dữ liệu của chúng ta bằng cách sử dụng .loc và .iloc:")
country_43_loc = data.loc[42, 'country']
country_43_iloc = data.iloc[42]['country']
print(f'{country_43_loc},{country_43_iloc}')
print("--------------------------------------------------------------------------------------------------------------")

print("Lấy các hàng đầu tiên, hàng thứ 100 và hàng thứ 1000 từ cột thứ nhất, thứ 4 và thứ 6:")
subset_data = data.iloc[[0, 99, 999], [0, 3, 5]]
print(f'{subset_data}')
print("--------------------------------------------------------------------------------------------------------------")
print("Lấy 10 hàng đầu tiên của dữ liệu của chúng tôi (tệp tsv):")
first_10_rows = data.head(10)
print(f'{first_10_rows}')

print("--------------------------------------------------------------------------------------------------------------")
print("Đối với mỗi năm trong dữ liệu của chúng ta, tính tuổi thọ trung bình:")
tuổi_trung_bình_kỳ_vọng_đời_cho_mỗi_năm = data.groupby('year')['lifeExp'].mean()
print(f'{tuổi_trung_bình_kỳ_vọng_đời_cho_mỗi_năm}')

print("--------------------------------------------------------------------------------------------------------------")
print("Sử dụng phương pháp lọc dữ liệu để giải quyết câu 15/:")
các_năm_độc_nhất = data['year'].unique()
tuổi_trung_bình_kỳ_vọng_đời_theo_năm_lọc = {}
for năm in các_năm_độc_nhất:
    subset = data[data['year'] == năm]
    trung_bình = subset['lifeExp'].mean()
    tuổi_trung_bình_kỳ_vọng_đời_theo_năm_lọc[năm] = trung_bình
print(f'{tuổi_trung_bình_kỳ_vọng_đời_theo_năm_lọc}')

print("--------------------------------------------------------------------------------------------------------------")
print("Tạo một series với chỉ mục 0 cho 'chuối' và chỉ mục 1 cho '42':")
series = pd.Series(['chuối', '42'], index=[0, 1])
print(f"{series}")

print("--------------------------------------------------------------------------------------------------------------")
print("Tương tự như 17, nhưng thay đổi chỉ mục 'Person' thành 'Wes MCKinney' và chỉ mục 'Who' thành 'Creator of Pandas':")
series = pd.Series(['Wes MCKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(f'{series}')
print("--------------------------------------------------------------------------------------------------------------")
print("Tạo một từ điển cho pandas với dữ liệu như 'Nghề nghiệp': ['Hóa học gia', 'Nhà thống kê'], 'Sinh': ['1920-07-25', '1876-06-13'], 'Mất': ['1958-04-16', '1937-10-16'], 'Tuổi': [37, 61] và chỉ mục là 'Franklin', 'Gosset' với bốn cột như đã chỉ định:\
python")
dictionary = {
    'Nghề nghiệp': ['Hóa học gia', 'Nhà thống kê'],
    'Sinh': ['1920-07-25', '1876-06-13'],
    'Mất': ['1958-04-16', '1937-10-16'],
    'Tuổi': [37, 61]
}
index = ['Franklin', 'Gosset']
df = pd.DataFrame(dictionary, index=index)
print(f'{df}')






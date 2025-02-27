#đọc file dữ liệu và hiển thị 7 dòng đầu của file dữ liệu theo mẫu bên dưới
import pandas as pd
df = pd.read_csv("/content/DATA.csv").head(7)
df

#tạo dataframe df2 bao gồm các cột sau: 'mack', 'year', 'car', 'roa', 'size', 'liq', 'dep', 'loa', 'lev', 'llr', 'npl', 'gdp', 'cpi', 'boads', 'indepb', 'femaleb'
df2 = pd.read_csv("/content/DATA.csv").iloc[:, :16]
df2

#với dataframe df2 vừa tạo, hãy lọc dữ liệu của cổ phiếu ABB, đặt tên cho file dữ liệu này là df_abb
df_abb = df2[df2["mack"] == "ABB"]
#df_abb.to_csv("df_abb.csv")
df_abb


#với dataframe df2 vừa tạo, hãy lọc dữ liệu của các cổ phiếu trong df2 vào năm 2020, đặt tên cho file dữ liệu này là df_2020
df_2020 = df2[df2["year"] == 2020]
#df_2020.to_csv("df_2020.csv")
df_2020


#với dataframe df_2020, hãy bỏ đi dữ liệu của các cổ phiếu VAB, VCA, VCB
df3 = df_2020[~df_2020["mack"].isin(["VAB", "VCA", "VCB"])]
df3

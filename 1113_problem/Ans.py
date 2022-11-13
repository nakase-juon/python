import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# problem2:pandasでデータを読み込んで、データ構造を表示せよ。全ペンギンの個体数はいくつか？
df = pd.read_csv('./python/1113_problem/penguins.csv')  # パスはそっちの環境に合わせて書き直す
print('Type of df:', type(df))
print()
df.info()  # データ構造の表示
print()
p_list = list(df.index)
print('全ペンギンの個体数:', len(p_list))  # 全ペンギンの個体数の表示

# problem3:データ欠損があるのでそのレコードは取り除け。

print()
df_dropped = df.dropna(how='any')
# df_dropped.info() # データ欠損を取り除いたデータ構造の表示。必要だったら表示させてね

# problem4:データをペンギンの種類ごとに分類し、別々の変数として保持せよ。

df_Adelie = df_dropped.groupby("species").get_group("Adelie")  # アデリーペンギンのデータ
df_Gentoo = df_dropped.groupby("species").get_group("Gentoo")  # ジェンツーペンギンのデータ
df_Chinstrap = df_dropped.groupby("species").get_group(
    "Chinstrap")  # チンストラップペンギンのデータ

# problem5:3種類のペンギンの特徴量（口ばしの長さ・厚み、足びれの長さ、体重）のいずれかの頻度分布を調べることで、どのペンギンの種類が一番大柄か、考察せよ。

data1 = np.array(df_Adelie['body_mass_g'])
data2 = np.array(df_Gentoo['body_mass_g'])
data3 = np.array(df_Chinstrap['body_mass_g'])
fig = plt.figure(figsize=(15, 5))

ax1 = fig.add_subplot(131)
ax1.hist(data1, bins=10, histtype='barstacked', ec='black')
ax1.set_title('Adelie')
ax1.set_xlabel('body_mass(g)')
ax1.set_ylabel('frequency')
ax1.set_xlim(2000, 6500)
ax1.set_ylim(0, 26.0)

ax2 = fig.add_subplot(132)
ax2.hist(data2, bins=10, histtype='barstacked', ec='black')
ax2.set_title('Gentoo')
ax2.set_xlabel('body_mass(g)')
ax2.set_ylabel('frequency')
ax2.set_xlim(2000, 6500)
ax2.set_ylim(0, 26.0)

ax3 = fig.add_subplot(133)
ax3.hist(data3, bins=10, histtype='barstacked', ec='black')
ax3.set_title('Chinstrap')
ax3.set_xlabel('body_mass(g)')
ax3.set_ylabel('frequency')
ax3.set_xlim(2000, 6500)
ax3.set_ylim(0, 26.0)

# plt.show()

# problem6:3種類のペンギンそれぞれについて、特徴量同士の相関を調べ、最も相関が高い特徴量同士の散布図を作成せよ。

df_Adelie_corr = df_Adelie.corr(numeric_only=True)
df_Gentoo_corr = df_Adelie.corr(numeric_only=True)
df_Chinstrap_corr = df_Adelie.corr(numeric_only=True)

print()
print('Adelie penguin data correlation:')
print(df_Adelie_corr)
print()
print('Gentoo penguin data correlation:')
print(df_Gentoo_corr)
print()
print('Chinstrap penguin data correlation:')
print(df_Chinstrap_corr)

fig2 = plt.figure(figsize=(15, 5))
ax_Ade_1 = fig2.add_subplot(131)
ax_Ade_1.scatter(df_Adelie[['culmen_depth_mm']], df_Adelie[['body_mass_g']])
ax_Ade_1.set_xlabel('culmen_depth(mm)')
ax_Ade_1.set_ylabel('body_mass(g)')

ax_Ade_2 = fig2.add_subplot(132)
ax_Ade_2.scatter(df_Adelie[['culmen_length_mm']], df_Adelie[['body_mass_g']])
ax_Ade_2.set_xlabel('culmen_length(mm)')
ax_Ade_2.set_ylabel('body_mass(g)')

ax_Ade_3 = fig2.add_subplot(133)
ax_Ade_3.scatter(df_Adelie[['flipper_length_mm']], df_Adelie[['body_mass_g']])
ax_Ade_3.set_xlabel('flipper_length(mm)')
ax_Ade_3.set_ylabel('body_mass(g)')

# df_Adelie_corr_1 = df_Adelie[['culmen_depth_mm', 'body_mass_g']]
# df_Adelie_corr_2 = df_Adelie[['culmen_length_mm', 'body_mass_g']]
# df_Adelie_corr_3 = df_Adelie[['flipper_length_mm', 'body_mass_g']]
# df_Adelie_corr_1.plot.scatter(x = 'culmen_depth_mm', y = 'body_mass_g')
# df_Adelie_corr_2.plot.scatter(x = 'culmen_length_mm', y = 'body_mass_g')
# df_Adelie_corr_3.plot.scatter(x = 'flipper_length_mm', y = 'body_mass_g')

plt.show()

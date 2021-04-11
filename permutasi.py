from itertools import permutations

data_list = [1, 2, 3, 4, 5]

# penggunaan permutation
permutasi = permutations(data_list)

# cetak object
print(permutasi)

# loop untuk mengetahui hasil dari fungsi permutation

for index, data in enumerate(list(permutasi), 1):
    print(f'hasil nomor: {index}. {data}')

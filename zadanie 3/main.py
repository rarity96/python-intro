from comparison import compare_methods

if __name__ == "__main__":
    df = compare_methods()
    print("Porównanie metod decyzyjnych (TOPSIS vs SPOTIS):")
    print(df.sort_values('TOPSIS_Rank'))
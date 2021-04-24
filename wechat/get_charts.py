import matplotlib.pyplot as plt

import seaborn as sns

if __name__ == '__main__':
    sns.set(style="white", context="notebook")
    plt.figure(dpi=300, figsize=(24, 8))
    plt.ylabel('MONEY', fontsize=20)
    plt.xlabel('IDX', fontsize=20)
    plt.yticks(fontsize=14)
    data = [6.76, 6.69, 6.53, 6.65, 6.66, 6.63, 6.56, 6.75, 6.63, 6.67, 6.79, 6.89, 6.78, 6.63, 6.8, 6.78, 6.6, 6.5, 6.72, 6.45, 6.62, 6.68, 6.61, 6.54, 6.78, 6.67, 6.65, 6.66, 6.67, 6.8]
    idx = [x for x in range(1, len(data) + 1)]
    plt.xticks(range(1, len(idx) + 1, 1))
    # 使用text显示数值
    for x, y in zip(idx, data):
        plt.text(x, y + 0.05, y, ha='center', va='bottom', fontsize=14)
    plt.bar(idx, data, color='c')
    sns.despine()
    plt.show()

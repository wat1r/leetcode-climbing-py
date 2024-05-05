import pandas as pd
import matplotlib as mpl
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
# from IPython.display import HTML
from datetime import datetime
from matplotlib import cm

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('axes', axisbelow=True)
mpl.rcParams['animation.embed_limit'] = 2 ** 128

df = pd.read_csv(r'/Users/frankcooper/Data/20tmp/main_country.csv', index_col=1)  # 改成自己的地址

for year in range(1960, 2018):
    df[str(year) + '_rank'] = 11 - df[str(year)].rank(ascending=False)


def draw_gdp(frame):
    ax.clear()
    left_year = 1960 + frame // 10
    if frame < 570:
        right_year = left_year + 1
        step = frame % 10
        rank_val = (df[str(right_year) + "_rank"] - df[str(left_year) + '_rank']) / 10 * step + df[
            str(left_year) + '_rank']
        gdp_val = (df[str(right_year)] - df[str(left_year)]) / 10 * step + df[str(left_year)]
    else:
        rank_val = df[str(left_year) + "_rank"]
        gdp_val = df[str(left_year)]
    colors = cm.Spectral_r(gdp_val.values / gdp_val.max())
    gdp_val = gdp_val / 1e11
    bars = ax.barh(rank_val.values, gdp_val.values, height=0.5, color=colors)
    ax.set_ylim(-0.6, 10.6)
    ax.spines['top'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['right'].set_color('none')
    rank_val = rank_val[(rank_val >= 0) & (rank_val < 11)]
    label = rank_val.index
    val = rank_val.values
    label = rank_val.index
    ax.set_yticks(val)
    ax.set_yticklabels(label)
    ax.text(0.8 * ax.get_xlim()[1], 1, str(left_year) + "年", fontsize=20)
    ax.set_title("1960-2017年世界GDP动态排名图(单位：百亿$)")
    for bar in bars:
        if bar.get_y() > 0:
            width = bar.get_width()
            plt.text(width + ax.get_xlim()[1] * 0.02, bar.get_y() + 0.125, "{:.2f}".format(width))


fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
plt.subplots_adjust(left=0.12, right=0.98, top=0.85, bottom=0.1, hspace=0, wspace=0)
animator = animation.FuncAnimation(fig, draw_gdp, np.arange(0, 571, 1), interval=100)
animator.save('gdp.gif', writer='pillow', savefig_kwargs={'facecolor': 'white'}, fps=10)
plt.show()
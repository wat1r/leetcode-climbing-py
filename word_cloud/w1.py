from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 示例文本
text = "This is a simple example showing how to generate a word cloud using the generate method. Generate method uses the input text directly."# 创建WordCloud对象
wordcloud = WordCloud(width=800, height=800, max_words=100, background_color='white').generate_from_text(text)

# 显示词云
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


# 第一回
# 沈小卫布暗棋伏脉千里
# 陆大侠遇奸计壮志难酬

# 第二回
# 逢良将裴英俊如鱼得水
# 叹华盖陆大侠二战被春

# 第三回
# 巧妇难炊小满淡然无牌徒叹
# 壮士缓兵森林保守三度翻十

# 第五回
# 失好局蚂蚁火山匪夷落败
# 得后手陆侠小满欢喜躺赢

# 第六回
# 牌投技合，小满焊死陆侠客
# 神分路陌，汪洲含嗔小冤家
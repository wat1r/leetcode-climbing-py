import re


url_pattern = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
)


urls_set = set()


# with open(r'C:\Users\wangzhou\Downloads\20241031.log', 'r',encoding='utf-8') as file:
with open(r'D:\Dev\wat1r\bot-ant\raw\20241105.log', 'r',encoding='utf-8') as file:
    for line in file:
        matches = url_pattern.findall(line)
        for match in matches:
            urls_set.add(match)



for url in urls_set:
    print(url)

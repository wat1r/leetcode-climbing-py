import vanna as vn


def test1():
    # api_key = vn.get_api_key('water8991@163.com')  # Put your email here
    api_key = '351ASG'
    vn.set_api_key(api_key)
    print(api_key)
    vn.set_model('chinook')
    vn.connect_to_sqlite(
        'https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite')
    vn.ask("What are the top 5 artists by sales?")


if __name__ == '__main__':
    test1()

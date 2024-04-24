import yaml


class Config:
    def __init__(self, data):
        self.username = data.get('username', None)
        self.password = data.get('password', None)
        self.entrance_url = data.get('entrance_url', None)
        self.cookie_filepath = data.get('cookie_filepath', 'cookies.json')

        if not self.username or not self.password \
                or not self.entrance_url:
            raise ValueError('账号/密码/URL存在空值, 请检测配置文件!')


def read_config_file(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return Config(config_data)
    except FileNotFoundError as e:
        raise ValueError("未找到配置文件: config.yml")

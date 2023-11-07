from config import local_environment as env


def test_env_vars():
    print(env.get_component())
    print(env.get_execution())
    print(env.get_browser())
    print(env.get_screen_size())
    print(env.get_platform())

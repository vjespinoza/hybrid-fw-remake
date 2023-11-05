from config.local_environment import get_no_var, get_var_one


def test_env_vars():
    print(get_no_var())
    print(get_var_one())

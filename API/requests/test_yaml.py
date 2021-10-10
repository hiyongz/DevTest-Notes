import yaml

def test_yaml2():
    env = {
        "default":"dev",
        "testing-studio":
        {
        "dev":"127.0.0.1",
        "test":"127.0.0.2"
        }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data = env,stream= f)
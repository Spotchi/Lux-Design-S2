from luxai_s2.config import EnvConfig

def test_config_defaults():
    default_env = EnvConfig()
    empty_dict_env = EnvConfig.from_dict({})
    assert default_env == empty_dict_env, "Environments built with empty dict should be the same as the default env"

def test_override_nested_kwarg():
    env_cfg = EnvConfig.from_dict({ "ROBOTS": { "HEAVY": { "METAL_COST": 1 } } })
    assert env_cfg.ROBOTS["HEAVY"].METAL_COST == 1, "HEAVY METAL_COST Should be set by the dictionary argument"

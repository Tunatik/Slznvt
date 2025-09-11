from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    name: str
    host: str
    user: str
    password: str

@dataclass
class Bot:
    token: str

@dataclass
class Config:
    bot: Bot
    db: DatabaseConfig

def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(
        bot=Bot(
            token=env('TOKEN'),
        ),
        db=DatabaseConfig(
            name=env('DB_NAME'),
            host=env('DB_HOST'),
            user=env('DB_USER'),
            password=env('DB_PASSWORD'),
        )
    )
from dataclasses import dataclass
import os

@dataclass
class AgentConfig:
    model: str
    name: str
    tone: str

    def __post_init__(self):
        missing = [f for f, v in vars(self).items() if not v]
        if missing:
            raise ValueError(f"Missing config fields: {missing}")

def load_agent_config(prefix: str) -> AgentConfig:
    return AgentConfig(
        model=os.getenv(f"{prefix}_MODEL"),
        name=os.getenv(f"{prefix}_NAME"),
        tone=os.getenv(f"{prefix}_TONE"),
    )
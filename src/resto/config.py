"""Configuration management for resto package."""
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Configuration for resto package."""
    clerk_secret_key: str
    supabase_url: str
    supabase_key: str

    @classmethod
    def from_env(cls) -> 'Config':
        """Create config from environment variables."""
        clerk_key = os.getenv("CLERK_SECRET_KEY")
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        missing = []
        if not clerk_key:
            missing.append("CLERK_SECRET_KEY")
        if not supabase_url:
            missing.append("SUPABASE_URL")
        if not supabase_key:
            missing.append("SUPABASE_KEY")
            
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
            
        return cls(
            clerk_secret_key=clerk_key,
            supabase_url=supabase_url,
            supabase_key=supabase_key
        )


# Global configuration instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the current configuration."""
    if _config is None:
        raise RuntimeError(
            "Configuration not initialized. Call init_config() or set_config() first."
        )
    return _config


def init_config(
    clerk_secret_key: Optional[str] = None,
    supabase_url: Optional[str] = None,
    supabase_key: Optional[str] = None
) -> Config:
    """
    Initialize configuration with optional explicit values.
    Falls back to environment variables for any values not provided.
    """
    global _config
    
    env_config = Config.from_env()
    _config = Config(
        clerk_secret_key=clerk_secret_key or env_config.clerk_secret_key,
        supabase_url=supabase_url or env_config.supabase_url,
        supabase_key=supabase_key or env_config.supabase_key
    )
    
    return _config


def set_config(config: Config) -> None:
    """Set configuration directly."""
    global _config
    _config = config

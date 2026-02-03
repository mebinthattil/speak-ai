"""Utility functions for Kokoro TTS in Sugar environment."""

import os
from loguru import logger


def get_sugar_cache_dir():
    """Get the Sugar activity root cache directory for HuggingFace downloads.
    
    Returns cache_dir path if Sugar activity root is available, None otherwise.
    When None is returned, huggingface_hub will use its default cache directory.
    """
    try:
        from sugar3.activity.activity import get_activity_root
        cache_dir = os.path.join(get_activity_root(), 'data', 'kokoro_cache')
        os.makedirs(cache_dir, exist_ok=True)
        return cache_dir
    except Exception as e:
        logger.warning(f"Sugar activity root not available: {e}")
        return None


def get_bundled_voices_dir():
    """Get the path to bundled voices directory."""
    return os.path.join(os.path.dirname(__file__), 'voices')


# Default voices bundled with the activity - these should NEVER be downloaded
BUNDLED_VOICES = ['af_heart', 'af_alloy', 'af_aoede']

#!/usr/bin/env python3
"""
tts.py — Doubao (豆包) TTS wrapper for English learning audio generation.

Replaces the macOS `say` command with high-quality Doubao synthesis.

Usage:
    python scripts/tts.py --text "Hello!" --voice samantha --rate 170 \
        --output materials/audio/2026-06-22-seg1.mp3 --play

Required env vars:
    DOUBAO_API_KEY              — from console.volcengine.com → API Key管理
    DOUBAO_SPEAKER_SAMANTHA     — American English female speaker ID
    DOUBAO_SPEAKER_DANIEL       — British English male speaker ID
    DOUBAO_SPEAKER_KAREN        — Australian English female speaker ID (or any EN female)
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import uuid

try:
    import requests
except ImportError:
    sys.exit("Error: 'requests' package not found. Run: pip install requests")

# ── API constants ────────────────────────────────────────────────────────────
API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
RESOURCE_ID = "seed-tts-2.0"

# Map macOS `say -r` word-per-minute values → Doubao speech_rate
# Doubao range: -50 (0.5×) to 100 (2.0×); 0 = natural speed
RATE_MAP = {
    150: -25,   # slow — for replay / shadowing practice
    170:   0,   # normal — default lesson pace
    190:  30,   # fast  — challenge mode
}

# Map friendly voice names → env var holding the Doubao speaker ID
VOICE_ENV = {
    "samantha": "DOUBAO_SPEAKER_SAMANTHA",  # female US
    "daniel":   "DOUBAO_SPEAKER_DANIEL",    # male UK
    "karen":    "DOUBAO_SPEAKER_KAREN",     # female AU
}


def _resolve_speaker(voice: str) -> str:
    """Look up the speaker ID from the environment, with a clear error if missing."""
    env_var = VOICE_ENV[voice]
    speaker = os.environ.get(env_var, "").strip()
    if not speaker:
        sys.exit(
            f"Error: {env_var} is not set.\n"
            f"Get a speaker ID from https://console.volcengine.com/speech/new/voices "
            f"and add it to your shell profile:\n"
            f"  export {env_var}=<speaker_id>"
        )
    return speaker


def _resolve_api_key() -> str:
    key = os.environ.get("DOUBAO_API_KEY", "").strip()
    if not key:
        sys.exit(
            "Error: DOUBAO_API_KEY is not set.\n"
            "Get your API key from https://console.volcengine.com/speech/new/setting/apikeys\n"
            "Then add to your shell profile:\n"
            "  export DOUBAO_API_KEY=<your_key>"
        )
    return key


def synthesize(text: str, speaker: str, api_key: str, speech_rate: int) -> bytes:
    """
    Call the Doubao HTTP Chunked TTS API and return raw MP3 bytes.

    The API streams the response as JSON-lines; each line carries a base64-encoded
    audio chunk in the 'data' field. We decode and concatenate them all.
    """
    headers = {
        "X-Api-Key": api_key,
        "X-Api-Resource-Id": RESOURCE_ID,
        "X-Api-Request-Id": str(uuid.uuid4()),
        "Content-Type": "application/json",
    }
    payload = {
        "req_params": {
            "text": text,
            "speaker": speaker,
            "audio_params": {
                "format": "mp3",
                "sample_rate": 24000,
                "speech_rate": speech_rate,
            },
            "explicit_language": "en",
        }
    }

    audio_chunks = bytearray()

    with requests.post(
        API_URL,
        headers=headers,
        json=payload,
        stream=True,
        timeout=60,
    ) as resp:
        if resp.status_code != 200:
            # Try to surface the error body
            try:
                err = resp.json()
                sys.exit(f"API HTTP {resp.status_code}: {err.get('message', resp.text)}")
            except Exception:
                sys.exit(f"API HTTP {resp.status_code}: {resp.text[:300]}")

        for raw_line in resp.iter_lines():
            if not raw_line:
                continue
            try:
                chunk = json.loads(raw_line)
            except json.JSONDecodeError:
                # Not a JSON line — skip (might be keep-alive or padding)
                continue

            code = chunk.get("code")
            if code is not None and code != 0:
                sys.exit(f"API error {code}: {chunk.get('message', 'unknown error')}")

            data = chunk.get("data")
            if data:
                audio_chunks.extend(base64.b64decode(data))

    if not audio_chunks:
        sys.exit(
            "Error: No audio data received from API.\n"
            "Check that your speaker ID and API key are correct."
        )

    return bytes(audio_chunks)


def main():
    parser = argparse.ArgumentParser(
        description="Doubao TTS — high-quality English audio for lesson material",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single speaker, normal speed, auto-play
  python scripts/tts.py --text "Good morning!" --voice samantha --rate 170 \\
      --output materials/audio/2026-06-22-1.mp3 --play

  # Slow replay (for shadowing / dictation)
  python scripts/tts.py --text "She sells seashells." --voice samantha --rate 150 \\
      --output materials/audio/2026-06-22-slow1.mp3 --play

  # Multi-speaker dialogue (run once per line, then play all)
  D="materials/audio/$(date +%F)"
  python scripts/tts.py --text "How did the meeting go?" --voice samantha --rate 170 --output "${D}-seg1.mp3"
  python scripts/tts.py --text "It went really well."   --voice daniel   --rate 170 --output "${D}-seg2.mp3"
  for f in ${D}-seg*.mp3; do afplay "$f"; done
        """,
    )
    parser.add_argument("--text",   required=True,
                        help="Text to synthesize (English)")
    parser.add_argument("--voice",  choices=["samantha", "daniel", "karen"],
                        default="samantha",
                        help="Voice: samantha=US female, daniel=UK male, karen=AU female (default: samantha)")
    parser.add_argument("--rate",   type=int, choices=[150, 170, 190],
                        default=170,
                        help="Speaking rate: 150=slow, 170=normal, 190=fast (default: 170)")
    parser.add_argument("--output", required=True,
                        help="Output MP3 file path (e.g. materials/audio/2026-06-22-1.mp3)")
    parser.add_argument("--play",   action="store_true",
                        help="Auto-play the file after generation via afplay (macOS)")
    args = parser.parse_args()

    api_key = _resolve_api_key()
    speaker = _resolve_speaker(args.voice)
    speech_rate = RATE_MAP[args.rate]

    # Ensure the output directory exists
    out_path = args.output
    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)

    print(f"[tts] voice={args.voice}  rate={args.rate}  → {out_path}")
    audio_bytes = synthesize(args.text, speaker, api_key, speech_rate)

    with open(out_path, "wb") as f:
        f.write(audio_bytes)
    print(f"[tts] ✓ {len(audio_bytes):,} bytes saved")

    if args.play:
        print(f"[tts] Playing …")
        subprocess.run(["afplay", out_path], check=True)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Extract audio and transcribe debate video with faster-whisper."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "debate-video"
DEFAULT_VIDEO = Path(r"c:\Users\sever\Desktop\Screen_Recording_20260829_211742_Instagram.mp4")


def fmt_ts(seconds: float) -> str:
    s = max(0.0, float(seconds))
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s % 60
    if h:
        return f"{h:02d}:{m:02d}:{sec:05.2f}".replace(".", ",")
    return f"{m:02d}:{sec:05.2f}".replace(".", ",")


def fmt_clock(seconds: float) -> str:
    s = max(0.0, float(seconds))
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = int(s % 60)
    if h:
        return f"{h}:{m:02d}:{sec:02d}"
    return f"{m}:{sec:02d}"


def extract_audio(video: Path, wav: Path) -> None:
    wav.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-c:a",
        "pcm_s16le",
        str(wav),
    ]
    subprocess.run(cmd, check=True)


def transcribe(wav: Path, model_size: str = "medium") -> dict:
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments_iter, info = model.transcribe(
        str(wav),
        language="ru",
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
        beam_size=5,
        word_timestamps=False,
    )
    segments = []
    full_parts = []
    for seg in segments_iter:
        text = (seg.text or "").strip()
        if not text:
            continue
        row = {
            "id": len(segments),
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "start_fmt": fmt_clock(seg.start),
            "end_fmt": fmt_clock(seg.end),
            "text": text,
        }
        segments.append(row)
        full_parts.append(f"[{row['start_fmt']}] {text}")
        print(f"{row['start_fmt']}  {text}", flush=True)

    return {
        "language": info.language,
        "duration": round(info.duration, 2),
        "duration_fmt": fmt_clock(info.duration),
        "model": model_size,
        "segment_count": len(segments),
        "segments": segments,
        "full_text": "\n".join(full_parts),
    }


def write_srt(segments: list[dict], path: Path) -> None:
    lines = []
    for i, seg in enumerate(segments, 1):
        lines.append(str(i))
        lines.append(f"{fmt_ts(seg['start'])} --> {fmt_ts(seg['end'])}")
        lines.append(seg["text"])
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    video = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_VIDEO
    model_size = sys.argv[2] if len(sys.argv) > 2 else "medium"
    if not video.exists():
        raise SystemExit(f"Video not found: {video}")

    OUT.mkdir(parents=True, exist_ok=True)
    wav = OUT / "audio.wav"
    meta_path = OUT / "source.json"
    meta_path.write_text(
        json.dumps(
            {
                "video": str(video),
                "video_name": video.name,
                "recorded": "2026-08-29",
                "platform": "Instagram screen recording",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    if not wav.exists() or wav.stat().st_size < 1000:
        print("Extracting audio…", flush=True)
        extract_audio(video, wav)
    else:
        print(f"Using existing audio: {wav}", flush=True)

    print(f"Transcribing with faster-whisper ({model_size})…", flush=True)
    data = transcribe(wav, model_size=model_size)
    data["source"] = json.loads(meta_path.read_text(encoding="utf-8"))

    (OUT / "transcript.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT / "transcript.txt").write_text(data["full_text"], encoding="utf-8")
    write_srt(data["segments"], OUT / "transcript.srt")
    print(f"Done: {len(data['segments'])} segments, {data['duration_fmt']}", flush=True)


if __name__ == "__main__":
    main()

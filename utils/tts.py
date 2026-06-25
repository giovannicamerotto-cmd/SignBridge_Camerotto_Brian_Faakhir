#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple text-to-speech helper for app.py."""

import platform
import queue
import subprocess
import threading


class TextToSpeech:
    def __init__(self):
        self._platform = platform.system().lower()
        self._queue = queue.Queue()
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()

    def speak(self, text):
        if not text:
            return
        self._queue.put(str(text))

    def _worker(self):
        while True:
            text = self._queue.get()
            if text is None:
                break
            try:
                self._do_speak(text)
            except Exception:
                pass
            self._queue.task_done()

    def _do_speak(self, text):
        if 'windows' in self._platform:
            self._speak_windows(text)
        elif 'darwin' in self._platform:
            self._speak_macos(text)
        else:
            self._speak_linux(text)

    def _speak_windows(self, text):
        command = [
            'powershell',
            '-NoProfile',
            '-Command',
            'Add-Type -AssemblyName System.Speech; $s = New-Object System.Speech.Synthesis.SpeechSynthesizer; $s.Speak([Console]::In.ReadToEnd())',
        ]
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        process.communicate(text)

    def _speak_macos(self, text):
        subprocess.run(['say', text], check=False)

    def _speak_linux(self, text):
        subprocess.run(['spd-say', text], check=False)

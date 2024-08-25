# Snakes Game

A simple implementation of the classic Snakes Game using Python. This project provides two versions:
1. A terminal-based version using the `curses` library.
2. A graphical version using the `pygame` library.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
  - [Terminal Version (curses)](#terminal-version-curses)
  - [Graphical Version (pygame)](#graphical-version-pygame)
- [Game Controls](#game-controls)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Snakes Game is a fun project that demonstrates the use of arrays, loops, and conditional statements in Python. The game involves controlling a snake to eat food, grow longer, and avoid collisions with the walls or itself.

## Features

- **Terminal Version**: A simple, text-based version of the Snakes Game.
- **Graphical Version**: A more visually appealing version using `pygame` for a graphical interface.
- **Score Tracking**: Tracks the player's score as the snake eats food.
- **Game Over Condition**: The game ends when the snake collides with itself or the wall.
- **Replay Option**: Option to replay the game upon game over in the `pygame` version.

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- Terminal that supports `curses` (Linux, macOS, or Windows with `windows-curses`).
- `pip` package installer for Python.

### Installing Dependencies

For the terminal version:
```bash
pip install windows-curses  # Only required for Windows users

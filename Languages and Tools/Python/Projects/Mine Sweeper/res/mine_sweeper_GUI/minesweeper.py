# Python Version 2.7.3
# File: minesweeper.py

import tkinter as tk
from tkinter import messagebox as tkMessageBox
from collections import deque
import random
import platform
from datetime import datetime

SIZE_X = 10
SIZE_Y = 10

STATE_DEFAULT = 0
STATE_CLICKED = 1
STATE_FLAGGED = 2

BTN_CLICK = "<Button-1>"
BTN_FLAG = "<Button-2>" if platform.system() == 'Darwin' else "<Button-3>"

class Minesweeper:
    def __init__(self, tk):
        self.tk = tk
        self.images = {
            "plain": tk.PhotoImage(file="images/tile_plain.gif"),
            "clicked": tk.PhotoImage(file="images/tile_clicked.gif"),
            "mine": tk.PhotoImage(file="images/tile_mine.gif"),
            "flag": tk.PhotoImage(file="images/tile_flag.gif"),
            "wrong": tk.PhotoImage(file="images/tile_wrong.gif"),
            "numbers": [tk.PhotoImage(file="images/tile_" + str(i) + ".gif") for i in range(1, 9)]
        }
        self.frame = tk.Frame(self.tk)
        self.frame.pack()
        self.labels = {
            "time": tk.Label(self.frame, text="00:00:00"),
            "mines": tk.Label(self.frame, text="Mines: 0"),
            "flags": tk.Label(self.frame, text="Flags: 0")
        }
        self.labels["time"].grid(row=0, column=0, columnspan=SIZE_Y)
        self.labels["mines"].grid(row=SIZE_X + 1, column=0, columnspan=int(SIZE_Y / 2))
        self.labels["flags"].grid(row=SIZE_X + 1, column=int(SIZE_Y / 2) - 1, columnspan=int(SIZE_Y / 2))
        self.restart()
        self.updateTimer()

    def setup(self):
        self.flagCount = 0
        self.correctFlagCount = 0
        self.clickedCount = 0
        self.startTime = None
        self.tiles = {}
        self.mines = 0
        for x in range(SIZE_X):
            self.tiles[x] = {}
            for y in range(SIZE_Y):
                id = str(x) + "_" + str(y)
                isMine = random.uniform(0.0, 1.0) < 0.1
                gfx = self.images["plain"]
                if isMine:
                    self.mines += 1
                tile = {
                    "id": id,
                    "isMine": isMine,
                    "state": STATE_DEFAULT,
                    "coords": {"x": x, "y": y},
                    "button": tk.Button(self.frame, image=gfx),
                    "mines": 0
                }
                tile["button"].bind(BTN_CLICK, self.onClickWrapper(x, y))
                tile["button"].bind(BTN_FLAG, self.onRightClickWrapper(x, y))
                tile["button"].grid(row=x + 1, column=y)
                self.tiles[x][y] = tile
        for x in range(SIZE_X):
            for y in range(SIZE_Y):
                mc = sum(1 for n in self.getNeighbors(x, y) if n["isMine"])
                self.tiles[x][y]["mines"] = mc

    def restart(self):
        self.setup()
        self.refreshLabels()

    def refreshLabels(self):
        self.labels["flags"].config(text="Flags: " + str(self.flagCount))
        self.labels["mines"].config(text="Mines: " + str(self.mines))

    def gameOver(self, won):
        for x in range(SIZE_X):
            for y in range(SIZE_Y):
                tile = self.tiles[x][y]
                if not tile["isMine"] and tile["state"] == STATE_FLAGGED:
                    tile["button"].config(image=self.images["wrong"])
                if tile["isMine"] and tile["state"] != STATE_FLAGGED:
                    tile["button"].config(image=self.images["mine"])
        self.tk.update()
        msg = "You Win! Play again?" if won else "You Lose! Play again?"
        res = tkMessageBox.askyesno("Game Over", msg)
        if res:
            self.restart()
        else:
            self.tk.quit()

    def updateTimer(self):
        ts = "00:00:00"
        if self.startTime is not None:
            delta = datetime.now() - self.startTime
            ts = str(delta).split('.')[0]
            if delta.total_seconds() < 36000:
                ts = "0" + ts
        self.labels["time"].config(text=ts)
        self.frame.after(100, self.updateTimer)

    def getNeighbors(self, x, y):
        coords = [
            {"x": x - 1, "y": y - 1},
            {"x": x - 1, "y": y},
            {"x": x - 1, "y": y + 1},
            {"x": x, "y": y - 1},
            {"x": x, "y": y + 1},
            {"x": x + 1, "y": y - 1},
            {"x": x + 1, "y": y},
            {"x": x + 1, "y": y + 1},
        ]
        return [self.tiles[n["x"]][n["y"]] for n in coords if n["x"] in self.tiles and n["y"] in self.tiles[n["x"]]]

    def onClickWrapper(self, x, y):
        return lambda Button: self.onClick(self.tiles[x][y])

    def onRightClickWrapper(self, x, y):
        return lambda Button: self.onRightClick(self.tiles[x][y])

    def onClick(self, tile):
        if self.startTime is None:
            self.startTime = datetime.now()
        if tile["isMine"]:
            self.gameOver(False)
            return
        if tile["mines"] == 0:
            tile["button"].config(image=self.images["clicked"])
            self.clearSurroundingTiles(tile["id"])
        else:
            tile["button"].config(image=self.images["numbers"][tile["mines"] - 1])
        if tile["state"] != STATE_CLICKED:
            tile["state"] = STATE_CLICKED
            self.clickedCount += 1
        if self.clickedCount == (SIZE_X * SIZE_Y) - self.mines:
            self.gameOver(True)

    def onRightClick(self, tile):
        if self.startTime is None:
            self.startTime = datetime.now()
        if tile["state"] == STATE_DEFAULT:
            tile["button"].config(image=self.images["flag"])
            tile["state"] = STATE_FLAGGED
            tile["button"].unbind(BTN_CLICK)
            if tile["isMine"]:
                self.correctFlagCount += 1
            self.flagCount += 1
            self.refreshLabels()
        elif tile["state"] == STATE_FLAGGED:
            tile["button"].config(image=self.images["plain"])
            tile["state"] = STATE_DEFAULT
            tile["button"].bind(BTN_CLICK, self.onClickWrapper(tile["coords"]["x"], tile["coords"]["y"]))
            if tile["isMine"]:
                self.correctFlagCount -= 1
            self.flagCount -= 1
            self.refreshLabels()

    def clearSurroundingTiles(self, id):
        queue = deque([id])
        while queue:
            key = queue.popleft()
            x, y = map(int, key.split("_"))
            for tile in self.getNeighbors(x, y):
                self.clearTile(tile, queue)

    def clearTile(self, tile, queue):
        if tile["state"] != STATE_DEFAULT:
            return
        if tile["mines"] == 0:
            tile["button"].config(image=self.images["clicked"])
            queue.append(tile["id"])
        else:
            tile["button"].config(image=self.images["numbers"][tile["mines"] - 1])
        tile["state"] = STATE_CLICKED
        self.clickedCount += 1

def main():
    window = tk.Tk()
    window.title("Minesweeper")
    minesweeper = Minesweeper(window)
    window.mainloop()

if __name__ == "__main__":
    main()

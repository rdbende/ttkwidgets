# Copyright (c) Dogeek 2019
# For license see LICENSE
from ttkwidgets import Notebook
from tests import BaseWidgetTest
from tkinter import ttk
import tkinter as tk


class TestNotebook(BaseWidgetTest):
    def test_notebook_init(self):
        nb = Notebook(self.window)
        nb.grid()
        self.window.update()

    def test_notebook_add_tab(self):
        nb = Notebook(self.window)
        frame = ttk.Frame(self.window, width=200, height=200)
        nb.add(frame, text="Frame")
        nb.grid()
        self.window.update()

    def test_notebook_select_tab(self):
        nb = Notebook(self.window)
        frame = ttk.Frame(self.window, width=200, height=200)
        frame2 = ttk.Frame(self.window, width=200, height=200)
        nb.add(frame, text="Frame")
        nb.add(frame2, text="Frame2")
        nb.grid()
        nb.select_next()
        nb.select_next()
        nb.select_prev()
        self.window.update()

    def test_notebook_move_tab(self):
        nb = Notebook(self.window, drag_to_toplevel=False)
        frames = []
        for i in range(3):
            frame = ttk.Frame(self.window, width=200, height=200)
            frames.append(frame)
            nb.add(frame, text="Frame" + str(i))
        nb._dragged_tab = nb._tab_labels[0]
        nb._swap(nb._tab_labels[1])
        nb._on_click(None)
        self.assertEqual(nb._visible_tabs, [1, 0, 2])

    def test_notebook_insert(self):
        nb = Notebook(self.window, drag_to_toplevel=False)
        for i in range(3):
            frame = ttk.Frame(self.window, width=200, height=200)
            nb.add(frame, text="Frame" + str(i))
        nb.insert(str(self.window) + '.!frame2',
                  ttk.Frame(self.window, width=200, height=200),
                  text="Added")

        self.assertEqual(nb._visible_tabs, [0, 3, 1, 2])

    def test_notebook_index(self):
        nb = Notebook(self.window)
        for i in range(10):
            frame = ttk.Frame(self.window, width=200, height=200)
            nb.add(frame, text="Frame" + str(i))

        with self.assertRaises(ValueError):
            nb.index(str(self.window) + '.!frame11')

        self.assertEqual(nb.index(str(self.window) + '.!frame'), 0)
        self.assertEqual(nb.index(tk.END), 10)
        nb.current_tab = 0
        self.assertEqual(nb.index(tk.CURRENT), 0)

        self.window.update()

    def test_notebook_forget_tab(self):
        nb = Notebook(self.window)
        for i in range(3):
            frame = ttk.Frame(self.window, width=200, height=200)
            nb.add(frame, text="Frame" + str(i))

        nb.forget(str(self.window) + '.!frame')

    def test_notebook_config_tab(self):
        nb = Notebook(self.window)
        for i in range(10):
            frame = ttk.Frame(self.window, width=200, height=200)
            nb.add(frame, text="Frame" + str(i))

        with self.assertRaises(ValueError):
            nb.tab(tk.CURRENT, state='random')

        nb.tab(tk.CURRENT, text="Changed")
        self.window.update()
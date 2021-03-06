#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from pygame.gfxdraw import aacircle, filled_circle, bezier, filled_polygon, aapolygon
from math import sqrt, sin, cos, pi
import random


def single_circle(surface, progress, mood):
    width, height = surface.get_size()
    r = int(progress*(sqrt((width/2)**2+(height/2)**2)+width//20))
    w = width//40
    aacircle(surface, width//2, height//2, r, mood.primary_color)
    filled_circle(surface, width//2, height//2, r, mood.primary_color)
    if r-w > 0:
        aacircle(surface, width//2, height//2, r-w, (0, 0, 0))
        filled_circle(surface, width//2, height//2, r-w, (0, 0, 0))


def horizontal_line(surface, progress, mood):
    width, height = surface.get_size()
    w = width // 40
    pos = int(progress*(height+2*w))
    surface.fill(mood.primary_color, (0, pos-w, width, min(pos, w)))


def vertical_line(surface, progress, mood):
    width, height = surface.get_size()
    w = width // 40
    pos = int(progress*(width+2*w))
    surface.fill(mood.primary_color, (pos-w, 0, min(pos, w), height))


def double_wave(surface, progress, mood):
    width, height = surface.get_size()
    w = width // 40
    for i in range(w):
        bezier(surface, [
            (int((-progress+0.25) % 1 * width), height // 2 + i),
            (int((-progress+0.25) % 1 * width + width / 2), i),
            (int((-progress+0.25) % 1 * width + width / 2), height + i),
            (int((-progress+0.25) % 1 * width + width), height // 2 + i)
        ], 16, mood.secondary_color)
        bezier(surface, [
            (int((-progress+0.25) % 1 * width - width), height // 2 + i),
            (int((-progress+0.25) % 1 * width - width / 2), i),
            (int((-progress+0.25) % 1 * width - width / 2), height + i),
            (int((-progress+0.25) % 1 * width), height // 2 + i)
        ], 16, mood.secondary_color)
    for i in range(w):
        bezier(surface, [
            (int(progress * width), height // 2 + i),
            (int(progress * width + width / 2), i),
            (int(progress * width + width / 2), height + i),
            (int(progress * width + width), height // 2 + i)
        ], 16, mood.primary_color)
        bezier(surface, [
            (int(progress * width - width), height // 2 + i),
            (int(progress * width - width / 2), i),
            (int(progress * width - width / 2), height + i),
            (int(progress * width), height // 2 + i)
        ], 16, mood.primary_color)


def bony_horizontal_line(surface, progress, mood):
    width, height = surface.get_size()
    w = width // 40
    bone_l = 7*w
    pos = int(progress * (height + 2 * w))
    for i in range(9):
        if i % 2 == 0:
            color = mood.primary_color
        else:
            color = mood.secondary_color
        filled_circle(surface, i * bone_l - height + pos, pos, w, color)
        aacircle(surface, i * bone_l - height + pos, pos, w, color)
        surface.fill(color, (i * bone_l - height + pos, pos - w//2, bone_l, min(pos + w//2, w)))


def point_circle(surface, progress, mood, num_points=6):
    width, height = surface.get_size()
    w = width // 40
    r = min(width - 2 * w, height - 2 * w) // 2
    for i in range(num_points):
        if i % 2 == 0:
            color = mood.primary_color
        else:
            color = mood.secondary_color
        alpha = i * 2 * pi / num_points + progress * 2 * pi
        filled_circle(surface, int(width//2 + sin(alpha) * r), int(height//2 + cos(alpha) * r), w, color)
        aacircle(surface, int(width // 2 + sin(alpha) * r), int(height // 2 + cos(alpha) * r), w, color)


def point_circle_10(surface, progress, mood):
    point_circle(surface, progress, mood, num_points=10)


def rotating_bones(surface, progress, mood, count=4):
    width, height = surface.get_size()
    w = width // 40
    r = min(width - 9 * w, height - 9 * w) // 2
    for i in range(count):
        alpha = progress * 2 * pi + i * pi * 8 / count
        pos_x = width // 2 + sin(alpha/4) * r * (count > 1)
        pos_y = height // 2 + cos(alpha/4) * r * (count > 1)
        if i % 2 == 0:
            color = mood.primary_color
        else:
            color = mood.secondary_color
        filled_circle(surface,
                      int(pos_x + sin(alpha) * 3.5 * w),
                      int(pos_y + cos(alpha) * 3.5 * w),
                      w, color)
        aacircle(surface,
                 int(pos_x + sin(alpha) * 3.5 * w),
                 int(pos_y + cos(alpha) * 3.5 * w),
                 w, color)
        filled_circle(surface,
                      int(pos_x - sin(alpha) * 3.5 * w),
                      int(pos_y - cos(alpha) * 3.5 * w),
                      w, color)
        aacircle(surface,
                 int(pos_x - sin(alpha) * 3.5 * w),
                 int(pos_y - cos(alpha) * 3.5 * w),
                 w, color)
        filled_polygon(surface, [
            (int(pos_x - sin(alpha) * 3.5 * w + sin(alpha + pi / 2) * w / 2),
             int(pos_y - cos(alpha) * 3.5 * w + cos(alpha + pi / 2) * w / 2)),
            (int(pos_x - sin(alpha) * 3.5 * w - sin(alpha + pi / 2) * w / 2),
             int(pos_y - cos(alpha) * 3.5 * w - cos(alpha + pi / 2) * w / 2)),
            (int(pos_x + sin(alpha) * 3.5 * w - sin(alpha + pi / 2) * w / 2),
             int(pos_y + cos(alpha) * 3.5 * w - cos(alpha + pi / 2) * w / 2)),
            (int(pos_x + sin(alpha) * 3.5 * w + sin(alpha + pi / 2) * w / 2),
             int(pos_y + cos(alpha) * 3.5 * w + cos(alpha + pi / 2) * w / 2))
            ], color)
        aapolygon(surface, [
            (int(pos_x - sin(alpha) * 3.5 * w + sin(alpha + pi / 2) * w / 2),
             int(pos_y - cos(alpha) * 3.5 * w + cos(alpha + pi / 2) * w / 2)),
            (int(pos_x - sin(alpha) * 3.5 * w - sin(alpha + pi / 2) * w / 2),
             int(pos_y - cos(alpha) * 3.5 * w - cos(alpha + pi / 2) * w / 2)),
            (int(pos_x + sin(alpha) * 3.5 * w - sin(alpha + pi / 2) * w / 2),
             int(pos_y + cos(alpha) * 3.5 * w - cos(alpha + pi / 2) * w / 2)),
            (int(pos_x + sin(alpha) * 3.5 * w + sin(alpha + pi / 2) * w / 2),
             int(pos_y + cos(alpha) * 3.5 * w + cos(alpha + pi / 2) * w / 2))
        ], color)


def rotating_bone_circle(surface, progress, mood):
    rotating_bones(surface, progress, mood, count=20)


def rotating_bone_1(surface, progress, mood):
    rotating_bones(surface, progress, mood, count=1)


def snow(surface, progress, mood, seed=1):
    width, height = surface.get_size()
    w = width // 40
    random.seed(a=seed)
    layers = [[(random.random()*width, random.random()*(height+2*w)) for _ in range((6-i)*10)] for i in range(6)]
    for i, positions in enumerate(layers):
        if i % 2 > 0:
            color = mood.primary_color
        else:
            color = mood.secondary_color
        for x, y in positions:
            filled_circle(surface, int(x), int((y + progress * (i+1)/6 * (height+2*w)) % (height+2*w) - w),
                          w//(6-i), color)
            aacircle(surface, int(x), int((y + progress * (i+1)/6 * (height+2*w)) % (height+2*w) - w),
                     w//(6-i), color)

import os
import sys
import time

from fleet.utility import *
from fleet.utility import LOG as L
from fleet.script import testcase

class TestCase(testcase.TestCase_Base):

    def initialize(self):
        if self.enable_timeout("home.png"):
            self.tap_timeout("action_formation.png"); time.sleep(2)
            self.tap_timeout("action_home.png")
            return self.enable_timeout("home.png")
        else:
            self.adb.stop("com.dmm.dmmlabo.kancolle/.AppEntry")
            time.sleep(5)
            self.adb.invoke("com.dmm.dmmlabo.kancolle/.AppEntry"); time.sleep(2)
            self.tap_timeout("start_music_off.png", timeout=2); time.sleep(2)
            self.tap_timeout("start_game.png", timeout=2); time.sleep(2)
            return self.enable_timeout("home.png")

    def supply(self, fleet):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_supply.png"); time.sleep(2)
        if not self.enable_timeout(self.__supply_fleet_focus(fleet), loop=2, timeout=2):
            self.tap_timeout(self.__supply_fleet(fleet)); time.sleep(2)
        self.tap_timeout("supply_all.png"); time.sleep(2)
        return True

    def __supply_fleet(self, fleet):
        return "supply_fleet_%s.png" % fleet

    def __supply_fleet_focus(self, fleet):
        return "supply_fleet_%s_focus.png" % fleet

    def exercises(self):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_sortie.png"); time.sleep(2)
        self.tap_timeout("sortie_exercises.png"); time.sleep(2)
        p = POINT(self.get("position.exercises_x"),
                  self.get("position.exercises_y"),
                  self.get("position.exercises_width"),
                  self.get("position.exercises_height"))
        for _ in range(5):
            if self.enable_pattern_crop("exercises_win_*.png", p, loop=3, timeout=1):
                L.info("I'm already fighting. I won.")
            elif self.enable_pattern_crop("exercises_lose_*.png", p, loop=3, timeout=1):
                L.info("I'm already fighting. I lost.")
            else:
                L.info(p);
                while not self.enable_timeout("exercises_start.png", loop=3, timeout=2):
                    self._tap(p); time.sleep(3)
                self.tap_timeout("exercises_start.png", loop=3, timeout=1); time.sleep(2)
                if self.enable_timeout("exercises_unable.png", loop=3, timeout=1):
                    return False
                self.tap_timeout("exercises_attack.png", loop=3, timeout=1); time.sleep(2)
                while not self.enable_timeout("next.png", loop=3, timeout=2):
                    if self.tap_timeout("trail_formation.png", loop=3, timeout=1): time.sleep(2)
                    if self.tap_timeout("night_battle_start.png"): time.sleep(1)
                    time.sleep(10)
                while self.tap_timeout("next.png", loop=3, timeout=2): time.sleep(5)
                break
            p.x = int(p.x) - int(p.width); L.info("Point : %s" % str(p))
            if int(p.x) < 0:
                self.home(); return False
        return self.enable_timeout("home.png")

    def expedition(self, fleet, id):
        if not self.enable_timeout("home.png"):
            return False
        self.tap_timeout("action_sortie.png"); time.sleep(2)
        self.tap_timeout("sortie_expedition.png"); time.sleep(2)
        self.__expedition_stage(id); time.sleep(2)
        self.tap_timeout(self.__expedition_id(id)); time.sleep(2)
        if self.enable_timeout("expedition_done.png", loop=2, timeout=2):
            return True
        self.tap_timeout("expedition_decide.png"); time.sleep(2)
        if not self.enable_timeout(self.__expedition_fleet_focus(fleet), loop=2, timeout=2):
            self.tap_timeout(self.__expedition_fleet(fleet)); time.sleep(2)
        if self.enable_timeout("expedition_unable.png", loop=2, timeout=2):
            return False
        self.tap_timeout("expedition_start.png"); time.sleep(2)
        return self.enable_timeout("expedition_done.png")


    def __expedition_id(self, id):
        return "expedition_%s.png" % id

    def __expedition_stage(self, id):
        if int(id) > 32: self.tap_timeout("expedition_stage_5.png"); time.sleep(1)
        elif int(id) > 24: self.tap_timeout("expedition_stage_4.png"); time.sleep(1)
        elif int(id) > 16: self.tap_timeout("expedition_stage_3.png"); time.sleep(1)
        elif int(id) > 8: self.tap_timeout("expedition_stage_2.png"); time.sleep(1)
        else: pass

    def __expedition_fleet(self, fleet):
        return "expedition_fleet_%s.png" % fleet

    def __expedition_fleet_focus(self, fleet):
        return "expedition_fleet_%s_focus.png" % fleet

    def expedition_result(self):
        if self.enable_timeout("expedition_result.png", loop=2, timeout=2):
            self.tap_timeout("expedition_result.png"); time.sleep(5)
            self.tap_timeout("next.png"); time.sleep(1)
            self.tap_timeout("next.png"); time.sleep(1)
            return self.enable_timeout("expedition_result.png", loop=3, timeout=2)
        else:
            return False

    def home(self):
        self.tap_timeout("action_home.png")
        return self.enable_timeout("home.png")

import os
import sys
import time

from atve.log import LOG as L
from atve.script import AtveTestCase


class TestCase(AtveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        try :
            self.assertTrue("atve.browser" in self.service.keys())
            b = self.service["atve.browser"].get("FireFox")
            self.assertTrue(b != None)
            b.start(self.get("browser.url"))
            b.find_element_by_name("q").send_keys("atve")
            b.find_element_by_name("q").submit()
            time.sleep(5)
            self.assertTrue(self.get("system.tmp") != None)
            b.screenshot(self.get("system.tmp"));
            self.assertTrue(os.path.exists(
                os.path.join(self.get("system.tmp"), "screen.png")))
        except Exception as e:
            L.warning(str(e))
        finally:
            b.quit()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)

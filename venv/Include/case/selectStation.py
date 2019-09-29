from case.baseCase import BaseCase
from page.selectStationPage import SelectStationPage
import unittest

class SelectStation(BaseCase):

    def test_selectStation(self):
        seStation = SelectStationPage(self.driver)
        seStation.duizhang_click()
        seStation.changeStation_click()

        # # 选择油站框是否弹出
        # if seStation.isSelect():
        #     self.log.info("已弹出")
        #     # seStation.selectStation()
        #     # seStation.submit_click()
        # else:
        #     self.log.info("未弹出")
        #     seStation.changeStation_click()
        #     # seStation.selectStation()
        #     # seStation.submit_click()

if __name__ == "__main__":
    unittest.main()
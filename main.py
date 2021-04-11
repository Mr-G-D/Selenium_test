from selenium import webdriver
import unittest
import time
from objects.object import stuff, about, home, Partners, programs, Volunteers


class checkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="D:/sparksFoundation/driver/chromedriver.exe") # Chrome driver path
        cls.driver.maximize_window()


    def test_home(self):

        self.driver.get(stuff.path) # sparksfoundation.org
        self.driver.implicitly_wait(10) # 10 ms

        print(".Home Page {")
        self.driver.find_element_by_id(home.video_id)
        print("   Element 1 ✅")
        self.driver.find_element_by_css_selector(home.para_class)
        print("   Element 2 ✅")
        print("}")
        

    def test_team(self):
        print("Team Page { ")
        self.driver.find_element_by_link_text(about.button1).click()
        self.driver.find_element_by_link_text(about.button2).click()
        print("   Element 7 ✅")
        self.driver.find_element_by_css_selector(about.member_image)
        print("   Element 8 ✅")
        self.driver.find_element_by_css_selector(about.member_details)
        print("   Element 9 ✅")
        self.driver.find_element_by_css_selector(about.nav)
        print("   Element 10 ✅")
        print("}")


    def test_programs(self):
        
        print("Programs Page {")
        self.driver.find_element_by_link_text(programs.button1).click()
        self.driver.find_element_by_link_text(programs.button2).click()
        print("   Element 5 ✅")
        self.driver.find_element_by_css_selector(programs.mentorship_program)
        print("   Element 6 ✅")
        self.driver.find_element_by_css_selector(programs.methods)
        print("}")


    # def test_volunteer(self):

    #     print("Volunteers Page {")
    #     self.driver.find_element_by_id(Volunteers.button_id).click()
    #     print("   Element 11 ✅")
    #     self.driver.find_element_by_css_selector(Volunteers.image_class)
    #     print("   Element 12 ✅")
    #     print("}")


    # def test_partners(self):
    #     print("Partners Page {")
    #     self.driver.find_element_by_id(Partners.button_id).click()
    #     print("   Element 3 ✅")
    #     self.driver.find_element_by_id(Partners.image_id)
    #     print("   Element 4 ✅")
    #     print("}")


    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()


#Driver's Code
 

if __name__=="__main__":
    unittest.main()


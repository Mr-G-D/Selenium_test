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
        print("   Element 1 "+ stuff.icon)
        self.driver.find_element_by_css_selector(home.para_class)
        print("   Element 2 "+ stuff.icon)
        print("}")
        

    def test_team(self):
        print("Executive Team Page { ")
        self.driver.find_element_by_link_text(about.button1).click()
        self.driver.find_element_by_link_text(about.button2).click()
        print("   Element 8 "+ stuff.icon)
        self.driver.find_element_by_css_selector(about.member_image)
        print("   Element 9 "+ stuff.icon)
        self.driver.find_element_by_css_selector(about.member_details)
        print("   Element 10 "+ stuff.icon)
        self.driver.find_element_by_css_selector(about.nav)
        print("   Element 11 "+ stuff.icon)
        print("}")


    def test_programs(self):
        
        print("Student Mentorship Program Page {")
        self.driver.find_element_by_link_text(programs.button1).click()
        self.driver.find_element_by_link_text(programs.button2).click()
        print("   Element 5 "+ stuff.icon)
        self.driver.find_element_by_css_selector(programs.mentorship_program)
        print("   Element 6 "+ stuff.icon)
        self.driver.find_element_by_css_selector(programs.methods)
        print("   Element 7 "+ stuff.icon)
        print("}")


    def test_volunteer(self):

        print("Events Volunteer Page {")
        self.driver.find_element_by_link_text(Volunteers.button1).click()
        self.driver.find_element_by_link_text(Volunteers.button2).click()
        print("   Element 11 "+ stuff.icon)
        self.driver.find_element_by_css_selector(Volunteers.body)
        print("   Element 12 "+ stuff.icon)
        self.driver.find_element_by_css_selector(Volunteers.form)
        print("   Element 13 "+ stuff.icon)
        print("}")


    def test_partners(self):
        print("Partners Page {")
        self.driver.find_element_by_link_text(about.button1).click()
        self.driver.find_element_by_link_text(Partners.button2).click()
        print("   Element 3 "+ stuff.icon)
        self.driver.find_element_by_css_selector(Partners.body)
        print("   Element 4 "+ stuff.icon)
        self.driver.find_element_by_css_selector(Partners.nav)
        print("   Element 5 "+ stuff.icon)
        print("}")


    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()


#Driver's Code
 

if __name__=="__main__":
    unittest.main()


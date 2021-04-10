from selenium import webdriver
import unittest
import time
from objects.object import stuff, team, home, Partners, programs, Volunteers


class checkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="D:/sparksFoundation/driver/chromedriver.exe") # Opening th Chrome driver
        cls.driver.maximize_window()


    def test_home(self):

        self.driver.get(stuff.path) # Openening the website
        self.driver.implicitly_wait(10) # Waiting Time

        print("Home Page {")
        self.driver.find_element_by_id(home.image_id)
        print("   Element 1 ✅")
        self.driver.find_element_by_id(home.para_id)
        print("   Element 2 ✅")
        print("}")
        

    def test_team(self):
        
        print("Team Page { ")
        self.driver.find_element_by_id(team.button_id).click()
        print("   Element 7 ✅")
        self.driver.find_element_by_id(team.director_id)
        print("   Element 8 ✅")
        self.driver.find_element_by_id(team.scholarship_director_id)
        print("   Element 9 ✅")
        self.driver.find_element_by_id(team.main_id)
        print("   Element 10 ✅")
        print("}")


    def test_programs(self):
        
        print("Programs Page {")
        self.driver.find_element_by_id(programs.button_id).click()
        print("   Element 5 ✅")
        self.driver.find_element_by_id(programs.cover_id)
        print("   Element 6 ✅")
        print("}")


    def test_volunteer(self):

        print("Volunteers Page {")
        self.driver.find_element_by_id(Volunteers.button_id).click()
        print("   Element 11 ✅")
        self.driver.find_element_by_css_selector(Volunteers.image_class)
        print("   Element 12 ✅")
        print("}")


    def test_partners(self):
        print("Partners Page {")
        self.driver.find_element_by_id(Partners.button_id).click()
        print("   Element 3 ✅")
        self.driver.find_element_by_id(Partners.image_id)
        print("   Element 4 ✅")
        print("}")


    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()


#Driver's Code
 

if __name__=="__main__":
    unittest.main()

